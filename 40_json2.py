# py'da json kullanmak için json modülü ekleriz.

import json
kullanıcı='{"isim":"x", "soyisim":"y", "yas":1}' #şuan bu bir str
#bu str'i json sayesinde bunu dicte dönüştürebiliriz

info=json.loads(kullanıcı)
info #shift enter yaptığımızda bir dict çıktısı alrız
#type() ile de tekrardan kontrol edilebilir dict olduğu

info["isim"] # output olarak x verecektri

# örnek olarak isimdeki değeri değiştirmek istiyorsak:

info["isim"] = "t" # artık shift+enter'da t verir.

## sözlüğü direkt olarak jsona dönüştürmek
kullanıcı=json.dumps(info)
kullanıcı
