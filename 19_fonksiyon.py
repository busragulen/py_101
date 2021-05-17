######### Fonksiyon ########
# Fonksiyon, belirli sayıda verileri kullanarak bunları işleyen ve bir sonuç üreten komut grubudur. 
# belirli bir ihtiyaç veya amaca yönelik olarak bir kere oluşturulur
# oluşuturlduktan sonra istenen kod bloğund da kullanılabiir.

####### değer döndürebilen fonksiyonlar ########

# bir hesaplamayı yaptıktan sonra elde ettiği sonucu döndürebilen fonksiyonlardır.

def sayi(x):
  return x+2
print(sayi(5))  # çıktısı 7 olur

####### değer döndüremeyen fonksiyonlar ########

# belli bir degere bağlı kalmaz
# sadece gerekli görevleri yapmak için oluştrurulur.
# yani "return" edemeyiz.

##### Fonksiyon kullanımı ######

# py dilinde fonksiyon oluşturabilmek için def yazılır

def fonksiyon_ismi():
  print("fonksiyon çalışıyor") # burada fonksiyon oluşturduk
  
fonksiyon() # bununla fonksiyonu çağırırız. 

# fonksiyonun içine değer atamak için:

def sayi(x):
  print("Kullanıcının atadığı parametre:", x)
  
sayi(10) # parantez içine x'i koymuş olduk


#####################

def toplama(x,y):
  print("toplami:", x+y)
toplama(7,5) # output 12
  
