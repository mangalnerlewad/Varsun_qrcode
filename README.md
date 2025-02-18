# Varsun_qrcode
QR Code Generator
This Python script generates a QR code for Varsun Electrotech using the qrcode library. The generated QR code can be scanned to quickly access the website.

Installation
Ensure you have the required dependencies installed:

bash
Copy
Edit
pip install qrcode[pil] pillow
Usage
Run the script to generate a QR code:

python
Copy
Edit
import qrcode
from PIL import Image  

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

qr.add_data("https://varsunelectrotech.in")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save("varsun_electrotech_qr.png")
Output
The script will generate a QR code image file named varsun_electrotech_qr.png, which can be used for scanning and quick access to the website.
