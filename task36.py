sozlar = input("Sozlarni bosh joy bilan kiriting: ").split()

eng_uzun = sozlar[0]

for soz in sozlar:
    if len(soz) > len(eng_uzun):
        eng_uzun = soz

print("Eng uzun soz:", eng_uzun)
