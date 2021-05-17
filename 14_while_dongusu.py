# while kullanmak için öncelikle bir şart vermek gerek.
# bu şart çeşitli işlemler olabilir
#örnek:

sayi=int(input("Lutfen bir sayi giriniz"))
while(0<sayi):
  print(sayi)
  sayi-=1 # sonsuz döngüye girmemesi için -1 artarak döngünün bitmesini tercih edebiliriz
print("dongu bitti") 
#girdiğimiz sayıdan 0'a kadar sayar, 0'a gelince döngüden çıkar.
#ancak bu üstteki kodda 0'ı ekranda göremeyiz
# 0'ı da görmek için:

sayi=int(input("Lutfen bir sayi giriniz"))
while(0<=sayi):
  print(sayi)
  sayi-=1
print("dongu bitti") 
#yapabiliriz.

#sayıyı azaltmak yerine arttıra da biliriz.

sayi=int(input("Lutfen bir sayi giriniz"))
while(sayi<=20):
  print(sayi)
  sayi+=1
print("dongu bitti") #20'ye kadar sayar

#20 de dahil.

#şöyle yaparsak 0'dan değil 1'den başlar; 20'de değil 21'de biter:

sayi=int(input("Lutfen bir sayi giriniz"))
while(sayi<=20):
  sayi+=1
  print(sayi)
print("dongu bitti") # diğer yol daha doğru sonuçlar verir
