import solution
import constants
import copy


class PARALLEL_HILL_CLIMBER:


    def __init__(self):
        self.parents = {}
        self.nextAvailableID = 0
        for i in range(0, constants.populationSize):
            self.parents.update({i: solution.SOLUTION(self.nextAvailableID)})
            self.nextAvailableID += 1


    # Starts and waits for each simulation to wait to avoid any parallel conflicts
    def Evaluate(self, solutions):
        for i in solutions:
            solutions[i].Start_Simulation('DIRECT')

        for i in solutions:
            solutions[i].Wait_For_Simulation_To_End()


    # runs evolve_for... for every child generation
    def Evolve(self):
        self.Evaluate(self.parents)

        for currentGeneration in range(constants.numberOfGenerations):
            if currentGeneration == 0:
                self.Evolve_For_One_Generation('GUI')
            else:
                self.Evolve_For_One_Generation('DIRECT')
        self.Show_Best()


    # Calls the evolution functions for the specified child
    def Evolve_For_One_Generation(self, directOrGUI):
        self.Spawn()
        self.Mutate()
        self.Evaluate(self.children)
        self.Print()
        self.Select()


    # Randomly changes one synapse weight of the child
    def Mutate(self):
        for i in range(0, constants.populationSize):
            self.children[i].Mutate()


    # Prints out the parent and child fitness side-by-side
    def Print(self):
        print("\n")
        for i in range(0, constants.populationSize):
            print("Parent: %10f,  Child: %10f" % (self.parents[i].fitness, self.children[i].fitness))
        print("\n")


    # Creates children from the parent
    def Spawn(self):
        self.children = {}
        for i in range(0, constants.populationSize):
            self.children.update({i: copy.deepcopy(self.parents[i])})
            self.children[i].Set_ID(self.nextAvailableID)
            self.nextAvailableID += 1


    # Selects for the more successful solution: parent or child and replaces parent with the better
    def Select(self):
        for i in range(0, constants.populationSize):
            if self.parents[i].fitness > self.children[i].fitness:
                self.parents[i] = self.children[i]


    # Shows the simulation for the best found solution
    def Show_Best(self):
        lowest = 100
        index = 0
        for i in range(0, constants.populationSize):
            if self.parents[i].fitness < lowest:
                lowest = self.parents[i].fitness
                index = i
        self.parents[index].Start_Simulation('GUI')