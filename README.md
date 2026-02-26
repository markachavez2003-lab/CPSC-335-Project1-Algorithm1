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
python --version
