import collections
from typing import List
from collections import OrderedDict


# ans.append(a.popitem()[0] if len(a.popitem()[0]) > 0 else "")
def reduce_directions(directions: List[str]) -> List[str]:
    # dic = collections.defaultdict(int)
    i = 0
    while i < len(directions):
        if i + 1 <= len(directions) - 1 and directions[i] == "SOUTH" and directions[i + 1] == "NORTH":
            directions.remove(directions[i])
            directions.remove(directions[i])
            i = -1
            continue
        if i + 1 <= len(directions) - 1 and directions[i] == "NORTH" and directions[i + 1] == "SOUTH":
            directions.remove(directions[i])
            directions.remove(directions[i])
            i = -1
        if i + 1 <= len(directions) - 1 and directions[i] == "EAST" and directions[i + 1] == "WEST":
            directions.remove(directions[i])
            directions.remove(directions[i])
            i = -1
        if i + 1 <= len(directions) - 1 and directions[i] == "WEST" and directions[i + 1] == "EAST":
            directions.remove(directions[i])
            directions.remove(directions[i])
            i = -1
        i += 1
    my_ordered_dict = OrderedDict.fromkeys(directions)
    my_list_without_duplicates = list(my_ordered_dict.keys())
    return my_list_without_duplicates if len(directions) > 0 else []
