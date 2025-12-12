# 一等公民

"函数是一等公民"（First-class citizen）是编程语言中的一个重要概念，理解这个概念对掌握 Python 的高级特性很有帮助。

在编程语言中，如果某个实体（如函数）具备以下特性，就称为"一等公民"：：
✅ 可以赋值给变量
✅ 可以作为参数传递
✅ 可以作为返回值
✅ 可以存储在数据结构中

# 作用域

作用域是程序中变量和函数的可访问范围。在 Python 中，作用域分为全局作用域和局部作用域。

| 关键字   | 作用域范围 |
| -------- | ---------- |
| global   | 全局作用域 |
| nonlocal | 局部作用域 |
| 无声明   | 当前作用域 |

# 鸭子类型

鸭子类型（Duck typing）是一种面向对象编程范式，它是一种动态类型检查的风格。

> 如果它走起来像鸭子，叫起来像鸭子，那么它就是鸭子

# 类控制符

```python
class Teacher:
    def __init__(self, name, age, password):
        self.name = name # 公有属性
        self._age = age # 受保护属性
        self.__password = password # 私有属性

t = Teacher("Tom", 25, "123456")
```

- **没有下划线前缀**
  > 可以在类内外自由访问
- **单下划线前缀**
  > **约定**：表示不应该直接访问，但技术上可以访问
  > 用于告诉其他开发者："这是内部使用的方法/属性"
- **双下划线前缀**
  > **真正的私有**：Python 会进行名称改写 (name mangling)
  > 外部无法直接访问，会变为 `_ClassName__attribute`

## 名称改写示例

```python
t = Teacher("Tom", 25, "123456")

# ✓ 可以访问
print(t.name)           # "Tom"

# ⚠️ 约定上不应该访问，但技术上可以
print(t._age)           # 25

# ✗ 无法直接访问，会报错
print(t.__password)     # AttributeError

# ✓ 通过改写后的名称可以访问
print(t._Teacher__password)  # "123456"
```

## 设计理念

Python 的访问控制更多是 **约定而非强制**：

- 单下划线：请求遵守约定
- 双下划线：强制性的私有保护

这种设计体现了 Python 的哲学："我们都是负责任的成年人"。

# 抽象类

**特性**

- 不能直接实例化
- 必须由子类继承并实现特定方法
- 可以定义抽象方法和属性，子类可以选择实现

**使用场景**

- **模板方法模式**：定义算法骨架，子类实现具体步骤
- **插件架构**：定义插件接口，不同插件实现具体功能
- **API 设计**：定义统一接口规范
- **多态实现**：确保所有子类都有相同的接口

**总结**：抽象类强制子类实现特定方法，确保接口一致性，是面向对象设计的重要工具。

# 类静态方法和类方法

| 特性             | `@staticmethod`                         | `@classmethod`                          |
| ---------------- | --------------------------------------- | --------------------------------------- |
| **第一个参数**   | 无特殊参数                              | `cls`（类），可以通过`cls`创建实例      |
| **访问类属性**   | 通过类名访问                            | 通过 `cls` 访问                         |
| **访问实例属性** | 不能访问                                | 不能访问                                |
| **继承行为**     | 绑定到定义类                            | 绑定到调用类                            |
| **用途**         | 纯函数，工具方法                        | 类工厂，配置管理                        |
| **调用方式**     | `Class.method()` 或 `instance.method()` | `Class.method()` 或 `instance.method()` |

**什么时候使用静态方法？**

- 纯函数逻辑，不需要访问类或实例
- 工具函数，与类相关但独立
- 数学计算、格式化等

**什么时候使用类方法？**

- 工厂方法，创建类的不同实例
- 操作类级别的状态
- 需要在继承中灵活调用的方法

记住：**静态方法是放在类中的普通函数，类方法是操作类本身的方法！**

## 最佳实践

