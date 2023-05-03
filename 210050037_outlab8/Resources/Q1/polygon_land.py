MAX = 1000000.0
def cost(points, i, j, k):
    p1 = points[i]
    p2 = points[j]
    p3 = points[k]
    return p1*p2*p3
 
 
# A recursive function to find minimum
# cost of polygon triangulation
# The polygon is represented by points[i..j].
def mTC(points, i, j):
     
    # There must be at least three points between i and j
    # (including i and j)
    if (j < i + 2):
        return 0
         
    # Initialize result as infinite
    res = MAX
     
    # Find minimum triangulation by considering all
    for k in range(i + 1, j):
        res = min(res, (mTC(points, i, k) + \
                        mTC(points, k, j) + \
                        cost(points, i, k, j)))
     
    return res
def minCost(values):
    r"""
        This function accepts list
        It returns the result as cost.
    """
    return mTC(values,0,len(values)-1)
    pass


if __name__ == "__main__":
    import argparse
    CLI=argparse.ArgumentParser()
    CLI.add_argument("--values",  nargs="*",  type=int, default=[1, 2, 3])
    args = CLI.parse_args()
    print("values: %r" % args.values)
    cost = minCost(args.values)
    print(cost)