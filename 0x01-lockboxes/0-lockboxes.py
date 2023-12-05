#!/usr/bin/python3
'''
determines if all the boxes in n number of locked boxes  can be opened.
'''


def canUnlockAll(boxes):
    '''
    Checking if all boxes in a list of boxes containing the keys
    to other boxes can be unlocked given that the first
    box is unlocked.
    Return True if all boxes can be opened, else return False
    '''
    n = len(boxes)
    opened_boxes = set([0])
    un_opened_boxes = set(boxes[0]).difference(set([0]))
    while len(un_opened_boxes) > 0:
        boxIdx = un_opened_boxes.pop()
        if not boxIdx or boxIdx >= n or boxIdx < 0:
            continue
        if boxIdx not in opened_boxes:
            un_opened_boxes = un_opened_boxes.union(boxes[boxIdx])
            opened_boxes.add(boxIdx)
    return n == len(opened_boxes)
