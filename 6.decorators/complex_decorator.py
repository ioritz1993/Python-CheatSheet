def decorator_function(function_param):
    def secondary_function(*args, **kwards):       
        print("Exec before call a function")
        function_param(*args, **kwards)     
        print("Exec after call a function")    
    return secondary_function


@decorator_function 
def example_function(arg1, arg2):
    print("============================")
    print("I am the main function. Receive {0} and {1}".format(arg1, arg2))
    print("============================")
    

example_function("Parameter example", arg2="Argument example")