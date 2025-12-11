import queue

expression1 = "[(2+3)*4+5]/6-{(7*8)+[4]}" # brackets ok
expression2 = "[(2+3]/4)"                 # brackets not correct
expression3 = "(2-3*4+(5/6)"               # brackets not correct

def brackets_ok(expression):
    # We use a standard Python list as a stack.
    # It allows append() to push and pop() to remove the top item.
    stack = []
    
    # Map closing brackets to their corresponding opening brackets for easy lookup
    # This helps us check matching pairs instantly
    pairs = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        # 1. Skip all but the brackets
        if char not in "()[]{}":
            continue
            
        # 2. If it is an opening bracket, put it on the stack
        if char in "([{":
            stack.append(char)
            
        # 3. If it is a closing bracket...
        elif char in ")]}":
            # Check if stack is empty (meaning a closing bracket with no opener)
            if not stack:
                return False
            
            # Get the item from the stack
            top_element = stack.pop()
            
            # Compare whether it is a matching opening bracket
            if top_element != pairs[char]:
                return False

    # Final check: If the stack is not empty, we have unclosed brackets left
    if len(stack) > 0:
        return False
        
    return True

# --- Testing the code ---

if brackets_ok(expression1):
    print(f"Expression 1: OK")
else:
    print(f"Expression 1: Incorrect")

if brackets_ok(expression2):
    print(f"Expression 2: OK")
else:
    print(f"Expression 2: Incorrect")

if brackets_ok(expression3):
    print(f"Expression 3: OK")
else:
    print(f"Expression 3: Incorrect")