## map ##

# map, temelde str'ler, touple'lar ve listelerde işlem gerçekleştirir
# bu komut sayesidnde fonk. tek satırda bir liste veya str içinde işlem yapabilr.

liste=[2,4,6]
bos=[]
def dort(x):
  return sayi**4
for sayi in liste:
  bos.append(dort(sayi))
  
print(bos)

# bu algoritmayi map ile daha farklı bi şekilde de yapabilirz:

liste=[2,4,6]
def dort(x):
  return sayi**4
sayilar=map(dort,liste) # ilk olarak fonk, ikinci olarak iterator konulur: yani döngüye sokmak istediğimiz bileşen 
# gerçekten 4 katına almış mı diye bakmak için boş bi listeye ihtiyaç var:
# daha kolay olsun diye print() içnde de liste koyablrz
print(list(sayilar))

# print ile liste yapmak istemiyosak

liste=[2,4,6]
def dort(x):
  return sayi**4
sayilar=map(dort,liste)
sayilar=list(sayilar)
print(sayilar) 
