'''
  what are Armstrong Numbers?
  when sum of all digits of an number which are powered or
  exponentialised with the highest place order of the number,
  is equal to the actual number are said to be an armstrong number.
'''


n = input() #take the number as string
l = len(n) # find the length of the number for exponential purpose
sum = 0
for x in n: # separate all digits
    sum += int(x)**l #exponent them
    
if int(n) == sum:
    print(str(n)+" is a armstrong number")

else:
    print(str(n) + " is not an armstron number")
