def decorator(func):
    def wrapper(*args,**kwargs):
        print("---starts---")
        func(*args,**kwargs)
        print("---ends---")
    return wrapper

@decorator
def printer(word1,word2,):
    print(word2)


printer("Hello World!","I am Karthick")