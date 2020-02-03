from collections import deque


class ToNumber:
    '''
        Transform numbers written in words to number representation
    '''

    def __init__(self):
        ''' init method '''

        self.__under_20 = {
            'zero':     0,  'one':        1,
            'two':      2,  'three':      3,
            'four':     4,  'five':       5,
            'six':      6,  'seven':      7,
            'eight':    8,  'nine':       9,
            'ten':      10, 'eleven':     11,
            'twelve':   12, 'thirteen':   13,
            'fourteen': 14, 'fifteen':    15,
            'sixteen':  16, 'seventeen':  17,
            'eighteen': 18, 'nineteen':   19
        }
        self.__tens = {
            'twenty':   20, 'thirty':  30,
            'forty':    40, 'fifty':   50,
            'sixty':    60, 'seventy': 70,
            'eighty':   80, 'ninety':  90
        }

        self.__above_100 = {'hundred': 100, 'thousand': 1000,
                            'million': 1000000, 'billion': 1000000000}

    def __words_to_numbers(self, string):
        '''
        Translate words to number representation
        e.g. ten thousand nine hundred sixty-seven
        deque([10, 1000, 9, 100, 60, 7])

        Args:
            string (str)
        Return:
            numbers (deque)

            for invalid input return deque([-1])

        '''
        string = string.replace(" ", "")
        string = string.replace("-", "")
        string = string.lower()  # e.g. tenthousandninehundredsixtyseven

        FOUND_AT_START = 0
        numbers = deque([])

        while(len(string)):

            for key, value in self.__under_20.items():
                if string == key:
                    numbers.append(value)
                    string = ""
                    break
                elif string.find(key) == FOUND_AT_START:
                    if string[len(key): len(key) + 1] in ('t', 'y', 'e'):
                        if string[len(key): len(key) + 8] in ('thousand'):
                            numbers.append(value)
                            string = string[len(key):]
                            break
                    else:
                        numbers.append(value)
                        string = string[len(key):]
                        break

            for key, value in self.__tens.items():
                if string.lower() == key:
                    string = ""
                    numbers.append(value)
                    break
                elif string.find(key) == FOUND_AT_START:
                    numbers.append(value)
                    string = string[len(key):]
                    break

            for key, value in self.__above_100.items():
                if string == key:
                    string = ""
                    numbers.append(value)
                    break
                elif string.find(key) == FOUND_AT_START:
                    numbers.append(value)
                    string = string[len(key):]
                    break

            if not numbers:
                numbers.append(-1)
                break

        return numbers

    def __parse_numbers(self, numbers):
        '''
        Transform deque numbers to decimal number
        e.g. deque([10, 1000, 9, 100, 60, 7])
        10967

        Args:
            numbers (deque)
        Return:
            number (int)

        '''
        aux = int()
        count = int()
        list_values = []

        if len(numbers) == 1:
            return numbers[0]
        if len(numbers) == 2:
            if numbers[1] in self.__above_100.values():
                return numbers[1]
            return sum(numbers)

        while numbers:
            num = numbers.popleft()
            if not aux:
                aux = num
                continue

            if num in self.__above_100.values():
                count = (aux * num)
            elif count < 1000:
                count = count + num
                aux = count
            else:
                list_values.append(count)
                count = int()
                aux = num
                if len(numbers) == 0:
                    count = aux
        return sum(list_values) + count

    def words_to_number(self, string):
        '''
        Translate words to number representation
        e.g. ten thousand nine hundred sixty-seven
        to 10967
        Args:
            string (str)
        Return:
            number (int)

            return -1 for invalid input

        '''
        numbers = self.__words_to_numbers(string)
        return self.__parse_numbers(numbers)
