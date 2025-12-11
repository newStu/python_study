# Mixin 模式
class JSONMixin:
    def to_json(self):
        import json
        return json.dumps(self.__dict__)

class XMLMixin:
    def to_xml(self):
        # XML 转换逻辑
        pass

class User(JSONMixin, XMLMixin):
    def __init__(self, name, age):
        self.name = name
        self.age = age