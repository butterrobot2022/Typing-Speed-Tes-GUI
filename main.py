from tkinter import *
from time import sleep
from tkinter import messagebox
from requests import *


def close_app():
    window.destroy()


def start():
    global seconds
    response = get(url="https://random-word-api.herokuapp.com/word?number=100")
    words = response.text.strip('[').strip(']').replace(",", '').replace('"', ' ')
    text.insert('1.0', words)
    text['state'] = 'disabled'
    text_content = text.get('1.0', 'end')
    improved_text_content = list(text_content.split())
    entry.delete(0, END)
    still_time = True
    while still_time:
        sleep(1)
        seconds -= 1
        time_text.config(text=f"Time: {seconds}")
        time_text.update()
        same_words = 0
        if seconds == 0:
            still_time = False
            seconds = 60
            entry_list = list(entry.get().split())
            for i in entry_list:
                if i in improved_text_content:
                    same_words += 1
                    high_score_list.append(int(same_words))
                    high_score_text.config(text=f"High Score: {max(high_score_list)}")
                    high_score_text.update()
                    entry.delete(0, END)
                    entry.insert(0, "Type here")
                    text.config(state=NORMAL)
                    text.delete('1.0', 'end')
            return messagebox.showinfo("Speed Test App", f"Your score is {same_words} word(s) correct for 1 minute!")


window = Tk()
window.title("Speed Test App")
window.minsize(width=500, height=450)

entry = Entry(window)
entry.insert(0, "Type here")
entry.place(x=190, y=360)


start_button = Button(text="Start Game!", command=start)
start_button.place(x=200, y=390)

text = Text(window, height=18, width=43, padx=5, pady=5, wrap=WORD)
text.place(x=90, y=40)

high_score = 0
high_score_text = Label(text=f"High Score {high_score}", font=("Arial", 10, "bold"))
high_score_text.place(x=400, y=0)

seconds = 60
time_text = Label(text=f"Time: {seconds}", font=("Arial", 10, "bold"))
time_text.place(x=200, y=0)

high_score_list = []
close = Button(text="Close App", command=close_app)
close.place(x=0, y=0)

window.mainloop()
