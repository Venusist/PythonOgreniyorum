import threading

def zaman_asimi():
    print("\nZaman doldu!")
    raise TimeoutError("Yanit verilmedi,süre doldu")

timer = threading.Timer(10, zaman_asimi)
timer.start()

try:
    sonuc=input("10 sn içinde cevap verin: ")
    timer.cancel()
    print(f"Girilen sonuc: {sonuc}")
except TimeoutError:
    print("Yanit verilmedi,süre doldu")


#timer.cancel etmezsen thread sadece bir kere başlatılabildiği için örneğin
#sürekli sana soru sorulup 5 sn içinde cevap vermen gerekirse eror alırsın o yüzden cancel edip yeniden başlayacak.
