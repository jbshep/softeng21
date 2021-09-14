from turtles import *

# Stack some turtles.
# Write a loop that shows the contents of the turtle stack.

c1 = ColossusTurtle('Timmy')
c2 = ColossusTurtle('Maximus', c1)
c3 = ColossusTurtle('Maximusser', c2)

t = c3
while t:
    print(t.name)
    if type(t) == ColossusTurtle:
        t = t.buddy
    else:
        t = None
