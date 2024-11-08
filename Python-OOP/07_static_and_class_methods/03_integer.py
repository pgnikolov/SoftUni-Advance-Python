class Integer:
    def __init__(self, value):
        self.value = value

    @staticmethod
    def from_float(float_value):
        if type(float_value) == float:
            return Integer(round(float_value))
        return 'value is not a float'

    @staticmethod
    def from_roman(value):
        roman_values = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        i = 0

        while i < len(value):
            s1 = roman_values[value[i]]

            if i + 1 < len(value) and s1 < roman_values[value[i + 1]]:
                result += roman_values[value[i + 1]] - s1
                i += 2
            else:
                result += s1
                i += 1

        return Integer(int(result))

    @staticmethod
    def from_string(value):
        if type(value) == str:
            return Integer(int(value))
        return 'wrong type'
