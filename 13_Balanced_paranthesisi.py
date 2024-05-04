# def is_balanced(parentheses):
#     stack = []
#     opening_brackets = "([{"
#     closing_brackets = ")]}"

#     for char in parentheses:
#         if char in opening_brackets:
#             stack.append(char)
#         elif char in closing_brackets:
#             if not stack:
#                 return False
#             top = stack.pop()
#             if opening_brackets.index(top) != closing_brackets.index(char):
#                 return False

#     return not stack

# # Example usage
# string = input()
# print(is_balanced(string))  # Output: True


parentheses = input("Enter a string containing parentheses, square brackets, and curly braces: ")

stack = []
opening_brackets = "([{"
closing_brackets = ")]}"

for char in parentheses:
    if char in opening_brackets:
        stack.append(char)
    elif char in closing_brackets:
        if not stack:
            balanced = False
            break
        top = stack.pop()
        if opening_brackets.index(top) != closing_brackets.index(char):
            balanced = False
            break
else:
    balanced = not stack

if balanced:
    print("The parentheses are balanced.")
else:
    print("The parentheses are not balanced.")
