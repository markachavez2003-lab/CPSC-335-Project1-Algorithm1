#Marco Chavez
#marco_chavez@csu.fullerton.edu
#Richard Le
#richard.le@csu.fullerton.edu
#Arman Madatyan 
#armanmadatyan@csu.fullerton.edu

# Algorithm 2: Preffered Stating City (Greedy)

def preferred_stating_city(distances, fuel, mpg):
    """
    distances[i] -> miles from city i to city i+1 (circular)
    fuel[i]      -> gallons available at city i
    mpg          -> miles per gallon

    Returns the index of the preferred starting city.
    """

    #number of cities
    n = len(distances)

    # candidate for starting city
    start_city = 0

    # drivable miles from current start
    current_miles = 0


    # Loops tyhrough each city once
    for i in range(n):

        # Convert gallons at city i into drivable miles
        gas_miles = fuel[i] * mpg

        cost_miles = distances[i]       # miles needed to get to the next city

        net_miles = (gas_miles - cost_miles)   # Net gain miless we gain or lose after visiting city i

        current_miles += net_miles       # Update the current miles we have after visiting city i net_miles       # Update the current miles we have after visiting city i

        # if we cannot reach the next city from the current start, we need to change our starting city
        if current_miles < 0:
            # Current start_city fails
            # Next City (i+1) becomes the new candidate for starting city
            start_city = i + 1

            # Reset current miles for the new candidate starting city
            current_miles = 0

    # The problem guarantees there is exactly one valid starting city,
    # so start_city will be correct by the end of the loop
    return start_city

if __name__ == "__main__":
    # Sample input from the project description
    distances = [5,25,15,10,15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    
    result = preferred_stating_city(distances, fuel, mpg)
    # Expected output: 4
    print("Preferred Starting City Index:", result) 
    

        
