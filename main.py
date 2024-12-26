from tkinter import *
import pandas as pd
import random
import time

window = Tk()
window.title("Flash Cards")
window.minsize(width=800,height=400)
window.config(bg="#B1DDC6", pady=25, padx=30)

canvas = Canvas(width=800, height=526, bg="#B1DDC6", highlightthickness=0)
card_back = PhotoImage(file="images/card_back.png")
back_image = canvas.create_image(400, 263, image=card_back)
word_text = canvas.create_text(310,250, text="French: ", font=("Aerial", 25, "bold"))
canvas.create_text(100,100, text="Score: 0",fill="#f0f0f0", font=("Aerial",25,"bold"))
time_text = canvas.create_text(600,100, text=f"Time: {time}",fill="#f0f0f0", font=("Aerial", 25, "bold"))
canvas.grid(column=0,row=0, columnspan=2)

def random_number():
    file = pd.read_csv("data/french_words.csv")
    num = random.randint(0, len(file)-1)
    return num

def timer(remaining_time):
    if remaining_time < 6:
        canvas.itemconfig(time_text,fill="red", text=f"Time: {remaining_time}")
    else:
        canvas.itemconfig(time_text, text=f"Time: {remaining_time}")

    if remaining_time == 0:
        english_word(random_number())

    window.after(1000,timer,remaining_time -1 )
def french_word(index_num):
    file = pd.read_csv("data/french_words.csv")
    file.to_dict(orient="records")
    word = file[index_num]['French']
    canvas.itemconfig(word_text, text=f"French: {word}")
    timer(2)

def english_word(index_num):
    # card_front = PhotoImage(file="images/card_front.png")
    # canvas.itemconfig(back_image, image=card_front)
    # file = pd.read_csv("data/french_words.csv")
    # new_word = file.French[index_num]
    # csv_dictionary = file.DataFrame.to_dict(orient='records')
    # new_ans = csv_dictionary[new_word]
    # canvas.itemconfig(word_text,text=f"English : {new_ans}")
    # canvas.grid(column=0, row=0, columnspan=2)

    card_front = PhotoImage(file="images/card_front.png")
    canvas.itemconfig(back_image, image=card_front)
    file = pd.read_csv("data/french_words.csv")
    dic_file= file.to_dict(orient="records")
    print(dic_file)
    new_word = file[index_num]["English"]
    canvas.itemconfig(word_text,text=f"English : {new_word}")
    canvas.grid(column=0, row=0, columnspan=2)






num = random_number()
french_word(num)

correct_image = PhotoImage(file="images/right.png")
right_button = Button(image=correct_image, highlightthickness=0)
right_button.grid(column=0, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
right_button = Button(image=wrong_image, highlightthickness=0)
right_button.grid(column=1, row=1)

wrong_button = Button()
window.mainloop()


