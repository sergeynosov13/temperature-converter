#I will using customtkinter for graphics
from customtkinter import *

#Creating window
window = CTk()
window.title("Temperature converter")
window.geometry("300x300")

#Convert function
def convert():
    gradus = int(input_entry.get())
    if choice_combobox.get() == "To Celsium":
        gradus = (gradus - 32) / 1.8
        result_lbl.configure(text=gradus)
    if choice_combobox.get() == "To Fahrenheit":
        gradus = gradus * 1.8 + 32
        result_lbl.configure(text=gradus)


#Objects
input_entry = CTkEntry(window, placeholder_text="Input temperature")
convert_btn = CTkButton(window, text="Convert!", command=convert)
choice_combobox = CTkComboBox(window, values = ["To Celsium", "To Fahrenheit"])
result_lbl = CTkLabel(window, text="")

#Placing objects
input_entry.grid(row=0, column=0, pady=7, padx=7)
choice_combobox.grid(row=0,column=1)
convert_btn.grid(row=1,column=0, padx=7, pady=7)
result_lbl.grid(row=1,column=1)

window.mainloop()