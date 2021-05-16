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
  
liste=[[1,2],[3,4]]
for i,j in liste:
  print("i degeri {}, j degeri{}" .format(i,j)) # i degeri 1, j degeri2, i degeri 3, j degeri4 şeklinde yazdıracaktır.
  
#i. eleman 1., j. eleman 2. eleman gibi olur.
  
###### NOT #####
# eğer üç elemanlı bir listeden veya demetten, iki elemanlı for döngüsü oluştutursak hata alırız.
