import qrcode

karekod = qrcode.QRCode(
    version = 1,
    error_correction = qrcode.constants.ERROR_CORRECT_L,
    box_size = 50,
    border = 2
)
karekod.add_data("https://www.youtube.com/watch?v=_iB6XAF6Vfs")
karekod.make(fit=True)

image = karekod.make_image(fill_color="yellow",back_color="red")
image.save("karekod.png")