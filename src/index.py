from tkinter import filedialog, Text
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from .main import analyzeLit

# 메인 윈도우 설정
root = tb.Window(themename="vapor")
root.title("갤창랭킹 시각화 프로그램")
root.geometry("600x450")

def open_file():
    fp = filedialog.askopenfilename(title="파일 선택", filetypes=[("JSON 파일", "*.json")])

    if fp:
        try:
            analyzeLit(fp)
        except 4

# 파일 열기 버튼
open_button = tb.Button(root, text="파일 열기", bootstyle=PRIMARY, command=open_file)
open_button.pack(pady=10)

# 프로그램 실행
root.mainloop()
