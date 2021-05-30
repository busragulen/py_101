### bu kip ile okuma ve yazma işlemlerini yapabiliriz

# yani tek tek w veya r kullanmaya gerek kalmaz
# güzel yönü w'de olan handikap r+'da yoktr. 
# yani biz yeni veri yazınca eskiler silinmez. 

with open("dosyaismi.txt", "r+" , encoding="utf-8") as islem:
  print(islem.read())
  
# r+'da da .seek() methodu kullanılabiliyor

with open("dosyaismi.txt", "r+" , encoding="utf-8") as islem:
  islem.seek(20)
  print(islem.read())
  
# bir bytetan itibaren yazmak için:

with open("dosyaismi.txt", "r+" , encoding="utf-8") as islem:
  islem.seek(40)
  islem.write("github")
  
# yaptığımız işlemin çıktısını görmke için:
with open("dosyaismi.txt", "r+" , encoding="utf-8") as islem:  
  print(islem.read())
    
# o byte'ta olan charı siler, yeni eklediğimiz charları yazdırır
# fakat diğer veriler aynen kalır

### yeni satıra geçip orada işlem yapmak istiyorsak a kipini kullanırız:

with open("dosyaismi.txt", "a" , encoding="utf-8") as islem:
  islem.write("bugün günlerden pazar")
 
# okumak için de:

with open("dosyaismi.txt", "r" , encoding="utf-8") as islem:  
  print(islem.read())
