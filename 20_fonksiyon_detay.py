#### değer dönderebilen fonksiyonlar ####

def sayi1(x):
  print(x)
def sayi2(y):
  print(y)
toplam1= sayi1(5)
toplam2= sayi2(10)

# toplam1 ve toplam2'yi toplayabilmek için değer döndürebiliyor olmak gerek.

def sayi1(x):
  return x
def sayi2(y):
  return y
print(sayi1(2)) # böyle olduğunda çıktı olarak 2 alabiliriz.

##toplamak için ise 

def sayi1(x):
  return x
def sayi2(y):
  return y

toplam1=sayi1(1)
toplam2=sayi2(2)
toplam1+toplam2  # output 9 olacaktır

#string döndürmek

def isim(isim):
  return(isim)
print(isim("github"))

## aynıları mantıksal değerler için de yapılabilir

def isim(isim):
  return(isim)
print(isim(True))

####### not: değer döndüremeyen fonksiyonlarda toplama gibi işlem yaptığımızda NonetType hatası alıyoruz.

def fonksiyon():
  print("Bu bir fonksiyondur")
fonksiyon()

# bu fonksiyonun tipini sorgulayacak olsaydık:

type(fonksiyon())

#output NonetType olur. yani tipi mevcut değil. tipsiz.

def sayi(x):
  return x
type(sayi(5)) # return olduğu için değer döndürebiliyor
# outputu int olur. yani artık fonksiyonun belirli bir tipi vardır.

# fonksiyon içerisinde bir değerin çift mi tek mi olduğunu anlayabilirz
# bunu şöyle yaparız

def cift_kontrol(x):
  if (x%2==0):
    return True
  else:
    return False
cift_kontrol(3)

# hem sayısal hem karaktersel işlem

 def bilgi(isim,soyisim,yas):
    print("Kullanıcının ismi:",isim," soyismi:", soyisim, " yası:",yas)
