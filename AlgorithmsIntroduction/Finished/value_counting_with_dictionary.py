def count_values(list):
    #Implement method
    return 0

# Usage example
color_list = ["red", "blue", "red", "green", "blue", "red", "red"]

color_counts = count_values(color_list)
print("Value counts: ", color_counts)

#------------------


items = ["red", "blue", "red", "green", "blue", "red", "red"]

counter = dict()

for item in items:
    if item in counter.keys():
        counter[item] += 1
    else:
        counter[item] = 1
        
print(counter)