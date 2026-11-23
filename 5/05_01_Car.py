class Car:
    def __init__(self, brand: str, model: str, year: int, mileage: float):
        self._brand = brand
        self._model = model
        self._year = year
        self._mileage = mileage

    @property
    def brand(self) -> str:
        return self._brand

    @property
    def model(self) -> str:
        return self._model

    @property
    def year(self) -> int:
        return self._year

    @property
    def mileage(self) -> float:
        return self._mileage

    def add_mileage(self, kilometers: float) -> None:
        if kilometers < 0:
            raise ValueError("Kilometrat e shtuara nuk mund të jenë negative.")
        self._mileage += kilometers


if __name__ == "__main__":
    car = Car("VW", "Golf", 2020, 45000.0)

    print("Marka:", car.brand)
    print("Modeli:", car.model)
    print("Viti:", car.year)
    print("Kilometrazhi:", car.mileage)

    car.add_mileage(250.5)
    print("Kilometrazhi pas shtimit:", car.mileage)

    try:
        car.add_mileage(-10)
    except ValueError as error:
        print("Gabim:", error)
