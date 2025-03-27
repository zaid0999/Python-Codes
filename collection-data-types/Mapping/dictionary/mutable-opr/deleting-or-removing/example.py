# Create Shoping Cart App 
# where perform operations like adding product, updating product 
# deleting product, view products 


cart={}
while True:
    print("1.Add Product")
    print("2.Update Product")
    print("3.Delete Product")
    print("4.View Products")
    print("5.Exit")

    opt=int(input("Enter Your Option "))
    if opt==1:
        pname=input("ProductName: ")
        if pname not in cart:
            qty=int(input("Qty: "))
            cart[pname]=qty
            print("Product Added to Cart")
        else:
            print(f'{pname} exists within cart')
    elif opt==2:
        pname=input("ProductName: ")
        if pname in cart:
            nqty=int(input("New Qty: "))
            cart[pname]=nqty
            print("Product Updated to Cart")
        else:
            print(f'{pname} not found within cart')
    elif opt==3:
        pname=input("ProductName: ")
        if pname in cart:
            del cart[pname]
            print("Product Deleted from Cart")
        else:
            print(f'{pname} Not found within Cart')
    elif opt==4:
        for pname,qty in cart.items():
            print(f'{pname}==>{qty}')
    elif opt==5:
        break
    else:
        print("invalid option")