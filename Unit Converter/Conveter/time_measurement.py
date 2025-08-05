class Second:
    min = hr = day = week = 0

    def __init__(self, s):
        self.s = s

    def s_to_m(self):

        while self.s > 59:
            self.min += 1
            self.s -= 60

        return f"{self.min} min,{self.s}sec or ", self.min

    def s_to_h(self):
        self.s_to_m()

        while self.min > 59:
            self.hr += 1
            self.min -= 60

        return f"{self.hr} hr, {self.min} min,{self.s}sec or ", self.hr

    def s_to_d(self):
        self.s_to_h()

        while self.hr > 23:
            self.day += 1
            self.hr -= 24

        return f"{self.day} Day, {self.hr} hr, {self.min} min,{self.s}sec or ", self.day

    def s_to_w(self):
        self.s_to_d()

        while self.day > 6:
            self.week += 1
            self.day -= 7

        return f"{self.week} week, {self.day} Day, {self.hr} hr, {self.min} min,{self.s}sec or ", self.week


class Minutes:
    sec = hr = day = week = 0

    def __init__(self, m):
        self.min = self.m = m

    def m_to_s(self):
        while self.m > 0:
            self.sec += 60
            self.m -= 1
        return f"{self.m} min or ", self.sec

    def m_to_h(self):

        while self.min > 59:
            self.hr += 1
            self.min -= 60
        return f"{self.hr} hr, {self.min} min or ", self.hr

    def m_to_d(self):
        self.m_to_h()
        while self.hr > 23:
            self.day += 1
            self.hr -= 24
        return f"{self.day} Day, {self.hr} hr, {self.min} min or ", self.day

    def m_to_w(self):
        self.m_to_d()
        while self.day > 6:
            self.week += 1
            self.day -= 7
        return f"{self.week} week, {self.day} Day, {self.hr} hr, {self.min} min or ", self.week


class Hours(Minutes):
    sec = min = day = week = 0

    def __init__(self, h):
        self.hr = self.h = h
        super().__init__(self.h_to_m()[1])

    def h_to_s(self):
        return self.m_to_s()

    def h_to_m(self):
        while self.h > 0:
            self.min += 60
            self.h -= 1
        return f"{self.min} min or ", self.min

    def h_to_d(self):
        while self.hr > 23:
            self.day += 1
            self.hr -= 24
        return f"{self.day} Day, {self.hr} hr or ", self.day

    def h_to_w(self):
        self.h_to_d()
        while self.day > 6:
            self.week += 1
            self.day -= 7
        return f"{self.week} week, {self.day} Day or ", self.week


class Day(Hours):
    sec = min = hr = week = 0

    def __init__(self, d):
        self.day = self.d = d
        super().__init__(self.d_to_h()[1])

    def d_to_s(self):
        self.h_to_s()
        return self.sec

    def d_to_m(self):
        return self.h_to_m()

    def d_to_h(self):
        while self.day > 0:
            self.hr += 24
            self.day -= 1
        return f"{self.hr} hr or ", self.hr

    def d_to_w(self):
        while self.d > 6:
            self.week += 1
            self.d -= 7
        return f"{self.week} week, {self.d} Day, {self.hr} hr or ", self.week


class Week(Day):
    sec = min = hr = day = 0

    def __init__(self, w):
        self.w = self.week = w
        super().__init__(self.w_to_d()[1])

    def w_to_s(self):
        return self.d_to_s()

    def w_to_m(self):
        return self.d_to_m()

    def w_to_h(self):
        return self.d_to_h()

    def w_to_d(self):
        self.w = self.week
        while self.w > 0:
            self.day += 7
            self.w -= 1
        return f"{self.day} day or ", self.day
