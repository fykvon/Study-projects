import unittest

from lesson_014.foreign_bowling_test import Bowling as bowling


class TestBowling(unittest.TestCase):

    def test_01(self):
        test_01 = bowling(name=None, game_result='811/X--3/XX171/43')
        self.assertEqual(test_01.run(), 127)

    def test_02(self):
        test_02 = bowling(name=None, game_result='--143/51635434184-53')
        self.assertEqual(test_02.run(), 72)

    def test_03(self):
        test_03 = bowling(name=None, game_result='XX539/XX8/X72-4')
        self.assertEqual(test_03.run(), 171)

    def test_04(self):
        test_04 = bowling(name=None, game_result='2/3/1/11--12528/--51')
        self.assertEqual(test_04.run(), 63)

    def test_05(self):
        test_05 = bowling(name=None, game_result='--6/719/X1/61-51/--')
        self.assertEqual(test_05.run(), 103)

    def test_06(self):
        test_06 = bowling(name=None, game_result='--4-8-535/1/513/4/X')
        self.assertEqual(test_06.run(), 96)

    def test_07(self):
        test_07 = bowling(name=None, game_result='3272XX5/26631/3/5/')
        self.assertEqual(test_07.run(), 126)


class TestBowling_Error(unittest.TestCase):

    def test_01(self):
        test_01 = bowling(name=None, game_result='1/6/1/--327-18812382')
        with self.assertRaises(Exception):
            test_01.run()

    def test_02(self):
        test_02 = bowling(name=None, game_result='725518X--8/--543152')
        with self.assertRaises(Exception):
            test_02.run()

    def test_03(self):
        test_03 = bowling(name=None, game_result='8/--35-47/371/518-4/')
        with self.assertRaises(Exception):
            test_03.run()

    def test_04(self):
        test_04 = bowling(name=None, game_result='42X--3/4/2-8271171/')
        with self.assertRaises(Exception):
            test_04.run()

    def test_05(self):
        test_05 = bowling(name=None, game_result='--/5X4/26X4572/2-6')
        with self.assertRaises(Exception):
            test_05.run()

    def test_06(self):
        test_06 = bowling(name=None, game_result='369/8/----4/2/2/-32/XX')
        with self.assertRaises(Exception):
            test_06.run()

    def test_07(self):
        test_07 = bowling(name=None, game_result='--9/5/--42--339//-X')
        with self.assertRaises(Exception):
            test_07.run()


if __name__ == '__main__':
    unittest.main()
