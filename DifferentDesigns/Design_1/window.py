from tkinter import *


def btn_clicked():
    print("Button Clicked")


window = Tk()

window.geometry("600x440")
window.configure(bg = "#ffffff")
canvas = Canvas(
    window,
    bg = "#ffffff",
    height = 440,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge")
canvas.place(x = 0, y = 0)

background_img = PhotoImage(file = f"images/background.png")
background = canvas.create_image(
    300.0, 220.0,
    image=background_img)

entry0_img = PhotoImage(file = f"images/img_textBox0.png")
entry0_bg = canvas.create_image(
    449.5, 156.0,
    image = entry0_img)

entry0 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry0.place(
    x = 345.0, y = 137,
    width = 209.0,
    height = 36)

entry1_img = PhotoImage(file = f"images/img_textBox1.png")
entry1_bg = canvas.create_image(
    449.5, 228.0,
    image = entry1_img)

entry1 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry1.place(
    x = 345.0, y = 209,
    width = 209.0,
    height = 36)

entry2_img = PhotoImage(file=f"images/img_textBox2.png")
entry2_bg = canvas.create_image(
    449.5, 300.0,
    image = entry2_img)

entry2 = Entry(
    bd = 0,
    bg = "#d9d9d9",
    highlightthickness = 0)

entry2.place(
    x = 345.0, y = 281,
    width = 209.0,
    height = 36)

img0 = PhotoImage(file = f"images/img0.png")
b0 = Button(
    image = img0,
    borderwidth = 0,
    highlightthickness = 0,
    command = btn_clicked,
    relief = "flat")

b0.place(
    x = 335, y = 342,
    width = 229,
    height = 38)

window.resizable(False, False)
window.mainloop()
