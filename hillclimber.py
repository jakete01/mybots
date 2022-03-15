import solution
import constants
import copy


class HILLCLIMBER:

    def __init__(self):
        self.parent = solution.SOLUTION()
        self.parent.Create_Brain()

    def Evolve(self):
        self.parent.Evaluate('DIRECT')
        for currentGeneration in range(constants.numberOfGenerations):
            if currentGeneration == 0:
                self.Evolve_For_One_Generation('GUI')
            else:
                self.Evolve_For_One_Generation('DIRECT')
        self.Show_Best()

    def Evolve_For_One_Generation(self, mode):
        self.Spawn()
        self.Mutate()
        self.child.Evaluate(mode)
        self.Print()
        self.Select()

    def Spawn(self):
        self.child = copy.deepcopy(self.parent)

    def Mutate(self):
        self.child.Mutate()

    def Select(self):
        if self.parent.fitness > self.child.fitness:
            self.parent = self.child

    def Print(self):
        print(str(self.parent.fitness) + ' ' + str(self.child.fitness))

    def Show_Best(self):
        self.parent.Evaluate('GUI')
