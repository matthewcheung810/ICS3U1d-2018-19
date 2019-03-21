def cigar_party(cigars, is_weekend):
    if (cigars >= 40) and (cigars <= 60):
        return(cigars == True)
    else:
        return(cigars == False)
    if is_weekend == True and cigar_party == True:
        return(cigar_party == True)
    else:
        return(cigar_party == false)

def main():
    cigars = int(input("How many cigars are there? "))
    is_weekend = input("Is it a weekend? True or False? ")
    cigar_party(cigars, is_weekend)

main()
