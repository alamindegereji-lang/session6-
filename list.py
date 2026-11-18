#original prices of 50 products
prices = [500, 1000, 1500, 1800, 2000,
    2500, 3000, 3500, 4000, 4500,
    600, 800, 1200, 1700, 1900,
    2200, 2800, 3200, 3800, 4200,
    700, 900, 1300, 1600, 1950,
    2100, 2600, 3100, 3600, 4100,
    550, 1100, 1400, 1750, 1850,
    2300, 2700, 3300, 3900, 4400,
    650, 950, 1250, 1550, 1980,
    2400, 2900, 3400, 3700,4800]
# empty list for updated prices 
updated_prices = []
# loop through the original price
for price in prices:
    if price < 2000:
        updated_price = price * 1.05
    else: 
        updated_price = price * 1.10
updated_prices.append(updated_price)



# Print the first 10 products

print("\nFIRST 10 PRODUCTS")

for old, new in zip(prices[:10], updated_prices[:10]):
    print(f"Old price: ₦{old:,.2f} | Updated price: ₦{new:,.2f}")


# Print the last 10 products

print("\nLAST 10 PRODUCTS")

for old, new in zip(prices[-10:], updated_prices[-10:]):
    print(f"Old price: ₦{old:,.2f} | Updated price: ₦{new:,.2f}")






