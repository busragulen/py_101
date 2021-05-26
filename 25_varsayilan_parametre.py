# bir ornek yapalım 

def soyisim(soy):
  print(soy)
soyisim(x)

# böyle shiftenter yapıp yazdırdığımızda çıktı olarak x verecektir
# fakat fonk'u çağırıp parantezi boş bırakırsak hata verecektir
# hata vermemesi için varsayılan (default) değer atanması gerekmektedir 
# bunu kodu yazarken manuel olarak atayabiliriz

def soyisim(soy="soyisim girilmedi"):
  print(soy)
soyisim()

# yaptığımız takdirde parantez boş olsa da hata almayız
# deger olmadığından bzizim atadığımız stringi yazdıracak

# sadece str olmak zorunda değil, sayısal ifadelerde de varsayılan parametre atayabilirz

# not -1 ifadesi yazılımda hataya denk gelmektedir
