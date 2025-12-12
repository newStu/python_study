print("------------观察者模式------------")

class Observable:
    """被观察者类"""
    
    def __init__(self):
        self._observers = []
    
    def add_observer(self, observer):
        """添加观察者"""
        if observer not in self._observers:
            self._observers.append(observer)
    
    def remove_observer(self, observer):
        """移除观察者"""
        if observer in self._observers:
            self._observers.remove(observer)
    
    def notify_observers(self, *args, **kwargs):
        """通知所有观察者"""
        for observer in self._observers:
            observer.update(self, *args, **kwargs)

class WeatherStation(Observable):
    """气象站（被观察者）"""
    
    def __init__(self):
        super().__init__()
        self._temperature = 0
        self._humidity = 0
    
    def set_weather(self, temperature, humidity):
        """设置天气数据"""
        self._temperature = temperature
        self._humidity = humidity
        print(f"气象站更新: 温度={temperature}°C, 湿度={humidity}%")
        self.notify_observers(temperature, humidity)
    
    @property
    def temperature(self):
        return self._temperature
    
    @property
    def humidity(self):
        return self._humidity

class Observer:
    """观察者基类"""
    
    def update(self, observable, *args, **kwargs):
        raise NotImplementedError

class PhoneDisplay(Observer):
    """手机显示（观察者）"""
    
    def update(self, weather_station, temperature, humidity):
        print(f"手机显示: {temperature}°C, {humidity}%")

class WebsiteDisplay(Observer):
    """网站显示（观察者）"""
    
    def update(self, weather_station, temperature, humidity):
        print(f"网站更新: 温度{temperature}°C, 湿度{humidity}%")

# 观察者模式测试
weather_station = WeatherStation()
phone = PhoneDisplay()
website = WebsiteDisplay()

weather_station.add_observer(phone)
weather_station.add_observer(website)

weather_station.set_weather(25, 60)
weather_station.set_weather(28, 65)


print("\n------------策略模式------------")

from abc import ABC, abstractmethod

class PaymentStrategy(ABC):
    """支付策略基类 - 抽象基类"""
    
    @abstractmethod
    def pay(self, amount: float) -> str:
        """支付方法 - 子类必须实现
        
        Args:
            amount: 支付金额
            
        Returns:
            str: 支付结果描述
        """
        pass  # pass在这里是为了满足语法要求，实际不会执行

class CreditCardPayment(PaymentStrategy):
    """信用卡支付策略"""
    
    def __init__(self, card_number: str, cvv: str) -> None:
        self.card_number = card_number
        self.cvv = cvv
    
    def pay(self, amount: float) -> str:
        return f"使用信用卡支付 ¥{amount:.2f} (卡号: {self.card_number[-4:]})"

class AlipayPayment(PaymentStrategy):
    """支付宝支付策略"""
    
    def __init__(self, account: str) -> None:
        self.account = account
    
    def pay(self, amount: float) -> str:
        return f"使用支付宝支付 ¥{amount:.2f} (账号: {self.account})"

class WechatPayment(PaymentStrategy):
    """微信支付策略"""
    
    def __init__(self, openid: str) -> None:
        self.openid = openid
    
    def pay(self, amount: float) -> str:
        return f"使用微信支付 ¥{amount:.2f} (OpenID: {self.openid[:8]}...)"

from typing import List, Tuple, Optional

class ShoppingCart:
    """购物车类"""
    
    def __init__(self) -> None:
        self.items: List[Tuple[str, float]] = []
        self.payment_strategy: Optional[PaymentStrategy] = None
    
    def add_item(self, item: str, price: float) -> None:
        """添加商品"""
        self.items.append((item, price))
    
    def set_payment_strategy(self, strategy: PaymentStrategy) -> None:
        """设置支付策略"""
        self.payment_strategy = strategy
    
    def checkout(self) -> str:
        """结账
        
        Raises:
            ValueError: 当未设置支付策略时
            
        Returns:
            str: 支付结果
        """
        if not self.payment_strategy:
            raise ValueError("请设置支付策略")
        
        total = sum(price for _, price in self.items)
        print(f"商品清单:")
        for item, price in self.items:
            print(f"  {item}: ¥{price:.2f}")
        print(f"总计: ¥{total:.2f}")
        
        return self.payment_strategy.pay(total)

# 策略模式测试
cart = ShoppingCart()
cart.add_item("手机", 2999)
cart.add_item("耳机", 299)

