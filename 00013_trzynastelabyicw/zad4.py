def insert_rek(self, val):
    def __insert_rek(cur, val):
        if cur.value == val:
            return False
        elif cur.value > val:
            if cur.children[0] is not None:
                return __insert_rek(cur.children[0], val)
            else:
                cur.children[0] = BST.Node(val)
                return True
        else:
            if cur.children[1] is not None:
                return __insert_rek(cur.children[1], val)
            else:
                cur.children[1] = BST.Node(val)
                return True

    if self.root is None:
        self.root = BST.Node(val)
        return True
    else:
        return __insert_rek(self.root, val)
