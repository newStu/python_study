print("------------反射机制------------")

class ReflectiveClass:
    """用于演示反射的类"""
    
    def __init__(self, name, value):
        self.name = name
        self._protected = "受保护属性"
        self.__private = "私有属性"
        self.value = value
    
    def public_method(self):
        """公有方法"""
        return f"公有方法调用，name: {self.name}"
    
    def _protected_method(self):
        """受保护方法"""
        return "受保护方法调用"
    
    def __private_method(self):
        """私有方法"""
        return "私有方法调用"
    
    @classmethod
    def class_method(cls):
        """类方法"""
        return "类方法调用"
    
    @staticmethod
    def static_method():
        """静态方法"""
        return "静态方法调用"

# 反射示例
obj = ReflectiveClass("测试对象", 42)

print("=== 属性反射 ===")
# 获取属性
print(f"name 属性: {getattr(obj, 'name', '默认值')}")
print(f"不存在的属性: {getattr(obj, 'nonexistent', '默认值')}")

# 设置属性
setattr(obj, 'new_attribute', '新属性值')
print(f"新增属性: {obj.new_attribute}")

# 检查属性是否存在
print(f"是否有 name 属性: {hasattr(obj, 'name')}")
print(f"是否有 xyz 属性: {hasattr(obj, 'xyz')}")

# 删除属性
delattr(obj, 'new_attribute')
print(f"删除后是否有 new_attribute: {hasattr(obj, 'new_attribute')}")

print("\n=== 方法反射 ===")
# 获取方法并调用
method = getattr(obj, 'public_method')
print(f"动态调用方法: {method()}")

# 获取类方法
class_method = getattr(ReflectiveClass, 'class_method')
print(f"动态调用类方法: {class_method()}")

# 获取静态方法
static_method = getattr(ReflectiveClass, 'static_method')
print(f"动态调用静态方法: {static_method()}")

# 尝试获取私有方法（通过名称重整）
private_method_name = f"_ReflectiveClass__private_method"
if hasattr(obj, private_method_name):
    private_method = getattr(obj, private_method_name)
    print(f"动态调用私有方法: {private_method()}")

print("\n=== 类信息反射 ===")
# 获取类的所有属性和方法
print(f"类名: {obj.__class__.__name__}")
print(f"模块: {obj.__class__.__module__}")
print(f"基类: {obj.__class__.__bases__}")

# 获取所有成员
print(f"所有成员: {dir(obj)}")

# 获取字典形式的所有属性
print(f"__dict__: {obj.__dict__}")

# 获取方法列表
methods = [name for name in dir(obj) if callable(getattr(obj, name)) and not name.startswith('__')]
print(f"所有方法: {methods}")


print("\n------------动态创建类和属性------------")

def create_dynamic_class(class_name: str, attributes: dict, methods: dict = None):
    """动态创建类"""
    if methods is None:
        methods = {}
    
    # 添加类方法
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)
    
    def __str__(self):
        attrs = {k: v for k, v in self.__dict__.items()}
        return f"{class_name}({attrs})"
    
    methods.update({
        '__init__': __init__,
        '__str__': __str__
    })
    
    # 动态创建类
    DynamicClass = type(class_name, (object,), methods)
    
    return DynamicClass

# 动态创建类
PersonClass = create_dynamic_class(
    "Person",
    {"name": str, "age": int},
    {
        "introduce": lambda self: f"我是{self.name}，今年{self.age}岁",
        "is_adult": lambda self: self.age >= 18
    }
)

# 使用动态创建的类
person = PersonClass(name="张三", age=25)
print(f"动态创建的实例: {person}")
print(f"自我介绍: {person.introduce()}")
print(f"是否成年: {person.is_adult()}")

# 动态添加属性和方法
class DynamicAdd:
    pass

# 动态添加类属性
DynamicAdd.new_class_attr = "这是动态添加的类属性"

