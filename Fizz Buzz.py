for num in range(1,101):
    ForB = "" # initialises a string / defines it without creating a value
    if num % 3 == 0: # if number can be divided by 3
        ForB = ForB + "Fizz" # print Fizz
    if num % 5 == 0: # if number can be divided by 5
        ForB = ForB + "Buzz" # print Buzz
    if num % 5 != 0 and num % 3 != 0:
        ForB = ForB + str(num) # add the numbers inbetween
    print(ForB) # print whole sequence

#ForB = Fizz or Buzz