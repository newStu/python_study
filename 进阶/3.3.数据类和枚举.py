print("------------数据类 dataclass------------")

from dataclasses import dataclass, field
from typing import List, Optional
from datetime import datetime

@dataclass
class User:
    """用户数据类"""
    name: str
    email: str
    age: int = 0
    is_active: bool = True
    created_at: datetime = field(default_factory=datetime.now)
    tags: List[str] = field(default_factory=list)
    
    def __post_init__(self):
        """初始化后处理"""
        if self.age < 0:
            raise ValueError("年龄不能为负数")
        
        # 自动将邮箱转为小写
        self.email = self.email.lower()
    
    def display_info(self) -> str:
        """显示用户信息"""
        return f"用户: {self.name}, 年龄: {self.age}, 邮箱: {self.email}"

# 数据类使用示例
user1 = User("张三", "ZHANG@EXAMPLE.COM", 25)
user2 = User("李四", "li@example.com", tags=["developer", "python"])

print(f"用户1: {user1}")
print(f"用户2: {user2}")
print(f"用户1显示: {user1.display_info()}")
print(f"用户1相等: {user1 == User('张三', 'zhang@example.com', 25)}")

@dataclass(order=True)
class Product:
    """支持排序的产品类"""
    sort_index: int = field(init=False, repr=False)
    name: str
    price: float
    
    def __post_init__(self):
        self.sort_index = self.price

# 数据类排序
products = [
    Product("苹果", 5.0),
    Product("香蕉", 3.0),
    Product("樱桃", 8.0)
]

print(f"原始产品顺序: {[p.name for p in products]}")
sorted_products = sorted(products)
print(f"按价格排序后: {[p.name for p in sorted_products]}")


print("\n------------枚举类------------")

from enum import Enum, IntEnum, Flag, auto

class Status(Enum):
    """状态枚举"""
    PENDING = "pending"
    RUNNING = "running"
    SUCCESS = "success"
    FAILED = "failed"

class Priority(IntEnum):
    """优先级枚举（整数枚举）"""
    LOW = 1
    MEDIUM = 2
    HIGH = 3
    URGENT = 4

class Permission(Flag):
    """权限枚举（标志枚举）"""
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    ADMIN = READ | WRITE | DELETE

class DayOfWeek(Enum):
    """星期枚举"""
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5
    SATURDAY = 6
    SUNDAY = 7
    
    @property
    def is_weekend(self):
        """判断是否是周末"""
        return self in [DayOfWeek.SATURDAY, DayOfWeek.SUNDAY]
    
    def next_day(self):
        """获取下一天"""
        days = list(DayOfWeek)
        current_index = days.index(self)
        return days[(current_index + 1) % len(days)]

# 枚举使用示例
task_status = Status.RUNNING
priority = Priority.HIGH
permissions = Permission.READ | Permission.WRITE
today = DayOfWeek.WEDNESDAY

print(f"任务状态: {task_status.value}")
print(f"优先级比较: {Priority.HIGH > Priority.MEDIUM}")
print(f"权限检查: {Permission.READ in permissions}")
print(f"今天是否周末: {today.is_weekend}")
print(f"明天是: {today.next_day()}")

# 遍历枚举
print("所有状态:")
for status in Status:
    print(f"  {status.name}: {status.value}")


print("\n------------命名元组------------")

from collections import namedtuple

# 定义命名元组
Point = namedtuple('Point', ['x', 'y'])
Circle = namedtuple('Circle', ['center_x', 'center_y', 'radius'], defaults=[0, 0, 1])

# 使用命名元组
p1 = Point(3, 4)
p2 = Point(x=1, y=2)

print(f"点1: {p1}")
print(f"点1的x坐标: {p1.x}")
print(f"点1的y坐标: {p1.y}")

c1 = Circle(5, 5, 3)
c2 = Circle(10, 10)  # 使用默认半径

print(f"圆1: {c1}")
print(f"圆2: {c2}")

# 命名元组是不可变的
try:
    p1.x = 10  # 会抛出异常
