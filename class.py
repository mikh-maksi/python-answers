class MyClass:
    i = 1
    def up(self):
        self.i += 1
        print(self.i)

a = MyClass()
a.up()



class MClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'

c = MClass()
print(c.f())
