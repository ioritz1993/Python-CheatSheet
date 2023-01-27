def decorator_function(function_param):
    def secondary_function():
        print("Exec before call a function")
        function_param()    
        print("Exec after call a function")  
    return secondary_function
  
@decorator_function   
def example_function():
    print("============================")
    print("I am the main function")
    print("============================")

example_function()
 
