# Problem: Apply Discount Every n Orders - https://leetcode.com/problems/apply-discount-every-n-orders/description/

class Cashier:

    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.customers = 0
        self.discount_frequency = n
        self.discount = discount
        self.d = {products[i]: prices[i] for i in range(len(prices))}

    def getBill(self, product: List[int], amount: List[int]) -> float:
        # increment customer count
        self.customers += 1

        # check if customer is eligible for discount
        is_discounted = self.customers % self.discount_frequency == 0
        total_bill = 0

        for prod, amt in zip(product, amount):
            total_price = self.d[prod] * amt

            if is_discounted:
                total_price = total_price * ((100 - self.discount) / 100)
            
            total_bill += total_price
        
        return total_bill


        


# Your Cashier object will be instantiated and called as such:
# obj = Cashier(n, discount, products, prices)
# param_1 = obj.getBill(product,amount)