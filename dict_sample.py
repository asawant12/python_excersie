keys = ["home_key", "2nd_home_key", "bike_key", "car_key","shop_key", "safe_key"]

for key in keys:
  if key == "safe_key":
    print("open the safe")
  else:
    print("thi is not safe key")

key_bunch = {
  "home_key" : "key1", 
  "2nd_home_key" : "key2", 
  "bike_key": "key3", 
  "car_key" : "key4",
  "shop_key": "key5", 
  "safe_key" : "key6"
}

print(key_bunch["safe_key"])

food_item = {
  1 : "pizza",
  2: "vadapav",
  3: "burger"
}
item = int(input("Enter your order:"))
print("You ordered:{0}".format(food_item[item]))

for key_label in key_bunch.keys():
  print(key_label)

for key_label in key_bunch.values():
  print(key_label)

for key_label,key_val in key_bunch.items():
  print(key_label+" " + key_val)
