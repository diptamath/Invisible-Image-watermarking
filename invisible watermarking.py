from PIL import Image

from sys import argv
from qrcode import make as makeQR

if __name__ == '__main__':
    qr = makeQR("hello sourya")
    qw, qh = qr.size

    im = Image.open("hello.jpg")
    w, h = im.size

    if qw > w:
        qr = qr.resize((w, w))
    elif qh > h:
        qr = qr.resize((h, h))
    qw, qh = qr.size

    imd = im.load()
    for i in range(w):
        for j in range(h):
            d = imd[i, j]
            imd[i, j] = d[:-1] + ((d[-1] | 1) if qr.getpixel((i % qw, j % qh)) else (d[-1] & ~1),)


    from os.path import splitext

    root, ext = splitext("hello.jpg")
    im.save(root + '_watermark.png')
    qr.save(root+'_qrcode'+'.png')

