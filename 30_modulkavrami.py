# modül kavramı #
# Modül, bir yazılımın bir veya daha fazla rutin işlemini içeren parçasına verilen isimdir
# knedi modüllerimizi de oluşturabilirz
# bir modül üzerinde işlem yapabilmek için bizim o modülü import etmemiz gerekmekte

import math # matematiksel formülleri kullanmaya yarayan modül
#dosyaya math modülü import eder yani indirir

# import edip etmediğimizi anlayabilmek için dir yazıyoruz:

dir(math) #kullanabileceğimiz fonksiyonları ve sınıfları gösterecektir

#kullanmak için ise basit bir yöntem bulunmakta:

faktoriyel=math.factorial(3) # math. yazdıktan sonra tab'a basıp funcları görebiliriz

#bu işlem bize 3'ün faktöriyelini verecek

#modülün ismini değiştirmek için şu kullanılır

import math as mat # mat yazsak da artık ok

# .sqrt ile karekök, .pow ile üs alırız. 
