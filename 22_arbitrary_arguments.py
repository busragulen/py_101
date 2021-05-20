## tek parametre ile çoklu değer atama ##

def toplam(x,y,z,w):
  print("Toplam: ",x+y+z+w)
toplama(4,5,6,7)

# bu basit yöntemdi. ancak işlevselliği yok.
# *args yöntemi:

def toplama(*args):
  print(args)
toplama(4,5,6)

#shift enterla yukarıdaki kodun çıktısını aldığımızda verdiğimiz değerlerden bir demet sunuyor.

def toplama(*args):
  toplam=0
  for i in args:
    toplam+=i
    print("Toplam: ", toplam)
    toplam=0
    
# bu algoritma tek parametre içinde birden fazla değerle işlem yapabiliriz. 
