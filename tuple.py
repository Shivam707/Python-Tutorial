#immutable - unable to change after creation
tuple = (9,8,7,2,0,1,4,5)

sorted_tuple = sorted(tuple) #sort the tuple and assign to another

print(sorted_tuple)


# sort according to given key.
  
def sortKey(n):
    return n[value]  
   
   
def sort(tuples):
  
    return sorted(tuples, key = sortKey)
   

t = [(23, 45, 20), (25, 44, 39), (89, 40, 23)]
value = 2
print("Sorted:"),
print(sort(t))