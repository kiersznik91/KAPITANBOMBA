import unittest
import KAPITANBOMBA.gra as gra


class HERO_test_case(unittest.TestCase):
    """Sprawdza klasę."""
    def test_case_ATAKBOMBY(self):
        """Czy wartość ataku to integer?"""
        mock = gra.KAPITANBOMBA(10, 10, 'karabinlaserowy', 'kombinezonbojowy')
        mock.attack_power()
        x = mock.weapon_power
        self.assertTrue(isinstance(x,int),msg= "Temat spierdolony, wynik musi być liczbą")
    def test_wynik_ataku_bomby(self):
        """Czy wynik liczenia ataku jest poprawny?"""
        mock = gra.KAPITANBOMBA(10, 10, 'karabinlaserowy', 'kombinezonbojowy')
        mock.attack_power()
        x = mock.weapon_power
        self.assertEqual(x, 12, msg="Źle liczy! Jest {} a ma być 12".format(x))

if __name__ == "__main__":
    unittest.main()
