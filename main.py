from tkinter import *
import winsound
clicks = 0
doubleclicker = "no"
autoclicker = "no"
trackpadskin = "no"
clicksound = 'mouseclick.wav'
buttonsound = 'buttonpress.wav'
errorsound = 'error.wav'
def sel1():
    print("sus1")
def sel2():
    if trackpadskin == "no":

def updateclickbutton():
    if trackpadskin == "no":
        clickbutton.config(command=click,image=(mousephoto),compound='top',relief=RAISED)
        clickbutton.pack()
    else:
        clickbutton.config(command=click, image=(trackpadphoto), compound='top', relief=RAISED)
        clickbutton.pack()
def updateclicks():
    clicklabel.config(text=clicks, font=('Segoe UI', 40))
    clicklabel.pack()
def messagedestroy():
    global messages
    messages.config(text="")
def click():
    global clicks
    if doubleclicker == "no":
        clicks += 1
    else:
        clicks += 2
    updateclickbutton()
    updateclicks()
    winsound.PlaySound(clicksound, winsound.SND_FILENAME)
    messagedestroy()
def doublebuybuttonpressed():
    global doubleclicker
    global messages
    global clicks
    if doubleclicker == "yes":
        messages.config(text="You have already bought this...", font=('Segoe UI', 20))
        messages.pack()
        winsound.PlaySound(errorsound, winsound.SND_FILENAME)
    elif clicks >= 100:
        messages.config(text="You can now get two clicks from just one!",font=('Segoe UI',20))
        messages.pack()
        clicks -= 100
        doubleclicker = "yes"
        updateclicks()
        winsound.PlaySound(buttonsound, winsound.SND_FILENAME)
    elif clicks < 100:
        howmuchleft = 100 - clicks
        messages.config(text="You don't have enough clicks, you need " + str(howmuchleft) + " more clicks.",font=('Segoe UI',20))
        messages.pack()
        winsound.PlaySound(errorsound, winsound.SND_FILENAME)
def trackpadbuybuttonpressed():
    global trackpadskin
    global messages
    global clicks
    if trackpadskin == "yes":
        messages.config(text="You have already bought this...", font=('Segoe UI', 20))
        messages.pack()
        winsound.PlaySound(errorsound, winsound.SND_FILENAME)
    elif clicks >= 10:
        messages.config(text="You got the trackpad skin, it does nothing!",font=('Segoe UI',20))
        messages.pack()
        clicks -= 10
        trackpadskin = "yes"
        updateclickbutton()
        updateclicks()
        winsound.PlaySound(buttonsound, winsound.SND_FILENAME)
    elif clicks < 10:
        howmuchleft = 10 - clicks
        messages.config(text="You don't have enough clicks, you need " + str(howmuchleft) + " more clicks.",font=('Segoe UI',20))
        messages.pack()
        winsound.PlaySound(errorsound, winsound.SND_FILENAME)
window = Tk()
window.geometry("650x510")
window.title("Mouse Clicker")
icon = PhotoImage(file='logo.png')
window.iconphoto(True,icon)
mousephoto = PhotoImage(file='computermouse.png')
trackpadphoto = PhotoImage(file='trackpad.png')
clicklabel = Label(window,text=clicks,font=('Segoe UI',40))
clickbutton = Button(window,command=click,image=(mousephoto),compound='top',relief=RAISED)
doublebuybutton = Button(window,text="Buy a double clicker",font=('Segoe UI',20),command=doublebuybuttonpressed,compound='bottom',relief=RAISED)
trackpadbuybutton = Button(window,text="Buy a trackpad cosmetic skin",font=('Segoe UI',20),command=trackpadbuybuttonpressed,compound='bottom',relief=RAISED)
messages = Label(window,text="")
var = IntVar()
R1 = Radiobutton(window, text="Mouse", variable=var, value=1,
                  command=sel1)
R2 = Radiobutton(window, text="Trackpad", variable=var, value=2,
                  command=sel2)
clicklabel.pack()
clickbutton.pack()
doublebuybutton.pack()
trackpadbuybutton.pack()
messages.pack()
R1.pack()
R2.pack()
window.mainloop()
clicklabel.mainloop()
doublebuybutton.mainloop()
trackpadbuybutton.mainloop()
messages.mainloop()
