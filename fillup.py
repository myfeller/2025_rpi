import zufall as zf

#txt    = "So einen Zufall kann es gar nicht geben, oder wir verstehen es nicht"-
txt    = "SoeinenZufallkannesgarnichtgeben,oderwirverstehenesnicht"
#txt    = "SoeinenZufallkannesgarnichtgeben,oderwirverstehenesnichtSoeinenZufallkannesgarnichtgeben,oderwirverstehenesnicht"

txts   = zf.getZufall(19)           # Schluesselbereich
runden = int(len(txt) / len(txts))  # Anzahl der Durchlaeufe

txtu   = []                         # Gesamtschluessel
txtv   = []                         # Verschluesselter Text
count  = 0


for i in range(runden):           # Aufbereitung des Gesamtschluessels
    addon = count * len(txts)
    for n in range(len(txts)):
        if (addon + int(txts[n])) < len(txt):
            txtu.append(addon + int(txts[n]))
    count += 1

for i in range(len(txt) - len(txtu)):
        txtu.append(addon + int(txts[i]))

txtv = ""
for i in range(len(txt)):
    #print(int(txtu[i]))
    txtv = txtv + txt[int(txtu[i])]

#print(txts)
#print(txtu)
#print(len(txt))
#print(len(txtu))
print(txt)
print(txtv)