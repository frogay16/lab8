from PIL import Image

img = Image.open("gift.jpg")

left = 150
top = 150
right = 500
bottom = 500

img_crop = img.crop((left, top, right, bottom))

img_crop.save("new_gift.jpg")
