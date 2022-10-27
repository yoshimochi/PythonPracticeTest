import re


class User:
    user_type = None

    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def increment_age(self):
        """年齢を１つ増やす"""
        self.age += 1

    def start_name(self):
        """nameの１文字目を取得する"""
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ''


# user1 = User('寺田学', 35, '東京都台東区')
# type(user1)
# print(user1.name)


# プロパティ
class User1:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def increment_age(self):
        """年齢を１つ増やす"""
        self.age += 1

    def start_name(self):
        """nameの１文字目を取得する"""
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ''

    @property
    def start_name(self):
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ''

    @start_name.setter
    def start_name(self, input_name):
        self.name = input_name
        if len(self.name) > 0:
            return self.name[0]
        else:
            return ''


user = User1('寺田学', 35, '東京都台東区')
print(user.start_name)

user.name = '高橋一郎'
print(user.start_name)

# 継承
import unittest
import pathlib


class TestBase(unittest.TestCase):
    def setUp(self) -> None:
        self.data_path = pathlib('/tmp/data')

    def tearDown(self) -> None:
        for p in self.data_path.iterdir():
            p.unlink()


class TestSample(TestBase):
    def setUp(self) -> None:
        super().setUp()
        p1 = self.data_path / 'sample.txt'
        p1.touch()
        p2 = self.data_path / 'sample2.txt'
        p2.touch()

    def test_two_files(self):
        self.assertEqual(len(list(self.data_path.iterdir())), 2)


class TestSample2(TestBase):
    def setUp(self) -> None:
        super().setUp()
        p3 = self.data_path / 'sample3.txt'
        p3.touch()

    def test_one_file(self):
        self.assertEqual(len(list(self.data_path.iterdir())), 1)
