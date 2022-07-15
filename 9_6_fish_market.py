price_skumria = float(input())
price_caca = float(input())
kg_palamud = float(input())
kg_safrid = float(input())
kg_midi = int(input())
price_palamud = price_skumria * 1.6
price_safrid = price_caca * 1.8
price_midi = 7.5
total_price = price_palamud * kg_palamud + price_safrid * kg_safrid + price_midi * kg_midi
print(f"{total_price:.2f}")

