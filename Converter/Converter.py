from tkinter import *

window = Tk()
window.title("Converter")

window.config(padx=20, pady=20)



def click():
    number = entry.get()
    number = int(number) * 1.609
    result["text"] = round(number, 2)


entry = Entry()
entry.grid(column=2, row=1)

my_label = Label(text="Mile", font=("Arial", 10, "bold"))
my_label.grid(column=3, row=1)

button = Button(text="Calculate", font=("Arial", 10, "bold"))
button.grid(column=2, row=3)

result = Label(text=f"0", font=("Arial", 10, "bold"))
result.grid(column=2, row=2)

my_label_1 = Label(text=f"is equal", font=("Arial", 10, "bold"))
my_label_1.grid(column=1, row=2)

my_label_2 = Label(text=f"km", font=("Arial", 10, "bold"))
my_label_2.grid(column=3, row=2)

button = Button(text="Calculate", command=click, font=("Arial", 10, "bold"))
button.grid(column=2, row=3)



window.mainloop()
