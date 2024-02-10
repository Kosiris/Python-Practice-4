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
  
  if len(lst) == 0:
    return 0
  
  prod = lst[0]

  
  if len(lst) > 1:
    for i in lst[1:]:
      prod = prod * i

  return prod
print(mult_list[1,2,3])
print(mult_list[15])

# Write a Python function called rev_string() to reverse a string.
def rev_string(str):
    rev = reversed(str)
    for i in rev:
        print(i)

rev_string("Apples and Oranges")

# Write a Python function called num_within() to check whether a number falls in a given range.

def num_within(num, beginning, end):
    if end >= num >= beginning:
        return True
    else:
        return False

print(num_within(44, 6, 13))
print(num_within(11, 17, 20))