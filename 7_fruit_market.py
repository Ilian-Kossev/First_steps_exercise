strawberry_price = float(input())
bananas = float(input())
oranges = float(input())
raspberries = float(input())
strawberries = float(input())
raspberry_price = strawberry_price / 2
orange_price = raspberry_price * 0.6
banana_price = raspberry_price * 0.2
money_needed = raspberry_price * raspberries\
               + orange_price * oranges \
               + banana_price * bananas\
               + strawberry_price * strawberries
print(money_needed)
