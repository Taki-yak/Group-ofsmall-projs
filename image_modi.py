from PIL import Image , ImageFilter, ImageEnhance
import os

my_image= Image.open (r"D:\taki\wallpapers\wall.jpg")
path=(r"D:\copy_taki\taki\ph")
pathout=(r"D:\copy_taki\taki\editiedimgs")
# cut=(0,0,350,350)
# my_newimage=my_image.crop(cut)
# my_newimage.show()
# myconvertedimage= my_image.convert("L")
# myconvertedimage.show()
for filename in os.listdir(path):
    img=Image.open (f"{path}/{filename}")
    edit=img.filter(ImageFilter.SHARPEN).convert("L").rotate(-90)
    factor=1.5
    enhancer=ImageEnhance.Contrast(edit)
    edit=enhancer.enhance(factor)
    clean_name= os.path.splitext(filename)[0]
    edit.save(f"{pathout}/{clean_name}_edited.jpg")
for image in os.listdir(path):
     img.show()    