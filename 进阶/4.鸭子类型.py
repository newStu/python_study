# "如果它走起来像鸭子，叫起来像鸭子，那么它就是鸭子"
class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

def make_sound(animal):
    # 不检查类型，只关心方法
    print(animal.speak())

make_sound(Dog())  # 正常工作
make_sound(Cat())  # 正常工作