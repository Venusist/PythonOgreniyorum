from random import randint
import threading
import time

print("-" * 50)
print("\t\tHOSGELDINIZ")
print("-" * 50)

class Oyun:
    def __init__(self):
        self.isim = input("Isminizi girin: ").strip()
        self.puan = 0
        self.zaman_gecti = False  # Zaman aşımı kontrolü için bir bayrak
        self.dogru_sayisi = 0
        self.yanlis_sayisi = 0

    def zaman_asimi(self):
        print("\nZaman doldu!")
        self.zaman_gecti = True
        self.puan -= 5
        self.yanlis_sayisi += 1
        print("5 puan kaybettiniz. Bir sonraki soruya geçiliyor...")

    def carpim(self, i, j, r):
        if r != "-1":
            result = str(i * j)
            if result == r:
                print("\t*****Dogru*****")
                self.puan += 10
                self.dogru_sayisi += 1
            else:
                print("\t*****Yanlis, cevap %s olmaliydi" % result)
                self.puan -= 5
                self.yanlis_sayisi += 1
        else:
            print("Cikis yapiliyor...")
            exit(0)

    def aralik(self, aralik_1, aralik_2):
        for _ in range(5):  # 5 soru sormak için
            sayi_1 = randint(aralik_1, aralik_2)
            sayi_2 = randint(aralik_1, aralik_2)
            self.zaman_gecti = False  # Her soru için bayrağı sıfırla

            def zaman_asimi_thread():
                time.sleep(10)  # 10 saniye bekle
                if not self.zaman_gecti:
                    self.zaman_asimi()  # Zaman dolduysa zaman aşımı fonksiyonunu çağır

            zaman_thread = threading.Thread(target=zaman_asimi_thread)
            zaman_thread.start()

            print("\t%d x %d kaçtır?" % (sayi_1, sayi_2))

            sonuc = None

            try:
                sonuc = input("Sonuç >> ")
                self.zaman_gecti = False  # Kullanıcı cevap verdi
            except:
                pass  # Zaman dolduğunda input çalışmaz, bu yüzden hatayı görmezden geleceğiz
                zaman_thread.join()  # Zaman aşımı işini tamamlayana kadar bekle

            if not self.zaman_gecti:
                self.carpim(sayi_1, sayi_2, sonuc)

            print(f"Güncel puan: {self.puan}")

        print("-" * 50)
        print(f"Test bitti! Doğru sayiniz: {self.dogru_sayisi}, Yanlis sayiniz: {self.yanlis_sayisi}")
        print(f"Son puaniniz: {self.puan}")
        self.puan_kaydet()
        self.yuksek_skor()
        print("-" * 50)

    def baslangic(self):
        print(" Hangi seviyeden başlamak istiyorsunuz? (cikis = -1)\n")
        print(" 1 - Kolay \n")
        print(" 2 - Orta \n")
        print(" 3 - Zor \n")
        print(" 4 - Çok Zor \n")

        seviye = input(" >> ")

        if seviye == "1":
            self.aralik(1, 6)
        elif seviye == "2":
            self.aralik(6, 12)
        elif seviye == "3":
            self.aralik(12, 25)
        elif seviye == "4":
            self.aralik(25, 100)
        elif seviye == "-1":
            print("Cikis yapiliyor...")
            exit(0)
        else:
            print("Gecersiz seviye. Lutfen tekrar deneyin")
            self.baslangic()

    def puan_kaydet(self):
        with open("skorlar.txt", "a") as file:
            file.write(f"{self.isim}: {self.puan}\n")

    def yuksek_skor(self):
        try:
            with open("skorlar.txt", "r") as file:
#"r": Okuma modu. Dosya sadece okunur. Eğer dosya yoksa hata verir.
#"w": Yazma modu. Dosya üzerine yazar. Eğer dosya yoksa yeni bir dosya oluşturur. Eğer dosya varsa var olan içeriği siler.
#"a": Ekleme modu. Dosya sonuna ekleme yapar. Eğer dosya yoksa yeni bir dosya oluşturur.
#"x": Oluşturma modu. Sadece dosya yoksa oluşturur. Eğer dosya varsa hata verir.
#"r+": Hem okuma hem yazma modu. Dosya başından itibaren okuma ve yazma yapılır. Dosya yoksa hata verir.
                skorlar = file.readlines()
                if skorlar:
                    skorlar.sort(key=lambda x: int(x.split(": ")[1]), reverse=True)  # Skorları büyükten küçüğe sırala
                    print("Yüksek Skorlar:")
                    for skor in skorlar[:5]:  # İlk 5 yüksek skoru göster
                        print(skor.strip())
                else:
                    print("Henüz hiç skor yok.")
        except FileNotFoundError:
            print("Skor dosyasi bulunamadi. Henuz hic skor kaydedilmemis.")

if __name__ == "__main__":
    oyun = Oyun()
    oyun.baslangic()