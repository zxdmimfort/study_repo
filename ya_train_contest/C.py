class Node:
    all_nodes = {}
    def __init__(self, num: int, parent: int) -> None:
        self.all_nodes[num] = self
        self.num = num
        if parent == 0:
            self.len = 1 
        else:
            self.parent = self.all_nodes[parent]
            self.len = self.parent.len + 1
            
    
    @classmethod
    def with_max_parents(cls):
        return max(cls.all_nodes.values(), key=lambda node: node.len)


def tree_solver(n: int):
    nodes = []
    for i in range(1, n + 1):
        nodes.append(Node(i, int(input())))
        
    print(Node.with_max_parents().num)


tree_solver(int(input()))
