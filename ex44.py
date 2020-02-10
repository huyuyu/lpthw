# nheritance versus Composition

class Parent(object):
    def implicit(self):
        print("PARENT implicit()") 
    def override(self):
        print("PARENT override()")
    def altered(self):
        print("PARENT altered()")

class Other(object): 
    def override(self):
        print("OTHER override()") 
    def implicit(self):
        print("OTHER implicit()") 
    def altered(self):
        print("OTHER altered()")

class Child1(Parent):
    pass
dad1 = Parent() 
son1 = Child1()
dad1.implicit() 
son1.implicit()

class Child2(Parent):
    def override(self):
        print("CHILD2 override()")
dad2 = Parent() 
son2 = Child2()
dad2.override()
son2.override()

class Child3(Parent):
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super().altered() 
        print("CHILD, AFTER PARENT altered()")
dad3 = Parent()
son3 = Child3()
dad3.altered()
son3.altered()

class Child4(Parent):
    def override(self):
        print("CHILD4 override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child4, self).altered() 
        print("CHILD, AFTER PARENT altered()")
dad4 = Parent()
son4 = Child4()
dad4.implicit()
son4.implicit()
dad4.override()
son4.override()
dad4.altered()
son4.altered()

class Child5(object):
    def __init__(self):
        self.other = Other()
    def implicit(self):
        self.other.implicit()
    def override(self):
        print("CHILD5 override()")
    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        self.other.altered()
        print("CHILD, AFTER PARENT altered()")
son5 = Child5()
son5.implicit()
son5.override()
son5.altered()