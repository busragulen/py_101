for x in [1,3,5,8]:
  print(x) #dediğimizde belirttiğimiz listedeki tüm x değerlerini yazdırır.
 

#aynı işlem şöyle de yapılabilir
sayilar=[1,3,5,8]
for x in sayilar:
  print(x)
  
#string tipindeki veriler için de aynısı yapılabilir

isim="github"
for harf in isim:
  print(harf) #tüm harfleri teker teker yazdıracaktır.
  
# for döngüsünde şöyle bir durum söz konusu:

isim="github"
for harf in isim:
  print(isim) #yaptığımızda, isimdeki karakter sayısı kadar isim yazdırır.
  
#bileşenleri yazdırmak istersek hem listelerde hem demetlerde şu metodu kullanabiliriz:
  
  lise=[[],[]]
