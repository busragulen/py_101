# ikisi de döngülerde kullanılır.

###### break ######

# break döngüyü sonlandırmaya yarar.

sayi=15
while(0<=sayi):
  print(sayi)
  sayi-=1
  if sayi ==5:
    break # normalde 0'a kadar sayardı ama ben 5'te dursun istedim. 
    # ekranda en son 6'yı görürüz.
    
###### continue ####
# atlamaya yarar

sayi=20
while(0<sayi):
  sayi-=1
  if sayi%2==0:
    continue
  print(sayi) #2'ye bölülenenleri atlar
  
  #yani 2'ye bölünenleri outputta göremeyiz
