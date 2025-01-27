import itertools # type: ignore
#print(dir(itertools))

l1=[1,2,3,4]
l2=['a','b','c']
l3=range(100,106)
i=itertools.chain(l1,l2,l3)
print(i)
for val in i:
    print(val) # type: ignore



#for using it for multiple purposes we use tee method
l1=[1,2]
l2=['a','b']
l3=range(100,103)
i=itertools.chain(l1,l2,l3)
t=list(itertools.tee(i,2))
print(t)

ind=0
while(ind<len(t)):
    for i in t[ind]:
        print(i)
    print("@@@@@@")
    ind+=1