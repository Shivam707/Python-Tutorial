# Key must either a string or an integer

dict = {} #defining a dictionary

dict = {1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",10:"ten"}

# print(dict[1]) # access the value of the key

dict.get(1) # to get the value of 1


# Nested dictionary
restaurants ={"Burger":{"veg","non-veg","onion","cheese","soya"},"Pizza":"veg","Samosa":"Only one type"}

print(restaurants["Burger"]) # prints - {'non-veg', 'soya', 'veg', 'cheese', 'onion'}

restaurants["French Fries"] = "perry-perry" # appends french fries to restaurants

restaurants.update({"Samosa":"Plain, Paneer, Spicy"}) #to update the value of samosa in restaurants

print(restaurants.items()) # prints whole dictionary restaurants (values only, not the key) - list of tuples/list of key value pair

print(restaurants)

dict[11] = "eleven" # appends elevento dict

del dict[1] # delete key 1 and it's value from dictionary dict

print(dict)

copyDict = dict # this is not recommended at all, copyDict is not a different dictionary, it is just a reference to dict.

# if you make any changes to copprintyDict, it will also reflect the changes to the dict

newDict = dict.copy() # this is how you should copya dictionary


#Dictionary.update - Credits -> geeksforkgeeks.com

# Dictionary with three items 
Dictionary1 = { 'A': 'Geeks', 'B': 'For', }
Dictionary2 = { 'B': 'Geeks' }
  
# Dictionary before Updation
print("Original Dictionary:")
print(Dictionary1)
  
# update the value of key 'B'
Dictionary1.update(Dictionary2)
print("Dictionary after updation:")
print(Dictionary1)


# for item, value in dict : 
    # print(item,value) # error 

for item, value in dict.items() :
    print(item,value) #prints whole dictionary

for item in dict:
    print(item) # print only keys