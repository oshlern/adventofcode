# class Setter:
#     def __init__(self, thing):
#         self.thing = thing

#     def __getattr__(self, s):
#         self.thing.set(s)
#         return self.thing
# #     metaclass, all same except .set()

# class SetNotter:
#     def __init__(self, thing):
#         self.thing = thing

#     def __getattr__(self, s):
#         self.thing.setNot(s)
#         return self.thing

# class Creator:
#     def __init__(self, thing, n):
#         self.thing = thing
#         self.n = n

#     def __getattr__(self, name):
#         if self.n == 1:
#             t = Thing(name)
#         else:
#             t = ThingList(name, n)
#         self.thing._has(t)
#         return self.thing
    
# # class Helper(type):
# # class Factory:
# #     def __init__(self):
# #         self.ctr = 0
        
# def makeClass(name, thing, callback):
# #     self.ctr += 1
# #     name = self.ctr
#     def callbacker(self, s):
#         callback(s)
#         return thing
#     c = type(name, (), {"__getattr__": callbacker})
# #         cls_instance = super().__new__(cls, name, bases, dct)

class Callbacker:
    def __init__(self, return_val, callback_fn, **kargs):
        self.return_val = return_val
        self.callback_fn = callback_fn
        self.kargs = kargs

    def __getattr__(self, s):
        self.callback_fn(s, **self.kargs)
        return self.return_val

class Thing:
    # TODO: make the magic happen
    def __init__(self, name):
        self.name = name
#         self.attributes = set()
#         self.is_a = Setter(self)
        self._is_list = set()
        self.is_a = Callbacker(self, lambda s: self._is_list.add(s))
        self._is_not_list = set()
        self.is_not_a = Callbacker(self, lambda s: self._is_not_list.add(s))
        
        
#         self._is_amakeClass("Setter", self, )
#         self.not_attributes = set()
#         self.is_not_a = SetNotter(self)
        self.has = lambda n: Callbacker(self, self._has, n=n)
    
    def __getattr__(self, name):
        if name.startswith("is_a_"):
            x = name[5:]
            if x in self._is_list:
                return True
            elif x in self._is_not_list:
                return False
            assert False
            
#     def _is_a(self, at):
#         self._is_list.add(at)
    
#     def _is_not_a(self, at):
#         self._is_not_attributes.add(at)

#     def _has(self, n):

# class ThingList(Thing):
#     def __init__(self, name, n):
#         super(ThingList, self).__init__(self, name)
#         self._list = [Thing('') for i in range(n)]

#     def __len__(self):
#         return len(self._list)
    
#     def each(self, fn):
#         map(fn, self._list)
        

        
        
    

# #     @property
# #     def is_a(self):
# #         class 
        
        
        
# #     class Subprop:
# #         def __init__(self, prop1, prop2):
# #             self.prop1 = prop1
# #             self.prop2 = prop2
# #         def sum(self):
# #             return self.prop1 + self.prop2
# # #     pass