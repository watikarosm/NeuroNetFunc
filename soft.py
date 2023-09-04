layer_outputs = [4.8, 1.21, 2.385]
e = 2.71828182846

def soft(l):
    exp_values = []

    for output in layer_outputs:
        exp_values.append(e**output)
    return exp_values

ans = soft(layer_outputs)
print("ans: ", ans)

# normalizing to get rid of the negative values
norm_base = sum(ans)
norm_values = []

for value in ans:
    norm_values.append(value/norm_base)

print(norm_values)
print(sum(norm_values))