# 动态添加实例方法
def instance_method(self):
    return f"实例方法调用，{self}"

DynamicAdd.instance_method = instance_method

# 动态添加类方法
@classmethod
def class_method(cls):
    return f"类方法调用，{cls.__name__}"

DynamicAdd.class_method = class_method

# 动态添加静态方法
@staticmethod
def static_method():
    return "静态方法调用"

DynamicAdd.static_method = static_method

# 测试动态添加的方法
instance = DynamicAdd()
print(f"动态类属性: {DynamicAdd.new_class_attr}")
print(f"动态实例方法: {instance.instance_method()}")
print(f"动态类方法: {DynamicAdd.class_method()}")
print(f"动态静态方法: {DynamicAdd.static_method()}")


print("\n------------装饰器高级用法------------")

def timer_decorator(func):
    """计时装饰器"""
    import time
    
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"{func.__name__} 执行时间: {end - start:.4f}秒")
        return result
    
    return wrapper

def cache_decorator(func):
    """缓存装饰器"""
    cache = {}
    
    def wrapper(*args, **kwargs):
        # 创建缓存键
        key = str(args) + str(sorted(kwargs.items()))
        
        if key not in cache:
            cache[key] = func(*args, **kwargs)
            print(f"缓存新结果: {key}")
        else:
            print(f"使用缓存结果: {key}")
        
        return cache[key]
    
    return wrapper

def retry_decorator(max_retries=3, delay=1):
    """重试装饰器"""
    def decorator(func):
        import time
        
        def wrapper(*args, **kwargs):
            for attempt in range(max_retries):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_retries - 1:
                        raise e
                    print(f"第{attempt + 1}次尝试失败，{delay}秒后重试: {e}")
                    time.sleep(delay)
        
        return wrapper
    return decorator

# 装饰器组合使用
@timer_decorator
@cache_decorator
def fibonacci(n):
    """斐波那契数列（带缓存）"""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

@retry_decorator(max_retries=3, delay=0.5)
def unreliable_function():
    """不可靠的函数（用于演示重试）"""
    import random
    if random.random() < 0.7:  # 70% 的概率失败
        raise ValueError("随机失败")
    return "成功!"

# 装饰器测试
print("斐波那契数列计算:")
print(f"fibonacci(10): {fibonacci(10)}")
print(f"fibonacci(10): {fibonacci(10)}")  # 使用缓存

print("\n重试机制测试:")
try:
    result = unreliable_function()
    print(f"结果: {result}")
except Exception as e:
    print(f"最终失败: {e}")


print("\n------------属性描述符进阶------------")

class ValidatedAttribute:
    """带验证的属性描述符"""
    
    def __init__(self, name, validator, default=None):
        self.name = name
        self.validator = validator
        self.default = default
        self.storage = {}
    
    def __get__(self, instance, owner):
        if instance is None:
            return self
        return self.storage.get(id(instance), self.default)
    
    def __set__(self, instance, value):
        if not self.validator(value):
            raise ValueError(f"{self.name} 验证失败: {value}")
        self.storage[id(instance)] = value
    
    def __delete__(self, instance):
        if id(instance) in self.storage:
            del self.storage[id(instance)]

def validate_string_length(min_length=0, max_length=100):
    """字符串长度验证器"""
    def validator(value):
        return isinstance(value, str) and min_length <= len(value) <= max_length
    return validator

def validate_age_range(min_age=0, max_age=150):
    """年龄范围验证器"""
    def validator(value):
        return isinstance(value, int) and min_age <= value <= max_age
    return validator

def validate_email_format():
    """邮箱格式验证器"""
    def validator(value):
        import re
        if not isinstance(value, str):
            return False
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, value) is not None
    return validator

