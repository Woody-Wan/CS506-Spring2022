from math import sqrt


def euclidean_dist(x, y):
    res = 0
    for i in range(len(x)):
        res += (x[i] - y[i])**2
    return res**(1/2)

def manhattan_dist(x, y):
    res = 0
    for i in range(x):
        res += x[i] + y[i]
    return res

def jaccard_dist(x, y):
    nominater =x.symmetric_difference(y)

    denominator = x.union(y)

    res = len(nominater) / len(denominator)

    return res

def cosine_sim(x, y):
    innerproduct = 0
    product_x = 0
    product_y = 0

    for i in range(len(x)):
        innerproduct += x[i] * y[i]
        product_x += x[i] * x[i]
        product_y += y[i] * y[i] 
    product_x = sqrt(product_x)
    product_y = sqrt(product_y)
    res = innerproduct / (product_x * product_y)
    return res

# Feel free to add more
