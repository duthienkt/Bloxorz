from DSA import *

__PROCESSING__ = False
if __PROCESSING__:
    from PDefine import *

ID_MASK = 0b00001111
SWITCH_MASK = 0b00110000
SWITCH_HEAVY = 0b00010000
SWITCH_SOFT = 0b00100000
SWAP_SWITCH = 0b01000000
ACTIVE_BRIDGE = 0b10000000
DES = 0b00001111

VERT = 0
HORIZ_I = 1
HORIZ_J = 2


def is_switch(x):
    return (x & SWITCH_MASK) != 0


def is_normal(x):
    return (x & ID_MASK) == x and x == 1


def is_des(x):
    return x == DES


def is_emp(x):
    return x == 0


def is_bride(x):
    return (x & ID_MASK) != 0 and (x & SWITCH_MASK) == 0


def is_switch(x):
    return (x & ID_MASK) != 0 and (x & SWITCH_MASK) != 0


def is_ground(x):
    return is_normal(x) or (is_bride(x) and (x & ACTIVE_BRIDGE != 0)) or is_des(x)


class BState(AState):
    def __init__(self, par, m, n, i, j, status, arr):
        self.par = par
        if par is not None:
            self.step = par.step +1
        else:
            self.step = 0
        self.log = []
        self.A = arr[:]
        self.m = m
        self.n = n
        self.i = i
        self.j = j
        self.status = status
        for i in range(self.m):
            for j in range(self.n):
                val = self.A[self.map_ij(i, j)]
                if is_des(val):
                    self.des_i = i
                    self.des_j = j

    def clone(self):
        return BState(self, self.m, self.n, self.i, self.j, self.status, self.A)

    def is_ok(self):
        if self.i < 0 or self.i >= self.m or self.j < 0 or self.j >= self.n:
            return False
        if not is_ground(self.A[self.map_ij(self.i, self.j)]):
            return False

        if self.status == HORIZ_I:
            if self.i + 1 >= self.m:
                return False
            if not is_ground(self.A[self.map_ij(self.i + 1, self.j)]):
                return False

        if self.status == HORIZ_J:
            if self.j + 1 >= self.n:
                return False
            if not is_ground(self.A[self.map_ij(self.i, self.j + 1)]):
                return False
        return True

    def move_left(self):
        self.log.append("move_left");
        if self.status == VERT:
            self.j -= 2
            self.status = HORIZ_J
        else:
            if self.status == HORIZ_I:
                self.j -= 1
            else:
                self.j -= 1
                self.status = VERT
        return self.is_ok()

    def move_right(self):
        self.log.append("move_right")
        if self.status == VERT:
            self.j += 1
            self.status = HORIZ_J
        else:
            if self.status == HORIZ_I:
                self.j += 1
            else:
                self.j += 2
                self.status = VERT
        return self.is_ok()

    def move_up(self):
        self.log.append("move_up")
        if self.status == VERT:
            self.i -= 2
            self.status = HORIZ_I
        else:
            if self.status == HORIZ_J:
                self.i -= 1
            else:
                self.i -= 1
                self.status = VERT
        return self.is_ok()

    def move_down(self):
        self.log.append("move_down")
        if self.status == VERT:
            self.i += 1
            self.status = HORIZ_I
        else:
            if self.status == HORIZ_J:
                self.i += 1
            else:
                self.i += 2
                self.status = VERT
        return self.is_ok()

    def draw(self):
        stroke(0, 0, 0)
        pushMatrix()
        if self.is_destination():
            fill(255, 0, 255)
        else:
            fill(100, 100, 255)
        if self.status == VERT:
            x = self.i * 10 + 5
            y = 10
            z = self.j * 10 + 5
            translate(x, y, z)
            box(10, 20, 10)
        else:
            if self.status == HORIZ_I:
                x = self.i * 10 + 10
                y = 5
                z = self.j * 10 + 5
                translate(x, y, z)
                box(20, 10, 10)
            else:
                x = self.i * 10 + 5
                y = 5
                z = self.j * 10 + 10
                translate(x, y, z)
                box(10, 10, 20)
        popMatrix()
        fill(255)
        for i in range(self.m):
            for j in range(self.n):
                x = i * 10 + 5
                y = - 1
                z = j * 10 + 5
                val = self.A[self.map_ij(i, j)]
                pushMatrix()
                translate(x, y, z)
                if is_des(val):
                    fill(0, 0, 255)
                    box(10, 2, 10)
                if is_normal(val):
                    fill(200)
                    box(10, 2, 10)
                popMatrix()

        pass

    def map_ij(self, i, j):
        return self.n * i + j

    def to_int(self):
        base = 1
        res = self.j
        base += self.n
        res += base * self.i
        base *= 8
        res += (self.status + 1) * base
        for i in range(self.m * self.n):
            base *= 256
            res += base * self.A[i]
        return res

    def next_states(self, Cmp):
        res = Heap(Cmp)
        v = self.clone()
        if v.move_left():
            res.push(v)

        v = self.clone()
        if v.move_right():
            res.push(v)

        v = self.clone()
        if v.move_up():
            res.push(v)

        v = self.clone()
        if v.move_down():
            res.push(v)

        return res

    def heuristic(self):
        di = self.i - self.des_i
        dj = self.j - self.des_j
        return - di * di - dj * dj

    def is_destination(self):
        val = self.A[self.map_ij(self.i, self.j)]
        return is_des(val) and self.status == VERT

    def prev_state(self):
        pass

    def DFS(self):
        res = []
        root = BTree(100000)
        v = Searcher.DFS(self, root)
        # print(root.count)
        if v is None:
            return None
        while v is not None:
            res = [v] + res
            v = v.par
        return res

    def BFS(self):
        res = []
        root = BTree(100000)
        v = Searcher.BFS(self, root)
        # print(root.count)
        if v is None:
            return None
        while v is not None:
            res = [v] + res
            v = v.par
        return res

    def A_Star(self):
        res = []
        root = BTree(100000)
        v = Searcher.AStarSearch(self, root)
        # print(root.count)
        if v is None:
            return None
        while v is not None:
            res = [v] + res
            v = v.par
        return res
