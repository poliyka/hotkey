import os

from PIL import Image, ImageGrab


def capture(x1, y1, x2, y2):
    """
    點1 = (x1, y1)
    點2 = (x2, y2)
    拍照範圍為點1, 點2所包圍之矩形
    """
    # 以PIL套件獲取螢幕截圖(方便快速)
    box = (x1, y1, x2, y2)
    img = ImageGrab.grab(box)

    directory = "../image"
    if not os.path.isdir(directory):
        os.mkdir(directory)

    file_name = "/capture.png"
    if not os.path.isfile(directory + file_name):
        img.save(directory + file_name)
    else:
        i = 1
        while True:
            file_name = f"/capture({i}).png"
            if not os.path.isfile(directory + file_name):
                img.save(directory + file_name)
                break
            i += 1

if __name__ == "__main__":
    capture(759, 197, 1882, 881)
