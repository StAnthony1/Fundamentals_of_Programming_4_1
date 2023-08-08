from blankquestions.Assignment import constantsAndVariables
from solutions.AssignmentSolutions import constantsAndVariables as constantsAndVariablesAnswer

def testconstantsAndVariables():
    assert constantsAndVariables() == 23

def testconstantsAndVariablessolutio():
    assert constantsAndVariablesAnswer() == 23