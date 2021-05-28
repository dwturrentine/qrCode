from pyzbar.pyzbar import decode
from PIL import Image

img = Image.open('/Users/dwt/PycharmProjects/qrCode/myqrcode.png')

result = decode(img)

print(result)
