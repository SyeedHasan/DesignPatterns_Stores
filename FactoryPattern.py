from __future__ import annotations
from abc import ABC, abstractmethod


class OrderFactory(ABC):
    @abstractmethod
    def dispatchOrder(self):
        pass

    def some_operation(self) -> str:
        # Call the factory method to create a Product object.
        product = self.dispatchOrder()

        # Now, use the product.
        result = f"{product.returnCost()}"

        return result

class ClothOrderFactory(OrderFactory):

    def dispatchOrder(self) -> ClothOrder:
        return ClothOrder()


class ShoesOrderFactory(OrderFactory):
    def dispatchOrder(self) -> ShoesOrder:
        return ShoesOrder()


class Order(ABC):
    @abstractmethod
    def returnCost(self) -> str:
        pass

class ClothOrder(Order):
    def returnCost(self) -> str:
        return "Cost of Cloth: $3.99"


class ShoesOrder(Order):
    def returnCost(self) -> str:
        return "Cost of Shoes $2.99"


def client_code(creator: OrderFactory) -> None:
    print(f"Client: I'm not aware of the creator's class, but it still works.\n"
          f"{creator.some_operation()}", end="")


if __name__ == "__main__":
    print("Launching: ClothOrderFactory.")
    client_code(ClothOrderFactory())
    print("\n")

    print("Launching: ShoesOrderFactory.")
    client_code(ShoesOrderFactory())