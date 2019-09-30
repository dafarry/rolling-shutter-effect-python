#!/usr/bin/env python3

import numpy as np
from PIL import Image, ImageColor # pillow fork of PIL
import os

height = 600
x, y = np.ogrid[-height/2: height/2, -height/2: height/2]
plane = x + 1j * y
bentprop = np.zeros_like(plane, dtype=np.bool)
os.makedirs("video", exist_ok=True)

for frame in range(height):
    backgnd = np.zeros_like(plane, dtype=np.uint8)
    propellor = np.zeros_like(plane, dtype=np.bool)
    angle = 2 * np.pi * ( frame / height + 1/12)
    for blade in range(6):
        phase = np.exp( 1j * (angle + blade * np.pi/3))
        ellipse = abs(plane - 0.49 * height * phase) + abs(plane)
        propellor |= ellipse < 0.5 * height

    bentprop[frame] = propellor[frame]
    greenbar = [f for f in range(frame, min(frame + 3, height -3))]
    colors = ("white","lightblue","red","green")
    rgbcolors = np.array(list(map(ImageColor.getrgb, colors)))
    composite = np.maximum.reduce((backgnd, propellor*1, bentprop*2))
    composite[greenbar] = 3
    rgb = rgbcolors.astype(np.uint8)[composite]
    image = Image.fromarray(rgb, mode="RGB")
    image.save('video/file{:04d}.png'.format(frame))

os.system("ffmpeg -y -loglevel warning -i video/file%04d.png " +
          "-framerate 25 -pix_fmt yuv420p rolling.mp4")

