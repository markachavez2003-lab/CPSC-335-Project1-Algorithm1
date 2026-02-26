# CPSC 335 — Project 1 — Algorithm 1  
## Connecting Pairs of Persons

## Description
This program rearranges people seated in a row so that each person sits next to their partner.  
Each individual is represented by a unique integer ID, and couples are defined as consecutive pairs:

(0,1), (2,3), (4,5), (6,7), etc.

The algorithm scans the seating arrangement two seats at a time.  
If a person is not seated next to their correct partner, the program swaps the adjacent person with the correct partner.  
This process continues until all couples are seated together.

---

## Python Version Requirement ⚠️

This program requires **Python 3.12 or newer**.

Algorithm 1 uses the function `itertools.batched`, which was introduced in Python 3.12.  
Running the program on an older Python version will result in an error or crash.

To check your Python version:

```bash
python --versio
```


# CPSC 335 — Project 1 — Algorithm 2
## Preferred Starting City (Greedy Algorithm)


## Description:
This program implements a greedy algorithm to determine the preferred starting city in a circular road system.

Given:
- An array of distances between neighboring cities
- An array of fuel available in each city
- A value for miles per gallon (MPG)_

The algorithm determines the unique city index from which a car can start with an empty tank, refuel at each city,
and complete a full circular route without running out of fuel!!
The problem guarantees only one valid starting point (starting city).

The algorithm iterates through the list of cities only once.
- It starts by converting fuel into drivable miles. 
- Subtract the miles required to reach the next city.
- Track the remainding drivable miles.
- If the remaining miles become negative, reset the starting city candidate to the next city, reset the current_miles (miles you can drive).
