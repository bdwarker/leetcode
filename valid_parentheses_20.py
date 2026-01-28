"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

"""
stack=[]
s=input("Enter string: ")
print(len(s))
brac_Map = {"(":")", "{":"}","[":"]"}
for i in s:
    if i in brac_Map.keys():
        stack.append(i)
    elif i in brac_Map.values():
        if not stack or brac_Map[stack[-1]]!=i:
            print(False)
            break
        stack.pop()
print(len(stack)==0)
