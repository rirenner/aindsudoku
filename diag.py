cols = '123456789'
rows = 'ABCDEFGHI'

def combine(a,b):
    result = list()
    for (x, y) in zip(a, b):
        result.append(x+y)
    return result

# diag = cross(rows, cols)
diag_top = combine(rows, cols)
diag_down = combine(rows, cols[::-1])

print("top down {}".format(diag_top))
print("down to top: {}".format(diag_down))
