import time
import win32gui
import win32ui
import win32con
import win32api
from PIL import Image
from PIL import ImageGrab

def window_capture():
    
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
    #圖片大小(空間大小)                                # 變小 乘數小
    saveBitMap.CreateCompatibleBitmap(mfcDC, int(w*0.106), int(h*0.19))
    # 高度saveDC，將截圖儲存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 擷取從左上角（0，0）長寬為（w，h）的圖片
                        #圖片大小(擷取大小)   #左移 數字大   #上移 數字大
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (int(w*0.286), int(h*0.246)), win32con.SRCCOPY)
    saveBitMap.SaveBitmapFile(saveDC,'test.png')

    # 以PIL套件獲取螢幕截圖(方便快速)
    # x = 2149
    # y = 454
    # m = 2351
    # n = 656

    # box = (x,y,m,n)
    # img = ImageGrab.grab(box)
    # img.save("test.png")

if __name__ == '__main__':
    
    window_capture()