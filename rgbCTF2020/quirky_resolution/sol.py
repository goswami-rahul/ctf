#!/usr/bin/env python
from PIL import Image
import numpy as np

img = np.array(Image.open('quirky_resolution.png'))
for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        for k in range(img.shape[2]):
            if img[i][j][k] == 254:
                img[i][j][k] = 0
Image.fromarray(img).save('qr.png')