import threading
import time
import logging
import traceback
from PyQt4 import QtCore
from PyQt4 import QtGui
from ui.motoreditor import Ui_Form

logger = logging.getLogger(__name__)

class MotorValueEditor(QtGui.QWidget):
    def __init__(self, parent, motor, row, enable_range_setting=True):
        super(MotorValueEditor, self).__init__(parent)
        self.tableWidget = parent
        self.motor = motor
        self.row = row
        self.app = QtGui.QApplication.instance()

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.motorValueDoubleSpinBox.valueChanged.connect(self.spinValueChanged)
        self.ui.motorValueSlider.valueChanged.connect(self.sliderValueChanged)
        self.ui.motorValueSlider.setMinimum(self.motor['min']*4)
        self.ui.motorValueSlider.setMaximum(self.motor['max']*4)
        self.ui.motorValueDoubleSpinBox.setMinimum(self.motor['min'])
        self.ui.motorValueDoubleSpinBox.setMaximum(self.motor['max'])
        self.ui.motorValueSlider.installEventFilter(self)
        self.ui.motorValueDoubleSpinBox.installEventFilter(self)
        self.ui.enableCheckBox.toggled.connect(self.enableMotor)

        self.polling = True
        self.stopped = False
        self.polljob = threading.Thread(target=self.poll)
        self.polljob.daemon = True
        self.polljob.start()

        self.destroyed.connect(self.delete)

        self.ui.setInitButton.setEnabled(enable_range_setting)
        self.ui.setMaxButton.setEnabled(enable_range_setting)
        self.ui.setMinButton.setEnabled(enable_range_setting)
        if enable_range_setting:
            self.ui.setInitButton.clicked.connect(self.setInitValue)
            self.ui.setMaxButton.clicked.connect(self.setMaxValue)
            self.ui.setMinButton.clicked.connect(self.setMinValue)
        else:
            self.ui.setInitButton.hide()
            self.ui.setMaxButton.hide()
            self.ui.setMinButton.hide()

    def get_controller(self):
        device = str(self.motor['device'])
        if device in self.app.motor_controllers:
            controller = self.app.motor_controllers[device]
            return controller
        else:
            logger.debug("Can't get controller {}".format(device))

    def sliderValueChanged(self, value):
        value = value/4.0
        if value > self.motor['max']:
            logger.warn("{} motor value {} is greater than maximum {}".format(self.motor['name'], value, self.motor['max']))
            return
        elif value < self.motor['min']:
            logger.warn("{} motor value {} is lower than minimum {}".format(self.motor['name'], value, self.motor['min']))
            return
        self.ui.motorValueDoubleSpinBox.setValue(value)
        self.setMotorTarget(value)

    def spinValueChanged(self, value):
        if value > self.motor['max']:
            logger.warn("{} motor value {} is greater than maximum {}".format(self.motor['name'], value, self.motor['max']))
            return
        elif value < self.motor['min']:
            logger.warn("{} motor value {} is lower than minimum {}".format(self.motor['name'], value, self.motor['min']))
            return
        self.ui.motorValueSlider.setValue(int(value*4))

    def poll(self):
        while not self.stopped:
            if self.polling:
                try:
                    controller = self.get_controller()
                    if controller is not None:
                        motor_id = self.motor['motor_id']
                        position = controller.getPosition(motor_id)
                        if position is not None:
                            self.ui.motorValueSlider.setMotorPosition(position)
                            #self.ui.motorValueSlider.setValue(int(position*4))
                            logger.debug("Get motor {}({}) position {}".format(self.motor['name'], motor_id, position))
                    time.sleep(0.05)
                except Exception as ex:
                    logger.error(traceback.format_exc())
            else:
                time.sleep(0.2)

    def setMotorTarget(self, value):
        if self.ui.enableCheckBox.isChecked():
            if value > self.motor['max']:
                logger.warn("{} motor value {} is greater than maximum {}".format(self.motor['name'], value, self.motor['max']))
                return
            elif value < self.motor['min']:
                logger.warn("{} motor value {} is lower than minimum {}".format(self.motor['name'], value, self.motor['min']))
                return
            controller = self.get_controller()
            if controller is not None:
                motor_id = self.motor['motor_id']
                if controller.hardware == 'dynamixel':
                    controller.setTarget(motor_id, int(value))
                else:
                    controller.setAcceleration(motor_id, 0)
                    controller.setSpeed(motor_id, int(self.motor['speed']))
                    controller.setTarget(motor_id, int(value*4))
                logger.info("Set motor {}({}) position {}".format(self.motor['name'], motor_id, value))
            else:
                logger.warn("Motor controller is None")
        else:
            logger.warn("Motor {} is not enabled".format(self.motor['name']))

    def getValue(self):
        return self.ui.motorValueDoubleSpinBox.value()

    def setValue(self, value):
        while True:
            self.setPolling(False)
            self.ui.motorValueDoubleSpinBox.setValue(value)
            self.setPolling(True)
            break
            time.sleep(0.1)

    def setInitValue(self):
        self.setMotorConfig('init', self.getValue())

    def setMaxValue(self):
        value = self.getValue()
        self.setMotorConfig('max', value)
        self.ui.motorValueSlider.setMaximum(value*4)
        self.ui.motorValueDoubleSpinBox.setMaximum(value)

    def setMinValue(self):
        value = self.getValue()
        self.setMotorConfig('min', value)
        self.ui.motorValueSlider.setMaximum(value*4)
        self.ui.motorValueDoubleSpinBox.setMaximum(value)

    def setMotorConfig(self, key, value):
        if self.motor is not None:
            self.motor[key] = value
            col = self.app.motor_header.values().index(key)
            item = self.tableWidget.item(self.row, col)
            if item is not None:
                item.setData(QtCore.Qt.EditRole, self.motor[key])

    def setPolling(self, polling):
        self.polling = polling

    def delete(self):
        self.stopped = True

    def eventFilter(self, obj, event):
        """Ignore wheel event"""
        if event.type() == QtCore.QEvent.Wheel:
            event.ignore()
            return True
        else:
            return False

    def enableMotor(self, enabled):
        controller = self.get_controller()
        if controller is not None:
            controller.enableMotor(self.motor['motor_id'], enabled)
