import random
import unittest
import rsaidnumber


def rsa_id_number():
    id_num = rsaidnumber.parse("9804205251081")
    return id_num.valid


class CheckingId(unittest.TestCase):
    def id_validation(self):
        rsaidnumber.parse("9804205251081")


def random_numbers():
    x = random.sample(range(1, 49), 6)
    print(x)
    return x


class Randomness(unittest.TestCase):
    def setUp(self):
        self.a = 1
        self.b = 49

    def test_gen_age(self):
        random_numbers()
        self.assertTrue(self.a >= 1 and self.b <= 49);
        if __name__ == '__main__':
            unittest.main()
