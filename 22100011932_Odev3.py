import random

# Öğrenci numarası: 22100011932
# Ad Soyad:Ceydanur Gezer

secim2=0
oyun_alani=[]
print("----AMİRAL BATTI OYUNUNA HOŞGELDİNİZ----")
while True:
    print("\n-------------MENU-----------------")
    print("1.Oyuna başlamak için 1'e basınız")
    print("2.Oyundan çıkmak için 2'ye basınız")
    secim=input("Lütfen bir seçim yapınız: ")
    if secim=="1":
        print("\n----------------OYUN MODU SEÇİMİ----------------")
        print("1.AÇIK MOD(GEMİ YERLERİ OYUN ALANINDA GÖZÜKÜR)")
        print("2.GİZLİ MOD(GEMİ YERLERİ OYUN ALANINDA GÖZÜKMEZ)")
        secim2=input("Lütfen bir mod seçimi yapınız:\n")
        if secim2 != "1" and secim2 != "2":
            print("\nYanlis tercih yaptiniz")
            continue
        boyut = int(input("\nLütfen oyun alanı için bir boyut giriniz:\n"))
        while boyut < 10 :
            print("\n10'dan kucuk boyut giremezsiniz")
            boyut = int(input("\nLütfen oyun alanı için bir boyut giriniz:\n"))
        atis_hakki = boyut * boyut // 3
        for i in range(0, boyut):
            oyun_alani.append(["?"] * boyut)

        yonler = ["Yukari", "Asagi", "Sag", "Sol"]
        gemi_boyut = 4
        gemi_listesi_yedek = []
        gemi_listesi = []
        gemi_tutucu1 = []
        gemi_tutucu2 = []
        gemi_tutucu3 = []
        gemi_tutucu4 = []
        gemi_sayisi = 4
        while gemi_sayisi > 0:
            gemi_boyut = gemi_sayisi
            yon = random.choice(yonler)
            if yon == "Yukari":
                x_kor = random.randint(0, boyut - 1)
                y_kor = random.randint(0, boyut - 1)
                while gemi_boyut != 0:
                    if [x_kor, y_kor] in gemi_listesi:
                        x_kor = random.randint(0, boyut - 1)
                        y_kor = random.randint(0, boyut - 1)
                        gemi_listesi_yedek.clear()
                        gemi_boyut = gemi_sayisi
                        continue
                    gemi_listesi_yedek.append([x_kor, y_kor])
                    x_kor -= 1
                    if x_kor < 0:
                        x_kor = random.randint(0, boyut - 1)
                        y_kor = random.randint(0, boyut - 1)
                        gemi_listesi_yedek.clear()
                        gemi_boyut = gemi_sayisi
                        continue
                    gemi_boyut -= 1
            elif yon == "Asagi":
                x_kor = random.randint(0, boyut - 1)
                y_kor = random.randint(0, boyut - 1)
                while gemi_boyut != 0:
                    if [x_kor, y_kor] in gemi_listesi:
                        x_kor = random.randint(0, boyut - 1)
                        y_kor = random.randint(0, boyut - 1)
                        gemi_listesi_yedek.clear()
                        gemi_boyut = gemi_sayisi
                        continue
                    gemi_listesi_yedek.append([x_kor, y_kor])
                    x_kor += 1
                    if x_kor > boyut:
                        x_kor = random.randint(0, boyut - 1)
                        y_kor = random.randint(0, boyut - 1)
                        gemi_listesi_yedek.clear()
                        gemi_boyut = gemi_sayisi
                        continue
                    gemi_boyut -= 1
            elif yon == "Sag":
                x_kor = random.randint(0, boyut - 1)
                y_kor = random.randint(0, boyut - 1)
                while gemi_boyut != 0:
                    if [x_kor, y_kor] in gemi_listesi:
                        x_kor = random.randint(0, boyut - 1)
                        y_kor = random.randint(0, boyut - 1)
                        gemi_listesi_yedek.clear()
                        gemi_boyut = gemi_sayisi
                        continue
                    gemi_listesi_yedek.append([x_kor, y_kor])
                    y_kor += 1
                    if y_kor > boyut - 1:
                        x_kor = random.randint(0, boyut - 1)
                        y_kor = random.randint(0, boyut - 1)
                        gemi_listesi_yedek.clear()
                        gemi_boyut = gemi_sayisi
                        continue
                    gemi_boyut -= 1
            elif yon == "Sol":
                x_kor = random.randint(0, boyut - 1)
                y_kor = random.randint(0, boyut - 1)
                while gemi_boyut != 0:
                    if [x_kor, y_kor] in gemi_listesi:
                        x_kor = random.randint(0, boyut - 1)
                        y_kor = random.randint(0, boyut - 1)
                        gemi_listesi_yedek.clear()
                        gemi_boyut = gemi_sayisi
                        continue
                    gemi_listesi_yedek.append([x_kor, y_kor])
                    y_kor -= 1
                    if y_kor < 0:
                        x_kor = random.randint(0, boyut - 1)
                        y_kor = random.randint(0, boyut - 1)
                        gemi_listesi_yedek.clear()
                        gemi_boyut = gemi_sayisi
                        continue
                    gemi_boyut -= 1
            if gemi_sayisi == 4:
                gemi_tutucu4 +=gemi_listesi_yedek
            elif gemi_sayisi == 3:
                gemi_tutucu3 += gemi_listesi_yedek
            elif gemi_sayisi == 2:
                gemi_tutucu2 += gemi_listesi_yedek
            elif gemi_sayisi == 1:
                gemi_tutucu1 += gemi_listesi_yedek
            gemi_listesi +=gemi_listesi_yedek
            gemi_listesi_yedek.clear()
            gemi_sayisi -= 1
            print(gemi_listesi)
        if secim2 == "1":
            print("-----------------AÇIK MOD-----------------")
            for koordinatlar in gemi_listesi:
                x, y = koordinatlar
                if oyun_alani[x][y] == "?":
                    oyun_alani[x][y] = "G"

            print('   ', end='')
            for j in range(0, boyut):
                if len(str(j)) > 1:
                    print('', j, end='')
                else:
                    print(' ', j, end='')
            print()
            for i in range(0, len(oyun_alani)):
                if len(str(i)) > 1:
                    print('', i, end='')
                else:
                    print(' ', i, end='')
                sayi = 0
                for j in range(len(oyun_alani[0])):
                    if sayi > 9:
                        print(' ', oyun_alani[i][j], end='')
                    else:
                        print(' ', oyun_alani[i][j], end='')
                    sayi += 1
                print()
        elif secim2 == "2":
            print("-----------------GİZLİ MOD-----------------")
            print('   ', end='')
            for j in range(0, boyut):
                if len(str(j)) > 1:
                    print('', j, end='')
                else:
                    print(' ', j, end='')
            print()
            for i in range(0, len(oyun_alani)):
                if len(str(i)) > 1:
                    print('', i, end='')
                else:
                    print(' ', i, end='')
                sayi = 0
                for j in range(len(oyun_alani[0])):
                    if sayi > 9:
                        print(' ', oyun_alani[i][j], end='')
                    else:
                        print(' ', oyun_alani[i][j], end='')
                    sayi += 1
                print()
        while atis_hakki > 0:
            print("Kalan atış hakkınız: ", atis_hakki)
            x = int(input("\nLütfen bir satir numarası giriniz:"))
            y = int(input("Lütfen bir sutun numarası giriniz:\n"))
            atis_hakki -=1 #yanlis yada dogru olan her atista dusurdugu icin burada atis hakkini guncelledim
            if x > boyut-1 or y > boyut-1 or x < 0 or y < 0:
                print("Oyun alanının sınırlarını aştınız")
                continue
            if oyun_alani[x][y] == "X" or oyun_alani[x][y] == "*":
                print("Daha önce bu koordinatları girdiniz\nLütfen tekrar giriniz")
                continue
            if [x, y] in gemi_listesi:
                oyun_alani[x][y] = "X"
                print("Tebrikler bir gemi vurdunuz")
                if [x, y] in gemi_tutucu1:
                    gemi_tutucu1.remove([x, y])
                    if len(gemi_tutucu1)==0:
                        print("Tebrikler! Bir gemi batırdınız.")
                elif [x, y] in gemi_tutucu2:
                    gemi_tutucu2.remove([x, y])
                    if len(gemi_tutucu2)==0:
                        print("Tebrikler! Bir gemi batırdınız.")
                elif [x, y] in gemi_tutucu3:
                    gemi_tutucu3.remove([x, y])
                    if gemi_tutucu3 == []:
                        print("Tebrikler! Bir gemi batırdınız.")
                elif [x, y] in gemi_tutucu4:
                    gemi_tutucu4.remove([x, y])
                    if gemi_tutucu4 == []:
                        print("Tebrikler! Bir gemi batırdınız.")
            elif [x, y] not in gemi_listesi:
                oyun_alani[x][y] = "*"
                print("Maalesef isabetli atış yapamadınız")
            print("--------------------------------------------")
            print('   ', end='')
            for j in range(0, boyut):
                if len(str(j)) > 1:
                    print('', j, end='')
                else:
                    print(' ', j, end='')
            print()
            for i in range(0, len(oyun_alani)):
                if len(str(i)) > 1:
                    print('', i, end='')
                else:
                    print(' ', i, end='')
                sayi = 0
                for j in range(len(oyun_alani[0])):
                    if sayi > 9:
                        print(' ', oyun_alani[i][j], end='')
                    else:
                        print(' ', oyun_alani[i][j], end='')
                    sayi += 1
                print()
            if len(gemi_tutucu4) == 0 and len(gemi_tutucu3) == 0 and len(gemi_tutucu2) == 0 and len(gemi_tutucu1) == 0:
                break
        if atis_hakki == 0:
            print("\nAtis hakkiniz bittigi icin kaybettiniz")
        else:
            print("\nTebrikler {} puan ile kazandınız".format(atis_hakki))
    elif secim=="2":
        print("\nOyundan çıkılıyor...")
        break
    else:
        print("\nYanlis tercih yaptiniz")
        continue