# 使用不同支付策略
cart.set_payment_strategy(CreditCardPayment("1234567890123456", "123"))
print(cart.checkout())

cart.set_payment_strategy(AlipayPayment("user@example.com"))
print(cart.checkout())


print("\n------------装饰器模式------------")

class Component:
    """组件基类"""
    
    def operation(self):
        raise NotImplementedError

class ConcreteComponent(Component):
    """具体组件"""
    
    def operation(self):
        return "具体组件操作"

class Decorator(Component):
    """装饰器基类"""
    
    def __init__(self, component):
        self._component = component
    
    def operation(self):
        return self._component.operation()

class ConcreteDecoratorA(Decorator):
    """具体装饰器A"""
    
    def operation(self):
        result = self._component.operation()
        return f"装饰器A({result})"

class ConcreteDecoratorB(Decorator):
    """具体装饰器B"""
    
    def operation(self):
        result = self._component.operation()
        return f"装饰器B({result})"

class LoggingDecorator(Decorator):
    """日志装饰器"""
    
    def operation(self):
        print("日志: 开始执行操作")
        result = self._component.operation()
        print(f"日志: 操作完成 - {result}")
        return result

# 装饰器模式测试
component = ConcreteComponent()
print(f"原始操作: {component.operation()}")

decorated_a = ConcreteDecoratorA(component)
print(f"装饰A后: {decorated_a.operation()}")

decorated_b = ConcreteDecoratorB(decorated_a)
print(f"再装饰B后: {decorated_b.operation()}")

logged = LoggingDecorator(decorated_b)
print(f"添加日志后: {logged.operation()}")


print("\n------------工厂模式------------")

class Animal:
    """动物基类"""
    
    def speak(self):
        raise NotImplementedError

class Dog(Animal):
    def speak(self):
        return "汪汪!"

class Cat(Animal):
    def speak(self):
        return "喵喵~"

class Duck(Animal):
    def speak(self):
        return "嘎嘎!"

class AnimalFactory:
    """动物工厂"""
    
    _animals = {
        'dog': Dog,
        'cat': Cat,
        'duck': Duck
    }
    
    @classmethod
    def create_animal(cls, animal_type):
        """创建动物实例"""
        animal_class = cls._animals.get(animal_type.lower())
        if not animal_class:
            raise ValueError(f"未知的动物类型: {animal_type}")
        return animal_class()
    
    @classmethod
    def register_animal(cls, animal_type, animal_class):
        """注册新的动物类型"""
        cls._animals[animal_type.lower()] = animal_class
    
    @classmethod
    def get_available_types(cls):
        """获取可用的动物类型"""
        return list(cls._animals.keys())

# 工厂模式测试
print(f"可用动物类型: {AnimalFactory.get_available_types()}")

dog = AnimalFactory.create_animal('dog')
cat = AnimalFactory.create_animal('cat')
duck = AnimalFactory.create_animal('duck')

print(f"狗叫: {dog.speak()}")
print(f"猫叫: {cat.speak()}")
print(f"鸭子叫: {duck.speak()}")

# 动态注册新的动物类型
class Cow(Animal):
    def speak(self):
        return "哞哞!"

AnimalFactory.register_animal('cow', Cow)

cow = AnimalFactory.create_animal('cow')
print(f"牛叫: {cow.speak()}")
print(f"更新后的动物类型: {AnimalFactory.get_available_types()}")


print("\n------------迭代器模式------------")

class NumberIterator:
    """数字迭代器"""
    
    def __init__(self, start, end, step=1):
        self.current = start
        self.end = end
        self.step = step
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        
        value = self.current
        self.current += self.step
        return value

class Container:
    """容器类"""
    
    def __init__(self, data):
        self.data = data
    
    def __iter__(self):
        """返回迭代器"""
        return NumberIterator(0, len(self.data))
    
    def __getitem__(self, index):
        """支持索引访问"""
        return self.data[index]
    
    def __len__(self):
        """支持len()函数"""
        return len(self.data)

# 迭代器模式测试
container = Container([10, 20, 30, 40, 50])

print("使用for循环:")
for index in container:
    print(f"  索引 {index}: {container[index]}")

print("直接使用迭代器:")
iterator = iter(container)
while True:
    try:
        index = next(iterator)
        print(f"  索引 {index}: {container[index]}")
    except StopIteration:
        break

print(f"容器长度: {len(container)}")