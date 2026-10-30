import random
from bitarray import bitarray
from math import e

n = 50  # Expected Number of Unique Items in S (n): 50
m = 500  # Bit Array Size (m): 500 bits
k = 2  # Number of Hash Functions (k): 2
p = 0.0 # Theoretical False Positive Rate
fp = 0 # Number of false positives
fpr = 0.0 # actual false positive rate
filterBitArray = bitarray(m)

S = {275, 591, 142, 803, 317, 650, 928, 489, 736, 110,
     543, 209, 876, 352, 604, 991, 168, 423, 705, 384,
     192, 537, 246, 811, 679, 400, 755, 331, 980, 215,
     502, 139, 888, 627, 360, 904, 447, 782, 125, 563,
     294, 851, 307, 693, 171, 468, 729, 395, 940, 582}

# Adds the 50 integer items in S to the filter by calculating h1(x) and
# h2(x), and setting the corresponding two bits in the array to 1.
def add(integer_item):
    for i in integer_item:
        filterBitArray[hash1(i)] = 1
        filterBitArray[hash2(i)] = 1

# Returns True if a new data item is potentially in the set (both bits at
# h1(x) and h2(x) are 1), or False otherwise.
def check(integer_item):
    if filterBitArray[hash1(integer_item)] & filterBitArray[hash2(integer_item)]:
        return True
    else:
        return False

def hash1(x):
    return (13*x)%500
def hash2(x):
    return (29*x+1)%500

if __name__ == "__main__":
    pExp = (-k*n)/m  # equation for calculating theoretical FPR exponent
    p = (1-e**pExp)**k # equation for calculating theoretical FPR

    print("Theoretical FPR: ", p)

    stream = random.sample(range(000, 999), m) # Stream simulation

    add(S) # adding set S to the bitarray

    for i in range(0, 499):
        if check(stream[i]):
            if stream[i] in S: # double check if false positive
                fp+=1

    fpr = fp/m # equation for actual FPR
    print("Actual FPR: ", fpr)

    # print(fp)
    # print(filter)
