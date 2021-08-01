# for loop->

# writing the 99 bottles song! xD

for n in range(99, 0, -1):
    if n >= 2:
        print(n, "bottles of beer on the wall,", n, "bottles of beer.")
        if n == 2:
            print("Take one down and pass it around, 1 bottle of beer on the wall.")
        else:
            print("Take one down and pass it around,", n - 1, "bottles of beer on the wall.")
    elif n == 1:
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down and pass it around, no more bottles of beer on the wall.")
    print("---")
print("""No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall.\n""")
