############### Demetler ############

# Demetlerin listelerden en buyuk farki, demetler icerisindeki indislere mudahale edemiyor olusumuzdur.

#Demetlerde normal parantez açılır. 
 
bilgi=(1,5,9,8,8) #bir demettir. Yani tuple'dır.

#Bir demette .count fonksiyonu ile bir bilesenden kac tane oldugunu ögrenebiliriz. 

bilgi.count(8) #kodunu yazdigimizda output olarak 2 aliriz.

# .count metoduna demette var olmayan bir bileseni girersek ekrana 0 getirecektir.

bilgi.count(3) #output 0 olur

# Demetteki bir bilesenin indisini ögrenmek için .index() metodu kullanilir.

bilgi.index(9) #output, 9 bileaeninin indisini yani 2'yi verir.
