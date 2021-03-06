import unittest
import numpy

from day20 import tile
from day20.tile import Tile


class MyTestCase(unittest.TestCase):
    def test_rotate(self):
        original = [['.', '#'],
                    ['#', '.']]

        expected = [['#', '.'],
                    ['.', '#']]
        rotated = tile.rotate(original)
        self.assertEqual(expected, rotated)

    def test_top_match(self):
        tile1 = [['.', '#'],
                 ['#', '.']]

        tile2 = [['#', '#'],
                 ['.', '#']]

        self.assertTrue(tile.is_top_match(tile1, tile2))

    def test_not_top_match(self):
        tile1 = [['.', '.'],
                 ['#', '.']]

        tile2 = [['.', '#'],
                 ['#', '#']]

        self.assertFalse(tile.is_top_match(tile1, tile2))

    def test_bottom_match(self):
        tile1 = [['.', '#'],
                 ['#', '.']]

        tile2 = [['#', '.'],
                 ['#', '#']]

        self.assertTrue(tile.is_bottom_match(tile1, tile2))

    def test_not_bottom_match(self):
        tile1 = [['.', '#'],
                 ['#', '#']]

        tile2 = [['#', '.'],
                 ['#', '.']]

        self.assertFalse(tile.is_bottom_match(tile1, tile2))

    def test_left_match(self):
        tile1 = [['#', '#'],
                 ['#', '.']]

        tile2 = [['#', '#'],
                 ['.', '#']]

        self.assertTrue(tile.is_left_match(tile1, tile2))

    def test_not_left_match(self):
        tile1 = [['#', '#'],
                 ['.', '.']]

        tile2 = [['#', '#'],
                 ['#', '#']]

        self.assertFalse(tile.is_left_match(tile1, tile2))

    def test_right_match(self):
        tile1 = [['#', '#'],
                 ['.', '.']]

        tile2 = [['#', '#'],
                 ['.', '#']]

        self.assertTrue(tile.is_right_match(tile1, tile2))

    def test_not_right_match(self):
        tile1 = [['#', '#'],
                 ['.', '.']]

        tile2 = [['#', '#'],
                 ['#', '#']]

        self.assertFalse(tile.is_right_match(tile1, tile2))

    def test_remove_border(self):
        tile_with_border = [
            ['.', '#', '.', '.'],
            ['#', '.', '#', '.'],
            ['#', '#', '#', '#'],
            ['.', '.', '.', '.']
        ]
        expected = [
            ['.', '#'],
            ['#', '#']
        ]

        border_removed_tile = tile.remove_border(tile_with_border)
        self.assertEqual(expected, border_removed_tile)







    def test_parse(self):
        input = """Tile 1319:
#.
##

Tile 3547:
##
.."""
        tile1 = Tile()
        tile1.id = 1319
        tile1.content = [['#', '.'], ['#', '#']]

        tile2 = Tile()
        tile2.id = 3547
        tile2.content = [['#', '#'], ['.', '.']]
        expected = [tile1, tile2]
        parsed = tile.parse(input)

        self.assertEqual(expected, parsed)


    def test_reconstruct(self):
        input = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

        expected = [['.','#','.','#','.','.','#','.','#','#','.','.','.','#','.','#','#','.','.','#','#','#','#','#',],
['#','#','#','.','.','.','.','#','.','#','.','.','.','.','#','.','.','#','.','.','.','.','.','.',],
['#','#','.','#','#','.','#','#','#','.','#','.','#','.','.','#','#','#','#','#','#','.','.','.',],
['#','#','#','.','#','#','#','#','#','.','.','.','#','.','#','#','#','#','#','.','#','.','.','#',],
['#','#','.','#','.','.','.','.','#','.','#','#','.','#','#','#','#','.','.','.','#','.','#','#',],
['.','.','.','#','#','#','#','#','#','#','#','.','#','.','.','.','.','#','#','#','#','#','.','#',],
['.','.','.','.','#','.','.','#','.','.','.','#','#','.','.','#','.','#','.','#','#','#','.','.',],
['.','#','#','#','#','.','.','.','#','.','.','#','.','.','.','.','.','#','.','.','.','.','.','.',],
['#','.','.','#','.','#','#','.','.','#','.','.','#','#','#','.','#','.','#','#','.','.','.','.',],
['#','.','#','#','#','#','.','.','#','.','#','#','#','#','.','#','.','#','.','#','#','#','.','.',],
['#','#','#','.','#','.','#','.','.','.','#','.','#','#','#','#','#','#','.','#','.','.','#','#',],
['#','.','#','#','#','#','.','.','.','.','#','#','.','.','#','#','#','#','#','#','#','#','.','#',],
['#','#','.','.','#','#','.','#','.','.','.','#','.','.','.','#','.','#','.','#','.','#','.','.',],
['.','.','.','#','.','.','#','.','.','#','.','#','.','#','#','.','.','#','#','#','.','#','#','#',],
['.','#','.','#','.','.','.','.','#','.','#','#','.','#','.','.','.','#','#','#','.','#','#','.',],
['#','#','#','.','#','.','.','.','#','.','.','#','.','#','#','.','#','#','#','#','#','#','.','.',],
['.','#','.','#','.','#','#','#','.','#','#','.','#','#','.','#','.','.','#','.','#','#','.','.',],
['.','#','#','#','#','.','#','#','#','.','#','.','.','.','#','#','#','.','#','.','.','#','.','#',],
['.','.','#','.','#','.','.','#','.','.','#','.','#','.','#','.','#','#','#','#','.','#','#','#',],
['#','.','.','#','#','#','#','.','.','.','#','.','#','.','#','.','#','#','#','.','#','#','#','.',],
['#','#','#','#','#','.','.','#','#','#','#','#','.','.','.','#','#','#','.','.','.','.','#','#',],
['#','.','#','#','.','.','#','.','.','#','.','.','.','#','.','.','#','#','#','#','.','.','.','#',],
['.','#','.','#','#','#','.','.','#','#','.','.','#','#','.','.','#','#','#','#','.','#','#','.',],
['.','.','.','#','#','#','.','.','.','#','#','.','.','.','#','.','.','.','#','.','.','#','#','#',]]
        tiles = tile.recontruct(input)
        expected = tile.rotate(expected)
        expected = numpy.fliplr(expected).tolist()
        self.assertEqual(expected, tiles)

    def test_count_sea_monsters(self):
        input = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

        expected = 2
        sea_monster_count = tile.count_sea_monsters(input)
        self.assertEqual(expected, sea_monster_count)

    def test_calc_roughness(self):
        input = """Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###..."""

        expected_roughness = 273
        roughness = tile.calc_roughness(input)
        self.assertEqual(expected_roughness, roughness)



if __name__ == '__main__':
    unittest.main()
