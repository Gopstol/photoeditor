from PIL import Image, ImageFilter, ImageTk, ImageDraw, ImageFont, FontFile
from tkinter import Tk, Scale, Button, filedialog, Menu, Label, colorchooser
from tkinter.filedialog import askopenfilename, asksaveasfile
import tkinter
import os
import sys
import pyautogui
import tkinter.ttk
from tkinter import messagebox as mbox
import easygui

x, y = pyautogui.position()


root = Tk()
root.title("Gopped edit")

sx = ''
sy = ''
global name

fi = open('./history/filepath.txt', 'r+')

name = fi.read()
fi.close()

savepath = '/home/dan/PycharmProjects/GraphicProjects/GopPackage/history/1.jpg'
menu = Menu(root, relief='flat')
root.config(menu=menu)

coor = x, y

image_width = 600

# MENU MENU MENU


def bw():
    grayscale_image = image.convert("L")
    grayscale_image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def conture():
    con = image.filter(ImageFilter.CONTOUR)
    con.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def emboss():
    con = image.filter(ImageFilter.EMBOSS)
    con.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def blur():
    con = image.filter(ImageFilter.BLUR)
    con.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def textfinal(size, text, hx):
    textfont = ImageFont.truetype('/home/dan/PycharmProjects/GraphicProjects/GopPackage/fonts/natural.ttf', int(size))
    ImageDraw.Draw(image).text((scalex.get(), scaley.get()), text, fill=hx, font=textfont, align="left")
    image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def textoptions():
    (rgb, hx) = colorchooser.askcolor()
    newwindow = tkinter.Toplevel(root)
    labelexample = tkinter.Label(newwindow, text="Текст", font=("Arial Bold", 20))
    entryexample = tkinter.Entry(newwindow)
    labelexample1 = tkinter.Label(newwindow, text="Размер", font=("Arial Bold", 20))
    entryexample1 = tkinter.Entry(newwindow)
    buttonok = tkinter.Button(newwindow, text="Применить", command=lambda: textfinal(entryexample1.get(), entryexample.get(), hx))

    labelexample.grid(column=0, row=0)
    entryexample.grid(column=0, row=1)
    labelexample1.grid(column=1, row=0)
    entryexample1.grid(column=1, row=1)
    buttonok.grid(column=0, row=2, columnspan=2)
    # return entryexample.get(), entryexample1.get()
    # newwindow.mainloop()


def imagefinal(way, xy):
    pasted = Image.open(way)
    xy = (int(xy[0]), int(xy[1]))
    pasted = pasted.resize(xy)
    print(xy)
    Image.Image.paste(image, pasted, (scalex.get(), scaley.get()))
    image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def imageoptions():
    way = easygui.fileopenbox(filetypes=["*.jpg"])
    newwindow = tkinter.Toplevel(root)
    labelexample = tkinter.Label(newwindow, text="Размер", font=("Arial Bold", 20))
    entryexample = tkinter.Entry(newwindow)
    labelexample1 = tkinter.Label(newwindow, text="Ширина X Высота", font=("Arial Bold", 8))
    print((str(image.size[0]), str(image.size[1])))
    size1 = (str(image.size[0]))
    size2 = (str(image.size[1]))
    labelexample2 = tkinter.Label(newwindow, text=size1+'X'+size2, font=("Arial Bold", 8))
    buttonok = tkinter.Button(newwindow, text="Применить", command=lambda: imagefinal(way,
                                                                                      (entryexample.get()).split('X')))

    labelexample.grid(column=0, row=0)
    entryexample.grid(column=0, row=1)
    labelexample1.grid(column=0, row=2)
    labelexample2.grid(column=0, row=3)
    buttonok.grid(column=0, row=4, columnspan=2)


