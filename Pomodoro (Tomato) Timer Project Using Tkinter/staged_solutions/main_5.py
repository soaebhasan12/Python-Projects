# 005 - Dynamic tyoing Explained.


from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    count_down(5 * 60)








# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # title_label.config(text=)
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count - 1)





# ---------------------------- UI SETUP ------------------------------- #

window = Tk()

window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=3)

reset_button = Button(text="Reset", highlightthickness=0)
reset_button.grid(column=2, row=3)

check_marks = Label(text="✔", fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="D:/PYTHON-PRACTICE/02-PYTHON-BOOTCAMP/28_Tkinter,_Dynamic_Typing_and_the_Pomodoro_GUI_Application/code/002 pomodoro-start/tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=2)

# count_down(7)


window.mainloop()