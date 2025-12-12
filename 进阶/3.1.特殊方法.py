print("------------类方法和静态方法------------")

class MathUtils:
    """数学工具类"""
    
    @staticmethod
    def add(a, b):
        """静态方法：不需要类或实例"""
        return a + b
    
    @classmethod
    def create_from_string(cls, math_string):
        """类方法：接收类作为第一个参数"""
        parts = math_string.split('+')
        return cls.add(int(parts[0]), int(parts[1]))
    
    def __init__(self, value):
        self.value = value
    
    def multiply(self, factor):
        """实例方法：接收实例作为第一个参数"""
        return self.value * factor

# 使用示例
print("静态方法调用:", MathUtils.add(3, 5))
print("类方法调用:", MathUtils.create_from_string("10+20"))

# 实例方法需要先创建实例
calc = MathUtils(5)
print("实例方法调用:", calc.multiply(3))



print("------------类方法和静态方法差别------------")
class Parent:
    parent_var = "父类变量"
    
    @staticmethod
    def static_method():
        return "静态方法：绑定到父类"
    
    @classmethod
    def class_method(cls):
        return f"类方法：绑定到 {cls.__name__}"

class Child(Parent):
    child_var = "子类变量"

print("--- 继承行为对比 ---")

# 静态方法：始终绑定到定义它的类
print(f"子类调用父类静态方法: {Child.static_method()}")

# 类方法：自动绑定到调用它的类
print(f"子类调用父类类方法: {Child.class_method()}")
print(f"父类调用类方法: {Parent.class_method()}")





print("\n------------描述符协议------------")

import weakref
from typing import Any, Union

class PositiveNumber:
    """描述符：确保数值为正数"""
    
    def __init__(self, default: Union[int, float] = 0):
        self.default = default
        self._value = weakref.WeakKeyDictionary()  # 使用弱引用避免内存泄漏
    
    def __get__(self, instance: Any, owner: Any) -> Union[int, float]:
        if instance is None:
            return 0
        # 返回实际数值而不是描述符本身，避免类型检查错误
        return self._value.get(instance, self.default)
    
    def __set__(self, instance: Any, value: Union[int, float]) -> None:
        if value < 0:
            raise ValueError("数值必须为正数")
        self._value[instance] = value
    
    def __delete__(self, instance: Any) -> None:
        if instance in self._value:
            del self._value[instance]

class Product:
    """使用描述符的类"""
    price = PositiveNumber(0)
    quantity = PositiveNumber(1)
    
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def total_value(self):
        return self.price * self.quantity

# 描述符验证
try:
    p = Product("苹果", 10, 5)
    print(f"产品总价: {p.total_value()}")
    p.price = -5  # 会抛出异常
except ValueError as e:
    print(f"错误: {e}")


print("\n------------运算符重载------------")

class Vector2D:
    """二维向量类"""
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):
        """加法重载"""
        if isinstance(other, Vector2D):
            return Vector2D(self.x + other.x, self.y + other.y)
        elif isinstance(other, (int, float)):
            # 支持标量加法
            return Vector2D(self.x + other, self.y + other)
        return NotImplemented
    
    def __sub__(self, other):
        """减法重载"""
        if isinstance(other, Vector2D):
            return Vector2D(self.x - other.x, self.y - other.y)
        elif isinstance(other, (int, float)):
            # 支持标量减法
            return Vector2D(self.x - other, self.y - other)
        return NotImplemented
    
    def __mul__(self, scalar):
        """乘法重载（标量乘法）"""
        if isinstance(scalar, (int, float)):
            return Vector2D(self.x * scalar, self.y * scalar)
        return NotImplemented
    
    def __rmul__(self, scalar):
        """右乘法重载（支持 scalar * vector）"""
        return self.__mul__(scalar)
    
    def __str__(self):
        """字符串表示"""
        return f"({self.x}, {self.y})"
    
    def __repr__(self):
        """开发者表示"""
        return f"Vector2D({self.x}, {self.y})"
    
    def __eq__(self, other):
        """相等性比较"""
        if isinstance(other, Vector2D):
            return self.x == other.x and self.y == other.y
        return False
    
    def magnitude(self):
        """计算向量长度"""
        return (self.x ** 2 + self.y ** 2) ** 0.5

# 运算符重载示例
v1 = Vector2D(3, 4)
v2 = Vector2D(1, 2)

print(f"向量加法: {v1} + {v2} = {v1 + v2}")
print(f"向量减法: {v1} - {v2} = {v1 - v2}")
print(f"标量乘法: {v1} * 3 = {v1 * 3}")
print(f"向量长度: |{v1}| = {v1.magnitude()}")
print(f"向量相等: {v1} == {v2} = {v1 == v2}")

