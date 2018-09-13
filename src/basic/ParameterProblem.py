

# In Python, you can define a function with optional parameters; if you specify a single * in front of a parameter,
# then that will be a tuple of all remaining unnamed values.
# And if you specify two *s in front of a parameter, that will be a dictionary of all remaining named parameters.

def demo(first, second, *third, **fourth):
    print("first" ,first)
    print("second" ,second)
    print("third" ,third)
    print("fourth" ,fourth)
    print()

demo(1 ,2 ,3 ,4 ,5 ,6 ,7)
demo(5 ,6 ,7 ,8 ,aa=9 ,bb=11 ,cc=44)
# Note that * and ** parameters must be the last parameters in a function definition,
# and if you're going to use both of them you put the ** at the very end, after the *.
