## Dosya Okuma İşlemi ##

# pythonda dosya okuma yapabilmek için kipi R olarak belirlememiz gerekiyor.
# read- r
# içine  hali hazırda bir şeyler yazmış olduğumuz bir text dosyasını okuyup py'da yazdırmak:
# ilk başta bir değişken oluşturuyoruz:

oku=open("dosyaismi","r", encoding="utf-8")

# read ile dosya oluşturulamaz
# var olan dosya okunabilir
# o yüzden var olmayan bir dosyanın ismini girmek hata ile sonuçlanır.

oku=open("dosyaismi","r", encoding="utf-8")
for i in oku:
  print(i) # for döngüsü ile oku deişkeni içindeki dosyanın bileşenlerini yazdırabilirzi
oku.close() # dosyayı her işlemden sonra kapatmayı unutma pls.

# eğer büyük dosyaları (özellikle de ağır dosyalar) kapatmazsak ideyi kapatsak bile dosyalar açık kalabilr
# sistem için mantıklı bi tercih diil.

# üstteki kodda her satır için fazladan bir tane daha \n koyar. fakat bunu isttemiyorsak:
# çünkü hem biz dosyada alt satıra geçerek \n koyduk, hem de for döngüsü yazdırırken doğası gereği \n koydu.
# bunu önlemek için:

oku=open("dosyaismi","r", encoding="utf-8")
for x in oku:
    print(x,end="") # end komutu ile bu işi halledebilirz. default olan \n yerine hiçbir şey koyduk...
oku.close()
