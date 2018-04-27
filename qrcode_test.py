import qrcode
import os

#在command-line中建立qrcode
os.system("qr \'create qrcode\' > create_qrcode.png")

#操作更多qrcode資料（現在不知如何出現，代run是不會有問題）
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data('Some data')
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")


#有詳細資料看https://github.com/lincolnloop/python-qrcode
