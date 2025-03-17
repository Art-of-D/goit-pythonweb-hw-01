import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from abc import ABC, abstractmethod
from logger import logger


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make, model):
        pass

    @abstractmethod
    def create_motorcycle(self, make, model):
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "US")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "US")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make, model):
        return Car(make, model, "EU")

    def create_motorcycle(self, make, model):
        return Motorcycle(make, model, "EU")


class Vehicle(ABC):
    def __init__(self, make, model, region):
        self.make = make
        self.model = model
        self.region = region

    @abstractmethod
    def start_engine(self):
        pass


class Car(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self):
        logger.info(f"{self.make} {self.model} ({self.region} Spec): Мотор заведено")


us_factory = USVehicleFactory()
eu_factory = EUVehicleFactory()

vehicle1 = us_factory.create_car("Ford", "Mustang")
vehicle1.start_engine()

vehicle2 = eu_factory.create_motorcycle("Suzuki", "SuperSport")
vehicle2.start_engine()
