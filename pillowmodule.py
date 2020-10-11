
import os

# img = Image.open('ww.jpg')
# img.save('ww.png')

# img.show()

# max_size = (100,120)
# img.thumbnail(max_size)
# img.save('wwmax_size.jpg')

# for item in os.listdir():
#     if item.endswith('.jpg'):
#         img = Image.open(item)
#         filename,extension = os.path.splitext(item)
#         img.save(f'{filename}.png')

from PIL import Image, ImageEnhance, ImageFilter

img = Image.open('ww.jpg')
# enhancer = ImageEnhance.Sharpness(img)
# enhancer.enhance(7).save('wwnew.jpg')

# img = Image.open('ww.jpg')
# enhancer = ImageEnhance.Color(img)
# enhancer.enhance(7).save('wwnew.jpg')

# img = Image.open('ww.jpg')
# enhancer = ImageEnhance.Brightness(img)
# enhancer.enhance(7).save('wwnew.jpg')

# img = Image.open('ww.jpg')
# enhancer = ImageEnhance.Contrast(img)
# enhancer.enhance(7).save('wwnew.jpg')


img.filter(ImageFilter.GaussianBlur(radius=54)).save('wwblur.jpg')
