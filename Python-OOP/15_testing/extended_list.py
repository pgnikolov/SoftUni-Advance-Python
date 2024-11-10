class IntegerList:
    def __init__(self, *args):
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


from unittest import TestCase, main


class TestIntegerList(TestCase):

    def setUp(self):
        self.list = IntegerList(1, 3, 9, 7, 5)

    def test_successful_initial(self):
        self.assertEqual([1, 3, 9, 7, 5], self.list._IntegerList__data)

    def test_init_il(self):
        result = self.list.get_data()
        expected = list([1, 3, 9, 7, 5])
        self.assertEqual(expected, result)

    def test_get_data(self):
        result = self.list.get_data()
        expected = list([1, 3, 9, 7, 5])

        self.assertEqual(expected, result)

    def test_add_element_success(self):
        result = self.list.add(100)
        expected = list([1, 3, 9, 7, 5, 100])
        self.assertEqual(expected, result)

    def test_add_element_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.list.add('100')
        self.assertEqual(str(ex.exception), "Element is not Integer")

    def test_remove_index_success(self):
        result = self.list.remove_index(0)
        expected = 1
        self.assertEqual(expected, result)

    def test_remove_index_fail(self):
        with self.assertRaises(IndexError) as ex:
            self.list.remove_index(7)
        self.assertEqual(str(ex.exception), "Index is out of range")

    def test_unsuccessful_insert_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.list.insert(6, 4)

        self.assertEqual(str(ie.exception), "Index is out of range")

    def test_unsuccessful_insert_with_wrong_element_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.list.insert(0, "1")

        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_successful_insert_element_in_list(self):
        self.list.insert(0, 10)

        self.assertEqual([10, 1, 3, 9, 7, 5], self.list._IntegerList__data)

    def test_successful_get_biggest_element_in_list(self):
        result = self.list.get_biggest()
        self.assertEqual(9, result)

    def test_successful_get_index_element_in_list(self):
        result = self.list.get_index(1)
        self.assertEqual(0, result)


if __name__ == '__main__':
    main()