```python
class BestPracticeExample:
    """最佳实践示例"""

    # ✅ 静态方法：纯函数，逻辑独立
    @staticmethod
    def validate_email(email):
        import re
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        return re.match(pattern, email) is not None

    # ✅ 类方法：工厂方法，操作类状态
    @classmethod
    def from_dict(cls, data):
        """从字典创建实例"""
        if not cls.validate_email(data.get('email', '')):
            raise ValueError("无效邮箱")
        return cls(data['name'], data['email'])

    # ✅ 类方法：修改类状态
    @classmethod
    def set_default_domain(cls, domain):
        """设置默认域名"""
        cls.default_domain = domain

    def __init__(self, name, email):
        self.name = name
        self.email = email

# 设置类级别配置
BestPracticeExample.set_default_domain("example.com")

# 创建实例
user = BestPracticeExample.from_dict({
    'name': '张三',
    'email': 'zhang@example.com'
})

# 验证邮箱
is_valid = BestPracticeExample.validate_email('test@example.com')

```

## 静态方法不能替换类方法案例

虽然 python 中`静态方法`可以直接用`类名`代替`类方法`的第一个参数`cls`, 也能通过`类名`调用类属性和其他方法，但这依然无法替代`类方法`。

**多态性缺失（最重要！）**

```python
class BaseSerializer:
    def __init__(self, data):
        self.data = data

    @staticmethod
    def static_serialize(data):
        # ❌ 问题：硬编码了 BaseSerializer
        return BaseSerializer(data)

    @classmethod
    def class_serialize(cls, data):
        # ✅ 正确：使用 cls 参数
        return cls(data)

    def display(self):
        return f"BaseSerializer: {self.data}"

class JSONSerializer(BaseSerializer):
    def display(self):
        return f"JSONSerializer: {self.data}"

    def to_json(self):
        import json
        return json.dumps({"data": self.data})

# 测试
data = {"name": "Alice"}

# 使用静态方法
result1 = JSONSerializer.static_serialize(data)
print(f"静态方法结果类型: {type(result1)}")  # <class '__main__.BaseSerializer'>
print(f"静态方法: {result1.display()}")      # BaseSerializer: {'name': 'Alice'}
# ❌ 问题：无法调用 to_json()，因为返回的是 BaseSerializer
# result1.to_json()  # AttributeError!

# 使用类方法
result2 = JSONSerializer.class_serialize(data)
print(f"\n类方法结果类型: {type(result2)}")   # <class '__main__.JSONSerializer'> ✅
print(f"类方法: {result2.display()}")         # JSONSerializer: {'name': 'Alice'} ✅
print(f"可以调用子类方法: {result2.to_json()}")  # ✅ 正常工作
```

**配置继承问题**

```python
class Config:
    default_value = "parent"

    @staticmethod
    def static_get_default():
        return Config.default_value  # 硬编码父类

    @classmethod
    def class_get_default(cls):
        return cls.default_value  # 动态查找

class ChildConfig(Config):
    default_value = "child"  # 重写类属性

# 测试
print("父类静态方法:", Config.static_get_default())  # parent
print("父类类方法:", Config.class_get_default())     # parent
print("子类静态方法:", ChildConfig.static_get_default())  # parent ❌ 错误！
print("子类类方法:", ChildConfig.class_get_default())     # child ✅ 正确！
```

## 选择指南

1. 使用类方法（`@classmethod`）当：
   - 需要支持继承和多态
   - 实现工厂方法
   - 操作类属性且可能被子类重写
   - 需要返回当前类或其子类的实例
2. 使用静态方法（`@staticmethod`）当：
   - 方法是纯函数，不依赖类或实例状态
   - 确定类不会被继承，或继承时不需要多态
   - 只是将相关函数组织在一起
   - 性能要求极高，需要避免 cls 参数开销（极少数情况）
3. 简单规则：
   - 如果方法中硬编码了类名，考虑是否应该用 `@classmethod`
   - 如果子类调用方法时应该返回子类实例，必须用 `@classmethod`
   - 如果方法只是工具函数，与类关系不大，用 `@staticmethod`
