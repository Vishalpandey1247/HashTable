class Hash():
   def __init__(self,key):
       self._elements=[""]
       for i in range(key-1):
           self._elements.append('')
           
   def add(self,key):
       if str(key).isdigit()==True:
          pos=int(int(key)%len(self._elements))
          if not self._elements[pos]:
             self._elements[pos]=int(key)
          else:
             i=0
             while i<=len(self._elements):
                 if pos==(len(self._elements)-1):
                    pos=0
                 else:
                    pos+=1
                 if not self._elements[pos]:
                    self._elements[pos]=int(key)
                    break
                 else:
                    i+=1
                    
   def index(self,key):
       if str(key).isdigit()==True:
          if int(key) in self._elements:
             return self._elements.index(int(key))
             
   def get(self,key):
       if str(key).isdigit()==True:
          if int(key)<len(self._elements):
             return self._elements[int(key)]
             
   def update(self,key,value):
       if str(key).isdigit()==True and str(value).isdigit()==True:
          if int(key)<len(self._elements):
             self._elements[int(key)]=int(value)
             
   def show(self):
       n=[]
       for k in self._elements:
           n.append(k)
       return n
   def rehash(self,c):
       for key in self._elements:
           self._elements[self._elements.index(key)]=''
           if str(key).isdigit()==True:
              pos=int(((int(key%(len(self._elements)-1))+key)*c)%(len(self._elements)-1))
              if not self._elements[pos]:
                 self._elements[pos]=int(key)
              else:
                 i=0
                 while i<=len(self._elements):
                     if pos==(len(self._elements)-1):
                        pos=0
                     else:
                        pos+=1
                     if not self._elements[pos]:
                        self._elements[pos]=int(key)
                        break
                     else:
                        i+=1