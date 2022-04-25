import stack

string = 'gninraeL nIdekniL htiw tol a nraeL'

reversed_string = ""

s = stack.Stack()


# solution
for x in string:
    s.push(x)

while not s.isEmpty():
    reversed_string += s.pop() 

print(reversed_string)

