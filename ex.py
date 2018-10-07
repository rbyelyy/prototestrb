import ex_pb2

y = ex_pb2.Bottle(note='Ahoy!')

with open('ex.pb', 'wb') as f:
    f.write(y.SerializeToString())

with open('ex.pb', 'rb') as f:
    x = ex_pb2.Bottle().FromString(f.read())

print(x)