class Car:
    fuel_price = 0.0

    def __init__(self, brand: str, fuel_consumption: float):
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def set_fuel_price(cls, new_price: float) -> None:
        if new_price < 0:
            raise ValueError("Çmimi i karburantit nuk mund të jetë negativ.")
        cls.fuel_price = new_price

    def calculate_cost(self, distance: float) -> float:
        if distance < 0:
            raise ValueError("Distanca nuk mund të jetë negative.")

        liters_needed = (distance / 100) * self.fuel_consumption
        return liters_needed * type(self).fuel_price


if __name__ == "__main__":
    Car.set_fuel_price(1.90)

    a1 = Car("VW", 6.0)

    print(f"Kostoja për 100 km: {a1.calculate_cost(100):.2f} €")
    print(f"Kostoja për 250 km: {a1.calculate_cost(250):.2f} €")

    Car.set_fuel_price(2.00)
    print(f"Kostoja për 100 km me çmimin e ri: {a1.calculate_cost(100):.2f} €")
