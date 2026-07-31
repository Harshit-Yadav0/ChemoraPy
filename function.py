def aafbau(Z):

    orbitals = [
        ("1s", 2), ("2s", 2), ("2p", 6),
        ("3s", 2), ("3p", 6), ("4s", 2),
        ("3d", 10), ("4p", 6), ("5s", 2),
        ("4d", 10), ("5p", 6), ("6s", 2),
        ("4f", 14), ("5d", 10), ("6p", 6),
        ("7s", 2), ("5f", 14), ("6d", 10),
        ("7p", 6)
    ]

    configuration = []

    for orbital, capacity in orbitals:

        if Z <= 0:
            break

        electrons = min(Z, capacity)

        configuration.append((orbital, electrons))

        Z -= electrons

    return configuration


def shealding_constant(z,e):

    shells = [
        ("1",2),("2",8),("3",18),
        ("4",32),("5",32),("6",18),
        ("7",8)
    ]

    shells_config=[]
    for shells, capacity in shells:

        if z<=0:
            break

        electrons = min(z, capacity)
        shells_config.append((shells, electrons))

        z-=electrons

    if z<e:
        break

    else:
        if e==z:
            a=len(shells_config)
            b=a-1
            for i in range(b):
                check=shell

                #Not completed yet 
