mikl = float(input("Dollarov u Mikla "))
ivan = float(input("Dollarov u Ivana "))
min_sum = float(input("Minimalnaja summa investicij "))
def itog(mikl, ivan, min_sum):
    it = 0
    if mikl >= min_sum and ivan >= min_sum:
        it = 2
    elif mikl >= min_sum and ivan < min_sum:
        it = str("Mike")
    elif mikl < min_sum and ivan >= min_sum:
        it = str("Ivan")
    elif mikl < min_sum and ivan < min_sum and (mikl + ivan) >= min_sum:
        it = 1
    else:
        it = 0
    return it
print ("Mogut vlozitsja: ", itog(mikl, ivan, min_sum))
        

