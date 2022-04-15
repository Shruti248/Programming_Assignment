# 1
try:  
    a = 10/0  
    print (a)
except ArithmeticError:  
        print ("This statement is raising an arithmetic exception.")
else:  
    print ("Success.")
    
    
# 2
try: 
    a = [1, 2, 3] 
    print (a[3]) 
except LookupError: 
    print (“Index out of bound error.”)
    
    
# 3
class Attributes(object):
    pass
  
object = Attributes()
print (object.attribute)

# 4
Import math
Print (math,exp(1000))

# 5
Array=[0,1,2]
Print(array[3])
