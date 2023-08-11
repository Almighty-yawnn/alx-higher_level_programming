#!/usr/bin/python3
import sys
def pr_args():
    argv2 = sys.argv[1:]
    num_args = len(argv2)
    
    if num_args == 0:
        print(f"{num_args} arguments.")
        return
    elif num_args == 1:
        print(f"{num_args} argument:")
    else:
        print(f"{num_args} arguments:")
    for i in range(num_args):
        print(f"{i + 1}: {argv2[i]}.")
if __name__ == "__main__":
    pr_args()
