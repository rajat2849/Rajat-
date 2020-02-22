name = "He is Ram He is good boy"
print(name.find("is")) #It'll print the postion of 'is' in this string
print(name.find("is",5)) #It'll print the postion of 'is' after first postion
#find the postion of word in a string in which we dont know the postion of first string
is_pos1=name.find("is")
is_pos2=name.find("is",is_pos1 + 1)
print(is_pos2)
