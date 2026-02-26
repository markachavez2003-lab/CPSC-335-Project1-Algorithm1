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

    # total distance traveled
    total_distance = 0

    for i in range(n):

        # Convert gallons at city i into drivable miles
        gas_miles = fuel[i] * mpg
        cost_miles = distance[i]
        current_miles += (gas_miles - cost_miles)

        
        if current_miles < 0:
            start_city = i + 1
            current_miles = 0

    # The problem guarantees there is exactly one valid starting city,
    # so start_city will be correct by the end of the loop
    return start_city

if __name__ == "__main__":
    # Sample input from the project description
    distances = [5,25,15,10,15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    
    # Expected output: 4
    print(preferred_starting_city(distances, fuel, mpg)) 
    

        
