# Write a Python function called max_num()to find the maximum of three numbers.

def max_number(numbers):
    max_num = max(numbers)
    print(max_num)

numbers = (1, 13, 19)
max_number(numbers)

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(values):
    total = 1
    for i in values:
        total *= i
    print(total)

values = [2, 5, 6]
mult_list(values)

# Write a Python function called mult_list() to multiply all the numbers in a list.

def mult_list(lst):
  result = 1
  for num in numbers:
     result = num
  return result

# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    return str[::-1]
print(rev_string("Apples and Oranges"))

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num, beginning, end):
    if end >= num >= beginning:
        return True
    else:
        return False

print(num_within(44, 6, 13))
print(num_within(11, 17, 20))

# Solution Code, I have no clue how to do this. Write a Python function called pascal() that prints out the first n rows of Pascal's triangle.
triangle = [[1],[1,1]]
def pascal(n):
  #base case
  if n < 1:
    print("invalid number of rows")
  elif n == 1:
    print(triangle[0])
  else:
    row_number = 2
    #fill up correct number of rows in triangle
    while len(triangle) < n:
      row = []
      row_prev = triangle[row_number - 1]
      #create correct row, then add to triangle (this row will be 1 longer than row before it)
      length = len(row_prev)+1
      for i in range(length):
        #first number is 1
        if i == 0:
          row.append(1)
        #intermediate nunmbers get added from previous rows
        elif i > 0 and i < length-1:
          row.append(triangle[row_number-1][i-1]+triangle[row_number-1][i])
        #last number is 1
        else:
          row.append(1)
      triangle.append(row)
      row_number += 1

    #print triangle
    for row in triangle:
      print(row)

pascal(2)
pascal(5)