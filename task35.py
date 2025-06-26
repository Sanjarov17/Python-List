sozlar = input("So‘zlarni vergul bilan kiriting: ").split(",")

kichik = []
orta = []
katta = []

for soz in sozlar:
    soz = soz.strip()
    uzunlik = len(soz)
    if uzunlik <= 3:
        kichik.append(soz)
    elif 4 <= uzunlik <= 6:
        orta.append(soz)
    else:
        katta.append(soz)

print("<=3 harfli:", kichik)
print("4-6 harfli:", orta)
print(">6 harfli:", katta)
