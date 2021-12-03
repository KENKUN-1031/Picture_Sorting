import os
import shutil

path = input("を入力してください：")

# path = "/Users/saryusoul/desktop/g12/sorting1/"
jpg = path + "jpeg/"
raw = path + "raw/"

os.mkdir(path + "raw_chosen")

search_pic = []
base_pic = []
save = []

img = os.listdir(jpg)
img_raw = os.listdir(raw)

for x in img:
    name = os.path.splitext(os.path.basename(x))[0]
    search_pic.append(name)

for a in img_raw:
    base_pic.append(a)

for now in search_pic:
    for y in base_pic:
        if now in y:
            save.append(y)

for b in base_pic:
    for c in save:
        if b == c:
            shutil.move(raw+b, path + "raw_chosen")


#search_pic= jpgの保存する写真
#base_pic = 全てのraw写真
#save = rawの保存する写真


print("successful")
