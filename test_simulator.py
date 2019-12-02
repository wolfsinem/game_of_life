from unittest import TestCase
from Simulator import *


class TestSimulator(TestCase):
    """
    Tests for ``Simulator`` implementation.
    """
    def setUp(self): #run method prior to each test
        self.sim = Simulator()
        self.world = self.sim.world()
    
    def tearDown(self): #invoke method after each test
        pass

    def test_update(self):
        """
        Tests that the update functions returns an object of World type.

        1) check for less than 2 neighbours [die]
        2) check for 2 or 3 neighbours [next generation]
        3) check for more than 3 neighbours [die] 
        4) check for dead cell with 3 neighbours alive [refactor]
        """
        self.assertIsInstance(self.sim.update(), World) #test if object is/isnt an instance of class

    def test_get_generation(self):
        """
        Tests whether get_generation returns the correct value:
            - Generation should be 0 when Simulator just created;
            - Generation should be 2 after 2 updates.
        """
        self.assertIs(self.sim.generation, self.sim.get_generation())
        self.assertEqual(self.sim.get_generation(), 0)
        self.sim.update()
        self.sim.update()
        self.assertEqual(self.sim.get_generation(), 2)

    def test_get_world(self):
        """
        Tests whether the object passed when get_world() is called is of World type, and has the required dimensions.
        When no argument passed to construction of Simulator, world is square shaped with size 20.
        """
        self.assertIs(self.sim.world, self.sim.get_world())
        self.assertEqual(self.sim.get_world().width, 20)
        self.assertEqual(self.sim.get_world().height, 20)

    def test_set_world(self):
        """
        Tests functionality of set_world function.
        """
        world = World(10)
        self.sim.set_world(world)
        self.assertIsInstance(self.sim.get_world(), World)
        self.assertIs(self.sim.get_world(), world)