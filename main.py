import os
import shutil
import cv2


def main():
    # definition img change and get path
    dirPath = "C:/Users/antho/Pictures/desktopimage/"
    originPath = "C:/Users/antho/AppData/Local/Packages/Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy/LocalState/Assets"

    # clean origin folder of images
    shutil.rmtree(dirPath)

    # get folder of all image
    shutil.copytree(originPath, dirPath, dirs_exist_ok=True)

    # rename all image to add jpg
    for count, filename in enumerate(os.listdir(dirPath)):
        src = dirPath + filename
        im = cv2.imread(src)
        h, w, c = im.shape

        dst = dirPath + filename + str(count) + ".jpg"

        if(w > 1900):
            os.rename(src, dst)
        else:
            os.remove(src)


if __name__ == '__main__':
    main()
