__all__ = ['Turtle', 'ColossusTurtle']

class Turtle(object):
    def __init__(self, name):
        self.name = name        

    def speak(self):
        print('Hi, my name is {}.'.format(self.name))

    def __repr__(self):
        return '<Turtle name={}>'.format(self.name)

class ColossusTurtle(Turtle):
    def __init__(self, name, buddy=None):
        super().__init__(name)    # NOTE: no 'self' here
        self.carry(buddy)

    def carry(self, buddy):
        self.buddy = buddy

    def __repr__(self):
        return '<ColossusTurtle name={} buddy={}>'.format(self.name, self.buddy)

def test_turtles():
    c1 = ColossusTurtle('Sven')
    c2 = ColossusTurtle('Guido')
    c2.carry(c1)
    if c1 == c2.buddy:
        print('Yay')
    else:
        print('Boo')

if __name__ == '__main__':
    t = Turtle('Timmy')
    t.speak()

    c1 = ColossusTurtle('Maximus', t)
    print(c1)

    c2 = ColossusTurtle('Maximusser')
    c2.carry(c1)
    print(c2)

