## Maximum Candies Allocated to K Children
**Problem Link:** https://leetcode.com/problems/maximum-candies-allocated-to-k-children/description

**Problem Statement:**
- Input format: `candies` (an array of integers representing the number of candies each child has), `k` (an integer representing the number of children to allocate candies to), `x` (an integer representing the number of candies to allocate to each child)
- Constraints: $1 \leq k \leq n \leq 10^4$, $1 \leq x \leq 10^4$, $1 \leq candies_i \leq 10^4$
- Expected output: The maximum number of candies that can be allocated to `k` children, with each child receiving `x` candies
- Key requirements: Find the maximum number of candies that can be allocated without exceeding the number of candies each child has
- Edge cases: Handle cases where `k` is equal to the number of children, or where `x` is greater than the number of candies each child has

**Example Test Cases:**
- `candies = [1, 2, 3, 4, 5], k = 3, x = 2` -> Output: `3`
- `candies = [1, 1, 1, 1, 1], k = 5, x = 2` -> Output: `0`

---

### Brute Force Approach
**Explanation:**
- Sort the `candies` array in ascending order
- Iterate over the sorted array, starting from the smallest number of candies
- For each child, check if they have at least `x` candies
- If they do, allocate `x` candies to the child and increment the count of allocated candies
- Continue this process until `k` children have been allocated candies or until there are no more children with at least `x` candies

```cpp
int maxCandiesAllocated(vector<int>& candies, int k, int x) {
    sort(candies.begin(), candies.end());
    int allocated = 0;
    for (int i = 0; i < candies.size() && allocated < k; i++) {
        if (candies[i] >= x) {
            allocated++;
        }
    }
    return allocated;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation, where $n$ is the number of children
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the allocated count
> - **Why these complexities occur:** The sorting operation dominates the time complexity, while the space complexity is constant because we only use a single variable to store the allocated count

---

### Optimal Approach (Required)
**Explanation:**
- Sort the `candies` array in ascending order
- Use a binary search approach to find the maximum number of candies that can be allocated to `k` children
- For each possible number of candies, check if it is possible to allocate that many candies to `k` children
- If it is possible, update the maximum number of candies that can be allocated

```cpp
int maxCandiesAllocated(vector<int>& candies, int k, int x) {
    sort(candies.begin(), candies.end());
    int low = 0, high = candies.size();
    while (low < high) {
        int mid = low + (high - low) / 2;
        int allocated = 0;
        for (int i = 0; i < candies.size(); i++) {
            if (candies[i] >= x) {
                allocated++;
            }
        }
        if (allocated >= k) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation and the binary search, where $n$ is the number of children
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the allocated count
> - **Optimality proof:** This approach is optimal because it uses a binary search to find the maximum number of candies that can be allocated, which reduces the number of iterations required

---

### Final Notes

**Learning Points:**
- The importance of sorting and binary search in solving problems involving arrays and counts
- The use of binary search to find the maximum number of candies that can be allocated
- The importance of considering edge cases and constraints in the problem statement

**Mistakes to Avoid:**
- Not considering the constraints on the input values, such as the range of `k` and `x`
- Not handling edge cases, such as when `k` is equal to the number of children or when `x` is greater than the number of candies each child has
- Not using a binary search approach to find the maximum number of candies that can be allocated, which can lead to inefficient solutions.