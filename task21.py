ismlar = ["Ali", "Laylo", "Jasur", "Diyorbek"]

ochiriladigan_ism = input("Ro'yxatdan o'chirmoqchi bo'lgan ismingizni kiriting: ")

if ochiriladigan_ism in ismlar:
    ismlar.remove(ochiriladigan_ism)
    print("Yangilangan ismlar ro'yxati:", ismlar)
else:
    print("Bu ism ro'yxatda topilmadi.")
