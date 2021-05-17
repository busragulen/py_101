####### METOT NEDİR #######

# Yazılımda özelleştirilmiş kod bloklarına verilen isimdir.
# besbe tabanlı programların vazgeçilmezidir.
# python'da metot nasıl kullanılır?

# obje_ismi.metot(deger) şeklinde yazabiliriz.
# örnek

liste=[1,2,3]
liste.append(4)
print(liste) 

# çıktısı 1,2,3 olr
# liste objesinden devam edecek olursak, insert() diye bir fonksiyon da bulunmakta.
# bu metotla bir indise, var olan degeri bir sonrakine kaydırmak yoluyala yeni bir değer ekleyebilirz. 

liste=[1,2,3,4]
liste.insert(1, 9)
print(liste)

# çıktısı  1,9,2,3,4 olacaktır.

# listenin içini boşaltmak için .clear() metotu kullanılır

isim.clear()
print(isim)

# çıktısı [] olur.

# bir listede bir elemandan kaç tane olduğunu .count() ile görebiliriz.

sayi=[1,1,1,2,2,2,3,3,3,5]
sayi.count(1) # parantez içindeki değerden 3 tane olduğundan çıktısı 3 olur.

# listedeki bir degeri silmek için .pop() kullanılır.

liste=[1,2,3,4]
liste.pop(0) # 0. indisi silecek
print(liste) # çıktısında 0. indis yani 1 artık yok.
