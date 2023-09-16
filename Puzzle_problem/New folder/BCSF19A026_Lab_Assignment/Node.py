class Node:
    def __init__(self, state=None, cost=0, hr = 0, parent=None, action=None):
        self.__state= state
        self.__action = action
        self.__parent = parent
        self.__cost = cost
        self.__hr = hr
    @property
    def hr(self):
        return self.__hr
    @property
    def state(self):
        return self.__state

    @property
    def action(self):
        return self.__action

    @property
    def parent(self):
        return self.__parent

    @property
    def cost(self):
        return self.__cost
    
    @hr.setter
    def hr(self, hr):
        self.__hr=hr

    @state.setter
    def status(self, state):
        self.__state = state

    @action.setter
    def action(self, action):
        self.__action = action

    @parent.setter
    def parent(self, parent):
        self.__parent = parent

    @cost.setter
    def cost(self, cost):
        self.__cost = cost
    def __lt__(self, other):
        return self.__hr < other.__hr
