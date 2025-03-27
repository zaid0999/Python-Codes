product={'monitor':5000,
         'keyboard':1000,
         'mouse':200}

pnames=product.keys()
print(pnames)
for pname in pnames:
    print(pname)

print("===================================")

product_prices=product.values()
print(product_prices)
for p in product_prices:
    print(p)

print("===================================")

prods=product.items()
print(prods)
for x in prods:
    print(x) 

    pn,p=x
    print(pn,p)