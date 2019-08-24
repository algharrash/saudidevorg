#day005 challange

#intiate the variables
x, y, z = "apple", "orange", "limon"

basket = x + y + z

#print the bsket before split
print("The basket items before spliting is:")
print(basket)

#first get the length of every item
item_x_len = len(x)
item_y_len = len(y)
item_z_len = len(z)

#split and print the list of item in basket
basket_items ="["
i = 0
basket_items = basket_items + basket[i:i+item_x_len] + ", "
i = item_x_len
basket_items = basket_items + basket[i:i+item_y_len] + ", "
i = i + item_y_len
basket_items = basket_items + basket[i:i+item_z_len] + "]"
print("The basket items after spliting is:")
print(basket_items)