v3 = Vector2D(3, 4)
print(f"相同向量: {v1} == {v3} = {v1 == v3}")


print("\n------------上下文管理器------------")

class DatabaseConnection:
    """数据库连接类"""
    
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None
    
    def __enter__(self):
        """进入上下文时调用"""
        print(f"连接到数据库: {self.db_name}")
        self.connection = f"模拟连接到 {self.db_name}"
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """退出上下文时调用"""
        print(f"关闭数据库连接: {self.db_name}")
        if exc_type:
            print(f"发生异常: {exc_val}")
        self.connection = None
        return True  # 表示异常已处理
    
    def query(self, sql):
        """执行查询"""
        if not self.connection:
            raise RuntimeError("未连接到数据库")
        print(f"执行SQL: {sql}")
        return f"查询结果: {sql}"

# 上下文管理器使用
try:
    with DatabaseConnection("test.db") as db:
        db.query("SELECT * FROM users")
        db.query("INSERT INTO users VALUES (1, '张三')")
        # 模拟异常
        # raise ValueError("数据库错误")
except Exception as e:
    print(f"捕获异常: {e}")


print("\n------------元类编程------------")

import threading

class SingletonMeta(type):
    """线程安全的单例元类"""
    
    _instances = {}
    _lock = threading.Lock()  # 添加线程锁保证线程安全
    
    def __call__(cls, *args, **kwargs):
        # 双重检查锁定模式
        if cls not in cls._instances:
            with cls._lock:
                if cls not in cls._instances:
                    cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=SingletonMeta):
    """使用单例元类的数据库类"""
    
    def __init__(self):
        print("创建数据库连接实例")
    
    def connect(self):
        return "已连接数据库"

# 单例测试
db1 = Database()
db2 = Database()

print(f"db1 是否等于 db2: {db1 is db2}")
print(f"db1 id: {id(db1)}, db2 id: {id(db2)}")


print("\n------------动态类创建------------")

def create_class(name, bases, attrs):
    """动态创建类的工厂函数"""
    
    # 验证类名
    if not isinstance(name, str) or not name.isidentifier():
        raise ValueError(f"无效的类名: {name}")
    
    # 验证基类
    for base in bases:
        if not isinstance(base, type):
            raise TypeError(f"基类必须是类型对象: {base}")
    
    def __init__(self, **kwargs):
        # 验证属性名
        for key, value in kwargs.items():
            if key.startswith('_') and not key.startswith('__'):
                raise ValueError(f"不能设置私有属性: {key}")
            setattr(self, key, value)
    
    def __str__(self):
        attrs = {k: v for k, v in self.__dict__.items() if not k.startswith('_')}
        return f"{self.__class__.__name__}({attrs})"
    
    # 避免覆盖现有属性
    if '__init__' not in attrs:
        attrs['__init__'] = __init__
    if '__str__' not in attrs:
        attrs['__str__'] = __str__
    attrs['created_dynamically'] = True
    
    return type(name, bases, attrs)

# 动态创建类
DynamicUser = create_class('DynamicUser', (), {})
DynamicProduct = create_class('DynamicProduct', (), {})

# 使用动态创建的类
user = DynamicUser(name="张三", age=25)
product = DynamicProduct(name="手机", price=2999)

print(f"动态用户: {user}")
print(f"动态产品: {product}")
print(f"类是否动态创建: {hasattr(user, 'created_dynamically')}")


print("\n------------多重继承和 super()------------")

class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal 初始化: {self.name}")
    
    def speak(self):
        return f"{self.name} 发出声音"

class Flyable:
    def __init__(self):
        print("Flyable 初始化")
        self.can_fly = True
    
    def fly(self):
        return "飞行中..."

class Bird(Animal, Flyable):
    def __init__(self, name, wingspan):
        # 使用 super() 正确处理多重继承的MRO
        super().__init__(name)  # 这会调用Animal.__init__
        # 由于Flyable没有使用super()，我们需要手动调用
        # 但更好的方式是让Flyable也使用super()
        if not hasattr(self, 'can_fly'):  # 避免重复初始化
            Flyable.__init__(self)
        self.wingspan = wingspan
        print(f"Bird 初始化: {name}, 翼展: {wingspan}")
    
    def speak(self):
        # 调用父类方法
        parent_speak = super().speak()
        return f"{parent_speak}（鸟叫声）"

# 多重继承测试
bird = Bird("麻雀", 15)
print(f"鸟会飞吗: {bird.can_fly}")
print(f"鸟说话: {bird.speak()}")
print(f"鸟飞行: {bird.fly()}")