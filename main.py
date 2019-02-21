# -*-coding:utf-8 -*-

import tkinter as tk
from tkinter import ttk
from func import *
from modif import *


class App:
    def __init__(self):
        # Create window
        self.raiz = tk.Tk()
        self.raiz.title("AnimaCombatHelper")
        self.raiz.resizable(0, 0)
        self.raiz.configure(bg='gray')
        notebook = ttk.Notebook(self.raiz)
        calc = ttk.Frame(notebook)
        mod = ttk.Frame(notebook)
        notebook.add(calc, text=u'Calculadora de daño')
        notebook.add(mod, text='Modificadores')
        notebook.pack(expand=1, fill='both')

    # ----------------Damage Calculator---------------- #
        # Create Labels
        atqframe = ttk.LabelFrame(calc, text='Atacante')
        defframe = ttk.LabelFrame(calc, text='Defensor')
        arolllabel = ttk.Label(atqframe, text='Tirada')
        atqlabel = ttk.Label(atqframe, text='Hab. Ataque')
        dmglabel = ttk.Label(atqframe, text=u'Daño base')
        drolllabel = ttk.Label(defframe, text='Tirada')
        deflabel = ttk.Label(defframe, text='Hab. Defensa')
        talabel = ttk.Label(defframe, text='TA')
        numdeflabel = ttk.Label(defframe, text=u'Defensa Nº')

        # Create Variables
        aroll, atq, dmg, droll = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar()
        deff, ta, acu, numdef = tk.StringVar(), tk.StringVar(), tk.IntVar(), tk.StringVar()
        aroll.set(0)
        droll.set(0)
        atq.set(0)
        deff.set(0)
        dmg.set(0)
        acu.set(0)

        # Create interactive fields
        arollbox = ttk.Entry(atqframe, width=12, textvariable=aroll)
        drollbox = ttk.Entry(defframe, width=12, textvariable=droll)
        atqbox = ttk.Entry(atqframe, width=12, textvariable=atq)
        defbox = ttk.Entry(defframe, width=12, textvariable=deff)
        dmgbox = ttk.Entry(atqframe, width=12, textvariable=dmg)
        taselect = ttk.Combobox(defframe, width=10, textvariable=ta)
        acubutton = ttk.Checkbutton(defframe, text=u'Acumulación', variable=acu)
        numdef = ttk.Combobox(defframe, width=10, textvariable=numdef)
        taselect['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        numdef['values'] = ('1', '2', '3', '4', '5+')
        taselect.current(0)
        numdef.current(0)

        # Place widgets
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

        final = ttk.Label(calc, text='No pasa nada')
        final.grid(column=0, row=2)

        acubutton.grid(column=0, row=2)
        numdeflabel.grid(column=1, row=2)
        numdef.grid(column=2, row=2)

    # ----------------Modifiers---------------- #
        # Create Frames
        atqmodframe = ttk.Labelframe(mod, text='Atacante', padding=(0, 0, 0, 227))
        defmodframe = ttk.Labelframe(mod, text='Defensor')

        # Create Labels
        atqnamelabel = ttk.Label(atqmodframe, text='Modificador')
        defnamelabel = ttk.Label(defmodframe, text='Modificador')
        atqhalflabel = ttk.Label(atqmodframe, text='Mitad')

        # Create Variables
        atqmodvars = []
        defmodvars = []
        atqmodhalfs = []
        for i in range(0, 23):
            aux = tk.IntVar()
            atqmodvars.append(aux)
            aux = tk.IntVar()
            atqmodhalfs.append(aux)
        for i in range(0, 35):
            aux = tk.IntVar()
            defmodvars.append(aux)

        # Create checkbuttons
        atqmodbuttons = []
        atqhalfbuttons = []
        defmodbuttons = []
        for i in range(0, 23):
            aux = ttk.Checkbutton(atqmodframe, text=list(modifatk.keys())[i], variable=atqmodvars[i], width=15)
            atqmodbuttons.append(aux)
            aux = ttk.Checkbutton(atqmodframe, variable=atqmodhalfs[i])
            atqhalfbuttons.append(aux)
        for i in range(0, 35):
            aux = ttk.Checkbutton(defmodframe, text=list(modifdef.keys())[i], variable=defmodvars[i], width=28)
            defmodbuttons.append(aux)

        # Place widgets
        atqmodframe.grid(column=0, row=0, padx=5)
        defmodframe.grid(column=1, row=0, padx=5)
        atqnamelabel.grid(column=0, row=0)
        atqhalflabel.grid(column=1, row=0)
        defnamelabel.grid(column=0, row=0)
        for i in range(0, 23):
            atqmodbuttons[i].grid(column=0, row=i+1)
            atqhalfbuttons[i].grid(column=1, row=i+1)
        for i in range(0, 35):
            defmodbuttons[i].grid(column=0, row=i+1)

        # -------------LOOP------------- #
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
                                            int(deff.get()), int(droll.get()), int(ta.get()),
                                            acu.get(), int(numdef.get()[0]), getmodat(atqmodvars,
                                            atqmodhalfs), getmoddef(defmodvars)))
            except ValueError:
                final.configure(text='No pasa nada')
            self.raiz.update_idletasks()
            self.raiz.update()




def main():
    window = App()
    return 0


if __name__ == '__main__':
    main()
