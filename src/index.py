from tkinter import filedialog, Text
from ttkbootstrap.constants import *
import ttkbootstrap as tb
from main import *

# 메인 윈도우 설정
root = tb.Window(themename="vapor")
root.title("갤창랭킹 시각화 프로그램")
root.geometry("600x450")

def open_file():
    fp = filedialog.askopenfilename(title="파일 선택", filetypes=[("JSON 파일", "*.json")])

    if fp:
        try:
            analyzeLit(fp)
            with open("../dist/res.txt", "r", encoding="utf-8") as f:
                content = f.read()

            text_box.delete("1.0", "end")
            text_box.insert("end", content)
        except Exception as e:
            text_box.delete("1.0", "end")
            text_box.insert("end", f"파일을 열 수 없습니다.\n오류: {e}")

# 파일 열기 버튼
open_button = tb.Button(root, text="파일 열기", bootstyle=PRIMARY, command=open_file)
open_button.pack(pady=10)

text_box = Text(root, wrap="word", height=20, width=70)
text_box.pack(padx=10, pady=10)

# 프로그램 실행
root.mainloop()
