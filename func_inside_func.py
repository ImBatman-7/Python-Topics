def to_power(x):
    def calc_power(n):
        return n**x
    return calc_power


s = to_power(3)
print(s(5))        