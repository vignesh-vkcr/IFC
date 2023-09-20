def repetition_decorator(repeat):
    def decorator(func):
        def wrapper():
            for r in range(repeat):
                print("---starts---")
                func()
                print("---ends---")
        return wrapper
    return decorator


#@repetition_decorator(5)
def printer():
    print("Hello World")

printer=repetition_decorator(5)(printer)
printer()