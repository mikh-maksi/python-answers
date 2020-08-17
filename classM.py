class Math:
    base = 1

    def plus(self,a):
        self.base += a


    def minus(self,a):
        self.base -= a

    def res(self):
        print(self.base)
        return(self.base)


m = Math()
print(m.res())

m.plus(5)
print(m.res())

m.minus(2)
print(m.res())
