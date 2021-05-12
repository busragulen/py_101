######### Listeler #########

# liste olustururken liste(degisken) isminden sonra = koyar ve [] arasina liste bilesenlerini yazariz.

liste= ["c","c++","c#"]
type(liste)  #output list olacaktir.

# bir listedeki verilerin veri tipleri ayni olmak zorunda degildir.

liste= ["c","c++","c#", 7, 9.0]

# fonksiyonla da liste olusturabiliriz:

liste= list()

# listeler mantigi = str mantigi, zaten str de bir liste. (unicode dizisi)
# listeler icinde de indis vardir.

liste= ["c","c++","c#"]
liste[1] #output "c++" olur.

######## Liste icine liste koymak #########

liste=[1,5,7,["hava", "yagmur"], "Sari"]
type(liste[3]) #output list olur cunku 3. indiste bir liste var.

######## Indisin indisini ekrana yazdirmak #######

liste=[1,5,7,["hava", "yagmur"], "Sari"]
print(liste[3][0]) #output hava olacaktir.

####################################################################

# Listeleri toplamak icin + kullaniriz.
 
l1=[9,8,7]
l2=["Ali", "Mahmut"]
l3=l1+l2 # artik  l3 = [9,8,7,"Ali", "Mahmut"] 

# Bir indisteki veriyi degistirmek için su kodları kullanabiliriz:

l1[2]=6 # l1 listesinin 2. indisindeki veri artik 6'dir.

# Bir listedeki bilesen sayisini len() fonksiyonu ile ögrenebiliriz. 

l3=[9,8,7,"Ali", "Mahmut"]
len(l3) # output: 5

# Bir listeye yeni deger eklemek icin + kullanablriz.

l1=l1+[Opeth] # l1=[9,8,7,"Opeth"]  olur

#Listeyi iki kez goruntulemek istersek: 

l1*2

############# Listeye bilesen eklerken .append metodunu kullanmak: ##############

l1.append(4) # dedigimizde l1 artik [9,8,7,"Opeth", 4] olur. 

# Bu .append metodu ile tum veri tiplerindeki degerler listelere eklenebilir, sayisal olmasina gerek yok.

