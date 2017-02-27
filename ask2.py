paras=input("Dwse parastash")
h=0
eleg=True
for i in paras :
 if paras[i]=="(" :    
  h=h+1
 else:
  h=h-1
 if h<0 :
  eleg=False
 else:
  eleg=False 
if eleg and h==0 :
 print "einai parastash"
else:
 print "den einai parastash"