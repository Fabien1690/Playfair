import unittest
from square import Square


class TestPlayfairSquare(unittest.TestCase):
    def setUp(self):
        tab_alphabet = dict(A=1, B=2, C=3, D=4, E=5,
                            F=6, G=7, H=8, I=9, J=10,
                            K=11, L=12, M=13, N=14, O=15,
                            P=16, Q=17, R=18, S=19, T=20,
                            U=21, V=22, X=23, Y=24, Z=25)

        self.carre_test = Square(tab_alphabet)

    def test_get_lettres_normal(self):
        self.assertEqual(self.carre_test.encrypt_letters("P", "V"), "QU")
        self.assertEqual(self.carre_test.encrypt_letters("N", "A"), "KD")
        self.assertEqual(self.carre_test.encrypt_letters("A", "S"), "DP")
        self.assertEqual(self.carre_test.encrypt_letters("C", "Z"), "EX")

    def test_get_lettres_horizontal(self):
        self.assertEqual(self.carre_test.encrypt_letters("M", "O"), "NK")
        self.assertEqual(self.carre_test.encrypt_letters("D", "E"), "EA")

    def test_get_lettres_vertical(self):
        self.assertEqual(self.carre_test.encrypt_letters("Z", "E"), "EJ")
        self.assertEqual(self.carre_test.encrypt_letters("A", "U"), "FA")

    def test_get_letters_same(self):
        self.assertEqual(self.carre_test.encrypt_letters("M", "M"), "MXM")

    def test_encrypt_text(self):
        self.assertEqual(self.carre_test.encrypt_text("WHATASTRANGENIGHT"),
                         "XGEPDPPSDKJBSNHIT")

    def test_decrypt_normal(self):
        self.assertEqual(self.carre_test.decrypt_letters("Q", "U"), "PV")
        self.assertEqual(self.carre_test.decrypt_letters("K", "D"), "NA")
        self.assertEqual(self.carre_test.decrypt_letters("D", "P"), "AS")
        self.assertEqual(self.carre_test.decrypt_letters("E", "X"), "CZ")

    def test_decrypt_horizontal(self):
        self.assertEqual(self.carre_test.decrypt_letters("N", "K"), "MO")
        self.assertEqual(self.carre_test.decrypt_letters("E", "A"), "DE")
        self.assertEqual(self.carre_test.decrypt_letters("U", "Z"), "ZY")

    def test_decrypt_vertical(self):
        self.assertEqual(self.carre_test.decrypt_letters("E", "J"), "ZE")
        self.assertEqual(self.carre_test.decrypt_letters("F", "A"), "AU")

    def test_decrypt_text(self):
        self.assertEqual(self.carre_test.decrypt_text("XGEPDPPSDKJBSNHIT"),
                         "VHATASTRANGENIGHT")

if __name__ == '__main__':
    unittest.main()
