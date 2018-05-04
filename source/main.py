from DSA import Comparator, Heap


class IntCmp(Comparator):
    def compare(self, a, b):
        return -a + b


int_h = Heap(IntCmp())


while not int_h.emp():
    print(int_h.pop())
