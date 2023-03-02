# python3

#import sys
#import threading
#import numpy


#def compute_height(n, parents):
    # Write this function
#    max_height = 0
    # Your code here
#    return max_height


#def main():
    # implement input form keyboard and from files
    
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision
    
    # input number of elements
    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
#    pass

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
#sys.setrecursionlimit(10**7)  # max depth of recursion
#threading.stack_size(2**27)   # new thread will get stack of such size
#threading.Thread(target=main).start()
#main()
# print(numpy.array([1,2,3]))

def height(tree):
    depth_list = [1]*len(tree)
    for i, n in enumerate(tree):
        while n != -1:
            depth_list[i] += 1
            n = tree[n]
    #print(depth_list)
             
    return depth_list

inp=input()

if "I" in inp:
    parents = inp.strip()
if "F" in inp:
    file_name = input()
    
    if "a" not in file_name:
        f = open(file_name, "r")
        parents= f.read()

lst=[int(x) for x in parents.split(" ")]
del lst[0]

print(max(height(lst)))

