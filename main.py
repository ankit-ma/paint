from tkinter import *
from tkinter import filedialog
from tkinter import font
import PIL
from PIL import ImageTk,Image,ImageDraw,ImageGrab

root = Tk()
root.geometry("1000x500")
root.minsize(1000,500)
root.maxsize(1000,500)
root.title("Paint")
#paint function
def paint(event):
    # get x1, y1, x2, y2 co-ordinates
    x1, y1 = (event.x-3), (event.y-3)
    x2, y2 = (event.x+3), (event.y+3)
    color = "black"
    # display the mouse movement inside canvas
    paintWindow.create_oval(x1, y1, x2, y2, fill=color, outline=color)


#newfile function
def newfile():
    paintWindow.delete('all')

#save canvas
def saveimage():
    image_file = filedialog.asksaveasfilename(defaultextension=".eps", initialdir="/Users/ankitsharma/Desktop/java code/python code/voice assistant/Paint",filetypes=(("EPS file","*.eps"),("All files","*.*")))
    if image_file:
        #imgq=image_file.replace(".eps","")
        paintWindow.postscript(file=image_file)
        # use PIL to convert to PNG
        img = Image.open(image_file)
        imgq = image_file.replace(".eps", "")
        img.save(imgq+'.png','png')


#create menu
menu_bar = Menu(root)
root.config(menu=menu_bar)
#file menu
file_menu=Menu(menu_bar)
menu_bar.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=newfile)
file_menu.add_command(label="Save",command=saveimage)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)
#paint window
paintWindow = Canvas(root,width=1000,height=500,bg='white')

paintWindow.bind('<B1-Motion>',paint)
paintWindow.pack()


root.mainloop()