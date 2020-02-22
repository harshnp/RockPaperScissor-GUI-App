from tkinter import *
import random

root = Tk()

dis2 = {
    "StoneStone": "Computer Choosed Stone Draw!",
    "StonePaper": "Computer Choosed Paper, so you Loose!",
    "StoneScissor": "Computer Choosed Scissor, so you Win!",
    "PaperStone": "Computer Choosed Stone, so you Win!",
    "PaperPaper": "Computer Choosed Paper, Draw!",
    "PaperScissor": "Computer Choosed Scissor, so you Loose!",
    "ScissorStone": "Computer Choosed Stone, So you Loose!",
    "ScissorPaper": "Computer Choosed Paper, so you Win!",
    "ScissorScissor": "Computer Choosed Scissor, Draw!"

}


def comp_choice(a):
    choices = ("Stone", "Paper", "Scissor")
    str1 = random.choice(choices)
    match = a + str1
    msg = dis2.get(match)
    msg_display = Message(root, text=msg)
    msg_display.grid(row=4, column=0, columnspan=4)


Title = root.title("Stone Paper Scissor")
root.geometry("150x250")

label0 = Label(root, text="****Select A option****")
label0.grid(row=0, column=0)

stoneBtn = Button(root, text="Stone", fg="red", bg="black", command=lambda: comp_choice("Stone"))
stoneBtn.grid(row=1, column=0, pady=3)

papperBtn = Button(root, text="Paper", fg="red", bg="black", command=lambda: comp_choice("Paper"))
papperBtn.grid(row=2, column=0, pady=3)

sissorBtn = Button(root, text="Scissor", fg="red", bg="black", command=lambda: comp_choice("Scissor"))
sissorBtn.grid(row=3, column=0, pady=3)

label1 = Label(root, text="Computer Chooses:")

root.mainloop()
