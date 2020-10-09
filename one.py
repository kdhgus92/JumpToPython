#one.py

print('hello')

def func():
    print("FUNC() IN ONE.PY")

def function1():
    pass

def function2():
    pass

print("TOP LEVEL IN ONE.PY")

if __name__ == "__main__":
    #run the script
    print('ONE.PY is being run directly!')
else:
    print('ONE.py has been imported!')