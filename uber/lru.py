import numpy as np
import time
import matplotlib.pyplot as plt
# Cache, discards least recently accessed items
# O(1) read


# read a_1, a_2, a_1, ...

# | a_1 | a_2 | |

# |


class LinkedList:
    def __init__(self, val, ref):
        self.val = val
        self.ref = ref

    def display(self):
        out = "LL"
        head = self
        while head != None:
            out += "->" + str(head.val)
            head = head.ref
        print(out)
    # val, ref


cache = None

class LRUCache:
    def __init__(self, max_size):
        self.max_size = max_size
        self.ll = None
        self.size = 0

    def get(self, addr):
        last = None
        head = self.ll

        while head != None:
            if head.val[0] == addr:
                # Pop it out to the front (already at the front if last is None)
                if last != None:
                    last.ref = head.ref
                    head.ref = self.ll
                    self.ll = head
                return head.val[1]
            head = head.ref

    def put(self, addr, val):
        v = self.get(addr)
        if not v:
            if self.size >= self.max_size:
                self._remove_last()
            else:
                self.size += 1
            self.ll = LinkedList((addr, val), self.ll)

    def _remove_last(self):
        head = self.ll
        last = None
        if head is None:
            return
        while head.ref is not None:
            last = head
            head = head.ref
        if last:
            last.ref = None
        del head

    def display(self):
        if self.ll:
            self.ll.display()


class DoubleLinkedList:
    def __init__(self, val, prev, ref):
        self.val = val
        self.prev = prev
        self.ref = ref

    def display(self):
        out = "LL"
        head = self
        while head != None:
            out += "->" + str(head.val)
            head = head.ref
        print(out)



class LRUCacheFast:
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = None
        self.tail = None
        self.hashmap = dict()
        self.size = 0

    def get(self, addr):
        node = self.hashmap.get(addr)
        if node is None:
            return None
        if node.prev is None:
            return node.val

        node.prev.ref = node.ref
        if node.ref is None:
            self.tail = node.prev
        else:
            node.ref.prev = node.prev
        node.prev = None
        node.ref = self.head
        self.head = node
        return node.val


    def put(self, addr, val):
        if not self.get(addr):
            if self.size >= self.max_size:
                self._remove_last()
            self._add_first(addr, val)

    def _add_first(self, addr, val):
        new_node = DoubleLinkedList(val, None, self.head)
        if self.head:
            self.head.prev = new_node
        self.head = new_node
        self.hashmap[addr] = new_node
        self.size += 1

    def _remove_last(self):
        if not self.tail:
            return
        if not self.tail.prev:
            old_tail = self.tail
            self.tail = None
            self.head = None
            del old_tail
            return
        old_tail = self.tail
        self.tail.prev.ref = None
        # del old_tail
        self.tail = self.tail.prev
        self.size -= 1

    def display(self):
        if self.head:
            self.head.display()

class LRUCacheElegant:
    def __init__(self, max_size):
        self.max_size = max_size
        self.head = DoubleLinkedList(None, None, None)
        self.tail = DoubleLinkedList(None, self.head, None)
        self.head.ref = self.tail
        self.hashmap = dict()
        self.size = 0

    def get(self, addr):
        node = self.hashmap.get(addr)
        if node is None:
            return None
        self._move_to_head(node)
        return node.val[1]

    def put(self, addr, val):
        if not self.get(addr):
            if self.size >= self.max_size:
                self._remove_last()
            self._add_first(addr, val)

    def _move_to_head(self, node):
        node.prev.ref = node.ref
        node.ref.prev = node.prev

        self.head.ref.prev = node
        node.ref = self.head.ref
        node.prev = self.head
        self.head.ref = node

    def _add_first(self, addr, val):
        new_node = DoubleLinkedList((addr, val), self.head, self.head.ref)
        self.head.ref.prev = new_node
        self.head.ref = new_node
        self.hashmap[addr] = new_node
        self.size += 1

    def _remove_last(self):
        if self.tail.prev == self.head:
            return
        stale_node = self.tail.prev
        stale_node.prev.ref = self.tail
        self.tail.prev = stale_node.prev
        del self.hashmap[stale_node.val[0]]
        del stale_node
        self.size -= 1

    def display(self):
        print("  size ", self.size, self.max_size)
        self.head.display()

c = LRUCacheElegant(2)
c.display()
c.put(1,1)
c.display()
c.put(2,2)
print("get 1", c.get(1))
c.display()

c.put(3,3)
c.display()
print("get 2", c.get(2))
c.display()
c.put(4,4)
c.display()
print("get 1", c.get(1))
c.display()
print("get 3", c.get(3))
c.display()
print("get 4", c.get(4))



# def test():
put_means, put_stds = [], []
get_means, get_stds = [], []
SIZES = [2, 10, 100, 1_000, 10_000, 100_000]#, 1_000_000, 10_000_000]
for SIZE in SIZES:
    # for N in [10**i for i in range(2, 6)]:
    N = 1_000_000
    M = 100_000
    # vals = [(i, str(i)) for i in range(M)]
    # vals = np.random.zipf(2, size=N) # Distribution: p ~ 1/x
    vals = np.random.randint(0,1000, size=N) # Distribution: p ~ 1/x

    c = LRUCache(SIZE)
    # c = LRUCacheElegant(SIZE)

    put_times = []
    get_times = []
    for val in vals:
        if np.random.random() < 0.3:
            s = time.time()
            c.put(val, val)
            e = time.time()
            put_times.append(e-s)
        else:
            s = time.time()
            c.get(val)
            e = time.time()
            get_times.append(e-s)

    # put_times = np.log10(put_times)
    # get_times = np.log10(get_times)
    # put_times = np.log10(put_times)
    # get_times = np.log10(get_times)


    put_mean = np.mean(put_times)
    put_std = np.std(put_times)
    get_mean = np.mean(get_times)
    get_std = np.std(get_times)
    print("SIZE", SIZE)
    print(put_mean*1_000_000_000, put_std*1_000_000_000)
    print(get_mean*1_000_000_000, get_std*1_000_000_000)

    put_means.append(put_mean)
    put_stds.append(put_std)
    get_means.append(get_mean)
    get_stds.append(get_std)



    # put_means.append()
    # put_stds.append(np.std(put_times))
    # get_means.append(np.mean(get_times))
    # get_stds.append(np.std(get_times))
plt.errorbar(np.log10(SIZES), put_means, yerr=put_stds)
plt.errorbar(np.log10(SIZES), get_means, yerr=get_stds)

    # matplotlib.pyplot.errorbar(SIZES, put_means, yerr=put_stds)

plt.show()
# test()
