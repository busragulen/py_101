def tip_bul(x):
  if(x==str(x)):
    return str
  elif(x==int(x)):
    return int
  elif(x==float(x)):
    return float
  elif(x==bool(x)):
    return bool
  
lise=[1,2,3,4.45,"fsdgsdag", 0.95, True, False]

for i in liste:
  print("Liste içerisindeki ", i," elemanı bir ", tip_bul(i),"'dir")
