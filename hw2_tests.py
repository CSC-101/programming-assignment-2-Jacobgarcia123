import data
import hw2
import unittest


# Write your test cases for each part below.

class TestCases(unittest.TestCase):
    # Part 1
    def test_create_rectangle_1(self):
        input1 = data.Point(2,2)
        input2 = data.Point(10,10)
        result = hw2.create_rectangle(input1,input2)
        expected = data.Rectangle(data.Point(2,10),data.Point(10,2))
        self.assertEqual(expected,result)
    def test_create_rectangle_2(self):
        input1 = data.Point(8,2)
        input2 = data.Point(9,0)
        result = hw2.create_rectangle(input1,input2)
        expected = data.Rectangle(data.Point(8,2),data.Point(9,0))
        self.assertEqual(expected,result)



    # Part 2
    def test_shorter_duration_than_1(self):
        input1 = data.Duration(6,7)
        input2 = data.Duration(9,23)
        result = hw2.shorter_duration_than(input1,input2)
        expected = True
        self.assertEqual(expected,result)

    def test_shorter_duration_than_2(self):
        input1 = data.Duration(3,13)
        input2 = data.Duration(2,23)
        result = hw2.shorter_duration_than(input1,input2)
        expected = False
        self.assertEqual(expected,result)



    # Part 3
    def test_songs_shorter_than_1(self):
        input1 = data.Song('Artist1', 'Title1', data.Duration(3, 58))
        input2 = data.Song('Artist2', 'Title2', data.Duration(3, 18))
        input3 = data.Song('Artist3', 'Title3', data.Duration(4, 58))
        input4 = data.Song('Artist4', 'Title4', data.Duration(3, 9))
        input5 = data.Duration(2, 10)
        input = [input1, input2, input3, input4]
        result = hw2.songs_shorter_than(input, input5)
        expected = []
        self.assertEqual(expected, result)

    def test_songs_shorter_than_2(self):
        input1 = data.Song('Artist1','Title1', data.Duration(4,58))
        input2 = data.Song('Artist2', 'Title2', data.Duration(2,18))
        input3 = data.Song('Artist3', 'Title3', data.Duration(4,58))
        input4 = data.Song('Artist4', 'Title4', data.Duration(3,9))
        input5 = data.Duration(3,10)
        input = [input1,input2,input3,input4]
        result = hw2.songs_shorter_than(input,input5)
        expected = [data.Song('Artist2','Title2',data.Duration(2,18)),
                    data.Song('Artist4','Title4',data.Duration(3,9))]
        self.assertEqual(expected,result)





    # Part 4
    def test_running_time_1(self):
        input1 = data.Song('Artist1','Title1', data.Duration(4,58))
        input2 = data.Song('Artist2', 'Title2', data.Duration(2,18))
        input3 = data.Song('Artist3', 'Title3', data.Duration(4,58))
        input4 = data.Song('Artist4', 'Title4', data.Duration(3,9))
        input5 = [0,1,2,3]

        input = [input1,input2,input3,input4]
        result = hw2.running_time(input,input5)
        expected = data.Duration(15,23)
        self.assertEqual(expected,result)

    def test_running_time_2(self):
        input1 = data.Song('Artist1','Title1', data.Duration(0,0))
        input2 = data.Song('Artist2', 'Title2', data.Duration(0,0))
        input3 = data.Song('Artist3', 'Title3', data.Duration(3,58))
        input4 = data.Song('Artist4', 'Title4', data.Duration(0,0))
        input5 = [0,1,1,0]

        input = [input1,input2,input3,input4]
        result = hw2.running_time(input,input5)
        expected = data.Duration(0,0)
        self.assertEqual(expected,result)


    # Part 5
    def test_validate_route_1(self):
        input1 = [['city1','city2'],['city3','city1'],['city4','city2'],['city4','city3']]
        input2 = ['city1','city2','city4']
        result = hw2.validate_route(input1,input2)
        expected = True
        self.assertEqual(expected, result)

    def test_validate_route_2(self):
        input1 = [['city1','city2'],['city3','city1'],['city4','city2'],['city4','city3']]
        input2 = ['city1','city2','city3']
        result = hw2.validate_route(input1,input2)
        expected = False
        self.assertEqual(expected, result)


    # Part 6
    def test_longest_repetition_1(self):
        input1 = [1,2,3,4,1,1,4,4,5,5,5,6,6,7,6]
        result = hw2.longest_repetition(input1)
        expected = 8
        self.assertEqual(expected, result)
    def test_longest_repetition_2(self):
        input1 = [1,1,1,1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,0]
        result = hw2.longest_repetition(input1)
        expected = 9
        self.assertEqual(expected, result)






if __name__ == '__main__':
    unittest.main()
