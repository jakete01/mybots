import solution
import constants
import copy


class HILLCLIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()
        self.parent.Create_Brain()

    def Evolve(self):
        self.parent.Evaluate()
        for currentGeneration in constants.numberOfGenerations:
            self.Evolve_For_One_Generation()

    def Evolve_For_One_Generation(self):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        pass

