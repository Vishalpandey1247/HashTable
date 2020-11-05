# HashTable 
It takes data from user and store it in hash table.

# Istallation
"pip install hash-table

Usage
It stores data
 from HashTable import Hash
 # To Add in Hash Table
 a = Hash(10) #we have to enter length of hash table we required
 h=a.add(44)
 print(h)

Output
['', '', '', '', 44, '', '', '', '', '']

 # To see index value of given data
 h=a.index(44)
 print(h)

 Output
4

# To get the the value by index number
h=a.index(4)
 print(h)

 Output
44

# Update the Value in Hash Table
h= a.update(3,30)
print(h)

Output
['', '', '', '30', 44, '', '', '', '', '']

# To Show the Hash Table
h=a.show()
print(h)

Output
['', '', '', '30', 44, '', '', '', '', '']

# To Rehash the table
a.rehash(3)
b=a.show()
print(b)

Output
[30, 44, '', '', '', '', '', '', '', '']# hash_table
# hash_table
# hash_table
