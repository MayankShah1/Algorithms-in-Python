## Function overloading not possible in Python

'''
def function_1(a,b):
    print('two parameters')

def function_1(a):
    print('one parameter')

function_1(10,20)
function_1(100)

'''

def func_def_params(a,b,c = 20):
    print('result of a * b + c :' ,a * b + c)

func_def_params(12,10)
func_def_params(12,10,15)
