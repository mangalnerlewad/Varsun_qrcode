import qrcode
# noqa
from PIL import Image  # noqa
# qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_H,box_size=10,border=4,)
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("https://varsunelectrotech.in")
qr.make(fit=True)
img=qr.make_image(fill_color="black",back_color="white")
# img.show()
img.save("varsun_electrotech_qr.png")
 