t1=0;t2=1
nextterm=1
for i in range(10):
   print(nextterm)
   nextterm=t1+t2
   t1=t2
   t2=nextterm
