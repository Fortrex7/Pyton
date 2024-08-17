class Cassa:
    summa=5125 # количество денег в кассе
    def top_up(self, pokup):
        self.pokup = pokup
        pokup += Cassa.summa
        return f"В кассу добавили {self.pokup} рублей. Общая сумма {pokup}"

    def count_1000(self):
        return f"В кассе {Cassa.summa//1000} целых тысяч"

    def take_away(self, x):
        if x <= self.summa:
            self.summa -= x
            return f"Из кассы забрали {x} рублей, в кассе осталось {self.summa} рублей."
        else:
            return f"Из кассы хотят взять {x} рублей. В кассе не достаточно денег!"

r=Cassa()

print(f"В кассе {Cassa.summa} рублей.")
print(r.top_up(125))
print(r.count_1000())
print(r.take_away(5000))
print(r.take_away(150))