from django.test import TestCase
from utilities.utility_number import ToNumber
words = {
    "one": (1, [1]),
    "eleven": (11, [11]),
    "thirty": (30, [30]),
    "ninetynine": (99, [90, 9]),
    "one hundred": (100, [1, 100]),
    "one hundred one": (101, [1, 100, 1]),
    "two hundred twelve": (212, [2, 100, 12]),
    "two hundred seventy-one": (271, [2, 100, 70, 1]),
    "one thousand one": (1001, [1, 1000, 1]),
    "one thousandone hundred one": (1101, [1, 1000, 1, 100, 1]),
    "fifteenthousand sixteen": (15016, [15, 1000, 16]),
    "nine hundred ninety-nine thousand nine hundred ninety-nine": (999999, [9, 100, 90, 9, 1000, 9, 100, 90, 9]),
    "eighty million two hundred thirteen thousand six hundred forty-two": (80213642, [80, 1000000, 2, 100, 13, 1000, 6, 100, 40, 2])
}


class TestWordsToNumber(TestCase):

    def test_words_to_number_deque(self):
        '''
        Test private method that should return representation numbers for
        each word
        e.g. ten thousand nine hundred sixty-seven
        deque([10, 1000, 9, 100, 60, 7])

        '''
        to_number = ToNumber()
        for word, value in words.items():
            test_list = value[1]
            list_numbers = list(to_number._ToNumber__words_to_numbers(word))
            self.assertListEqual(test_list, list_numbers)

    def test_invalid_words(self):
        '''
        test invalid input return -1
        '''
        to_number = ToNumber()
        invalid_imputs = ["Perrito", "Thirsty", "toww"]
        for word in invalid_imputs:
            number = to_number.words_to_number(word)
            self.assertEqual(-1, number)

    def test_valid_number(self):
        '''
        return valid number for each word
        '''
        to_number = ToNumber()
        for word, value in words.items():
            num_test = value[0]
            number = to_number.words_to_number(word)
            self.assertEqual(num_test, number)