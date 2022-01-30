from xml.dom.minidom import Element


el_dict = {'name': 'Hydrogen', 'symbol': 'H', 'number': 1}

hydrogen = Element(el_dict['name'], el_dict['symbol'], el_dict['number'])

hydrogen.name

hydrogen = Element(**el_dict)
hydrogen.name

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def dump(self):
        print('name=%s, symbol=%s, number=%s' %
                (self.name, self.symbol, self.number))

hydrogen= Element(**el_dict)
hydrogen.dump()

print(hydrogen)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    def __str__(self):
        return ('name=%s, symbol=%s, number=%s' %
                (self.name, self.symbol, self.number))

hydrogen = Element(**el_dict)
print(hydrogen)

class Element:
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number
    @property
    def name(self):
        return self.__name
    @property
    def symbol(self):
        return self.__symbol
    @property
    def number(self):
        return self.__number

hydrogen = Element('Hydrogen', 'H', 1)
hydrogen.name

hydrogen.symbol

hydrogen.number


    