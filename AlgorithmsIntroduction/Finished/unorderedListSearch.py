def search_list(lst, target):
    for item in lst:
        if item == target:
            return True
    return False

my_list = [ 23, 4, 61, 5, 128]
target = 129

if(search_list(my_list, target)):
    print(f"{target} is present in list")
else:
    print(f"{target} is not present in list")