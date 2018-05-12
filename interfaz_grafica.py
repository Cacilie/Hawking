#!/usr/bin/env python
# -*- coding: utf-8 -*-
import threading
import time
from Tkinter import *

alfabeto = [["A", "B", "C", "D", "E", "F", "G"], ["H", "I", "J", "K", "L", "LL", "M"], ["N", u"Ñ", "O", "P", "Q", "R", "S"], ["T", "U", "V", "W", "X", "Y", "Z"]]
fila_seleccionada = 0
columna_seleccionada = -1
repetir_fila = True
repetir_columna = False

def do_slow_stuff():
    global fila_seleccionada, columna_seleccionada
    while(True):
        if(columna_seleccionada == -1):
            while(repetir_fila):    
                for z in range(len(selfbutton[fila_seleccionada])):
                    if(not(repetir_fila)):
                        break
                    if(fila_seleccionada == 0):
                        for a in range(len(selfbutton[5])):
                            selfbutton[5][a].config(bg = "#bbb")
                    else:
                        for a in range(len(selfbutton[fila_seleccionada-1])):
                            selfbutton[fila_seleccionada-1][a].config(bg = "#bbb")
                    selfbutton[fila_seleccionada][z].config(bg = "#e86a6a")
                time.sleep(1.5)
                if(columna_seleccionada == -1):
                    if(fila_seleccionada < 5):
                        fila_seleccionada = fila_seleccionada + 1
                    else:
                        fila_seleccionada = 0
        else:
            for a in range(len(selfbutton[fila_seleccionada])):
                selfbutton[fila_seleccionada][a].config(bg = "#bbb")
            while(repetir_columna):
                for b in range(len(selfbutton[fila_seleccionada])):
                    if not(repetir_columna):
                        break
                    columna_seleccionada = b
                    if (b>0):
                        selfbutton[fila_seleccionada][b-1].config(bg = "#bbb")
                    else:
                        selfbutton[fila_seleccionada][len(selfbutton[fila_seleccionada]) - 1].config(bg = "#bbb")
                    selfbutton[fila_seleccionada][b].config(bg = "#e86a6a")
                    time.sleep(1.5)


def do_slow_stuff_2():
    global repetir_columna, repetir_fila, columna_seleccionada, fila_seleccionada, string_var
    if(columna_seleccionada == -1):
        repetir_fila = False
        repetir_columna = True
        columna_seleccionada = 0
    else:
        texto_actual = text_input.get()
        if(fila_seleccionada < 4):
            texto_actual = texto_actual + alfabeto[fila_seleccionada][columna_seleccionada]
        elif(fila_seleccionada == 4 and columna_seleccionada == 0):
            texto_actual = texto_actual + " "
        elif(fila_seleccionada == 4 and columna_seleccionada == 1):
            texto_actual = texto_actual[:-1]
        elif(fila_seleccionada == 5 and columna_seleccionada == 1):
            texto_actual = ""
        text_input.delete(0, END)
        text_input.insert(0, texto_actual)
        
        selfbutton[fila_seleccionada][columna_seleccionada].config(bg = "#bbb")
        
        fila_seleccionada = 0
        columna_seleccionada = -1
        repetir_columna = False
        repetir_fila = True


def check_if_ready(thread):
    print('check')
    if thread.is_alive():
        # not ready yet, run the check again soon
        root.after(200, check_if_ready, thread)

def start_doing_slow_stuff():
    thread = threading.Thread(target=do_slow_stuff)
    thread.start()
    root.after(200, check_if_ready, thread)


root = Tk()
root.title("Proyecto vision")
root.geometry("600x400")
frame=Frame(root)
Grid.rowconfigure(root, 0, weight=1)
Grid.columnconfigure(root, 0, weight=1)
frame.grid(row=0, column=0, sticky=N+S+E+W)
grid=Frame(frame)
grid.grid(sticky=N+S+E+W, column=0, row=7, columnspan=2)
Grid.rowconfigure(frame, 7, weight=1)
Grid.columnconfigure(frame, 0, weight=1)

selfbutton = [[0 for x in xrange(7)] for x in xrange(4)] 
selfbutton.append([0,0])
selfbutton.append([0,0])
buttonoptions = [[0 for x in xrange(2)] for x in xrange(2)]
#example values
for x in range(7):
    for y in range(4):
        selfbutton[y][x] = Button(frame, bg="#bbb", text=alfabeto[y][x])
        selfbutton[y][x].grid(column=x, row=y, sticky=N+S+E+W)

botones_opciones= [["Espacio", "Borrar"], ["Enviar", "Reset"]]

for x in range(2):
    for y in range(2):
        selfbutton[y+4][x] = Button(frame, bg="#bbb", text=botones_opciones[y][x])
        if(x == 0):
            selfbutton[y+4][x].grid(column=x, row=y+4, columnspan=3, sticky=N+S+E+W)
        else:
            selfbutton[y+4][x].grid(column=x+3, row=y+4, columnspan=3, sticky=N+S+E+W)

label = Label(frame, text="Texto").grid(column=0, row=7, sticky=N+S+E+W)

#string_var = StringVar()
text_input = Entry(frame)
text_input.grid(column=1, row=7, columnspan=6, sticky=N+S+E+W)

boton_final = Button(frame, bg="#00dd80", text="Ejecutar", command=do_slow_stuff_2)
boton_final.grid(column=0, row=8, columnspan=2, sticky=N+S+E+W)

for x in range(7):
    Grid.columnconfigure(frame, x, weight=1)

for y in range(9):
    Grid.rowconfigure(frame, y, weight=1)


start_doing_slow_stuff()
root.mainloop()