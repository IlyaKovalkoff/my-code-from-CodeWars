
def FirstFactorial(num):
    count = 1
    while num > 0 :
        count *= num
        num -= 1
  # code goes here
    return count

# keep this function call here 
print(FirstFactorial(3))