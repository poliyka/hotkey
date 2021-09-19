import os

import win32api
import win32con
import win32gui
import win32ui
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

    """
    # 以api方式擷取畫面 (步驟複雜可控性多)

    hwnd = 0  # 視窗的編號，0號表示當前活躍視窗
    # 根據視窗控制代碼獲取視窗的裝置上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)

    # 根據視窗的DC獲取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC建立可相容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 建立bigmap準備儲存圖片
    saveBitMap = win32ui.CreateBitmap()
    # 獲取監控器資訊
    MoniterDev = win32api.EnumDisplayMonitors(None, None)
    w = MoniterDev[2][2][2]
    h = MoniterDev[2][2][3]

    # 為bitmap開闢空間
    # 圖片大小(空間大小)                                # 變小 乘數小
    saveBitMap.CreateCompatibleBitmap(mfcDC, int(w * 0.106), int(h * 0.19))
    # 高度saveDC，將截圖儲存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 擷取從左上角（0，0）長寬為（w，h）的圖片
    # 圖片大小(擷取大小)   #左移 數字大   #上移 數字大
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (int(w * 0.286), int(h * 0.246)), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC, "capture.png")
    """


if __name__ == "__main__":
    capture(759, 197, 1882, 881)
