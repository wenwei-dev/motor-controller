from PyQt4 import QtCore
from PyQt4 import QtGui
from ui.motoreditor import Ui_Form
import copy

class MotorValueEditor(QtGui.QWidget):
    def __init__(self, parent, model, row):
        super(MotorValueEditor, self).__init__(parent)
        self.model = model
        self.row = row
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.motorValueSpinBox.valueChanged.connect(self.spinValueChanged)
        self.ui.motorValueSlider.valueChanged.connect(self.sliderValueChanged)
        self.ui.setInitButton.clicked.connect(self.setInitValue)
        self.ui.setMaxButton.clicked.connect(self.setMaxValue)
        self.ui.setMinButton.clicked.connect(self.setMinValue)

    def sliderValueChanged(self, value):
        self.setValue(value)

    def spinValueChanged(self, value):
        self.setValue(value)

    def setValue(self, value):
        self.ui.motorValueSpinBox.setValue(value)
        self.ui.motorValueSlider.setValue(value)

    def getValue(self):
        return self.ui.motorValueSpinBox.value()

    def setInitValue(self):
        index = self.model.createIndex(self.row, self.model.header.index('Init'))
        self.model.setData(index, self.getValue(), QtCore.Qt.EditRole)

    def setMaxValue(self):
        index = self.model.createIndex(self.row, self.model.header.index('Max'))
        self.model.setData(index, self.getValue(), QtCore.Qt.EditRole)

    def setMinValue(self):
        index = self.model.createIndex(self.row, self.model.header.index('Min'))
        value = self.getValue()
        self.model.setData(index, self.getValue(), QtCore.Qt.EditRole)

class MotorValueDelegate(QtGui.QItemDelegate):

    def __init__(self, model):
        super(MotorValueDelegate, self).__init__()
        self.model = model

    def createEditor(self, parent, option, index):
        editor = MotorValueEditor(parent, self.model, index.row())
        return editor

    def setEditorData(self, editor, index):
        motor = self.model.motors[index.row()]
        value = self.model.motors[index.row()]['init']
        editor.setValue(value)

    def setModelData(self, editor, model, index):
        print "setModelData"
        print editor.ui.getValue()

    def updateEditorGeometry(self, editor, option, index):
        editor.setGeometry(option.rect)


class MotorItemModel(QtCore.QAbstractTableModel):

    def __init__(self):
        super(MotorItemModel, self).__init__()
        self.motors = []
        self.fields = ['name', 'device', 'motor_id', 'init', 'min', 'max']
        self.header = ['Name', 'Device', 'MotorID', 'Init', 'Min', 'Max', 'Editor']

    def addMotor(self, motor):
        self.motors.append(motor)

    def rowCount(self, parent):
        return len(self.motors)

    def columnCount(self, parent):
        return len(self.header)

    def headerData(self, section, orientation, role):
        if role == QtCore.Qt.DisplayRole:
            if orientation == QtCore.Qt.Horizontal:
                return self.header[section]

    def data(self, index, role):
        col = index.column()
        if col >= len(self.fields):
            return
        field = self.fields[col]
        if role == QtCore.Qt.DisplayRole or role == QtCore.Qt.EditRole:
            motor = self.motors[index.row()]
            return motor.get(field, 'None')
        elif role == QtCore.Qt.BackgroundRole:
            motor = self.motors[index.row()]
            if motor.get('saved_{}'.format(field)) != motor.get(field):
                bg = QtGui.QBrush(QtCore.Qt.yellow)
                return bg

    def flags(self, index):
        if not index.isValid(): return
        return super(MotorItemModel, self).flags(index) | QtCore.Qt.ItemIsEditable

    def setData(self, index, data, role):
        col = index.column()
        if col >= len(self.fields):
            return False
        field = self.fields[col]
        if index.isValid() and role == QtCore.Qt.EditRole:
            motor = self.motors[index.row()]
            if isinstance(data, QtCore.QVariant):
                data = data.toPyObject()
            motor[field] = data
            return True
        else:
            return False

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    editor = MotorValueEditor()
    editor.show()
    sys.exit(app.exec_())
