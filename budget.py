import calendar
from datetime import datetime


class Period(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def overlapping_days(self, another):
        overlapping_start = self.start if self.start > another.start else another.start
        overlapping_end = self.end if self.end < another.end else another.end
        return (overlapping_end - overlapping_start).days + 1


class Budget(object):
    def __init__(self, year_month, amount):
        self.year_month = year_month
        self.amount = amount
        self.year = int(self.year_month[:4])
        self.month = int(self.year_month[4:])

    def first_day(self):
        return datetime(self.year, self.month, 1)

    def last_day(self):
        days = calendar.monthrange(self.year, self.month)[1]
        return datetime(self.year, self.month, days)

    def get_period(self):
        return Period(self.first_day(), self.last_day())

    def get_daily_amount(self):
        return self.amount / self.last_day().day


class BudgetRepo:
    @staticmethod
    def get_all() -> list[Budget]:
        return []


class BudgetService:
    @staticmethod
    def query(start: datetime, end: datetime) -> float:
        budgets = BudgetRepo.get_all()
        for budget in budgets:
        # if len(budgets) > 0:
        #     budget = budgets[0]
            if end < budget.first_day() or start > budget.last_day():
                return 0
            period = Period(start, end)
            overlapping_days = period.overlapping_days(budget.get_period())
            return overlapping_days * budget.get_daily_amount()
        return 0
