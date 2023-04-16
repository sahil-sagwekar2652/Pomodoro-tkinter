from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    Timer_label.config(text="Timer", fg=GREEN, font=(FONT_NAME, 50, 'bold'), bg=YELLOW)
    tick_mark_label.config(text="")
    global reps
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1

    if reps == 1 or reps == 3 or reps == 5 or reps == 7:
        count_down(WORK_MIN * 60)
        Timer_label.config(text="Work", fg=GREEN)
    if reps == 2 or reps == 4 or reps == 6:
        count_down(SHORT_BREAK_MIN * 60)
        Timer_label.config(text="Break", fg=PINK)
    if reps == 8:
        count_down(LONG_BREAK_MIN * 60)
        Timer_label.config(text="Break", fg=RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):

    count_min = count // 60
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    if count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        if reps % 2 == 0:
            tick_mark_label.config(text="✔"*(reps // 2))


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=40, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)


Timer_label = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50, 'bold'), bg=YELLOW)
Timer_label.grid(column=1, row=0)

start_button = Button(text="Start", font=(FONT_NAME, 12, 'bold'), highlightthickness=0, command=start_timer)
start_button.config(height=1, width=5)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", font=(FONT_NAME, 12, 'bold'), highlightthickness=0, command=reset_timer)
reset_button.config(height=1, width=5)
reset_button.grid(column=2, row=2)

tick_mark_label = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, 'bold'))
tick_mark_label.grid(column=1, row=3)

window.mainloop()
