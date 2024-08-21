import os

os.chdir("img")
num = 1

imgs = os.listdir()

for img in imgs:

    os.rename(img, str(num) + ".jpg")

    print("renamed to: ", num)

    num +=1

print("done")
    