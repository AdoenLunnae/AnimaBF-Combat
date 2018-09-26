# -*-coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
from func import *


class App:
    def __init__(self):
        self.raiz = tk.Tk()
        self.raiz.title("AnimaCombatHelper")
        self.raiz.resizable(0, 0)
        self.raiz.configure(bg='gray')

        atqframe = ttk.LabelFrame(self.raiz, text='Atacante')
        defframe = ttk.LabelFrame(self.raiz, text='Defensor')
        arolllabel = ttk.Label(atqframe, text='Tirada')
        atqlabel = ttk.Label(atqframe, text='Hab. Ataque')
        dmglabel = ttk.Label(atqframe, text=u'Daño base')
        drolllabel = ttk.Label(defframe, text='Tirada')
        deflabel = ttk.Label(defframe, text='Hab. Defensa')
        talabel = ttk.Label(defframe, text='TA')
        numdeflabel = ttk.Label(defframe, text=u'Defensa Nº')

        aroll, atq, dmg, droll, deff, ta, acu, numdef = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), \
            tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.StringVar()
        aroll.set(0)
        droll.set(0)
        atq.set(0)
        deff.set(0)
        dmg.set(0)
        acu.set(0)
        arollbox = ttk.Entry(atqframe, width=12, textvariable=aroll)
        drollbox = ttk.Entry(defframe, width=12, textvariable=droll)
        atqbox = ttk.Entry(atqframe, width=12, textvariable=atq)
        defbox = ttk.Entry(defframe, width=12, textvariable=deff)
        dmgbox = ttk.Entry(atqframe, width=12, textvariable=dmg)
        taselect = ttk.Combobox(defframe, width=10, textvariable=ta)
        acubutton = ttk.Checkbutton(defframe, text=u'Acumulación', variable=acu)
        numdef = ttk.Combobox(defframe, width=10, textvariable=numdef)
        taselect['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        numdef['values'] = (u'1ª', u'2ª', u'3ª', u'4ª', u'5ª+')
        taselect.current(0)
        numdef.current(0)

        atqframe.grid(column=0, row=0)
        defframe.grid(column=0, row=1)

        arolllabel.grid(column=0, row=0)
        atqlabel.grid(column=1, row=0)
        dmglabel.grid(column=2, row=0)
        arollbox.grid(column=0, row=1)
        atqbox.grid(column=1, row=1)
        dmgbox.grid(column=2, row=1)

        drolllabel.grid(column=0, row=0)
        deflabel.grid(column=1, row=0)
        talabel.grid(column=2, row=0)
        drollbox.grid(column=0, row=1)
        defbox.grid(column=1, row=1)
        taselect.grid(column=2, row=1)
        final = ttk.Label(self.raiz, text='No pasa nada')
        final.grid(column=0, row=2)
        acubutton.grid(column=0, row=2)
        numdeflabel.grid(column=1, row=2)
        numdef.grid(column=2, row=2)
        while 1:
            if acu.get():
                deff.set(0)
                droll.set(0)
                defbox.configure(state='disabled')
                drollbox.configure(state='disabled')
            else:
                defbox.configure(state='normal')
                drollbox.configure(state='normal')
            try:
                final.configure(text=getdmg(int(atq.get()), int(aroll.get()), int(dmg.get()),
                                            int(deff.get()), int(droll.get()), int(ta.get()), acu.get(), int(numdef.get()[0])))
            except ValueError:
                final.configure(text='No pasa nada')
            self.raiz.update_idletasks()
            self.raiz.update()


def main():
    window = App()
    return 0


if __name__ == '__main__':
    main()
