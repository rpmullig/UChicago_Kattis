import sys

x = str(sys.stdin.readline()).replace('\n', '').split(' ')
#print x

def rpn(input):
    for i in xrange(len(x)):
        if x[i] is "false":
            x[i] = "False"
        elif x[i] is "true":
            x[i] = "True"


    operators = ["+", "*", "==", "and", "or"]
    boolops = ["and", "or"]
    stack = []

    for elm in input:
        #print elm
        if elm not in operators:
            stack.append(elm)
            #print stack
        if elm in operators:
            if len(stack) < 2:
                return "SYNTAX ERROR"
            else:
                operand_2 = stack.pop()
                operand_1 = stack.pop()
                if type(operand_1) != type(operand_2):
                    return "TYPE ERROR"
                elif elm in boolops and (type(operand_1) is bool or type(operand_2) is bool):
                    return "TYPE ERROR"
                elif elm not in boolops and (type(operand_1) is int or type(operand_2) is int):
                    return "TYPE ERROR"
                else:
                    tmp = operand_1 + " " + elm + " " + operand_2
                    stack = [str(eval(tmp))] + stack

                                       
    if len(stack) != 1:
        return "SYNTAX ERROR"
    else:
        return stack[0]


print rpn(x)
