from typing import Iterable, Sequence

class Callbacker:
    def __init__(self, callback_fn, **kargs):
        self.callback_fn = callback_fn
        self.kargs = kargs
    def __getattr__(self, s):
        return self.callback_fn(s, **self.kargs)

class Thing:
    def __init__(self, name):
        self.name = name
        self.is_a = Callbacker(self._is_a)
        self.is_not_a = Callbacker(self._is_not_a)
        self.is_the = Callbacker(lambda x_of: Callbacker(lambda s: self._is_the(x_of, s)))
        self.being_the = self.and_the = self.is_the
        self.has = self.having = lambda n: Callbacker(self._has, n=n)
        self.can = Callbacker(lambda verb: lambda method, archive=None: self._can(verb, method, archive))

    def __getattr__(self, name):
        if name.startswith("is_a_"):
            x = name[5:]
            if x in self._is_list:
                return True
            elif x in self._is_not_list:
                return False
            assert False

    def _is_a(self, s):
        setattr(self, 'is_a_'+s, True)
        return self

    def _is_not_a(self, s):
        setattr(self, 'is_a_'+s, False)
        return self

    def _is_the(self, x_of, s):
        setattr(self, x_of, s)
        return self

    def _has(self, s, n):
        if n == 1:
            t = Thing(s)
        else:
            t = ThingList(s, n)
        setattr(t, "is_"+s, True)
        setattr(self, s, t)
        return t

    def _can(self, verb, method, archive=None):
        if archive:
            setattr(self, archive, [])
            def method_wrapper(*args, **kwargs):
                out = method(self, *args, **kwargs)
                getattr(self, archive).append(out)
                return out
            setattr(self, verb, method_wrapper)
        else:
            def method_wrapper(*args, **kwargs):
                return method(self, *args, **kwargs)
        setattr(self, verb, method_wrapper)
        return self


class ThingList(Thing, Sequence):
    def __init__(self, name, n):
        super().__init__(name)
        single_name = name[:-1]
        self._list = [Thing(single_name) for i in range(n)]
        for t in self._list:
            setattr(t, "is_"+single_name, True)

    def __len__(self):
        return len(self._list)
    
    def __getitem__(self, item):
        return self._list[item]

    def each(self, fn):
        list(map(fn, self._list))
        return self