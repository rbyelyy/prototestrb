import ex_pb2

my_bottle = ex_pb2.Bottle(note='Ahoy!')

with open('my_bottle.pb', 'wb') as f:
    f.write(my_bottle.SerializeToString())

with open('my_bottle.pb', 'rb') as f:
    x = ex_pb2.Bottle().FromString(f.read())

print(x)