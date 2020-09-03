from __future__ import annotations

class ClothingStore:
    def __init__(self, ClothesDpt: ClothesDepartment, ShoesDpt: ShoesDepartment) -> None:
        
        self._ClothesDpt = ClothesDpt or ClothesDepartment()
        self._ShoesDpt = ShoesDpt or ShoesDepartment()

    def handleOperations(self) -> str:
        results = []
        results.append("\n")
        results.append("ClothingStore initializing all subsystems or components:")
        results.append("\n")
        results.append(self._ClothesDpt.initialize())
        results.append(self._ShoesDpt.initialize())
        results.append("ClothingStore will now send out requests to return final cost after Decorators:")
        results.append(self._ClothesDpt.returnCost())
        results.append(self._ShoesDpt.returnCost())
        results.append("\n")
        return "\n".join(results)


class ClothesDepartment:
    def initialize(self) -> str:
        return "ClothesDepartment: Ready!"

    def returnCost(self) -> str:
        return "ClothesDepartment: $3.99"


class ShoesDepartment:
    def initialize(self) -> str:
        return "ShoesDepartment: Ready!"

    # ...

    def returnCost(self) -> str:
        return "ShoesDepartment: $49.99"


def Bot(facade: ClothingStore) -> None:
    print(facade.handleOperations(), end="")


if __name__ == "__main__":
    ClothesDpt = ClothesDepartment()
    ShoesDpt = ShoesDepartment()
    facade = ClothingStore(ClothesDpt, ShoesDpt)
    Bot(facade)