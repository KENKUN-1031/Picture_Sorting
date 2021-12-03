import os
import shutil

path = input("pathを入力してください：")
# path = "/Users/saryusoul/desktop/g12/sorting1/"

img = os.listdir(path)

os.mkdir(path + "raw")
os.mkdir(path + "jpeg")

for x in img:
    if x.endswith(".JPG"):
        shutil.move(path+x, path + "jpeg")
        # os.replace(path + x, path + "jpeg")
    else:
        continue

for x in img:
    if x.endswith(".CR2"):
        shutil.move(path+x, path + "raw")
        # os.replace(path+x, path + "raw")
    else:
        continue

print("successful")
