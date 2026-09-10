class A:
    def show(self):
        print('A')
class B(A):
    def show(self):
        print('B')
    b = B()
    b.show()