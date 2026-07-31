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


def shealding_constant(z):

    shell = [
        [1,2],[2,8],[3,18],
        [4,32],[5,32],[6,18],
        [7,8]
    ]

    
    shells_config=[]
    for shells, capacity in shell:
        
    
        if z<=0:
            break

        electrons = min(z, capacity)
        shells_config.append((shells, electrons))

        z-=electrons
    length_n=len(shells_config)-1
    length_n1=len(shells_config)-2
    result=list( shells_config[length_n])
    result2=list( shells_config[length_n1])
    x,y=result[0],result[1]
    x1,y1=result2[0],result[1]
    first=(y-1)*0.35
    second=y1*0.85
    third=(z-(y+y1))*(-1)
    S=first+second+third
    Y = 0.000185 * (S**3) + 1.345975 * S - 3.12
    sigma = Y - 0.72 + 8.1 * (z // 3) - 1.2 * (z // 11) + 0.35 * (z - 1)
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
