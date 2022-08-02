"""
This script is working as Goal Seek function in Excel for single variable functions.
It is using Newton-Rapson method. A root-finding algorithm, which produces successively better approximations to the roots (or zeroes) of a real-valued function.
It is using first derivative during iterative proces to find the best aproximation of the root.
"""

def first_derivative(function, point, dx=1e-5):
    #Function calculating first derivative of given function.
    
    #input:
    #function  - given function, which derivative is to be found
    #point     - viarable value for which derivative should be found
    #dx        - infinitesimal change in function's variable

    f_x1 = function(point)
    f_x2 = function(point+dx)

    return (f_x2-f_x1)/dx

def goal_seek(function, goal, start, max_iterations=1000, trace=1, epsilon=1e-5):
    #Goal seek function is solving non-linear equetion to indicated goal. 
    # It is using Newton-Rapson method 
    
    #input:
    #function       - given function, which derivative is to be found
    #start          - initial gues of root
    #max_iteration  - maximum iterations made by algorithm, default value 1000
    #trace          - paramether tooks value 1 not to print iteration process or 0 to trace iteration proces
    #epsilon        - level of approximation, default value 1e-5
    
    fun = lambda y: function(y)-goal

    #Newton-Rapson method
     
    if abs(fun(start))<=epsilon:
        
        return start
    
    x=start

    for i in range(max_iterations):
        xn = x-(fun(x)/first_derivative(fun,x))
        if trace ==0:
            print(f'iteration: {i+1}, x = {x}, xn = {xn}, f(x)= {fun(x)}, df/dx = {first_derivative(fun,x)}')
        if abs(xn-x)<=epsilon:
            break
        else:
            x=xn

    return x


if __name__ == "__main__":

    from math import *

    #Test of the given script
    fun = input("Give example of f(x) function: ")
    goal = float(input("Give want goal to be achieved: "))
    x0 = float(input("Give a number which is suspected to be root of function: "))
   

    input_fun = lambda x: eval(fun)
    print(f'The root of given function is: {goal_seek(input_fun, goal, x0, epsilon=1e-7 ,trace=0)}')

