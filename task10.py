mevalar = ["olma", "banan", "anor", "shaftoli", "uzum"]

indeks = int(input("Qaysi indeksdagi mevaning nomini o'zgartirmoqchisiz? (0-4): "))
yangi_meva = input("Yangi meva nomini kiriting: ")

if 0 <= indeks < len(mevalar):
    mevalar[indeks] = yangi_meva
    print("Yangilangan ro'yxat:", mevalar)
else:
    print("Notogri indeks kiritildi.")
