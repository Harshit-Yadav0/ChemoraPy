def aafbau(Z):

    orbitals = [
        ["1s", 2], ["2s", 2], ["2p", 6],
        ["3s", 2], ["3p", 6], ["4s", 2],
        ["3d", 10], ["4p", 6], ["5s", 2],
        ["4d", 10], ["5p", 6], ["6s", 2],
        ["4f", 14], ["5d", 10], ["6p", 6],
        ["7s", 2], ["5f", 14], ["6d", 10],
        ["7p", 6]
    ]

    configuration = []

    for orbital, capacity in orbitals:

        if Z <= 0:
            break

        electrons = min(Z, capacity)

        configuration.append((orbital, electrons))

        Z -= electrons

    return configuration


def shielding_constant(Z):
    """
    Calculates the Slater shielding constant (sigma) for the outermost electron
    of a neutral atom with atomic number Z using Slater's rules.
    """
    if Z <= 0:
        return 0.0

    # 1. Standard Aufbau order to determine the electronic configuration
    aufbau_orbitals = [
        ("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2),
        ("3d", 10), ("4p", 6), ("5s", 2), ("4d", 10), ("5p", 6), ("6s", 2),
        ("4f", 14), ("5d", 10), ("6p", 6), ("7s", 2), ("5f", 14), ("6d", 10), ("7p", 6)
    ]

    # Fill subshells based on Z
    remaining = Z
    subshells = [] # List of elements like ['1s', 2]
    for orb, cap in aufbau_orbitals:
        if remaining <= 0:
            break
        e = min(remaining, cap)
        subshells.append([orb, e])
        remaining -= e

    # Identify the outermost subshell containing the target electron
    last_orb, last_electrons = subshells[-1]
    n_val = int(last_orb[0])
    l_val = last_orb[1]

    # Deduct the target electron itself from the count
    subshells[-1][1] -= 1

    sigma = 0.0

    # 2. Calculate shielding based on Slater's specific rules
    for orb, e in subshells:
        if e == 0:
            continue
        
        n_i = int(orb[0])
        l_i = orb[1]

        # Case A: Outermost electron is in an s or p orbital
        if l_val in ('s', 'p'):
            if n_i == n_val:
                # Exception for 1s shell
                same_shell_factor = 0.30 if n_val == 1 else 0.35
                sigma += e * same_shell_factor
            elif n_i == n_val - 1:
                sigma += e * 0.85
            elif n_i < n_val - 1:
                sigma += e * 1.00

        # Case B: Outermost electron is in a d or f orbital
        elif l_val in ('d', 'f'):
            if n_i == n_val and l_i == l_val:
                sigma += e * 0.35
            elif n_i < n_val or (n_i == n_val and l_i != l_val):
                # All lower groups shield by 1.00
                sigma += e * 1.00

    return round(sigma, 4)

# Example verification:
# Carbon (Z=6): Configuration 1s2 2s2 2p2. Outermost (2p) has 3 other electrons in n=2, 2 in n=1.
# Sigma = (3 * 0.35) + (2 * 0.85) = 1.05 + 1.70 = 2.75
#print(f"Carbon (Z=6) Sigma: {shielding_constant(6)}") 


def mole(n,g,m):
    moles=0
    if n!=0:
        Na=6.022*10**23
        moles=n/Na

    elif n==0:
        moles=g/m

    return moles

def ntp(v):
    moles=v/22.4
    return moles

def stp(v):
    moles=v/22.7
    return moles

def density(x,y):
    dense=x/y
    return dense

def vepdens(M):
    result=M/2
    return result

def limitreact(m1,c1,m2,c2):
    sa1=m1/c1
    sa2=m2/c2
    if sa1>sa2:
        result=[sa2,"2nd option"]
        return result
        #still working





def Zeff(Z):
    s=shielding_constant(Z)
    result=Z-s
    return result

def IEnthalpy(Z):
    Zef=Zeff(Z)
    config=aafbau(Z)
    last=len(config)-1
    new=config[last]
    x,e=new[0],int(new[1])
    n,l=int(x[0]),x[1]
    
    H=1312*((Zef**2)/n**2)

    return H
