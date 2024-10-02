def ValidParenthesis(String):
    Map={
        ')':'(',
        '}':'{',
        ']':'['
    }
    Stack=[]
    for char in String:
        if char in Map:
            Top_Element=Stack.pop() if Stack else '#'
            if Map[char] != Top_Element:
                return False
        else:
            Stack.append(char)
    return not Stack
print(ValidParenthesis("()"))
print(ValidParenthesis("(]"))         
print(ValidParenthesis("([])")) 
print(ValidParenthesis("()[]{}"))