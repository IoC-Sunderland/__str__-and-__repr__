# Withour __str__ and __repr__
class My_without_str__Class:

    def __init__(self):
        pass

c1 = My_without_str__Class()

print(c1) # __main__.My_without_str__Class object at XXX

# With __str__ and __repr
class My_with__str__Class:
    
    def __init__(self):
        pass
    
    def __str__(self):
        return "Hi from MyClass!"
    
    def __repr__(self):
        return "MyClass()"

c2 = My_with__str__Class()

print(c2) # Hi from MyClass!

# Finally, try accessing the c1 and c2 instances from the REPL e.g.

# > c1
# > c2

