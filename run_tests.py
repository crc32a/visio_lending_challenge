#!/usr/bin/env python

from visio_lending import visio
import sys
import unittest

tests_cases = []

rules = visio.load_json("rules.json")
engine = visio.RulesEngine()

class TestCases(unittest.TestCase):
    def test_a(self):
        person = visio.Person(600, "Florida")
        product = visio.Product("7-1 ARM", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 6.0)
        self.assertEqual(product.disqualified, True)

    def test_b(self):
        person = visio.Person(600, "Florida")
        product = visio.Product("other", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 5.5)
        self.assertEqual(product.disqualified, True)

    def test_c(self):
        person = visio.Person(600, "Texas")
        product = visio.Product("7-1 ARM", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 6.0)
        self.assertEqual(product.disqualified, False)

    def test_d(self):
        person = visio.Person(600, "Texas")
        product = visio.Product("other", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 5.5)
        self.assertEqual(product.disqualified, False)

    def test_e(self):
        person = visio.Person(720, "Florida")
        product = visio.Product("7-1 ARM", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 5.2)
        self.assertEqual(product.disqualified, True)

    def test_f(self):
        person = visio.Person(720, "Florida")
        product = visio.Product("other", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 4.7)
        self.assertEqual(product.disqualified, True)

    def test_g(self):
        person = visio.Person(720, "Texas")
        product = visio.Product("7-1 ARM", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 5.2)
        self.assertEqual(product.disqualified, False)

    def test_h(self):
        person = visio.Person(720, "Texas")
        product = visio.Product("other", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 4.7)
        self.assertEqual(product.disqualified, False)

    def test_i(self):
        person = visio.Person(800, "Florida")
        product = visio.Product("7-1 ARM", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 5.2)
        self.assertEqual(product.disqualified, True)

    def test_j(self):
        person = visio.Person(800, "Florida")
        product = visio.Product("other", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 4.7)
        self.assertEqual(product.disqualified, True)

    def test_k(self):
        person = visio.Person(800, "Texas")
        product = visio.Product("7-1 ARM", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 5.2)
        self.assertEqual(product.disqualified, False)

    def test_l(self):
        person = visio.Person(800, "Texas")
        product = visio.Product("other", None, None)
        engine.runRules(person, product, rules)
        self.assertEqual(product.interest_rate, 4.7)
        self.assertEqual(product.disqualified, False)


if __name__ == "__main__":
    unittest.main()
