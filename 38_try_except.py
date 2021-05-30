# bu bir hata ayıklama ifadesidir
# mesela

print(isim) # dediğimizde isim değişkeni tanımlanmadığı için hata alırız.

# bu basit bir kod ve otomatik olarak program bize hatayı gösterir.
# fakat hatayı kendimiz de bulabilirz
# bunun için iki çeşit (try ve except) blok kullanırız.

try:
  print(isim)
  print("isim")
except:
  print("boyle bir degisken daha onceden tanimlanmadi..")
  
# bu ifade sayesinde artık bir nameerror vermemekte
# kendi hatamızı kendimiz tespit etmiş olduk

# şöyle de yapabiliriz:

try:
  print(isim)
  print("isim")
except NameError:
  print("boyle bir degisken daha onceden tanimlanmadi..") # ama bunun çalışma sebebi bizim hatamızın NameError hatası oluşu
  
# başka tipte bi hata yapsak çalışmazdı

try:
  print(754365495/0)
  print("isim")
except NameError:
  print("boyle bir degisken daha onceden tanimlanmadi..") # mesela burda yine error alırdık çünkü hata nameerror hatası değil.
  
  
# bunun için şu yapılabilir:

try:
  print(isim)
  print("isim")
except NameError:
  print("boyle bir degisken daha onceden tanimlanmadi..")
except:
  print("bir hata olustu") # böyle olduğunda bir sorun çıkmaz.
