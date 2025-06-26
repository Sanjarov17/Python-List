sonlar = [3, 5, 3, 2, 5, 5, 1]

eng_kop_son = sonlar[0]
eng_kop_soni = sonlar.count(eng_kop_son)

for son in sonlar:
    takror_soni = sonlar.count(son)
    if takror_soni > eng_kop_soni:
        eng_kop_son = son
        eng_kop_soni = takror_soni

print("Eng ko‘p takrorlangan son:", eng_kop_son)
