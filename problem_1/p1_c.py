'''
Problem 1c

input: File containing an integer n followed by 2n lines containing the preferences of the n students and then the n hospitals (see README).
output: Dictionary mapping students to hospitals. 

TODO: Implement the Gale-Shapley algorithm to run in O(n^2).
'''

def stable_matching_1c(file) -> dict:
    n = 0
    doctors_pref = []
    hospitals_pref = []

    with open(file, "r") as f:
        n = int(f.readline())
        for _ in range(n):
            d_pref = f.readline().split()
            doctors_pref.append([int(x) for x in d_pref])

        for _ in range(n):
            h_pref = f.readline().split()
            hospitals_pref.append([int(x) for x in h_pref])


    pairs = {}
    free_hospitals = list(range(n)) # queue where all hospitals are free

    while free_hospitals:
        h = free_hospitals.pop() # first free hospital

        if not hospitals_pref[h]:
            continue

        d = hospitals_pref[h].pop(0) # that hospital chooses a doctor

        # if doctor hasn't been picked
        if d not in pairs:
            pairs[d] = h

        # if doctor has been picked
        else:
            current_h = pairs[d] # doctor's current hospital pick
            # h ranks higher than current_h
            h_idx = doctors_pref[d].index(h)
            current_h_idx = doctors_pref[d].index(current_h)
            if h_idx < current_h_idx:
                pairs[d] = h
                free_hospitals.append(current_h) # old hospital becomes free

            else:
                free_hospitals.append(h)

    
    return pairs






