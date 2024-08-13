class Market:
    def __init__(self, name: str, address: str) -> None:
        self.products = {}  
        self.balance = 0.0  
        self.name = name    
        self.address = address  

    def get_products_info(self) -> str:
        if not self.products:
            return "No products available."
        info = "Products in market:\n"
        for product, details in self.products.items():
            info += f"{product}: Price: {details['price']}, Quantity: {details['quantity']}\n"
        return info

    def add_product(self, product: str, price: float, quantity: int) -> None:
        if product in self.products:
            self.products[product]['price'] = price
            self.products[product]['quantity'] += quantity
        else:
            self.products[product] = {'price': price, 'quantity': quantity}

    def remove_product(self, product: str) -> None:
        if product in self.products:
            del self.products[product]

    def add_money(self, amount: float) -> None:
        self.balance += amount

    def sell(self, product: str, quantity: int) -> None:
        if product in self.products and self.products[product]['quantity'] >= quantity:
            total_price = self.products[product]['price'] * quantity
            self.products[product]['quantity'] -= quantity
            self.add_money(total_price)
        else:
            print("Product not available or insufficient quantity.")


market = Market("SuperMart", "123 Market St")
market.add_product("Apple", 1.5, 50)
market.add_product("Banana", 0.5, 100)
market.sell("Apple", 10)
print(market.get_products_info())
print(f"Balance: ${market.balance:.2f}")
market.remove_product("Banana")
print(market.get_products_info())
