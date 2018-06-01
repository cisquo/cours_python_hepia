# str -> bool
def est_numerique(s):
    if s[0] == '-':
        return s[1:].isnumeric()

    return s.isnumeric()

    # return s[1:].isnumeric() if s[0] == '-' else s.isnumeric()


# [str] -> [int]
def double(xs):
    ys = []
    for x in xs:
        if est_numerique(x):
            ys.append( 2*int(x) )
    return ys


# [str] -> bool
def verifier(xs):
    return len(xs) == len(double(xs))
