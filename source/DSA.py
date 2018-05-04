from abc import abstractmethod


class Comparator:
    @abstractmethod
    def compare(self, a, b):
        return 0


class AstarCmp(Comparator):
    def compare(self, a, b):
        return b.step + b.heuristic() - a.heuristic() - a.step


class HeuristicCmp(Comparator):
    def compare(self, a, b):
        return b.heuristic() - a.heuristic()


class Heap:
    data = []
    n = 0
    comparator = Comparator

    def __init__(self, comp):
        self.data = []
        self.comparator = comp
        self.n = 0

    def emp(self):
        return self.n == 0

    def __upHeap__(self, i):
        if i == 0:
            return self
        pr = (i - 1) >> 1
        if self.comparator.compare(self.data[pr], self.data[i]) >= 0:
            return self
        t = self.data[i]
        self.data[i] = self.data[pr]
        self.data[pr] = t
        return self.__upHeap__(pr)

    def __downHeap__(self, i):
        if i * 2 + 1 >= self.n:
            return self
        child = i * 2 + 1
        if i * 2 + 2 < self.n:
            if self.comparator.compare(self.data[child], self.data[child + 1]) < 0:
                child += 1
        if self.comparator.compare(self.data[child], self.data[i]) <= 0:
            return self
        t = self.data[i]
        self.data[i] = self.data[child]
        self.data[child] = t
        return self.__downHeap__(child)

    def push(self, x):
        self.n += 1
        if self.n > len(self.data):
            self.data.append(x)
        else:
            self.data[self.n - 1] = x
        self.__upHeap__(self.n - 1)
        return self

    def pop(self):
        self.n -= 1
        t = self.data[0]
        self.data[0] = self.data[self.n]
        self.__downHeap__(0)
        return t


class BTree:
    count = 0
    left = None
    right = None
    val = 0

    def __init__(self, _val):
        """
        :param _val: int
        """
        self.left = None
        self.right = None
        self.val = _val

    def find(self, _val):
        """
        :param _val: int
        :return: BTree
        """
        if self.val == _val:
            return self
        res = None
        if _val < self.val:
            if self.left is not None:
                res = self.left.find(_val)
        if _val > self.val:
            if self.right is not None:
                res = self.right.find(_val)
        return res

    def add(self, _tree):
        """
        :param _tree: BTree
        :return: self
        """
        if _tree.val < self.val:
            if self.left is None:
                self.left = _tree
                self.count += 1
            else:
                self.left.add(_tree)
        else:
            if _tree.val > self.val:
                if self.right is None:
                    self.right = _tree
                    self.count += 1
                else:
                    self.right.add(_tree)
        return self

    def __str__(self):
        return super().__str__()


class AState:

    @abstractmethod
    def to_int(self):
        return 0

    @abstractmethod
    def next_states(self):
        return Heap(Comparator)

    @abstractmethod
    def heuristic(self):
        return 0

    @abstractmethod
    def is_destination(self):
        return False

    @abstractmethod
    def prev_state(self):
        return None



class Searcher:

    @staticmethod
    def DFS(state, map_tree):
        """
        :param state: AState => the state of game
        :param map_tree: BTree => List of visited state
        :return: AState => destination
        """
        if map_tree.find(state.to_int()) is not None:
            return None
        if state.is_destination():
            return state
        map_tree.add(BTree(state.to_int()))
        e = state.next_states()
        while not e.emp():
            choice = e.pop()
            res = Searcher.DFS(choice, map_tree)
            if res is not None:
                return res
        return None

    @staticmethod
    def BFS(state, map_tree):
        queue = [state]
        left = 0
        map_tree.add(BTree(state.to_int()))
        while left < len(queue):
            p = queue[left]
            left += 1
            if p.is_destination():
                return p
            t = p.next_state(HeuristicCmp())
            while not t.emp():
                e = t.pop()
                if map_tree.find(e.to_int()) is None:
                    map_tree.add(BTree(e.to_int()))
                    queue.append(e)
        return None

    @staticmethod
    def AStarSearch(state, map_tree):
        priority_queue = Heap(AstarCmp())
        priority_queue.push(state)
        map_tree.add(BTree(state.to_int()))
        while not priority_queue.emp():
            p = priority_queue.pop()
            if p.is_destination():
                return p
            t = p.next_state(HeuristicCmp())
            while not t.emp():
                e = t.pop()
                if map_tree.find(e.to_int()) is None:
                    priority_queue.push(e)
                    map_tree.add(BTree(e.to_int()))
        return None
