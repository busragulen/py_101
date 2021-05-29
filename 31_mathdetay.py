import math as mat
# içindeki bir func'u kullanmak için parametreye atarız
x= mat.pow(2,3)
# x'i 8 dönderir. (döndermek ne yahu?? yazılımcılar niye kullanıyor böyle kelek bi kelimeyi?)

# biz şimdi bunu böyle yaptık kanks ama math modülü full yüklendi
# yani fazladan yer kaplıyor
# bu yüzden de sadece istediğimiz func'ı kullansak daha mantılı gibi:

from math import pow # math'tan pow'u import et diyor...
pow(2,3) # çıktı 8

# başka bi örnek:
from math import cos
cos(90) # outputu -0,44...

# sadece gerekli funcı import edince proje daha stabilite kazanmış oluyor.
