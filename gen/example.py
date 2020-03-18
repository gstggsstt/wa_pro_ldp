import gen;

# 10 users and k = 3
d=gen.generator(10,3)
print(d.gen())

# 10 users and k = 3 and seed = 12345
d=gen.generator(10,3,12345)
print(d.gen())
