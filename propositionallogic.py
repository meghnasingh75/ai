# ALGORITHM:
# Propositional logic is also called Boolean logic as it works on 0 and 1. 
# ● In propositional logic, we use symbolic variables to represent the logic, and we 
# can use any symbol to represent a proposition, such as A, B, C, P, Q, R, etc. 
# ● Propositions can be either true or false, but it cannot be both. 
# ● Propositional logic consists of an object, relations or function, and logical 
# connectives.
# ● These connectives are also called logical operators. 
# ● The propositions and connectives are the basic elements of the propositional 
# logic.




def truthTable(expression,inputs=2): 
    print("Boolean Expression:") 
    print(" X = " + expression.upper()) 
    expression = expression.lower() 
    expression = expression.replace("and","&") 
    expression = expression.replace("xor","^") 
    expression = expression.replace("or","|") 
    expression = expression.replace("not","~") 

    print("\nTruth Table:") 
    if inputs==2: 
        print(" -------------") 
        print(" | A | B | X |") 
        print(" -------------") 

        for a in range(0,2):
            for b in range(0,2): 
                x = eval(expression) 
                print(" | " + str(a) + " | " + str(b) + " | " + str(x) + "|" )
                print(" -------------") 

    elif inputs==3: 
        print(" -----------------") 
        print(" | A | B | C | X |") 
        print(" -----------------") 

        for a in range(0,2): 
            for b in range(0,2): 
                for c in range(0,2): 
                    x = eval(expression)
                    print(" | " + str(a) + " | " + str(b) + " | " + str(c) + " | " + str(x) + " |" ) 
                    print(" -----------------") 

A = input('Enter first statement: ') 
B = input('Enter second statement: ') 
expression = A +" "+ B 
truthTable(expression,2)