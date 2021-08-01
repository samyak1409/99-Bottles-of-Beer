print('LYRICS of the song "99 Bottles of Beer" \n')

for n in range(99, 0, -1):  # start, stop, step

    if n > 1:
        print(f"{n} bottles of beer on the wall, {n} bottles of beer.")  # f-string (literal string interpolation)
        print(f"Take one down, pass it around, {n-1} {'bottles' if (n != 2) else 'bottle'} of beer on the wall.")

    else:  # (if n == 1) last bottle
        print("1 bottle of beer on the wall, 1 bottle of beer.")
        print("Take one down, pass it around, no more bottles of beer on the wall.")

    print('--')  # divider

print("""No more bottles of beer on the wall, no more bottles of beer.
Go to the store and buy some more, 99 bottles of beer on the wall...""")  # outro
