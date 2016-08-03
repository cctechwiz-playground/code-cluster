# ###################################################################
# Basic method for automating class generation

class Structure:
    _fields = []
    def __init__(self, *args):
        for name, val in zip(self._fields, args):
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']

# ###################################################################
# This new method enforces arguments and does error checking, etc.
# Learn more about Python3 Signatures adn Parameters
# can call inspect.signature(Stock) to get the signature returned
# python3 -i meta_class.py

from inspect import Parameter, Signature

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        for name in names)

class Structure:
    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    __signature__ = make_signature(['name', 'shares', 'price'])

class Point(Structure):
        __signature__ = make_signature(['x', 'y'])

class Address(Structure):
    __signature__ = make_signature(['hostname', 'port'])

# ###################################################################
# Here is another way to do this, a little better, but not much

from inspect import Parameter, Signature

def add_signature(*names):
    def decorator(cls):
        cls.__signature__ = make_signature(names)
        return cls
    return decorator

class Structure:
    __signature__ = make_signature([])
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

@add_signature('name', 'shares', 'price')
class Stock(Structure):
    pass

@add_signature('x', 'y')
class Point(Structure):
    pass

@add_signature('hostname', 'port')
class Address(Structure):
    pass

# ###################################################################
# Here is a much better way, offers the same simplicity and enforement
# Using metaprogramming =>

from inspect import Parameter, Signature

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        for name in names)

class StructMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']

class Point(Structure):
    _fields = ['x', 'y']

class Address(Structure):
    _fields = ['hostname', 'port']

# ###################################################################
# Using properties and attributes to check values
# Using descriptor (own the . operator)

from inspect import Parameter, Signature
import re

# Captures the . operator for the attribute applied to
class Descriptor:
    def __init__(self, name=None):
        self.name = name # key in the instance dictionary
    # The name has to match what is in the dictionary, issues with get???
    # def __get__(self, instance, cls):
        # instance: is the instance being manipulated
        # e.g. Stock instance
        # print("Get", self.name)
        # return instance.__dict__[self.name]
    def __set__(self, instance, value):
        print("Set", self.name, value)
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        print("Delete", self.name)
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object # expected type
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            rais TypeError("Expected %s" % self.ty)
        super().__set__(instance, value)

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str

# Mix-in class, used with multiple inheritance
class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Must be >= 0')
        super().__set__(instance, value)

# Inheritance order matters, must make sure it's an interger before > 0
# .__mro__ method resolution order => order of class application
# defines the order super() goes up the tree! <mind blown>
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

# Length checking
class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError('Too Big')
        super().__set__(instance, value)

class SizedString(String, Sized):
    pass

# Pattern matching
class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if not self.pat.match(value):
            raise ValueError('Invalid string')
        super().__set__(instance, value)

class SizedRegexString(SizedString, Regex):
    pass

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        for name in names)

class StructMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsobj = super().__new__(cls, clsname, bases, clsdict)
        sig = make_signature(clsobj._fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
    # shares = Descriptor('shares') # Redefines Stock.shares (get, set, del)
    #name = String('name')
    name = SizedRegexString('name', pat='[A-Z]+$', maxlen=8)
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

class Point(Structure):
    _fields = ['x', 'y']
    x = Integer('x')
    y = Integer('y')

class Address(Structure):
    _fields = ['hostname', 'port']


# ###################################################################
# Removing repetition from the above with MetaClasses

from inspect import Parameter, Signature
import re
from collections import OrderedDict

# Captures the . operator for the attribute applied to
class Descriptor:
    def __init__(self, name=None):
        self.name = name # key in the instance dictionary
    # The name has to match what is in the dictionary, issues with get???
    # def __get__(self, instance, cls):
        # instance: is the instance being manipulated
        # e.g. Stock instance
        # print("Get", self.name)
        # return instance.__dict__[self.name]
    def __set__(self, instance, value):
        print("Set", self.name, value)
        instance.__dict__[self.name] = value
    def __delete__(self, instance):
        print("Delete", self.name)
        del instance.__dict__[self.name]

class Typed(Descriptor):
    ty = object # expected type
    def __set__(self, instance, value):
        if not isinstance(value, self.ty):
            rais TypeError("Expected %s" % self.ty)
        super().__set__(instance, value)

class Integer(Typed):
    ty = int

class Float(Typed):
    ty = float

class String(Typed):
    ty = str

# Mix-in class, used with multiple inheritance
class Positive(Descriptor):
    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Must be >= 0')
        super().__set__(instance, value)

# Inheritance order matters, must make sure it's an interger before > 0
# .__mro__ method resolution order => order of class application
# defines the order super() goes up the tree! <mind blown>
class PositiveInteger(Integer, Positive):
    pass

class PositiveFloat(Float, Positive):
    pass

# Length checking
class Sized(Descriptor):
    def __init__(self, *args, maxlen, **kwargs):
        self.maxlen = maxlen
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if len(value) > self.maxlen:
            raise ValueError('Too Big')
        super().__set__(instance, value)

class SizedString(String, Sized):
    pass

# Pattern matching
class Regex(Descriptor):
    def __init__(self, *args, pat, **kwargs):
        self.pat = re.compile(pat)
        super().__init__(*args, **kwargs)

    def __set__(self, instance, value):
        if not self.pat.match(value):
            raise ValueError('Invalid string')
        super().__set__(instance, value)

class SizedRegexString(SizedString, Regex):
    pass

def make_signature(names):
    return Signature(
        Parameter(name, Parameter.POSITIONAL_OR_KEYWORD)
        for name in names)

class StructMeta(type):
    @classmethod
    def __prepare__(cls, name, bases): # records the order declared below
        return OrderedDict()

    def __new__(cls, clsname, bases, clsdict):
        fields = [key for key, val in clsdict.items()
                    if isinstance(val, Descriptor)]
        for name in fields:
            clsdict[name].name = name
        # must convert OrederedDict to a regular one before class creation
        clsobj = super().__new__(cls, clsname, bases, dict(clsdict))
        sig = make_signature(fields)
        setattr(clsobj, '__signature__', sig)
        return clsobj

class Structure(metaclass=StructMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound = self.__signature__.bind(*args, **kwargs)
        for name, val in bound.arguments.items():
            setattr(self, name, val)

class Stock(Structure):
    name = SizedRegexString('name', pat='[A-Z]+$', maxlen=8)
    shares = PositiveInteger('shares')
    price = PositiveFloat('price')

class Point(Structure):
    x = Integer('x')
    y = Integer('y')

class Address(Structure):
    hostname = String('hostname')
    port = PositiveInteger('port')
