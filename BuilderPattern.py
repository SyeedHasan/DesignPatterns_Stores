from __future__ import annotations
from abc import ABC, abstractmethod, abstractproperty
from typing import Any

class ManufacturerBuilder(ABC): 
    @abstractproperty
    def product(self) -> None:
        pass

    @abstractmethod
    def gatherRawMaterials(self) -> None:
        pass

    @abstractmethod
    def stitchAll(self) -> None:
        pass

    @abstractmethod
    def packStuff(self) -> None:
        pass


class ClothesBuilder(ManufacturerBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Clothes()

    @property
    def product(self) -> Clothes:
        product = self._product
        self.reset()
        return product

    def gatherRawMaterials(self) -> None:
        self._product.add("Cloth: Raw Materials Gathered")

    def stitchAll(self) -> None:
        self._product.add("Cloth: Stitched")

    def packStuff(self) -> None:
        self._product.add("Cloth: Quality Control Completed and Packed")

class ShoeBuilder(ManufacturerBuilder):
    def __init__(self) -> None:
        self.reset()

    def reset(self) -> None:
        self._product = Clothes()

    @property
    def product(self) -> Clothes:
        product = self._product
        self.reset()
        return product

    def gatherRawMaterials(self) -> None:
        self._product.add("Shoe: Raw Materials Gathered")

    def stitchAll(self) -> None:
        self._product.add("Shoe: Stitched")

    def packStuff(self) -> None:
        self._product.add("Shoe: Quality Control Completed and Packed")

class Clothes:

    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def listSteps(self) -> None:
        print(f"Steps Completed for {', '.join(self.parts)}", end="")

class Shoes:
    
    def __init__(self) -> None:
        self.parts = []

    def add(self, part: Any) -> None:
        self.parts.append(part)

    def listSteps(self) -> None:
        print(f"Steps Completed for {', '.join(self.parts)}", end="")



class Director:
    def __init__(self) -> None:
        self._builder = None

    @property
    def builder(self) -> ManufacturerBuilder:
        return self._builder

    @builder.setter
    def builder(self, builder: ManufacturerBuilder) -> None:
        self._builder = builder

    def returnRawMaterials(self) -> None:
        self.builder.gatherRawMaterials()

    def makeClothes(self) -> None:
        self.builder.gatherRawMaterials()
        self.builder.stitchAll()
        self.builder.packStuff()


if __name__ == "__main__":
    director = Director()
    builder = ClothesBuilder()
    shoeBuilder = ShoeBuilder()
    
    director.builder = builder

    print("Standard Raw Materials for Order: ")
    director.returnRawMaterials()
    builder.product.listSteps()

    print("\n")

    print("Standard Full-featured Product: ")
    director.makeClothes()
    builder.product.listSteps()

    print("\n")