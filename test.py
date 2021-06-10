"""Unit tests for blagues-api wrapper"""

import unittest
import os
import dotenv

import BlaguesApi

dotenv.load_dotenv()

TOKEN = os.getenv('MY_ENV_VAR')

Jokes = BlaguesApi.Jokes(TOKEN)
JokesAround = BlaguesApi.JokesAround(TOKEN)

class WrapperTests(unittest.TestCase):

    def test_token(self):
        """ Check token existance in .env """
        self.assertIsInstance(TOKEN, str)

    def test_random_joke(self):
        """ Check random joke """
        response = Jokes.random()
        self.assertIsInstance(response, dict)
        self.assertIsInstance(response["id"], int)
        self.assertIn(response["type"], BlaguesApi.JokeTypes)
        self.assertIsInstance(response["joke"], str)
        self.assertIsInstance(response["answer"], str)

    def test_random_with_disallowed_without_params(self):
        """ Check random with disallowed type without params """
        response = Jokes.random_without()
        self.assertIn(response["type"], BlaguesApi.JokeTypes)

    def test_random_with_disallowed(self):
        """ Check random with disallowed DARK type """
        response = Jokes.random_without(BlaguesApi.Types.DARK)
        self.assertIsInstance(response, dict)
        self.assertIsInstance(response["id"], int)
        self.assertNotEqual(response["type"], BlaguesApi.Types.DARK)
        self.assertIsInstance(response["joke"], str)
        self.assertIsInstance(response["answer"], str)

    def test_by_id(self):
        """ Check joke by ID """
        response = Jokes.from_id(1)
        self.assertIsInstance(response, dict)
        self.assertEqual(response["id"], 1)
        self.assertIn(response["type"], BlaguesApi.JokeTypes)
        self.assertIsInstance(response["joke"], str)
        self.assertIsInstance(response["answer"], str)
    
    def test_random_joke_arround(self):
        """ Check random joke (arround)"""
        response = JokesAround.random()
        self.assertIsInstance(response, dict)
        self.assertIsInstance(response["id"], int)
        self.assertIn(response["type"], BlaguesApi.JokeTypes)
        self.assertIsInstance(response["joke"], str)
        self.assertIsInstance(response["answer"], str)

    def test_random_with_disallowed_without_params_arround(self):
        """ Check random with disallowed type without params (arround)"""
        response = JokesAround.random_without()
        self.assertIn(response["type"], BlaguesApi.JokeTypes)

    def test_random_with_disallowed_arround(self):
        """ Check random with disallowed DARK type (arround)"""
        response = JokesAround.random_without(BlaguesApi.Types.DARK)
        self.assertIsInstance(response, dict)
        self.assertIsInstance(response["id"], int)
        self.assertNotEqual(response["type"], BlaguesApi.Types.DARK)
        self.assertIsInstance(response["joke"], str)
        self.assertIsInstance(response["answer"], str)

    def test_by_id_arround(self):
        """ Check joke by ID (arround)"""
        response = JokesAround.from_id(1)
        self.assertIsInstance(response, dict)
        self.assertEqual(response["id"], 1)
        self.assertIn(response["type"], BlaguesApi.JokeTypes)
        self.assertIsInstance(response["joke"], str)
        self.assertIsInstance(response["answer"], str)


if __name__ == '__main__':
    unittest.main()
