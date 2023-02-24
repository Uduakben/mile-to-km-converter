from tkinter import *
import math

new_timer = None


#_____________________________________resetting the timer________________________________________________________________________
def reset_timer():
    canvas.itemconfig(time_text, text="00:00")
    window.after_cancel(new_timer)



#___________________________________defining the timer function ___________________________________________________________________
def start_timer():
    count_down(6 * 60)

#____________________________________defining the countdown function ________________________________________________________________
def count_down(count):
    count_in_min = math.floor(count / 60)
    count_in_sec = count % 60
    if count_in_sec < 10:
        count_in_sec = f"0{count_in_sec}"


    canvas.itemconfig(time_text, text=f"{count_in_min}:{count_in_sec}")
    if count > 0:
        global new_timer
        new_timer = window.after(1000, count_down, count - 1)



#__________________________________________USER INTERFACE OF OUR PROGRAM_______________________________________________________________


window = Tk()
window.title("Timer")
window.config(padx=50, pady=50, bg="blue")


canvas = Canvas(width=430, height=220)
timer = PhotoImage(file="timer.png")
canvas.create_image(215, 110, image=timer)
time_text = canvas.create_text(215, 110, text="00:00", fill="white", font=("Courier", 35, "bold"))
canvas.pack()


start = Button(text="START", bg="blue", fg="white",  font=("Arial", 10, "bold"), command=start_timer)
start.place(x=130, y=230)

reset = Button(text="RESET", bg="blue", fg="white", font=("Arial", 10, "bold"), command=reset_timer)
reset.place(x=250, y=230)

window.mainloop()
