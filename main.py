# -*-coding:utf-8 -*-

import math
import tkinter as tk
from tkinter import ttk


class App():
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

        aroll, atq, dmg, droll, deff, ta, acu = tk.StringVar(), tk.StringVar(), tk.StringVar(), tk.StringVar(), \
            tk.StringVar(), tk.StringVar(), tk.IntVar()
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
        taselect['values'] = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        taselect.current(0)

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
        final = ttk.Label(self.raiz, text='0')
        final.grid(column=0, row=2)
        acubutton.grid(column=1, row=2)
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
                final.configure(text=self.getdmg(int(atq.get()), int(aroll.get()), int(dmg.get()),
                                                          int(deff.get()), int(droll.get()), int(ta.get()), acu.get()))
            except ValueError:
                final.configure(text=0)
            self.raiz.update_idletasks()
            self.raiz.update()

    def getdmg(self, atq, aroll, base, deff, droll, ta, acu):
        if acu:
            abs = 20+10*ta
            diff = 10 * math.trunc((atq + aroll - abs) / 10)
            if diff > 0:
                dmg = base*diff//100
                if dmg > 0:
                    return u'{}%. {} de daño'.format(diff, dmg)
                else:
                    return u'No produce daño'
            elif diff < 0:
                return u'No produce daño'

        else:
            diff = 10*math.trunc((atq+aroll-deff-droll)/10)
            if diff > 0:
                abso = 20+10*ta
                diff -= abso
                dmg = base*diff//100
                if dmg > 0:
                    return '{}%. {} de daño'.format(diff, dmg)
                else:
                    return 'A la defensiva'
            elif diff < 0:
                contr = -diff//2
                return 'Contraataque con +{}'.format(contr)



def main():
    window = App()
    return 0


if __name__ == '__main__':
    main()
