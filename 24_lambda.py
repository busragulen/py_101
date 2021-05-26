# Lambda #
# lambda fonksiyonu, bir fonksiyonu tek satırda yazmamıza olanak sağlar
# örnek olarak karekok adında bir fonk oluşturalım

def karekok(x):
  return x**0.5
karekok(4) # çıktı 2 olur.

#bunu lambda ile şöyle yazarız

karekok=lambda x: x**0.5
karekok(25) # boyle oldugunda çıktı olarak 5 verir.

#yani aynı fonk'u tek satırda yazaraqk bu şekilde oluşturduk
