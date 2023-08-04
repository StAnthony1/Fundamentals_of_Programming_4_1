"""
Q1
CONSTANTS and variables
In this task, your job is to use the constants A = 5 & B = 7 and any
of the following operators (*, **, -, /, //, %) to generate a value
of 23 for variable c. This is made more difficult by the following rules:

1. you cannot directly assign a value to c i.e. it is not legal to  say c = 1,
c must be assigned using A, B, c and any operator. So c = A/B would be legal; c = c * c would be legal.
2. No other variables or constants may be used other than those declared above.
3. You may not use the addition (+) operator.
"""
def constantsAndVariables():
    A = 5
    B = 7
    # c = 7 % 5 = 2
    c = B % A
    # c = 2 ** 2 = 4
    c = c**c
    # c = 4 * 7 = 28
    c = c * B
    # c = 28 - 5 = 23
    c = c - A
    return c

print(constantsAndVariables())
