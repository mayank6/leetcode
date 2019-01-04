ops= ["5","-2","4","C","D","9","+","+"]
stack = []
for op in ops:
            if op == '+':
                stack.append(stack[-1] + stack[-2])
            elif op == 'C':
                stack.pop()
            elif op == 'D':
                stack.append(2 * stack[-1])
            else:
                stack.append(int(op))
print(sum(stack))
