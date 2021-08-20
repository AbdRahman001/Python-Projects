import pyqrcode
from pyzbar.pyzbar import decode
from PIL import Image

qr = pyqrcode.create("www.tfp.is")
qr.png("myCode.png", scale=5)

d = decode(Image.open("myCode.png"))
print(d[0].data.decode("ascii"))