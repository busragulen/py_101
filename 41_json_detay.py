# alttaki kodu json dosyası olarak kaydediyoruz. ismi: x.json olsun
{
  "isim":"x",
  "yas":9
} # ctrl+s

#bundan sonrası py3 devam:

import json
with open( "x.json", "r", encoding="utf-8" ) as dosya:
  print(dosya.read()) 
  
#json uzantılı dosyanın içindeki verilere ulaşabildik
  

