from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.tp = TennisPlayer("Ivan", 36, 100)

    def test_init(self):
        self.assertEqual("Ivan", self.tp.name)
        self.assertEqual(36, self.tp.age)
        self.assertEqual(100, self.tp.points)
        self.assertEqual([],self.tp.wins)

    def test_name_setter_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.tp.name = "I"
        self.assertEqual("Name should be more than 2 symbols!", str(ex.exception))

    def test_age_setter_fail(self):
        with self.assertRaises(ValueError) as ex:
            self.tp.age = 17
        self.assertEqual("Players must be at least 18 years of age!", str(ex.exception))

    def test_add_new_win_success(self):
        self.tp.add_new_win("T1")
        self.assertEqual(["T1"], self.tp.wins)

    def test_add_new_win_fail(self):
        self.tp.wins = ["T1"]
        result = self.tp.add_new_win("T1")
        self.assertEqual("T1 has been already added to the list of wins!", result)

    def test_dunder_lt_1(self):
        self.tp2 = TennisPlayer("Gosho", 36, 101)
        result = self.tp.__lt__(self.tp2)
        self.assertEqual("Gosho is a top seeded player and he/she is better than Ivan", result)

    def test_dunder_lt_2(self):
        self.tp2 = TennisPlayer("Gosho", 36, 101)
        result = self.tp2.__lt__(self.tp)
        self.assertEqual("Gosho is a better player than Ivan", result)

    def test_dunder_str(self):
        self.tp2 = TennisPlayer("Gosho", 36, 70)
        result1 = str(self.tp)
        result2 = str(self.tp2)

        t_player_3 = TennisPlayer("Name", 20, 20)
        t_player_3.add_new_win("Win1")
        t_player_3.add_new_win("Win2")
        t_player_3.add_new_win("Win3")

        result3 = str(t_player_3)

        self.assertEqual('Tennis Player: Ivan\nAge: 36\nPoints: 100.0\nTournaments won: ', result1)
        self.assertEqual('Tennis Player: Gosho\nAge: 36\nPoints: 70.0\nTournaments won: ', result2)
        self.assertEqual('Tennis Player: Name\nAge: 20\nPoints: 20.0\nTournaments won: Win1, Win2, Win3', result3)




if __name__ == '__main__':
    main()
