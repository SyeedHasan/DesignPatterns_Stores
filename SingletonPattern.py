class UserCartMeta(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]


class UserCart(metaclass=UserCartMeta):
    
    def __init__(self):
        super().__init__()
        self.var = 10
    
    def returnCartCost(self):
        self.var = self.var+10
        return f"User's Cart: ${self.var}"

        # ...


if __name__ == "__main__":
    cloth = UserCart()
    shoe = UserCart()
    
    if id(cloth) == id(shoe):
        print("UserCart works, both variables contain the same instance.")
    else:
        print("UserCart failed, variables contain different instances.")
        
    print(cloth.returnCartCost())
    print(shoe.returnCartCost())