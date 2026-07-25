set={1,2,3,4,4,}#set is well defined and distinct
set2={3,4,5,6}
#empty_set=set()
#print(type(empty_set))
#set is muatble that we can make any changes to existing set
#some methods of set
set.add(5)
print(set)
set[1]=6#though sets are mutable but still this is not allowed in set beacuse set does not support indexxing
print(set)

set.remove(4)
print(set)
set.clear()#clear all the elements of the set
set.pop()#remove any random value from the set
print(set.union(set2))
print(set.intersection(set2))

#IN PYTHON 9=9.0 though they are different datatypes but python treated them as equal
#so to store them in set we can use the following method
s={(9,int),(9.0,float)}
print(s)

