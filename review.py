
#solution 1
number = int(input("Enter a number: "))
#
#def factorial(number):
#    count = 1
#    while number >= 1:
#        count = count * number
#        number -= 1
#        print(count)
#factorial(number)
result = 1
#solution two
#this solution prints the answer from 15 down to zero
for number in range(number,0,-1):   #increments the amount of places as the last number
    result = number * result            
    #or result *= num for short hand
print(result)    


#to increment forward:
for num in range(1,5+1):
    print(num)








