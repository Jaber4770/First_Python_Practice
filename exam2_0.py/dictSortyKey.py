# 17. **Dictionary Sorting by Key and Value**
#    Given a dict:
#
#    * Print dict sorted by keys
#    * Print dict sorted by values
#

data = {
    "banana": 40,
    "apple": 10,
    "mango": 25,
    "orange": 15
}

def sortByKey(dct):
    sort_b_key = {}
    sort_b_value = {}
    
    sort_b_value = dict(sorted(dct.items(), key=lambda x: x[1]))
    sort_b_key = dict(sorted(dct.items()))
        
    print("sorted by key: ", sort_b_key)
    print("sorted by value: ", sort_b_value)

sortByKey(data)

