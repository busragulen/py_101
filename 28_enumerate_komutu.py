# bu fonksiyon sayesinde indexleme işlemleri daha kolay bir şekilde halledebilir

liste=["x","y","z"]
sayi=1
for op in liste:
  print(sayi,op)
  sayi+=1
  
# böyle yaptığımda 1 x, 2 y, 3 z olarak alt alta output verecek.
# bu kodu daha kolay ve daha kısa bir şekilde enumerate fonk'u ile yazarız:

liste=["x","y","z"]
for index,op in enumerate(liste,start=1): 
  # burada op, listedeki bileşenleri döndürürken index de indexlerini döndürecek.
  # enumerate()'e değer ekliyoruz: liste oluşturduk diye listeyi aldım. start dediğim sayıdan indexlemeye başlıyo
  # start 1 olduğu için indis 0 da olsa ilk maddeye 1 verecek print fonksiyonu içinde
    print(index,op)
