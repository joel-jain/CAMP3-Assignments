class Box():
    def __init__(self):
        self.width=0
        self.height=0
        self.depth=0

    def get_volume(self):
        return self.width*self.height*self.depth

objBox1=Box()
objBox2=Box()

objBox1.width=10
objBox1.height=10
objBox1.depth=10

objBox2.width=5
objBox2.height=5
objBox2.depth=5


print(f"volume of box1:{objBox1.get_volume()}")
print(f"volume of box2:{objBox2.get_volume()}")

class parabox:
    def __init__(self,width,height,depth):
        self.width=width
        self.height=height
        self.depth=depth
    def get_volume(self):
        return self.width*self.depth*self.height

print("\n with parameterized constructor")
print("--------------------------------")

objBox3=parabox(4,4,4)
objBox4=parabox(8,8,8)

print(f"volume of box3:{objBox3.get_volume()}")
print(f"volume of box4:{objBox4.get_volume()}")