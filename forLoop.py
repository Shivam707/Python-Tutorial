list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
# -----------------------------Basic but Important----------------------
# i in range vs i in list/iterable objects or iterable containers 
for i in range(0,len(list)):
    print("index is ",i," value is:",list[i]) # printing i means printing the index of the list 

for i in list:
    print(i) # prints list[i]

#--------------------------IMPORTANT------------------------

listNew = [["a",1],["b",2],["c",3],["d",4],["e",5]]

for a,b in listNew:
    print(a,"->",b)
