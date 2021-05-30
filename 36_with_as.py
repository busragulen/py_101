# .close() methoduna alternatif

with open("dosyaismi","r", encoding="utf-8") as dosya:
  for x in oku:
    print(x,end="")
    
# bunu böyle çalıştırdığımızda dosya otomatik bir şekilde kapanmaktadır.

# okumaya başladığ byte:

with open("dosyaismi","r", encoding="utf-8") as dosya:
  print(dosya.tell()) # output olarak 0 verir
  
# sadece belirli bytetan itibaren veriyi çekme:

with open("dosyaismi","r", encoding="utf-8") as dosya:
  dosya.seek(10) # bu func ile dosyayı okumaya 10. byte'tan itibaren başlıyoruz.
  print(dosya.tell())
  
# peki aynı filtrelemeyi sondan başlayarak yapsaydık:
with open("dosyaismi","r", encoding="utf-8") as dosya:
  dosya.seek(10) # bu func ile dosyayı okumaya 10. byte'tan itibaren başlıyoruz.
  y=dosya.read(15) # read()'ın içine verdiğimiz sayı okunacak byte sayısını ifade ediyor.
  print(y)
