class A:
    def __init__(self):
        self.x=100

class B(A):
    def __init__(self):
        super().__init__()
        self.y=200

class C(B):
    def __init__(self):
        super().__init__()
        self.z=300

objc=C()
print(objc.x)
print(objc.y)
print(objc.z)