class Node:
    def __init__(self, father, state, depth):
        self.father = father
        self.state = state
        self.depth = depth

    def get_father(self):
        return self.father

    def get_state(self):
        return self.state

    def get_depth(self):
        return self.depth

    def set_depth(self, new_depth):
        self.depth = new_depth

    def get_children(self):
        children = []
        for child in self.state.get_children():
            children.append(Node(self, child, self.depth + 1))
        return children

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(self.state)
