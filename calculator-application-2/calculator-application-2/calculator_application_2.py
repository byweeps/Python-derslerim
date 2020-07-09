print("""
[1]Toplama
[2]Çıkarma
[3]Çarpma
[4]Bölme
[0]Çıkış""")

giris=input("Seçmek istediğiniz işlem ? : ")

if giris=="1":
    s1=input("1. Sayı ---> : ")
    s1=float(s1)
    s2=input("2. Sayı ---> : ")
    s2=float(s2)
    print("Toplama işleminizin sonucu = ",s1 + s2,"'dir")
elif giris=="2":
    s1=input("1. Sayı ---> : ")
    s1=float(s1)
    s2=input("2. Sayı ---> : ")
    s2=float(s2)
    print("Çıkarma işleminizin sonucu = ",s1 - s2,"'dir")
elif giris=="3":
    s1=input("1. Sayı ---> : ")
    s1=float(s1)
    s2=input("2. Sayı ---> : ")
    s2=float(s2)
    print("Çarpma işleminizin sonucu = ",s1 * s2,"'dir")
elif giris=="4":
    s1=input("1. Sayı ---> : ")
    s1=float(s1)
    s2=input("2. Sayı ---> : ")
    s2=float(s2)
    print("Bölme işleminizin sonucu = ",s1 / s2,"'dir")
elif giris=="0":
    quit()
else:
    print("Hatalı Giriş")
    quit()