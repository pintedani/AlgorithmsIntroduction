def count_values(list):
    counter = dict()
    for item in list:
        if item in counter.keys():
            counter[item] +=1
        else:
            counter[item] = 1
    return counter

# Usage example
color_list = ["red", "blue", "red", "green", "blue", "red", "red"]

color_counts = count_values(color_list)
print("Value counts: ", color_counts)
