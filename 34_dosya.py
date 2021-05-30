# dosya işlemleri
# dosya açmak

open("dosyaismi.txt", "w") 

# w burda var olmayan bir dosyayı açmak veya 
# var olan dosyanın güncellenmesi gibi işlemlerde kullanıılır

# w gibi farklı ifadeler de bulunmakta. w sadece bunlardan biri. bu ifadelere "kip" denir

# bir işlem yapabilmek için değişkene bunu atıyoruz:

sayilar=open("dosyaismi.txt", "w")
sayilar.write("1 2 3 4 5")

# 9 bytelık bir dosya yazdırıldı
# 9 byte çünkü her char 1 byte etti. boşluklar da dahil. 9 char var, 9 byte.
# fakat şuanda "dosyaismi.txt" adlı text dosyasında hiçbir işlem yok. yani dosyaya girersek boş bir ekranla karşılaşırız
# çünkü bir işlem yaptık fakat kapatmadık..

sayilar=open("dosyaismi.txt", "w")
sayilar.write("1 2 3 4 5") # bu kodu yazdıktan sonra close() ile kapamak gerek.
sayilar.close() # şimdi dosyaya baktığımızda write() ile yazdığımız charları dosya içinde görürüz.

# yani dosyayı kapamazsak hiçbir veri işlenmez ve kaydolmaz.

sayilar.write("merhaba, lolololol") # diyelim ki dosyaya farklı bir şey daha eklemek istedik
# ama şuan dosya kapalı ? o yüzden error verir
# dosyayı bir daha tanımlayıp açmak gerekiyor.

sayilar=open("dosyaismi.txt", "w")
sayilar.write("merhaba, lolololol") # 22 bytelık bir veri yazıldı
sayilar.close() # şuan oldu. 

# ama bunu yaptığımızda daha önce yazmış olduğumuz 1 2 3 4 5 verisi silindi ve yeni yazdığımız eklendi.
# bu handikaptan dolayı w kipi tehlikeli sayılabilecek bir kip.
# zaten çok da tavsiye edilmiyor kullanılması :D

# şuan dosyada türkçe karakterler kullanıldığı takirde encoding hatası alırız ve verileri işlemez/kaydetmez.

sayilar=open("dosyaismi.txt", "w", encoding="utf-8")
# artık tr karakterler de yazılabiliyor.
