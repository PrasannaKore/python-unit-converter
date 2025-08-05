class Milligram:
    def __init__(self, mg):
        self.mg = mg

    def mg_to_g(self):
        return self.mg / 1000

    def mg_to_kg(self):
        return self.mg / 1000000

    def mg_to_t(self):
        return self.mg / 1000000000


class Gram:
    def __init__(self, g):
        self.g = g

    def g_to_mg(self):
        return self.g * 1000

    def g_to_kg(self):
        return self.g / 1000

    def g_to_t(self):
        return self.g / 1000000


class Kilogram:
    def __init__(self, kg):
        self.kg = kg

    def kg_to_mg(self):
        return self.kg * 1000000

    def kg_to_g(self):
        return self.kg * 1000

    def kg_to_t(self):
        return self.kg / 1000


class Tonne:
    def __init__(self, t):
        self.t = t

    def t_to_mg(self):
        return self.t * 1000000000

    def t_to_g(self):
        return self.t * 1000000

    def t_to_kg(self):
        return self.t * 1000
