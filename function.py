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


def shealding_constant(Z):
    """Calculate the Slater shielding constant (sigma) for the outermost electron
    of a neutral atom with atomic number Z using Slater's rules.

    Returns the shielding constant sigma (float).
    """
    if Z <= 0:
        return 0.0

    # Orbital order matches aafbau so we can build the subshell configuration
    orbitals = [
        ["1s", 2], ["2s", 2], ["2p", 6],
        ["3s", 2], ["3p", 6], ["4s", 2],
        ["3d", 10], ["4p", 6], ["5s", 2],
        ["4d", 10], ["5p", 6], ["6s", 2],
        ["4f", 14], ["5d", 10], ["6p", 6],
        ["7s", 2], ["5f", 14], ["6d", 10],
        ["7p", 6]
    ]

    # Build subshell filling without mutating the caller's Z
    remaining = Z
    subshells = []
    for orb, cap in orbitals:
        if remaining <= 0:
            break
        e = min(remaining, cap)
        subshells.append((orb, e))
        remaining -= e

    # Outermost occupied subshell
    last_orb, last_electrons = subshells[-1]

    # parse principal quantum number and orbital type (assumes format like '3p', '4f')
    try:
        n_val = int(last_orb[0])
        l_val = last_orb[1]
    except Exception:
        return 0.0

    sigma = 0.0

    # Slater's rules:
    # - For s/p valence electrons:
    #     same shell: 0.35 each (0.30 for 1s other electron)
    #     (n-1) shell: 0.85 each
    #     lower shells: 1.00 each
    # - For d/f valence electrons:
    #     same shell: 0.35 each (exclude the electron itself)
    #     lower shells: 1.00 each
    if l_val in ("s", "p"):
        same_shell_factor = 0.30 if n_val == 1 and l_val == "s" else 0.35
        for orb, e in subshells:
            n_i = int(orb[0])
            if n_i == n_val:
                if orb == last_orb:
                    sigma += (e - 1) * same_shell_factor
                else:
                    sigma += e * same_shell_factor
            elif n_i == n_val - 1:
                sigma += e * 0.85
            elif n_i < n_val - 1:
                sigma += e * 1.00
    else:
        # d or f valence electron
        for orb, e in subshells:
            n_i = int(orb[0])
            if n_i == n_val:
                if orb == last_orb:
                    sigma += (e - 1) * 0.35
                else:
                    sigma += e * 0.35
            elif n_i < n_val:
                sigma += e * 1.00

    return sigma
    else:
        # d or f valence electron: all electrons in shells lower than n_val
        # contribute 1.00; electrons in the same shell contribute 0.35 (exclude the electron itself)
        for orb, e in subshells:
            n_i = int(orb[0])
            if n_i == n_val:
                if orb == last_orb:
                    sigma += (e - 1) * 0.35
                else:
                    sigma += e * 0.35
            elif n_i < n_val:
                sigma += e * 1.00

    return sigma
# the function of slaters rule is not working correctly


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
    return ntp

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
