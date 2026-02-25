#Marco Chavez
#marco_chavez@csu.fullerton.edu

from itertools import batched
    
couples = [2,4,7,5,1,0,3,6]


def pairing_alg():

    #swap counter
    num_swaps = 0

    #The following should loop between each pair searching for correct match
    for i in range(0, len(couples),2):
        seat = couples[i]
        

        #Checks for the correct partenr by changing the last bit of the seat number
        partner = seat ^ 1

        if couples[i+1] != partner:

            #swaps correct partner since the match above failed
            partner_row = couples.index(partner)
            couples[i+1], couples[partner_row] = couples[partner_row], couples[i+1]
            
            #counts number of swaps made
            num_swaps+=1
            
    #formats the pairs for display
    paired_couples = list(batched(couples, 2))
    print(f" Total swaps: {num_swaps} swaps\n  Final seating:{paired_couples}")    
            
print(f"Orignal Seating: {couples}")
pairing_alg()   
        


