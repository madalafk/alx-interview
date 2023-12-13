#!/usr/bin/python3
'''
This module defines a function, minOperations, that computes
the fewest number of operations needed to result in exactly n
H characters.
'''

def minOperations(n):
    '''
    Computes the fewest number of operations needed to result
    in exactly n H characters.
    Parameters:
    n (int): The target number of H characters.
    Returns:
    int: The fewest number of operations needed.
    '''
    if not isinstance(n, int):
        return 0

    ops_count = 0
    clipboard = 0
    done = 1

    while done < n:
        if clipboard == 0:
            # Initialize (the first copy all and paste)
            clipboard = done
            done += clipboard
            ops_count += 2
        elif n - done > 0 and (n - done) % done == 0:
            # Copy all and paste
            clipboard = done
            done += clipboard
            ops_count += 2
