from abc import ABC, abstractmethod

class AbstractParent(ABC): 
    
    @abstractmethod
    def hello_friend(self):
        raise NotImplementedError

class Mother:
    def __init__(self, age = 0):
        self.age = age
        print("mother constructor")

    def do_work(self):
        print("I'm working")

    def do_house_work(self):
        print("listening music")

    def sleep_at_night(self):
        print("I'm sleeping")

class Father(AbstractParent):

    def __init__(self):
        print("father constructor")

    def play_guitar(self):
        print("play guitar")

    def do_house_work(self):
        print("sitting on the sofa and drink beer")

class Daughter(Mother, Father):

    def __init__(self, age = 0):
        Father.__init__(self)
        Mother.__init__(self, age=age)

    def hello_friend(self):
        pass

    def do_work(self):
        print("I'm working like a horse")

class Friend:
    pass

def greet_mother(mother : Mother):
    print ("hello mother!!!!")
    mother.do_work()

def greet_father(father: Father):
    print ("time for beer")
    father.play_guitar()

if __name__ == "__main__":
    daughter = Daughter()
    # mother.do_work()

    # change object class
    # daughter.__class__ = Friend

    greet_mother(daughter)
    greet_father(daughter)
    daughter.hello_friend()
    daughter.do_house_work()
    daughter.sleep_at_night()

    for x in [daughter]:
        x.do_house_work()

    # list
    povtorka_list = ["mathan_2", "programming_2", "superprise"]

    # tuple
    vasian = ("11 years", 12, 3.14, daughter)

    # set
    my_set = {23, 11, 10, "call"}

    # frozen set
    another_set = frozenset(["di_", "mi", "do"])

    # dictionary
    my_dict = {1: "first", "2": 123, (1,2,3): "tuple_as_a_key"}
