# import sys
# max_recussion= sys.getrecursionlimit()
# print(max_recussion)



# def hello():
#     print(hello)
#     hello()
# hello()

# def countdown(start):
#     '''countdown from a number'''
#     print(start)
#     if start < 10 :
#      countdown(start+1)
# countdown(0)

# def fact(n):
#   f=1
#   for i in range(1,n+1):
#     f=f*i
#   return f

# result=fact(10)
# print(result)


def factorial(n):
    '''calculate the factorial of a number'''
    if n == 0 :
     return 1
    else:
       return n(n-1)
    print(factorial(n))

