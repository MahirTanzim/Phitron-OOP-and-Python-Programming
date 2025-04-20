class A:
    def __init__(self, x):
        x = 3
        self.x = x
    def change(self):
        self.x = 12

ans = []
a = A(13)
ans.append(a. x)
a.change ()
ans.append(a.x)
print(ans)