def openfile():
    name = easygui.fileopenbox(filetypes=["*.jpg"])
    image = Image.open(name)
    image.save(savepath)
    fi = open('./history/filepath.txt', 'r+')
    os.system(r' >./history/filepath.txt')
    fi.write(name)
    fi.close()
    f.write('0')
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def newfinale(hx, size):
    image = Image.new(mode='RGB', size=(int(size[0]), int(size[1])), color=hx)
    image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def newfile():
    (rgb, hx) = colorchooser.askcolor()
    newwindow = tkinter.Toplevel(root)
    labelexample = tkinter.Label(newwindow, text="Размер", font=("Arial Bold", 20))
    entryexample = tkinter.Entry(newwindow)
    labelexample1 = tkinter.Label(newwindow, text="Ширина X Высота", font=("Arial Bold", 8))

    buttonok = tkinter.Button(newwindow, text="Применить", command=lambda: newfinale(hx,
                                                                                      (entryexample.get()).split('X')))

    labelexample.grid(column=0, row=0)
    entryexample.grid(column=0, row=1)
    labelexample1.grid(column=0, row=2)
    buttonok.grid(column=0, row=3, columnspan=2)


def savefile():
    saved = asksaveasfile(mode='w', defaultextension=".jpg")
    if saved is None:  # asksaveasfile return `None` if dialog closed with "cancel".
        return


def cropround(s, image):
    s = list(s)
    s[0] = int(s[0])
    s[1] = int(s[1])
    w, h = image.size
    k = w / s[0] - h / s[1]
    if k > 0:
        image = image.crop(((w - h) / 2, 0, (w + h) / 2, h))
    elif k < 0:
        image = image.crop((0, (h - w) / 2, w, (h + w) / 2))
    antialias = 2
    mask = Image.new('L', (size[0] * antialias, size[1] * antialias), 0)
    ImageDraw.Draw(mask).ellipse((0, 0) + mask.size, fill=255)
    mask.resize(size, Image.ANTIALIAS)
    image = mask
    image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def cropmenu(text, image):
    newwindow = tkinter.Toplevel(root)
    labelexample = tkinter.Label(newwindow, text="Размер", font=("Arial Bold", 20))
    entryexample = tkinter.Entry(newwindow)
    if text == 'Радиус':
        buttonok = tkinter.Button(newwindow, text="Применить", command=lambda: (cropround((entryexample.get(), entryexample.get()), image)))

    labelexample1 = tkinter.Label(newwindow, text=text, font=("Arial Bold", 8))

    labelexample.grid(column=0, row=0)
    entryexample.grid(column=0, row=1)
    labelexample1.grid(column=0, row=2)
    buttonok.grid(column=0, row=3, columnspan=2)


filemenu = Menu(menu, tearoff=0, relief='flat', bd='1')
filtermenu = Menu(menu, tearoff=0, relief='flat', bd='1')
textmenu = Menu(menu, tearoff=0, relief='flat', bd='1')
formmenu = Menu(menu, tearoff=0, relief='flat', bd='1')
menu.add_cascade(label="Файл", menu=filemenu)
menu.add_cascade(label="Фильтры", menu=filtermenu)
menu.add_cascade(label="Вставка", menu=textmenu)
menu.add_cascade(label="Форма", menu=formmenu)


filemenu.add_command(label="Сохранить", command=savefile)
filemenu.add_command(label="Открыть", command=openfile)
filemenu.add_command(label="Создать пустой проект", command=newfile)

filtermenu.add_command(label="Оттенки серого", command=bw)
filtermenu.add_command(label="Контур", command=conture)
filtermenu.add_command(label="Эмбосс", command=emboss)
filtermenu.add_command(label="Размытие", command=blur)

textmenu.add_command(label="Текст", command=textoptions)
textmenu.add_command(label="Картинка", command=imageoptions)

formmenu.add_command(label="Круг", command=lambda: cropmenu('Радиус', image))


# DEF DEF DEF


def openfile():
    name = askopenfilename(initialdir="/GopPackage/",
                           filetypes=(("Text File", "*.jpg"), ("All Files", "*.*")),
                           title="Choose a file."
                           )
    print(name)


