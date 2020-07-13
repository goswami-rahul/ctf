# Quirky Resolution

We have the file  

![image](https://github.com/goswami-rahul/ctf/raw/master/rgbCTF2020/quirky_resolution/quirky_resolution.png)

We see only white color.
Analyzing the file, we can see that each pixel is either (255, 255, 255) (white), or (254, 254, 254), so indistinguishable by eyes.  

Create a new file with all (254, 254, 254) pixels to (0, 0, 0) (black) to clearly see the pattern.  

```py
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
```

![QR](https://github.com/goswami-rahul/ctf/raw/master/rgbCTF2020/quirky_resolution/qr.png)

It's a QR code. Scan this file using any QR scanner and get the flag. 

```txt
rgbCTF{th3_qu1rk!er_th3_b3tt3r}
```
