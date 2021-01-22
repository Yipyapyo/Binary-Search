import math

def binary_search():
    array_type = input("Do you want to type in your own array? ")
    if array_type == "no" or array_type == "No" or array_type == "NO" or array_type == "n" or array_type == "N":
        array = []
        num = int(input('How many numbers in the array: '))
        for n in range(num):
            numbers = (n + 1)
            array.append(numbers)
        print (array)
    elif array_type == "yes" or array_type == "Yes" or array_type == "YES" or array_type == "y" or array_type == "Y":
        array = []
        num = int(input('How many numbers in the array: '))
        for n in range(num):
            numbers = int(input('Enter number ' + str(n+1) + " "))
            array.append(numbers)
        array = sorted(array)
        print (array)
    else:
        print("You didn't answer the question")#
        binary_search()
        
    element = int(input("What do you want to find? "))
    length = len(array)
    UB = (length)
    LB = 0
    for i in range(0, len(array)): 
      if i == (len(array)-1):
          last_element = int(array[i])
          first_element = int(array[0])
    if element > last_element or element < first_element:
        print ("This number is not in the list")
        binary_search()
                
    found = False
    checks = 1
    
    while found == False:
          midpoint = (math.ceil((UB + LB) / 2))
          if array[midpoint - 1] == element:
              found = True
          else:
              if array[midpoint - 1] > element:
                  UB = (midpoint - 1)
                  checks = (checks + 1)
              else:
                  LB = (midpoint + 1)
                  checks = (checks +1)
    
    if midpoint == 10:
        print ("Found at the " + str(midpoint) + "th position")
        binary_search()
    elif midpoint == 11:
        print ("Found at the " + str(midpoint) + "th position")
        binary_search()
    else:
        
        n = str(midpoint)
        digit = int(n[-1])
    
        if digit == 1:
            print ("Found at the " + str(midpoint) + "st position")
        elif digit == 2:
            print ("Found at the " + str(midpoint) + "nd position")
        elif digit == 3:
            print ("Found at the " + str(midpoint) + "rd position")
        else:
            print ("Found at the " + str(midpoint) + "th position")
            
    if checks == 1:
        print ("It took " + str(checks) + " check")
    else:
        print ("It took " + str(checks) + " checks")         
        
        binary_search()
    
binary_search()


