"""Read but DON'T TOUCH the Quote - go to Question 1 below"""

Quote = "A few people laughed; a few people cried. Most people were silent. " \
       "I remembered the line from the Hindu scripture, the Bhagavad Gita; " \
       "Vishnu is trying to persuade the prince that he should do his duty, " \
       "and to impress him, takes on his multiarmed form and says, " \
       "‘Now I am become Death, the destroyer of worlds.’ " \
       "I suppose we all thought that, one way or another."



"""
Question 1

CONSTANTS and variables
In this task, your job is to use the constants A = 5 & B = 7 and any
of the following operators (*, **, -, /, //, %) to generate a value
of 23 for variable c. This task is made more difficult by the following rules:

1. you cannot directly assign a value to c i.e. it is not legal to  say c = 1,
c must be assigned using A, B, c and any operator. So c = A/B would be legal; c = c * c would be legal.
2. No other variables or constants may be used other than those declared above.
3. You may NOT use the addition (+) operator.
"""
def constantsAndVariables() -> int:
    A = 5
    B = 7
    c = A  # alter this line and add any others to generate a value
    # of 23 for c before the return statement (below). Make sure
    # your indentation matches the other constants (A & B) and variable (c)

    return c


"""
Question 2
Use string handling functions (see textbook p.5) to determine the following
a)
the number of times the number of characters in the quote fit in to 23.
"""
def numTimesQuoteIn23() -> int:
    #write your code here and return the variable which stores the answer to question 2.a
    return 0# you are expected to replace this 0 return value.


"""
b)
the two numbers representing the start and the end indices of the substring "Now I am become Death, 
the destroyer of worlds" (excluding the quote marks) - to help you check your answer you might choose to
use those numbers to see if you can extract the substring from the quote. This can be done using Python 
syntax: Quote[0:10] would, for instance, return the string: "A few peop" - use the test space below to 
try this out.
"""
def startAndEndIndicesOfSubString() -> (int, int):
    # write your code here
    return 0, 0 #return the variables storing the int at the start of the quote first


"""
c) the string value of characters represented by the following integer sequence:
74 32 82 111 98 101 114 116 32 79 112 112 101 110 104 101 105 109 101 114 
"""
def integerSeqToString() -> str:
    #write your code here - this may take a number of lines!
    return ""

#TESTING SPACE: write any tests/experiments you want to do below
print("Example test output")