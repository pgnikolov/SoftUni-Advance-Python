from project.hero import Hero
from unittest import TestCase, main


class TestHero(TestCase):
    def setUp(self) -> None:
        self.hero = Hero("hero", 2, 100, 50)
        self.enemy = Hero('enemy', 2, 100, 50)

    def test_init(self):
        self.assertEqual(self.hero.username, "hero")
        self.assertEqual(self.hero.level, 2)
        self.assertEqual(self.hero.health, 100)
        self.assertEqual(self.hero.damage, 50)

    def test_battle_yourself_fail(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual(str(ex.exception), "You cannot fight yourself")

    def test_battle_health_zero(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(Hero("enemy", 4, 100, 70))

        self.assertEqual(str(ex.exception), "Your health is lower than or equal to 0. You need to rest")

    def test_battle_enemy_health_zero(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(str(ex.exception), f"You cannot fight {self.enemy.username}. He needs to rest")

    def test_battle_win(self):
        self.enemy.health = 70
        self.enemy.damage = 45
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.hero.level, 3)
        self.assertEqual(self.hero.health, 15)
        self.assertEqual(self.hero.damage, 55)
        self.assertEqual("You win", result)

    def test_successful_battle_draw(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(0, self.hero.health)
        self.assertEqual(0, self.enemy.health)

    def test_battle_lose(self):
        self.hero.health = 70
        self.hero.damage = 45
        result = self.hero.battle(self.enemy)
        self.assertEqual(self.enemy.level, 3)
        self.assertEqual(self.enemy.health, 15)
        self.assertEqual(self.enemy.damage, 55)
        self.assertEqual("You lose", result)

    def test__str__(self):
        self.assertEqual("Hero hero: 2 lvl\n"
                         "Health: 100\n"
                         "Damage: 50\n", str(self.hero))


if __name__ == "__main__":
    main()
