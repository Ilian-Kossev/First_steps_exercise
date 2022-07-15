price_per_kg_vegetables = float(input())
price_per_kg_fruit = float(input())
total_kg_vegetables = int(input())
total_kg_fruit = int(input())
final_price_vegetables_eur = price_per_kg_vegetables * total_kg_vegetables / 1.94
final_price_fruit_eur = price_per_kg_fruit * total_kg_fruit / 1.94
final_total_price_eur = final_price_vegetables_eur + final_price_fruit_eur
print(f"{final_total_price_eur:.2f}")
