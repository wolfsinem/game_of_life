from World import *

class Simulator:
    """
    Game of Life simulator. Handles the evolution of a Game of Life ``World``.
    Read https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life for an introduction to Conway's Game of Life.
    """

    def __init__(self, world = None, regelset="B3/S23"):
        """
        Constructor for Game of Life simulator.
        
        BX/BY B3/S23 birth bij 3 levende buren, survival bij 2 of 3 levende buren
        @param world: (optional) environment used to simulate Game of Life.
        @param survival: number of neighbours required for survival
        @param birth: number of neighbours required for birth

        @type world: int
        @type survival: list of int
        @type birth: list of int
        """
        regelset = regelset.split("/")
        self.birth = list(map(int,str(regelset[0][1])))
        self.survive = list(map(int,str(regelset[1][1:])))
        
        self.generation = 0
        if world == None:
            self.world = World(20)
        else:
            self.world = world


    def update(self) -> World:
        """
        Updates the state of the world to the next generation. Uses rules for evolution.

        :return: New state of the world.
        """
        self.generation += 1

        #TODO: Do something to evolve the generation

        return self.world

    def get_generation(self):
        """
        Returns the value of the current generation of the simulated Game of Life.

        :return: generation of simulated Game of Life.
        """
        return self.generation

    def get_world(self):
        """
        Returns the current version of the ``World``.

        :return: current state of the world.
        """
        return self.world

    def set_world(self, world: World) -> None:
        """
        Changes the current world to the given value.

        :param world: new version of the world.

        """
        self.world = world