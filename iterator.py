#iterator => whick consists of __iter__ and __next__ methods
l=[1,2,3,4] # list is not iterator but it can be convert to iterator by using iter(name)
#print(dir(l))
#print(l.__dir__())
print("__iter__" in dir(l))
print("__next__" in dir(l))
l=iter(l)
#print(dir(l))
#print("__iter__" in dir(l))
#print("__next__" in dir(l))
print("List :: ",l)
print(next(l))
#print(l[0]) list iterator doesn't support indexing
l=list(l)
print(l)

l2=[10,20,30,40,50,60,70,80,90,100]
i=iter(l2)
print(next(i))
l=list(i)
print(l,l2)