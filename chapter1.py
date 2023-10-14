

l = {
    "Ahmed":2001,
    # "Sara":2000,
    "Lyla":2001,
    "Noha":2003,
}

def inner(ex):
    s_vallue =None
    S_ket= None
    for key,value in ex.items():
        if s_vallue is None or value < s_vallue:
            s_vallue = value
            S_ket = key
    return f'the samallest num is  {s_vallue} for {S_ket}'

print(inner(l))
