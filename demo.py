"""def numbers(limit):
    i = 0
    numbers = []

    while i < limit:
        numbers.append(i)
        i = i + 1
    return numbers

user_limit = int(input("Give me a limit "))
print(numbers(user_limit))"""

"""def xxx():
    a=10
    b=15
    c=20
    return a,b

def yyy():
    a,b = xxx()
    print(a)      
    print(b)        

print(yyy())



def squared(x):
	y = x * x
	return y

def sum_of_squares(x, y, z):
	e = squared(x)
	print(e)
	b = squared(y)
	print(b)
	c = squared(z)
	print(c)

	return e + b + c

a = -5
b = 2
c = 10
result = sum_of_squares(a, b, c)
print(result)"""


"""def func1():
	a=8
	b=9
	return a,b
def func2(x,y):

	a,b = func1()
	z=x+y+a+b
	return z
 
a=func2(4,6)
print(a)"""

import re

"""email = "sarandeveloper94@gmail.com"

EMAIL_REGEX = re.compile(r"[^@]+@[^@]+\.[^@]+")
if EMAIL_REGEX.match(email):
	print("Valid")
else:
	print("Invalid")	"""


name = "saran33434"

demo = "[a-zA-Z_][a-zA-Z0-9]*"	
if re.search(demo, name):
	print("Correct")
else:
	print("No")

"""phonenumber= "51623232"

regex= "(0/91)?[7-9][0-9]{9}"

if re.search(regex, phonenumber):
	print("Valid phone number")
else:
	print("Invalid phone number") """

"""def profile():
    name = "Danny"
    age = 30
    return (name, age)

profile_data = profile()
print(profile_data[0])
# Output: Danny

print(profile_data[1])
# Output: 30





my_variable = 0
saran = 5

def func1():
    global my_variable, saran
    my_variable = -1
    print("func1:{0}{1}".format(my_variable,saran))


def gillespie():
    global my_variable, saran
    my_variable = 4
    print("gillespie:{0} {1}".format(my_variable,saran))


#
print("before:{0}{1}".format(my_variable,saran))
func1()
gillespie()
print("after:{0}{1}".format(my_variable,saran))"""