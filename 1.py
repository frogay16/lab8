from PIL import Image

gift = Image.open("gift.jpg")

left = 150
top = 150
right = 500
bottom = 500

gift_crop = gift.crop((left, top, right, bottom))
gift_crop.save("new_gift.jpg")

print('Готово, изменения сохранены.')