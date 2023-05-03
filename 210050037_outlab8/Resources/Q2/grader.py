
import string
from tokenize import Double

def add(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 + arg2).

        You are expected to think of corner cases,
        and appropriately raise Exception.
    """
    if not type(arg1) is float and not type(arg1) is int:
        raise TypeError("Only numbers are allowed")
    if not type(arg2) is float and not type(arg2) is int:
        raise TypeError("Only numbers are allowed")
    return arg1+arg2

def subtract(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 - arg2).

        As the previous function, you are expected to think of corner cases,
        and appropriately raise Exception.
    """
    if not type(arg1) is float and  not type(arg1) is int:
        raise TypeError("Only numbers are allowed")
    if not type(arg2) is float and  not type(arg2) is int:
        raise TypeError("Only numbers are allowed")
    return arg1-arg2

def divide(arg1, arg2):
    r"""
        This function accepts two arguments - arg1 and arg2.
        It returns the result of the operation (arg1 / arg2).

        You are expected to think of corner cases, and appropriately raise Exception.
    """
    if not type(arg1) is float and not type(arg1) is int:
        raise TypeError("Only numbers are allowed")
    if not type(arg2) is float and not type(arg2) is int:
        raise TypeError("Only numbers are allowed")
    if (arg2==0):
        raise Exception("Division by zero is Inappropriate")
    return arg1/arg2

def str_left_rotate(arg1, arg2):
    r"""
        This function should left rotate a string by the specified amount.
        arg1 signifies the input string and arg2 signifies the amount of rotation.

        Example - 
        1. str_left_rotate("hello", 2) should return "llohe"
        2. str_left_rotate("hello", 1) should return "elloh"
        3. str_left_rotate("hello", 4) should return "ohell" and so on

        You are not to use any inbuilt string method, the implementation has to be
        done by you!!

        Again, you are expected to think of corner cases, and appropriately raise Exception.
    """
    if not type(arg1) is str:
        raise TypeError("arg1 must be string")
    if not type(arg2) is int:
        raise TypeError("arg2 must be int")
    arg2 = arg2 % len(arg1)
    x = list(range(0,len(arg1)))
    for i in range(0,len(arg1)):
        x[i]=(x[i]+arg2)%len(arg1)
    str1=""
    for i in x:
        str1=str1+arg1[i]
    return str1

def apply(fn, args):
    r"""
        This is the API end-point available to the grader.
        The grader will supply the function pointer to this function,
        along with the arguments and expect the return value.

        Example - 
        1. apply(add, (2, 3)) will expect 5 as the answer.
        2. apply(subtract, (2, 3)) will expect -1 as the answer.
    """

    if(len(args) != 2):
        raise Exception("Incorrect number of arguments")
    arg1 = args[0]
    arg2 = args[1]
    return fn(arg1,arg2)
