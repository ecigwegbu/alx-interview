#!/usr/bin/python3

"""Lock-boxes.

You have n number of locked boxes in front of you.
Each box is numbered sequentially from 0 to n-1 and each box may contain keys
to other boxes.

TODO: Write a method that determines if all the boxes can be opened.

TODO: Write function def can_unlock_all(boxes)

- the parameter boxes is a list of lists.
- a key with the same number as a box opens that box
- assume all keys will be positive integers
- there can be keys that do not have boxes
- the first box boxes[0] is unlocked
- return True if all boxes can be opened, else return False
"""


# def canUnlockAll(boxes: list) -> bool:
def canUnlockAll(boxes):
    """A function which determines whether the boxes within the list passed
    as a parameter can be unlocked, using keys procured from prior unlocked
    boxes."""
    # type hinting - function takes list, returns boolean

    # initialising variables
    num_unlocked_boxes = 1
    list_of_keys = []  # list of keys starts off empty

    list_of_unlocked_boxes = []

    list_of_keys.extend(boxes[0])  # first box is unlocked
    list_of_unlocked_boxes.extend([boxes[0]])  # first box is unlocked

    box_nums = []

    while num_unlocked_boxes <= len(boxes):

        for box_num, box in enumerate(boxes):
            if box_num in list_of_keys:
                # key can be used to unlock box
                # add new keys from newly unlocked box to list of keys
                list_of_keys.extend(boxes[box_num])
                list_of_keys.sort()
                list_of_keys = list(set(list_of_keys))
                if box not in list_of_unlocked_boxes:
                    # update number and list of unlocked boxes
                    num_unlocked_boxes += 1
                    list_of_unlocked_boxes.append(box)

            for key in box:
                if key == box_num and key not in list_of_keys:
                    # box cannot be unlocked
                    return False

        if num_unlocked_boxes == len(boxes):
            # all boxes have been unlocked
            return True
