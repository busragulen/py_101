# tarih modülü

import datetime
dir(datetime) # sınıf ve funcları verir.
# ama bunlar hakkında detaylı bilgiyi help() ile de edinebiliriz
help(datetime)

#hangi ayda olduğumuzu gösteren komut:

ay=datetime.datetime.now()
print(ay.strftime(%B))

# ay yerine günü vermek istersek:
ay=datetime.datetime.now()
print(ay.strftime(%A)) # bu yüzdelerin hepsi farklı farklı
