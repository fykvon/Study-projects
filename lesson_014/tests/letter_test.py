import unittest

from lesson_014.bowlingtest import Bowling as bowling


# TODO т.к. bowling модуль для хранения классов нашей программы, возможно, стоит подобрать другой синоним
#  к классу Bowling отличный от названия bowling, чтобы случайно не получить пересечение имён.


class TestBowling(unittest.TestCase):

    def test_01(self):
        test_01 = bowling(name=None, game_result='24X4/626/-41/618-3/')
        self.assertEqual(test_01.run(), 113)

    def test_02(self):
        test_02 = bowling(name=None, game_result='4-3/7/3/8/X711627-5')
        self.assertEqual(test_02.run(), 113)

    def test_03(self):
        test_03 = bowling(name=None, game_result='3532X332/3/62--62X')
        self.assertEqual(test_03.run(), 105)

    def test_04(self):
        test_04 = bowling(name=None, game_result='811/X--3/XX171/43')
        self.assertEqual(test_04.run(), 129)

    def test_05(self):
        test_05 = bowling(name=None, game_result='-263X815/5/27-----6')
        self.assertEqual(test_05.run(), 85)

    def test_06(self):
        test_06 = bowling(name=None, game_result='--8-X3/4/1/-12651X')
        self.assertEqual(test_06.run(), 108)

    def test_07(self):
        test_07 = bowling(name=None, game_result='3-6/5/9/5---1/--5-52')
        self.assertEqual(test_07.run(), 80)


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
