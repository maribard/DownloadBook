from data_of_books import download_book_with_name
import unittest
import downloading
import data_of_books
import os
from os import path



class TestCase(unittest.TestCase):

    def test_check_a_file(self):
        self.assertEqual(download_book_with_name("Online Consumer Trends 2020"), True)



if __name__== "__main__":
   unittest.main()