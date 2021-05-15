### Koşullu Yapılar ######

# İlk bakacağımız kavram " if "
# if, "eğer" anlamına gelmekte.

# if kavramının yanına yazdığımız durumu kontrol eder, 
# eğer durum öyleyse verdiğimiz komutu yaptırır.
# fakat verdiğimiz durum sağlanmıyorsa bir sonraki bloğa geçer.

a = 33
b = 200
if b > a:
  print("b is greater than a") #burada b a'dan büyük olduğu için ekrana yazı yazdırır.
  
########################

b = 33
a = 200
if b > a:
  print("b is greater than a")
else:
  print("a is greater than b") #buradaysa ise if yapısı sağlanmadığı için ikinci koşula geçti.
  
# eğer ikiden fazla koşul varsa elif kullanılır.

b = 33
a = 200
if b > a:
  print("b is greater than a")
elif b=a:
  print("b and a are equals")
else:
  print("a is greater than b") # eğer iki kere if yazsaydık sağlıklı olmazdı.
  
########################

# Koşullarla işlemler arasında bir tab kadar boşluk verilmeli,
# aksi takdirde hata alırız.

a = 33
b = 200
if b > a:
print("b is greater than a") # bu kod hata verecektir.
