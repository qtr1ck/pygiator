def power(x, y): 
      
    if y == 0: 
        return 1
    if y % 2 == 0: 
        return power(x, y // 2) * power(x, y // 2) 
          
    return x * power(x, y // 2) * power(x, y // 2) 

# THIS IS A PLAGIAT! Method to do Radix Sort 
def radixSort(arr): 
  
    # Find the maximum number to know number of digits 
    max1 = max(arr) 
  
    while max1/exp > 0: 
        countingSort(arr,exp) 
        exp *= 10

# Function to calculate order of the number 
def order(x): 
  
    # Variable to store of the number 
    n = 0
    while (x != 0): 
        n = n + 1
        x = x // 10
          
    return n 
  
# Driver code 
x = 153
print(isArmstrong(x)) 
  
x = 1253
print(isArmstrong(x)) 