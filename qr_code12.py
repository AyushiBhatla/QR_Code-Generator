import qrcode
from PIL import Image
import qrcode.constants

# qr version,error correction Highlevel and css
qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

# Data for qrcode
qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&list=PLjVLYmrlmjGfAUdLiF2bQ-0l8SwNZ1sBl")
qr.make(fit=True)
img=qr.make_image(fill_color="red",back_color="blue")
img.save("youtube_link.png")