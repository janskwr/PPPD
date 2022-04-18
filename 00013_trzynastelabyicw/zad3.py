def as_list(self):
    def __as_list(node, l):
        if node is None:
            return
        __as_list(node.children[0], l)
        l.append(node.val)
        __as_list(node.children[1], l)

    res = []
    __as_list(self.root, res)
    return res
