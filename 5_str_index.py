################ String ################

# Bir degiskenin icine str veri atarsak, verinin her karakterinin bir indisi olur. 
# indisi [] ile buluruz.
# indis 0'dan baslayarak sayar.

isim="github"
isim[0] #output g olacaktir.

# verinin sadece bir kismini secmek istiyorsak skala belirleriz.

yazi="Bugun hava cok guzel"
yazi[3:14] #3. indisten 14. indise kadar ekrana yazdirir. 

# sinirlandirmayi yaparken soldan baslamak istiyorsak soyle kullanabilriz:

yazi="Bugun hava cok guzel"
yazi[:12] # output su olur: Bugun hava c

#eger bu usttekini soldan degil de sagdan yapsaydik soyle olurdu:

yazi="Bugun hava cok guzel"
yazi[12:]

# indislerin belirli araliklarla ilerlemesini istiyorsak soyle yapabiliriz:

yazi="Bugun hava cok guzel"
yazi[::2] #burada ikiser ikiser ilerliyor.
#output Bgnhv o ue olur. 
