from tkinter import *
import qrcode

root =Tk()
root.title("QR Generator")
root.geometry("1000x550")
root.config(bg="#AE2321")
root.resizable(False,False)

#icon image
icon=PhotoImage(file="icon.png")
root.iconphoto(False,icon)


def generate():
    name=title.get()
    qr=qrcode.make(entry.get())
    qr.save("QR Codes/"+str(name)+".png")

    global Image
    Image=PhotoImage(file="QR Codes/"+str(name)+".png")
    Image_view.config(image=Image,borderwidth=4,relief=RAISED)



Image_view=Label(root,bg="#AE2321",borderwidth=4,border=1)
Image_view.pack(padx=50,pady=10,side=RIGHT)
Label(root,text="Title",fg="white",bg="#AE2321",font=15).place(x=50,y=170)
title=Entry(root,width=13,font="arial 15 bold",borderwidth=3)
title.place(x=50,y=200)

entry = Entry(root,width=28,font="arial 15 bold",borderwidth=3)
entry.place(x=50,y=250)

Label(root,text="URL",fg="white",bg="#AE2321",font=15).place(x=380,y=250)
Button(root,text="Generate",width=20,height=2,bg="black",borderwidth=3,fg="white",command=generate).place(x=50,y=300)
Label(root,text="QR Generator",fg="white",bg="#AE2321",font="arial 30 bold",borderwidth=4,relief=RAISED,padx=10,pady=20).place(x=50,y=50)
root.mainloop()
