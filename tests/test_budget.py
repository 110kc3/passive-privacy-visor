from decimal import Decimal
import unittest

from scripts.budget import calculate, load_bom


class BudgetTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = load_bom()

    def test_core_delivered_total(self):
        result = calculate(self.data, "core")
        self.assertEqual(Decimal(result["items_pln"]), Decimal("86.79"))
        self.assertEqual(Decimal(result["shipping_pln"]), Decimal("23.19"))
        self.assertEqual(Decimal(result["delivered_total_pln"]), Decimal("109.98"))

    def test_complete_delivered_total(self):
        result = calculate(self.data, "complete")
        self.assertEqual(Decimal(result["items_pln"]), Decimal("102.81"))
        self.assertEqual(Decimal(result["shipping_pln"]), Decimal("23.19"))
        self.assertEqual(Decimal(result["delivered_total_pln"]), Decimal("126.00"))

    def test_optional_sewing_supplies_add_no_shipping_group(self):
        core = Decimal(calculate(self.data, "core")["delivered_total_pln"])
        complete = Decimal(calculate(self.data, "complete")["delivered_total_pln"])
        self.assertEqual(complete - core, Decimal("16.02"))


if __name__ == "__main__":
    unittest.main()
