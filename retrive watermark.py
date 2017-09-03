from PIL import Image

from sys import argv
from qrcode import make as makeQR

if __name__ == '__main__':
    im = Image.open("hello_watermark.png")
    s = w, h = im.size
    imd = im.load()

    oim = Image.new('1', s)
    oimd = oim.load()

    for i in range(w):
        for j in range(h):
            d = imd[i, j]
            oimd[i, j] = 255 * (d[-1] & 1)
            # oimd[i,j] = 255 * (d[-1]>>1 & 1)
            # oimd[i,j] = 255 * (1 if d[-1] & 0b111 == 0b111 else 0)

    from os.path import splitext

    root, ext = splitext("hello_watermark.png")
    fname = root + '_1bit' + ext
    oim.save(fname)

