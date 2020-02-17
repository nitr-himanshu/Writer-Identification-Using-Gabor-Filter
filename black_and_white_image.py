import cv2
import glob


def convertToBlackAndWhite(img_path, inplace=True, new_img_path=""):
    originalImage = cv2.imread(img_path)
    grayImage = cv2.cvtColor(originalImage, cv2.COLOR_BGR2GRAY)
    (thresh, blackAndWhiteImage) = cv2.threshold(
        grayImage, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
    if(inplace):
        new_img_path = img_path
    cv2.imwrite(new_img_path, blackAndWhiteImage)

for path in glob.glob("/media/himanshu/C2B05102B050FDFB/dataset/exp/lines/**/*.png",recursive=True):
    convertToBlackAndWhite(path, 128)
print("Done")