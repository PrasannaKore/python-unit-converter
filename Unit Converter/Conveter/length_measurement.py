class Millimeter:
    def __init__(self, mm):
        self.mm = mm

    def mm_to_cm(self):
        return self.mm / 10

    def mm_to_m(self):
        return self.mm / 1000

    def mm_to_km(self):
        return self.mm / 1000000


class Centimeter:
    def __init__(self, cm):
        self.cm = cm

    def cm_to_mm(self):
        return self.cm * 10

    def cm_to_m(self):
        return self.cm / 100

    def cm_to_km(self):
        return self.cm / 100000


class Meter:
    def __init__(self, m):
        self.m = m

    def m_to_mm(self):
        return self.m * 1000

    def m_to_cm(self):
        return self.m * 100

    def m_to_km(self):
        return self.m / 1000


class Kilometer:
    def __init__(self, km):
        self.km = km

    def km_to_mm(self):
        return self.km * 1000000

    def km_to_cm(self):
        return self.km * 100000

    def km_to_m(self):
        return self.km * 1000
