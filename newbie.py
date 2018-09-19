#normal print
print("Hello world\n")

#input long strings
str = """For long string
with new lines
it may print the new lines toooooo!\n"""    
print (str)

#list
list = ['a', 'abc', 'ab sdasd ', 1]
print(list)
    #append on list
list.append("new component append at the end of list")
print(list[4])
    #remove selected value
list.remove('a')
print(list[0])
    #delete element on the position
del list[0]
print(list[0])
print('')

#dictionary
dicdata = {'location' : 'irvine', 'number' : '7143360420'}
print(dicdata['location'])
    #add dic data
dicdata['company'] = 'blizzard'
print(dicdata)
    #del dic data
del dicdata['location']
print(dicdata)
    #get dic keys, values, items
print(dicdata.keys())
print(dicdata.values())
print(dicdata.items())

#Tuples... similar with list
#But tuple values cannot be edited
tupledata = (1,2,3) #list = [1,2,3]
print('')

#sequence data
str = "ABCDEFG"
list = [1,2,3,4,5]
tuple = (6,7,8,9,10)
    #indexing
print(str[2])
    #slicing...[start_index : end_index : step(default 1)]... end index is not included
print(str[0:3])
print(str[3:])
print(str[:-2]) #until last 2
print(str[::2]) #A(B)C(D)E(F)G
    #connect
str1 = "AB"; str2 = "CD"
print(str1+str2)
print(str1*3)
    #check a member
print('A' in str1)
print('C' in str1)
    #length
print(len(str1))

#print without newline ... end=' '
print("There will be no new line", end = '')
print("!CHECK!")