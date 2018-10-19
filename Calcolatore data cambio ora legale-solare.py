# -*- coding: cp1252 -*-

import calendar

print("Calcolatore giorno cambio ora legale/solare e viceversa\n")
str_anno = input("Inserire l'anno di cui si vogliono sapere le date\n==>")

anno = int (str_anno)

month = calendar.monthcalendar(anno, 3)
giorno_di_marzo = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
month = calendar.monthcalendar(anno, 10)
giorno_di_ottobre = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
month = calendar.monthcalendar(anno + 1, 3)
giorno_inizio_ora_legale = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
month = calendar.monthcalendar(anno - 1, 10)
giorno_inizio_ora_solare = max(month[-1][calendar.SUNDAY], month[-2][calendar.SUNDAY])
print("L'ora solare è iniziata il " + str(giorno_inizio_ora_solare) + " ottobre " + str(anno - 1))
print("Il cambio dall'ora solare a quella legale avverrà il " + str(giorno_di_marzo) + " marzo " + str(anno) + ": alle ore 02:00 gli orologi andranno portati avanti di un'ora\nIl cambio dall'ora legale a quella solare avverrà il " + str(giorno_di_ottobre) + " ottobre " + str(anno) + ": alle ore 03:00 gli orologi andranno portati indietro di un'ora")
print("L'ora solare sarà in vigore fino al " + str(giorno_inizio_ora_legale) + " marzo " + str(anno + 1))