def cropul():
    new_image = image.crop((0, 0, (scalex.get()), (scaley.get())))
    new_image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def cropur():
    new_image = image.crop((scalex.get(), 0, int(size[0]*(image_width/size[1])), (scaley.get())))
    new_image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def cropdl():
    new_image = image.crop((0, (scaley.get()), (scalex.get()), image_width))
    new_image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def cropdr():
    new_image = image.crop(((scalex.get()), (scaley.get()), int(size[0]*(image_width/size[1])), image_width))
    new_image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def rotatea():
    new_image = image.rotate(90)
    new_image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def rotateb():
    new_image = image.rotate(270)
    new_image.save(savepath)
    f.write('1')
    print(f.read())
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def origin():
    f.write('0')
    f.close()
    python = sys.executable
    os.execl(python, python, *sys.argv)


def addtext():
    pass


def onchoose():
    (rgb, hx) = colorchooser.askcolor()


f = open('./history/history.txt', 'r+')
if f.read()[-1] == '0':
    image = Image.open(name)
    orig_size = image.size
else:
    image = Image.open(savepath)
    print(savepath)

size = image.size

draw = ImageDraw.Draw(image)  # Создаем инструмент для рисования
pix = image.load()  # Выгружаем значения пикселей


print(size)
canvas = tkinter.Canvas(root, height=image_width, width=int(size[0]*(image_width/size[1])))
image = image.resize((int(size[0]*(image_width/size[1])), image_width))
photo = ImageTk.PhotoImage(image)
image_n = canvas.create_image(0, 0, anchor='nw', image=photo)
canvas.grid(row=0, column=0, columnspan=4)

scaley = Scale(from_=0, to=image_width, length=image_width, variable=sy)
scalex = Scale(from_=0, to=int(size[0]*(image_width/size[1])), orient="horizontal", length=(int(size[0]*(image_width/size[1]))), variable=sx)
btnul = Button(root, font=("Arial Bold", 20), command=cropul, text="ВЛ")
btnur = Button(root, font=("Arial Bold", 20), command=cropur, text="ВП")
btndl = Button(root, font=("Arial Bold", 20), command=cropdl, text="НЛ")
btndr = Button(root, font=("Arial Bold", 20), command=cropdr, text="НП")

btnrota = Button(root, font=("Arial Bold", 20), command=rotatea, text="<-90")
btnrotb = Button(root, font=("Arial Bold", 20), command=rotateb, text="90->")

btnopen = Button(root, font=("Arial Bold", 20), command=openfile, text="Открыть")

btnorig = Button(root, font=("Ubuntu Bold", 20), command=origin, text="Оригинал")

lblcursor = Label(root, font=("Ubuntu Light", 15), text=coor)

btntext = Button(root, font=("Ubuntu Bold", 20), command=addtext, text="Текст")

scaley.grid(column=5, row=0)
scalex.grid(column=0, row=1, columnspan=4, sticky='W')

btnul.grid(column=0, row=2, sticky='E')
btnur.grid(column=1, row=2, sticky="W")
btndl.grid(column=0, row=3, sticky='E')
btndr.grid(column=1, row=3, sticky='W')

btnrota.grid(column=0, row=4, sticky='E')
btnrotb.grid(column=1, row=4, sticky='W')

# btnopen.grid(column=6, row=0)

btnorig.grid(column=6, row=0)

lblcursor.grid(column=0, row=5, sticky='W')

#btntext.grid(column=0, row=7)


def print_widget_under_mouse(root):
    try:
        x, y = canvas.winfo_pointerxy()
        widget = root.winfo_containing(x, y)
        y = y-60
        x = x-1
        if widget == canvas:
            lblcursor['text'] = (x, y)
        root.after(10, print_widget_under_mouse, root)
    except:
        root.after(100, print_widget_under_mouse, root)


print_widget_under_mouse(root)

root.mainloop()
