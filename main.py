import qrcode

# Encoding

data = 'Don\'t forget to subscribe'

# Changing QR Style

qr = qrcode.QRCode(version = 1, box_size=10, border=5)

qr.add_data(data)

qr.make(fit=True)
img = qr.make_image(fill_color = 'green', back_color = 'white')
img.save('/Users/dwt/PycharmProjects/qrCode/myqrcode1.png')

# Creates QR Code

# img = qrcode.make(data)

# img.save('/Users/dwt/PycharmProjects/qrCode/myqrcode.png')

# Decoding QR Code


