class Node:
    def __init__(self, father, state):
        self.father = father
        self.state = state

    def getFather(self):
        return self.father

    def getState(self):
        return self.state

    def get_children(self):
        children = []
        for child in self.state.get_children():
            children.append(Node(self, child))
        return children

    def __eq__(self, other):
        return self.state == other.state

