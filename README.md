# 自動化映射鍵鼠工具

## 使用說明

> 1.安裝依賴 lib

```h
python3 ./setup.py
```

> 2.在[script.py](./script.py)撰寫腳本

> 3.執行 GUI 程式[gui.py](./gui.py)

```h
python3 ./gui.py
```

> 4.使用 pyinstaller 打包 EXE

```h
在cmd環境下cd到檔案目錄
1.pyinstaller -D -w .\gui.py
    -F 打包成一個exe文件
    –icon=圖標路徑
    -w 使用視窗，無控制台
    -c 使用控制台，無視窗
    -D 創建一個目錄，包含exe以及其他一些依賴性文件
    --hidden-import module

2.如有已有.spec文件 可調整細部參數或手動import lib 資源
3.修改gui.spec內文
4.再次輸入 pyinstaller -D -w gui.spec
```

[手動 import 資源參考](https://codingdailyblog.wordpress.com/2018/03/24/python-pyinstaller%E6%89%93%E5%8C%85exe%E4%B8%80%E4%BD%B5%E5%8C%85%E5%90%AB%E7%85%A7%E7%89%87%E6%AA%94%E6%8A%80%E5%B7%A7/)
