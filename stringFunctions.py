str = "this is a string"

print(str.endswith("ing")) # True

print(str.endswith("xyz")) # False

print(str.isalpha()) # False because spaces are aso there in string

str_2 = "shivamisagoodboy"

print(str.isalnum()) # False because stirng is not alphanumeric

print(str.count("s")) # counts the frequency of the letter/word in string

print(str.capitalize()) # Capitalize string

print(str.find("s")) # returns first occuence of the word/letter

print(str.lower()) # converts to lower case 

print(str.upper())  #converts to upper case 

print(str.replace("is" , "are")) # replace the word in string with second argument

