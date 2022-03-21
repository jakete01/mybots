import solution
import constants
import copy


class PARALLEL_HILL_CLIMBER:

    def __init__(self):
        self.parents = {}
        for i in range(0, constants.populationSize):
            self.parents.update({i: solution.SOLUTION()})

        # self.parent = solution.SOLUTION()
        # self.parent.Create_Brain()

    def Evolve(self):
        for i in self.parents:
            print('parent ' + str(i))
            self.parents[i].Evaluate('GUI')

        # self.parent.Evaluate('DIRECT')
        # for currentGeneration in range(constants.numberOfGenerations):
        #     if currentGeneration == 0:
        #         self.Evolve_For_One_Generation('GUI')
        #     else:
        #         self.Evolve_For_One_Generation('DIRECT')
        # self.Show_Best()

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
