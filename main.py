import time


from plyer import notification


print("Bildirim Ekle    : ")
print("Bildirim eklemek için başlık ve mesaj belirleyin   :")
title = input("Bildirim Başlığı  :\n")
message = input("Bildirim Mesajı  :\n")

takvim = (input("Tarih eklemek ister misin? (Evet veya Hayır)\n"))
cevap = takvim.upper()
if cevap == "EVET":
    bildirim_tarihi = float(input("Bildirimi kaç dk sonra almak istersin\n"))
    time.sleep(bildirim_tarihi*60)
    notification.notify(title=title, message=message,app_icon=None, timeout=10,toast=False)
elif cevap == "HAYIR":
    notification.notify(title=title, message=message, app_icon=None, timeout=10,toast=False)
else:
    print("Girilen değer uyuşmuyor lütfen tekrar deneyiniz!")