class UserProfile:
    """用户档案类，使用描述符验证"""
    
    username = ValidatedAttribute('username', validate_string_length(3, 20))
    email = ValidatedAttribute('email', validate_email_format())
    age = ValidatedAttribute('age', validate_age_range(0, 120))
    bio = ValidatedAttribute('bio', validate_string_length(0, 500))
    
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if hasattr(self, key):
                setattr(self, key, value)

# 描述符验证测试
try:
    profile = UserProfile(
        username="testuser",
        email="test@example.com",
        age=25,
        bio="这是一个测试用户"
    )
    
    print(f"用户名: {profile.username}")
    print(f"邮箱: {profile.email}")
    print(f"年龄: {profile.age}")
    
    # 测试验证
    profile.username = "newuser"  # 有效
    print(f"修改后的用户名: {profile.username}")
    
    # 测试无效数据
    # profile.age = -5  # 会抛出异常
    # profile.email = "invalid-email"  # 会抛出异常
    
except ValueError as e:
    print(f"验证错误: {e}")


print("\n------------元编程：函数工厂------------")

def create_operation_function(operation):
    """创建数学运算函数的工厂"""
    
    if operation == 'add':
        def add(a, b):
            return a + b
        add.__name__ = 'add'
        add.__doc__ = '加法函数'
        return add
    
    elif operation == 'multiply':
        def multiply(a, b):
            return a * b
        multiply.__name__ = 'multiply'
        multiply.__doc__ = '乘法函数'
        return multiply
    
    elif operation == 'power':
        def power(base, exponent):
            return base ** exponent
        power.__name__ = 'power'
        power.__doc__ = '幂运算函数'
        return power
    
    else:
        raise ValueError(f"不支持的操作: {operation}")

# 函数工厂使用
add_func = create_operation_function('add')
multiply_func = create_operation_function('multiply')
power_func = create_operation_function('power')

print(f"5 + 3 = {add_func(5, 3)}")
print(f"5 * 3 = {multiply_func(5, 3)}")
print(f"5 ^ 3 = {power_func(5, 3)}")

# 动态创建多个函数
operations = ['add', 'multiply', 'power']
functions = {op: create_operation_function(op) for op in operations}

print(f"函数字典: {[func.__name__ for func in functions.values()]}")


print("\n------------类方法和实例方法的动态切换------------")

class MethodSwitcher:
    """方法切换器"""
    
    def __init__(self, mode='normal'):
        self.mode = mode
    
    def process(self, data):
        """根据模式选择不同的处理方法"""
        if self.mode == 'normal':
            return self._normal_process(data)
        elif self.mode == 'reverse':
            return self._reverse_process(data)
        elif self.mode == 'uppercase':
            return self._uppercase_process(data)
        else:
            raise ValueError(f"未知的模式: {self.mode}")
    
    def _normal_process(self, data):
        return f"正常处理: {data}"
    
    def _reverse_process(self, data):
        return f"反转处理: {data[::-1]}"
    
    def _uppercase_process(self, data):
        return f"大写处理: {data.upper()}"

# 动态修改方法
class DynamicMethod:
    def __init__(self):
        self.methods = {}
    
    def register_method(self, name, method):
        """注册方法"""
        self.methods[name] = method
        setattr(self, name, method)
    
    def execute_method(self, method_name, *args, **kwargs):
        """执行指定方法"""
        if method_name in self.methods:
            return self.methods[method_name](*args, **kwargs)
        else:
            raise ValueError(f"方法 {method_name} 不存在")

# 测试动态方法
switcher = MethodSwitcher('reverse')
print(f"反转模式: {switcher.process('hello')}")

switcher.mode = 'uppercase'
print(f"大写模式: {switcher.process('hello')}")

dynamic = DynamicMethod()

# 动态注册方法
dynamic.register_method('greet', lambda name: f"你好, {name}!")
dynamic.register_method('calculate', lambda a, b: a + b)

print(f"动态问候: {dynamic.execute_method('greet', '张三')}")
print(f"动态计算: {dynamic.execute_method('calculate', 10, 20)}")