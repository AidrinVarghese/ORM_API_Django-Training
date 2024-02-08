# print("Hello world!")

# x = "Apples"
# print(type(x))

# y = "orange"

# print(type(y))

# print(x + y)


# y = str(45)

# z = ["orange", "apples", "banana"]
# print(z)

# # methods to study
# # 1. String methods
# # 2. Integer methods
# # 3. Float
# # 4. List
# # 5. Tuple
# # 6. Dictionary
# # 7. Set
# # 8. Boolean
# # 9. Null

def my_functions(**kid):
    print(kid)
    print("His last name is " + kid["lname"])
my_functions(fname ="Tobias", lname ="Refsnes")

def my_fun(arg1,*args):
    print("First argument is " + arg1)
    print(arg1[0])
    print(type(arg1))    
my_fun("hello", 45, None, True)





####   Lambda functions

my_lambda_function = lambda a,b: a + b
def my_function(a,b):
    return  a + b
print(my_function(5,3))
print(my_lambda_function(5,10))
