from project.movie import Movie
from unittest import TestCase, main


class TestMovie(TestCase):

    def setUp(self) -> None:
        self.m = Movie('test', 2024, 5.00)

    def test_movie_init(self):
        self.assertEqual(self.m.name, 'test')
        self.assertEqual(self.m.year, 2024)
        self.assertEqual(self.m.rating, 5.00)
        self.assertEqual(self.m.actors, [])

    def test_movie_name_set_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.m.name = ''
        self.assertEqual(str(ex.exception),"Name cannot be an empty string!")

    def test_movie_year_set_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.m.year = 1800
        self.assertEqual(str(ex.exception),"Year is not valid!")

    def test_add_actor_success(self):
        self.m.add_actor('Peter')
        self.assertEqual(self.m.actors, ['Peter'])

    def test_add_actor_fail(self):
        self.m.actors = ['Peter']
        result = self.m.add_actor('Peter')
        self.assertEqual(result,
            "Peter is already added in the list of actors!")

    def test_movie__gt__better(self):
        other = Movie('test2', 2024, 6.00)
        result = self.m.__gt__(other)
        self.assertEqual(result, '"test2" is better than "test"')

    def test_movie__gt__worse(self):
        other = Movie('test2', 2024, 4.00)
        result = self.m.__gt__(other)
        self.assertEqual(result, '"test" is better than "test2"')

    def test_movie__repr__(self):
        self.m.actors = ['Peter']
        result = self.m.__repr__()
        expected = 'Name: test\nYear of Release: 2024\nRating: 5.00\nCast: Peter'
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()
