class BinarySearchTree:
    __slots__ = ["root"]

    class Node:
        __slots__ = ["val", "children"]

        def __init__(self, v):
            self.val = v
            self.children = [None, None]

    def __init__(self):
        self.root = None

    def insert(self, v):
        tmp = self.root
        p = None
        c = 0
        while tmp is not None:
            if v < tmp.val:
                p = tmp
                c = 0
                tmp = tmp.children[0]
            elif v > tmp.val:
                p = tmp
                c = 1
                tmp = tmp.children[1]
            else:
                return False
        if p is None:
            self.root = BinarySearchTree.Node(v)
            return True
        p.children[c] = BinarySearchTree.Node(v)
        return True


t = BinarySearchTree()
t.insert(4)
t.insert(3)
t.insert(5)
