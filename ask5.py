for i in range (10,99) :
 z=i/10
 x=i%10
 sum=x+z
 if i%sum==0 :
  print i
 if z!=0 and x!=0 :
  gin=z*x
  if i%gin==0 :
   print i

for i in range (100,999) :
 z=i/100
 x=(i%100)/10
 a=(i%100)%10
 sum=z+x+a
 gin=z*x*a
 if i%sum==0 :
  print i
 if gin!=0 :
  if i%gin==0 :
   print i