#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    total_score = sum(s * w for s, w in my_list)
    total_weight = sum(w for s, w in my_list)
    return total_score / total_weight
