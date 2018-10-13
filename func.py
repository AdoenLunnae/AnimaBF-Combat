# -*-coding:utf-8-*-
import math
from modif import *


def getdmg(atq, aroll, base, deff, droll, ta, acu, numdef, modatq, moddef):
    if acu:
        abso = 20 + 10 * ta
        diff = 10 * math.trunc((atq + aroll + modatq - abso) / 10)
        if diff > 0:
            dmg = base * diff // 100
            if dmg > 0:
                return u'{}%. {} de daño'.format(diff, dmg)
            else:
                return u'No produce daño'
        elif diff < 0:
            return u'No produce daño'

    else:
        pendef = [0, -30, -50, -70, -90]
        totalat = atq + aroll + modatq
        totaldef = deff + droll + pendef[numdef-1] + moddef
        diff = 10 * math.trunc((totalat-totaldef) / 10)
        if diff > 0:
            abso = 20 + 10 * ta
            diff -= abso
            dmg = base * diff // 100
            if dmg > 0:
                return '{}%. {} de daño'.format(diff, dmg)
            else:
                return 'A la defensiva'
        elif diff < 0:
            contr = -diff // 2
            return 'Contraataque con +{}'.format(contr)


def getmodat(varlist, halflist):
    mod = 0
    for i in range(0, 23):
        mod += modifatk[list(modifatk.keys())[i]] * varlist[i].get() / (halflist[i].get() + 1)
    return mod


def getmoddef(varlist):
    mod = 0
    for i in range(0, 35):
        mod += modifdef[list(modifdef.keys())[i]] * varlist[i].get()
    return mod


