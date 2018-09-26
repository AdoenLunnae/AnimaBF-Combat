# -*-coding:utf-8-*-
import math


def getdmg(atq, aroll, base, deff, droll, ta, acu, numdef):
    if acu:
        abs = 20 + 10 * ta
        diff = 10 * math.trunc((atq + aroll - abs) / 10)
        if diff > 0:
            dmg = base * diff // 100
            if dmg > 0:
                return u'{}%. {} de daño'.format(diff, dmg)
            else:
                return u'No produce daño'
        elif diff < 0:
            return u'No produce daño'

    else:
        pendef=[0, -30, -50, -70, -90]
        totalat= atq+aroll
        totaldef= deff+droll+pendef[numdef]
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