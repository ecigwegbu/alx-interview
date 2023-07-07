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

    # prelim argument check
    if not type(boxes) == list:
        exit(98)
    if boxes == []:
        return True

    # init list of locked boxes:
    boxKeys = []
    keyIndex = 0
    boxKeys += boxes[keyIndex]
    openBoxes = [0]

    found = True  # True if a box key is found in the box of keys in a round
    while len(openBoxes) != len(boxes) and (found is True):
        found = False  # reset for the round
        for key in range(len(boxes)):  # loop over all boxes
            # search for matching key for box:
            if key in openBoxes:
                continue  # found before, so skip
            if key in boxKeys:
                boxKeys += boxes[key]  # update list of available keys
                openBoxes.append(key)  # update list of opened boxes
                found = True  # key forund in this round
                break  # start over
        if found is False:  # ie we have a round in which no key is found
            return False
    if len(openBoxes) == len(boxes):  # ie we opened all boxes
        return True

    return False
