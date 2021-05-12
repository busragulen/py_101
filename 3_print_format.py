############# Print Fonksiyonu #############

# print() ekrana yazi yazdirmamizi saglayan / standart cikti fonksiyonudur.
# icine str veriler yazilirken tek veya cift tirnak icine alinir.

print("Hello") # ekrana hello yazdirir.

######## print() fonksiyonunda .format metodunu kullanmak ########

isim="Busra"
soyisim="Gulen"
yas="17"
print("İsim: {} Soyisim: {} Yas: {} " .format(isim,soyisim,yas))

# .format metodu ile burada print icerisinde degiskenlerin degerini kullanabildik. 

# .format() metoduyla {} icine indis (index) konulursa, parantez icindeki veri degil indisdeki veri kullanilir.
# indislerde sayma 0'dan baslar. ustteki ornekte isim'in indisi 0, soyisim'in 1 ve yas'in 2'dir.

# .format() metodunun alternatifi olarak string'in yanina virgul konup degiskenin ismi yazilabilir. (C gibi)
# eger yanina baska seyler de yazilacaksa virgul konup devam edilebilir.

p=8
print("P degiskeni=", p) 

#################### NOT #######################
#Alt satira gecmek için \n karakteri kullanilir: new line.
#Bir tab kadar bosluk birakmak icin \t karakteri kullanilir: tab.
