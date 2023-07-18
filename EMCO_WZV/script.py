# WZV
# Python 3.10.6 64-bit
# pip install openpyxl

from argparse import Namespace
from openpyxl import Workbook
from datetime import date

print("-- Easy Fanuc WZV by Vidmar P. --")
datei = open('PRNT0001.dat', 'r')
WerkzeugDornDaten = datei.readline()
Messung1 = datei.readline()
m1 = [float(Messung1[4:11]), float(Messung1[15:22]),
      float(Messung1[26:33]), float(Messung1[37:44])]
Messung2 = datei.readline()
m2 = [float(Messung2[4:11]), float(Messung2[15:22]),
      float(Messung2[26:33]), float(Messung2[37:44])]
Messung3 = datei.readline()
m3 = [float(Messung3[4:11]), float(Messung3[15:22]),
      float(Messung3[26:33]), float(Messung3[37:44])]
Messung4 = datei.readline()
m4 = [float(Messung4[4:11]), float(Messung4[15:22]),
      float(Messung4[26:33]), float(Messung4[37:44])]
Messung5 = datei.readline()
m5 = [float(Messung5[4:11]), float(Messung5[15:22]),
      float(Messung5[26:33]), float(Messung5[37:44])]
# T7 - T8 Offen
MessungT5 = 0
MessungT6 = 0
MessungT7 = 0
MessungT8 = 0
# offen -Fanuc Daten Fehlen

Maschinennummer = input("Bitte Maschinennummer eingeben:  ")
Name = input("Bitte Namen eingeben:  ")

excel = Workbook()
blatt = excel.active
blatt.column_dimensions['A'].width = 20
blatt["A1"] = "Maschinennummer:"
blatt["B1"] = Maschinennummer
blatt["A2"] = "Datum:"
blatt["B2"] = str(date.today())
blatt["A3"] = "Techniker:"
blatt["B3"] = Name

blatt["A5"] = "Einstelllehre"
blatt["A6"] = "A = 500"
blatt["B6"] = float(WerkzeugDornDaten[4:11])
blatt["A7"] = "B = 501"
blatt["B7"] = float(WerkzeugDornDaten[15:22])
blatt["A8"] = "C = 508"
blatt["B8"] = float(WerkzeugDornDaten[26:33])
blatt["A9"] = "C = 509"
blatt["B9"] = float(WerkzeugDornDaten[37:44])

blatt["A11"] = "Wiederholgenauigkeit kalibrieren"

blatt["A12"] = "Messung 1"
blatt["B12"] = m1[0]
blatt["C12"] = m1[1]
blatt["D12"] = m1[2]
blatt["E12"] = m1[3]

blatt["A13"] = "Messung 2"
blatt["B13"] = m2[0]
blatt["C13"] = m2[1]
blatt["D13"] = m2[2]
blatt["E13"] = m2[3]

blatt["A14"] = "Messung 3"
blatt["B14"] = m3[0]
blatt["C14"] = m3[1]
blatt["D14"] = m3[2]
blatt["E14"] = m3[3]

blatt["A15"] = "Messung 4"
blatt["B15"] = m4[0]
blatt["C15"] = m4[1]
blatt["D15"] = m4[2]
blatt["E15"] = m4[3]

blatt["A16"] = "Messung 5"
blatt["B16"] = m5[0]
blatt["C16"] = m5[1]
blatt["D16"] = m5[2]
blatt["E16"] = m5[3]

blatt["A17"] = "MIN"
blatt["B17"] = min(m1[0], m2[0], m3[0], m4[0], m5[0])
blatt["C17"] = min(m1[1], m2[1], m3[1], m4[1], m5[1])
blatt["D17"] = min(m1[2], m2[2], m3[2], m4[2], m5[2])
blatt["E17"] = min(m1[3], m2[3], m3[3], m4[3], m5[3])

blatt["A18"] = "MAX"
blatt["B18"] = max(m1[0], m2[0], m3[0], m4[0], m5[0])
blatt["C18"] = max(m1[1], m2[1], m3[1], m4[1], m5[1])
blatt["D18"] = max(m1[2], m2[2], m3[2], m4[2], m5[2])
blatt["E18"] = max(m1[3], m2[3], m3[3], m4[3], m5[3])

blatt["A19"] = "Abweichung"
blatt["B19"] = max(m1[0], m2[0], m3[0], m4[0], m5[0]) - \
    min(m1[0], m2[0], m3[0], m4[0], m5[0])
blatt["C19"] = max(m1[1], m2[1], m3[1], m4[1], m5[1]) - \
    min(m1[1], m2[1], m3[1], m4[1], m5[1])
blatt["D19"] = max(m1[2], m2[2], m3[2], m4[2], m5[2]) - \
    min(m1[2], m2[2], m3[2], m4[2], m5[2])
blatt["E19"] = max(m1[3], m2[3], m3[3], m4[3], m5[3]) - \
    min(m1[3], m2[3], m3[3], m4[3], m5[3])

excel.save("WZV_Protokoll.xlsx")
print("Done")
