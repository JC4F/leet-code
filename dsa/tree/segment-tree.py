"""
The building operation takes O(N) time
The query operation takes O(logN) time
Each update is performed in O(logN) time
"""

# python3 code for segment tree with sum
# range and update query
A = []
ST = []


def build(node, L, R):
    global A, ST

    # Leaf node where L == R
    if L == R:
        ST[node] = A[L]

    else:
        # Find the middle element to
        # split the array into two halves
        mid = (L + R) // 2

        # Recursively travel the
        # left half
        build(2 * node, L, mid)

        # Recursively travel the
        # right half
        build(2 * node + 1, mid + 1, R)

        # Storing the sum of both the
        # children into the parent
        ST[node] = ST[2 * node] + ST[2 * node + 1]


def update(node, L, R, idx, val):
    global A, ST

    # Find the lead node and
    # update its value
    if L == R:
        A[idx] += val
        ST[node] += val

    else:
        # Find the mid
        mid = (L + R) // 2

        # If node value idx is at the
        # left part then update
        # the left part
        if L <= idx and idx <= mid:
            update(2 * node, L, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, R, idx, val)

        # Store the information in parents
        ST[node] = ST[2 * node] + ST[2 * node + 1]


def query(node, tl, tr, l, r):
    global A, ST

    # If it lies out of range then
    # return 0
    if r < tl or tr < l:
        return 0

    # If the node contains the range then
    # return the node value
    if l <= tl and tr <= r:
        return ST[node]
    tm = (tl + tr) // 2

    # Recursively traverse left and right
    # and find the node
    return query(2 * node, tl, tm, l, r) + query(2 * node + 1, tm + 1, tr, l, r)


# Driver code
if __name__ == "__main__":
    n = 6
    A = [0, 1, 3, 5, -2, 3]

    # Create a segment tree of size 4*n
    ST = [0 for _ in range(4 * n)]

    # Build a segment tree
    build(1, 0, n - 1)
    print(f"Sum of values in range 0-4 are: {query(1, 0, n - 1, 0, 4)}")

    # Update the value at idx = 1 by
    # 100 ths becoming 101
    update(1, 0, n - 1, 1, 100)
    print("Value at index 1 increased by 100")
    print(f"sum of value in range 1-3 are: {query(1, 0, n - 1, 1, 3)}")

    # This code is contributed by rakeshsahni
