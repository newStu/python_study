print("------------普通类------------")
class Student: 
    def __init__(self, obj):  
        self.name = obj["name"]
        self.age = obj["age"]
        self.score = obj["score"]

    def show_age(self):
        print(self.age)


student = Student({"name": "wzy", "age": 17, "score": 100})
student.show_age()



print("------------私有和公有------------")
class Teacher: 
    def __init__(self, name, age, password):
        self.name = name
        self._age = age 
        self.__password = password

    @property
    def age(self):
        """获取受保护的_age属性"""
        return self._age

    @age.setter
    def age(self, value):
        """设置受保护的_age属性，带有验证逻辑"""
        if value < 0:
            raise ValueError("年龄不能为负")
        self._age = value

    @property
    def password(self):
        print(self.__password)

    def show_name(self):
        print(self.name)


teacher = Teacher("wzy", 17, "152346")
# 公有属性，可以直接访问
print(teacher.name)
# 受保护属性，可以直接访问, 但是不推荐
print(teacher._age)
# 私有属性，无法直接访问, 可以通过 _类名__属性名 访问, 但是不推荐
# print(teacher._Teacher__password)
teacher.password
print(teacher.name)
teacher.age = 18
teacher.age





print("------------抽象类------------")
from abc import ABC, abstractmethod

class Vehicle(ABC):
    # 抽象属性
    @property
    @abstractmethod
    def brand(self):
        """车辆品牌"""
        pass
    
    @property
    @abstractmethod
    def max_speed(self):
        """最高速度"""
        pass

    # 可选实现的抽象方法
    def start(self):
        print("启动")
    
    # 必须实现的抽象方法 
    @abstractmethod
    def stop(self):
        """停止"""
        pass

class Car(Vehicle):
    def __init__(self, brand, max_speed):
        self._brand = brand
        self._max_speed = max_speed
    
    @property
    def brand(self):
        return self._brand
    
    @property
    def max_speed(self):
        return self._max_speed
    

    def stop(self):
        print("停止")



car = Car("奔驰", 200)
print(car.brand)      # 奔驰
print(car.max_speed)  # 200
car.start()
car.stop()





print("------------继承顺序, 决定优先级------------")
# Mixin 模式
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class XMLMixin:
    def to_xml(self):
        # XML 转换逻辑
        pass
    def to_json(self):
        return "json"

class User(JSONMixin, XMLMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age


user = User("wzy", 17)
print(user.to_json()) # 调用 JSONMixin 的 to_json


class UserA(XMLMixin, JSONMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age

user_a = UserA("wzy", 17)
print(user_a.to_json()) # 调用 XMLMixin 的 to_json



 