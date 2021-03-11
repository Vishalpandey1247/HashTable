# HashTable 
It takes data from user and store it in hash table.

# Installation
```pip install hash-table```

# Usage
It stores data in hash table in the form of arrays 

 # To Add Data
```python
   from HashTable import Hash
   a = Hash(10) 
   h=a.add(44) 
   print(h)
```

Output:

```
[None, None, None, None, 44, None, None, None, None, None]
```

 # To see index value of given data
 ```python
 h=a.index(44)
 print(h)
```
 Output:
```
4
```

# To get the the value by index number
```python
h=a.index(4)
 print(h)
```
 Output
```
44
```
# Update the Value in Hash Table
```python
h= a.update(3,30)
print(h)
```
Output:
```
[None, None, None, '30', 44, None, None, None, None, None]
```

# To Show the Hash Table
```python
h=a.show()
print(h)
```
Output
```
[None, None, None, '30', 44, None, None, None, None, None]
```

# To Rehash the table
```python
a.rehash(3)
b=a.show()
print(b)
```
Output;
```
[30, 44, None, None, None, None, None, None, None, None]
```
