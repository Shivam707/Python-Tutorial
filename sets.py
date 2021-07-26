# set does not contain duplicate values
# A Set is an unordered collection data type that is iterable, mutable and has no duplicate elements.

# mutable set type - 
myset = set([1,2,3,4,5,6,1,2,5]) # 

set = {"Burger","coffee","cheese","cold-coffee","cheese","hot-choclate"}

print(set) # cheese is present twice in set but it store only one cheese

numSet = {1,2,3,4,5,6,1,2,3}

print(numSet) # {1,2,3,4,5,6} -> no duplicate values

numSet.add(10) #add 10 t numSet

numSet.remove(5) #remove 5 from set
 
unionSet = numSet.union({10,20,30}) #to find union of two sets
# -------------------------------------OR-----------------------------------
unionSet = numSet.union(myset)

intersectSet = numSet.intersection({1,2,876,463,4123}) #to find common elements in two sets/ intersection of two sets
# -------------------------------------OR-----------------------------------                    
intersectSet = numSet.intersection(myset)

numSet.isdisjoint(myset) # return true if no element is common between two sets/ intersection of two sets is zero

