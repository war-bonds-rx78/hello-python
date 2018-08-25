import tkinter as tk
import tkinter.filedialog as fd

# アプリウィドウを表示しない
root = tk.Tk()
root.withdraw

# オープンダイアログを表示する
file = fd.askopenfilename(
    title = "ファイルを選んでください",
    filetypes =[("TEXT", ".txt"), ("TEXT", ".py"), ("HTML", ".html")]
)

if file :
    with open (file, "r", encoding="utf_8") as fileObj :
        text = fileObj.read()
        print(text)