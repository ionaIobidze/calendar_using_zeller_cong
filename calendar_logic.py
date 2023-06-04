class CalendarLogic:
    def __init__(self, month, year):
        self.month = month
        self.year = year
        self.month_dic = {
            1: "January",
            2: "February",
            3: "March",
            4: "April",
            5: "May",
            6: "June",
            7: "July",
            8: "August",
            9: "September",
            10: "October",
            11: "November",
            12: "December",
        }
        self.month_days_dic = {
            1: 31,
            2: 28,
            3: 31,
            4: 30,
            5: 31,
            6: 30,
            7: 31,
            8: 31,
            9: 30,
            10: 31,
            11: 30,
            12: 31,
        }

    def zeller_congruence(self, date, month, year):
        if month == 1 or month == 2:
            month += 12
            year -= 1
        k = year % 100
        j = year // 100
        return (date + ((13 * (month + 1)) // 5) + k + (k // 4) + (j // 4) + 5 * j) % 7

    def get_calendar(self):
        if self.year % 4 == 0 and (self.year % 100 != 0 or self.year % 400 == 0):
            self.month_days_dic[2] = 29

        days_in_month = self.month_days_dic[self.month]
        calendar_str = []
        calendar_str.append(f"{self.month_dic[self.month]} {self.year}".center(20))
        calendar_str.append("Mo Tu We Th Fr Sa Su")

        first_day = self.zeller_congruence(1, self.month, self.year)
        if first_day == 0:
            first_day = 7

        week = ['   '] * (first_day - 1)
        day_counter = 1

        while day_counter <= days_in_month:
            if len(week) == 7:
                calendar_str.append(' '.join(week))
                week = []

            week.append(f"{day_counter:2d}")
            day_counter += 1

        if week:
            calendar_str.append(' '.join(week))

        return '\n'.join(calendar_str)
