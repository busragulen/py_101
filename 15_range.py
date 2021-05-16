# range belirli aralıktaki değerleri döndürmemize olanak sağlar.
# 3 türde range vardır

# 1

range(5) 
#içine tek bir sayı verdiğimiz range'dir
# (0,5) gibi bir çıktı verir. aralığı belirtir
# ancak 5 dahil değildir!

###### NOT ####
# Range'İ çıktı almak istiyorsak balına * koymak gerek
#örnek
print(*range(5)) 
# çıktısı 0 1 2 3 4  olur

# 2

range(5,10) # iki parametreli range() kullanım şeklidir
# 5'ten 10'a kadar sayar, 10 dahil değil.
# default başlangıç değeri 0'dır. bu durumda onu değiştirmiş oluyoruz.

# 3

# 3 parametreli range() de kullanabiliriz
# 3. değer bu sayıların kaçar kaçar ilerleyeceğini gösterir.


# range()'i for döngüsünde de kullanabiliriz.

for i in range(10):
  print(i) # 1'den 10'a kadar yazdırır. 10 dahil değil.
  
# range()'İ bir değişkenin içine atayabiliriz

sayi=range(51)
for i in sayi:
  print(i)
