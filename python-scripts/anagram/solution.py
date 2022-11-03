def main(bigstr, smallstr):
    bigstr = list(bigstr.strip())
    for l_ in list(smallstr.strip()):
        if l_ not in bigstr:
            return False
        del bigstr[bigstr.index(l_)]
    return True
