import unittest
from datetime import datetime
from mock import patch

from budget import BudgetService
from budget import Budget


class BudgetTestCase(unittest.TestCase):
    def test_no_budgets(self):
        start = datetime(2023, 7, 15)
        end = datetime(2023, 7, 16)
        got = BudgetService.query(start, end)
        self.assertEqual(0, got)

    @patch("budget.BudgetRepo.get_all")
    def test_query_full_month(self, mock_get_all):
        mock_get_all.return_value = [Budget("202307", 31)]
        start = datetime(2023, 7, 1)
        end = datetime(2023, 7, 31)
        got = BudgetService.query(start, end)
        self.assertEqual(31, got)

    @patch("budget.BudgetRepo.get_all")
    def test_period_inside_budget(self, mock_get_all):
        mock_get_all.return_value = [Budget("202307", 31)]
        start = datetime(2023, 7, 15)
        end = datetime(2023, 7, 16)
        got = BudgetService.query(start, end)
        self.assertEqual(2, got)

    @patch("budget.BudgetRepo.get_all")
    def test_period_no_overlap_before_budget_first_day(self, mock_get_all):
        mock_get_all.return_value = [Budget("202307", 31)]
        start = datetime(2023, 6, 1)
        end = datetime(2023, 6, 2)
        got = BudgetService.query(start, end)
        self.assertEqual(0, got)

    @patch("budget.BudgetRepo.get_all")
    def test_period_no_overlap_after_budget_last_day(self, mock_get_all):
        mock_get_all.return_value = [Budget("202307", 31)]
        start = datetime(2023, 8, 2)
        end = datetime(2023, 8, 4)
        got = BudgetService.query(start, end)
        self.assertEqual(0, got)

    @patch("budget.BudgetRepo.get_all")
    def test_period_overlap_budget_first_day(self, mock_get_all):
        mock_get_all.return_value = [Budget("202307", 31)]
        start = datetime(2023, 6, 28)
        end = datetime(2023, 7, 15)
        got = BudgetService.query(start, end)
        self.assertEqual(15, got)

    @patch("budget.BudgetRepo.get_all")
    def test_period_overlap_budget_last_day(self, mock_get_all):
        mock_get_all.return_value = [Budget("202307", 31)]
        start = datetime(2023, 7, 28)
        end = datetime(2023, 8, 2)
        got = BudgetService.query(start, end)
        self.assertEqual(4, got)

    @patch("budget.BudgetRepo.get_all")
    def test_daily_amount_100(self, mock_get_all):
        mock_get_all.return_value = [Budget("202307", 3100)]
        start = datetime(2023, 7, 28)
        end = datetime(2023, 8, 2)
        got = BudgetService.query(start, end)
        self.assertEqual(400, got)

    @patch("budget.BudgetRepo.get_all")
    def test_multiple_months(self, mock_get_all):
        mock_get_all.return_value = [Budget("202306", 30),
                                     Budget("202307", 310),
                                     Budget("202308", 3100)]
        start = datetime(2023, 6, 29)
        end = datetime(2023, 8, 10)
        got = BudgetService.query(start, end)
        self.assertEqual(1 * 2 + 310 + 100 * 10, got)


if __name__ == '__main__':
    unittest.main()
