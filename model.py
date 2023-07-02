from math import floor


class Time:
    def __init__(self, s=0, m=0, h=0):
        self.s = s%60
        self.m = (m + s//60)%60
        self.h = h + (m + s//60)//60
        self.d = self.h//24
        self.h = self.h%24

    def __str__(self) -> str:
        if self.d != 0:
            return "{}d{}h".format(int(self.d), int(self.h))
        if self.h != 0:
            return "{}h{}m".format(int(self.h), int(self.m))
        if self.m != 0:
            return "{}m{}s".format(int(self.m), int(self.s))
        return "{}s".format(int(self.s))
    
    def toInt(self):
        return self.h * 3600 + self.m * 60 + self.s


class Value:
    def __init__(self, n=0, k=0, m=0, b=0):
        self.n = n + k*1000 + m*1000000 + b*10**9

    def __str__(self) -> str:
        if self.n >= 10**9:
            return "{}b".format(round(self.n/10**9, 2))
        if self.n >= 1000000:
            return "{}m".format(round(self.n/1000000, 2))
        if self.n >= 1000:
            return "{}k".format(round(self.n/1000, 2))
        return "{}".format(round(self.n, 2))

    def toInt(self):
        return self.n


class Resources:
    def __init__(self, name, value):
        self.name = name
        self.value = value
    
    def __repr__(self) -> str:
        return "Resources({}, {})".format(self.name, self.value)
        

class Ores (Resources):
    def __init__(self, name, value):
        super().__init__(name, value)

    def __repr__(self) -> str:
        return "Ores({}, {})".format(self.name, self.value)


class Products (Resources):
    def __init__(self, name, value, ingredients: dict, time: Time):
        super().__init__(name, value)
        self.ingredients = ingredients
        self.time = time
        self.addedValue = 0
        self.gainPerHour = 0
    
    def __repr__(self) -> str:
        return "({}, {}, {}, {}, {}, {}/h)".format(self.name, self.value, self.ingredients, self.time, self.addedValue, self.gainPerHour)


class Refined (Products):
    def __init__(self, name, value, ingredients: dict, time: Time):
        super().__init__(name, value, ingredients, time)

class Component (Products):
    def __init__(self, name, value, ingredients: dict, time: Time):
        super().__init__(name, value, ingredients, time)
