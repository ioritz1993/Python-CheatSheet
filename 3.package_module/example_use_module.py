import functions_example
from package_example.general_functions import exec_function_from_general_functions


functions_example.exec_function() # When doing it WITHOUT FROM the syntax is package.function
exec_function_from_general_functions() # When doing it WITH FROM calls the function directly
