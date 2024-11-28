#QR code Generator in python 

import qrcode 

features = qrcode.QRCode(version = 1, box_size = 40, border = 8)

features.add_data('Hello i am new to python programming')
features.make(fit= True)
generate_image = features.make_image(fill_color = "Purple", back_color = "White")
generate_image.save('image.png')
