class Clothes():

    def operation(self) -> str:
        pass

class Trouser(Clothes):

    def operation(self) -> str:
        return "Order: Simple Trouser"

class AddOnDecorator(Clothes):

    _Clothes: Clothes = None

    def __init__(self, component: Clothes) -> None:
        self._component = component

    @property
    def component(self) -> str:
        return self._component

    def operation(self) -> str:
        return self._component.operation()


class CustomPrint(AddOnDecorator):
    
    def operation(self) -> str:
        return f"CustomPrint({self.component.operation()})"


class CustomEmbellishment(AddOnDecorator):
    
    def operation(self) -> str:
        return f"CustomEmbellishment({self.component.operation()})"

class CustomSize(AddOnDecorator):

    def operation(self) -> str:
        return f"CustomSize({self.component.operation()})"


def client_code(component: Clothes) -> None:
    print(f"RESULT: {component.operation()}", end="")

if __name__ == "__main__":

    simple = Trouser()
    print("Client: I've got a simple component:")
    client_code(simple)
    print("\n")


    decorator1 = CustomPrint(simple)
    decorator2 = CustomEmbellishment(simple)
    decorator3 = CustomSize(simple)
    print("Client: Now I've got a decorated component:")
    client_code(decorator3)