except AttributeError as e:
    print(f"错误: {e}")

# 可以创建新实例
p3 = p1._replace(x=10)
print(f"修改后的点: {p3}")


print("\n------------类型提示和协议------------")

from typing import Protocol, TypeVar, Generic, List, Dict

T = TypeVar('T')

class Comparable(Protocol):
    """可比较协议"""
    
    def __lt__(self, other) -> bool: ...
    def __gt__(self, other) -> bool: ...
    def __eq__(self, other) -> bool: ...

def find_max(items: List[Comparable]) -> Comparable:
    """找到最大值"""
    if not items:
        raise ValueError("列表不能为空")
    
    max_item = items[0]
    for item in items[1:]:
        if item > max_item:
            max_item = item
    return max_item

class Container(Generic[T]):
    """泛型容器类"""
    
    def __init__(self):
        self._items: List[T] = []
    
    def add(self, item: T) -> None:
        self._items.append(item)
    
    def get_items(self) -> List[T]:
        return self._items.copy()
    
    def find(self, predicate) -> List[T]:
        return [item for item in self._items if predicate(item)]

# 泛型使用示例
class Person:
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def __lt__(self, other):
        return self.age < other.age
    
    def __gt__(self, other):
        return self.age > other.age
    
    def __eq__(self, other):
        return self.age == other.age
    
    def __repr__(self):
        return f"{self.name}({self.age})"

# 协议使用
people = [Person("张三", 25), Person("李四", 30), Person("王五", 20)]
oldest = find_max(people)
print(f"最年长的人: {oldest}")

# 泛型使用
person_container = Container[Person]()
person_container.add(Person("赵六", 35))
person_container.add(Person("钱七", 28))

adults = person_container.find(lambda p: p.age >= 30)
print(f"成年人: {adults}")


print("\n------------上下文变量------------")

import contextvars

# 创建上下文变量
user_id = contextvars.ContextVar('user_id', default=None)
request_id = contextvars.ContextVar('request_id')

def process_request():
    """处理请求的函数"""
    current_user = user_id.get()
    current_request = request_id.get()
    print(f"处理请求 - 用户ID: {current_user}, 请求ID: {current_request}")

def middleware(user_id_value, request_id_value):
    """中间件：设置上下文变量"""
    # 设置上下文变量
    user_id.set(user_id_value)
    request_id.set(request_id_value)
    
    # 处理请求
    process_request()

# 模拟不同用户的请求
print("用户A的请求:")
middleware("user123", "req001")

print("用户B的请求:")
middleware("user456", "req002")

# 创建独立的上下文
ctx = contextvars.copy_context()
ctx.run(middleware, "user789", "req003")


print("\n------------数据验证------------")

class ValidationError(Exception):
    """验证错误"""
    pass

def validate_email(email: str) -> bool:
    """验证邮箱格式"""
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_age(age: int) -> bool:
    """验证年龄"""
    return 0 <= age <= 150

def validate_required_fields(data: dict, required_fields: List[str]) -> None:
    """验证必需字段"""
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValidationError(f"缺少必需字段: {missing_fields}")

def validate_user_data(data: dict) -> dict:
    """验证用户数据"""
    # 验证必需字段
    validate_required_fields(data, ['name', 'email'])
    
    # 验证邮箱
    if not validate_email(data['email']):
        raise ValidationError("邮箱格式无效")
    
    # 验证年龄（如果存在）
    if 'age' in data and not validate_age(data['age']):
        raise ValidationError("年龄必须在0-150之间")
    
    return data

# 数据验证示例
try:
    valid_data = {
        'name': '张三',
        'email': 'zhang@example.com',
        'age': 25
    }
    
    validated = validate_user_data(valid_data)
    print(f"验证通过: {validated}")
    
    # 测试无效数据
    invalid_data = {
        'name': '李四',
        'email': 'invalid-email'
    }
    validate_user_data(invalid_data)
    
except ValidationError as e:
    print(f"验证失败: {e}")