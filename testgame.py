import unittest
import game

class TestTreasureHunt(unittest.TestCase):

    def test_create_map(self):
        """Test if the game map is created with the correct size."""
        size = 5
        expected_map = [['.' for _ in range(size)] for _ in range(size)]
        result_map = game.create_map(size)
        self.assertEqual(result_map, expected_map)

    def test_place_treasure(self):
        """Test if the treasure is placed on the map."""
        game_map = [['.' for _ in range(5)] for _ in range(5)]
        game.place_treasure(game_map)
        treasure_count = sum(row.count('T') for row in game_map)
        self.assertEqual(treasure_count, 1)

    def test_check_treasure(self):
        """Test the check_treasure function for a known treasure location."""
        game_map = [['.' for _ in range(5)] for _ in range(5)]
        # Place treasure at a known location
        treasure_x, treasure_y = 2, 3
        game_map[treasure_x][treasure_y] = 'T'
        self.assertTrue(game.check_treasure(game_map, treasure_x, treasure_y))
        self.assertFalse(game.check_treasure(game_map, 0, 0))

    # Additional tests can be written for other functions like update_map, get_player_move, etc.

if __name__ == '__main__':
    unittest.main()
