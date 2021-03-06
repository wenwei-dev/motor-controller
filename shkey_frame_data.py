#!/usr/bin/env python3
#
# This script should be run in blender.
# It fetches the face data of 200 frames for a specific animation.

import roscom
import bpy
from collections import defaultdict
import time
import os
import shutil

frames = defaultdict(list)
output_dir = os.path.expanduser('/tmp/shapekey_data')
if os.path.isdir(output_dir):
    shutil.rmtree(output_dir)
os.makedirs(output_dir)

for action in bpy.data.actions:
    if not action.name.startswith('EMO-'):
        continue
    bpy.context.object.animation_data.action = action
    name = action.name

    frame_size = bpy.context.scene.frame_end+1
    for i in range(frame_size):
        bpy.context.scene.frame_set(i)
        time.sleep(0.01)
        data=roscom.api.getFaceData()
        print("frame", i)
        for k, v in data.items():
            frames[k].append(v)

    with open(os.path.join(output_dir, '{}.csv'.format(name)), 'w') as f:
        header = sorted(frames.keys())
        f.write('%s\n' % ','.join(header))
        for i in range(frame_size):
            values = [frames[k][i] for k in header]
            f.write('%s\n' % ','.join(map(str, values)))
        print('write done')