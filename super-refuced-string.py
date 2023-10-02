#Problem link: https://www.hackerrank.com/challenges/reduced-string/
def superReducedString(s):
    element = []
    for char in s:
        if element and element[-1] == char:
            element.pop()
        else:
            element.append(char)
    
    if not element:
        return "Empty String"
    else:
        return ''.join(element)
