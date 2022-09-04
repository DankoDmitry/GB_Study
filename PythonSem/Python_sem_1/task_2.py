for X in range(0,2):
    for Y in range(0,2):
        for Z in range(0,2):
            print("{} {} {}".format(X, Y, Z))
            print(not (X or Y or Z) == (not X and not Y and not Z))