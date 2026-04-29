def half(value):
    return value / 2 

def double(value):
    return value * 2 

def second(value):
    return value[1]

print(half(22))
print(half("hello"))
print(half("22"))

# exercise
# Predict what double("22") will do. Then run the code and check. Did it do what you expected? Why did it return the value it did?
# --> answer: I think it may return error of type. 
# after running, the code returned: "TypeError: unsupported operand type(s) for /: 'str' and 'int'". I think because the function expects the input to be integer but they were strings