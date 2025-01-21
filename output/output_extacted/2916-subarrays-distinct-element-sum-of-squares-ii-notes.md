## Subarrays with Distinct Element Sum of Squares II
**Problem Link:** https://leetcode.com/problems/subarrays-distinct-element-sum-of-squares-ii/description

**Problem Statement:**
- Input format and constraints: Given an array `nums` of length `n`, find the number of subarrays with distinct elements such that the sum of squares of these elements is less than or equal to `k`.
- Expected output format: The number of subarrays meeting the specified condition.
- Key requirements and edge cases to consider: 
  - The array `nums` can contain duplicate elements.
  - The sum of squares of elements in a subarray must not exceed `k`.
  - Subarrays can have varying lengths, from 1 to `n`.
- Example test cases with explanations:
  - For `nums = [1, 2, 3]` and `k = 10`, all subarrays have distinct elements and the sum of squares does not exceed `k`.
  - For `nums = [1, 2, 2]` and `k = 5`, subarrays with repeated elements should not be counted.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this, we can generate all possible subarrays, calculate the sum of squares for each, and check for distinct elements.
- Step-by-step breakdown of the solution:
  1. Generate all possible subarrays of `nums`.
  2. For each subarray, calculate the sum of squares of its elements.
  3. Check if all elements in the subarray are distinct.
  4. If the sum of squares does not exceed `k` and all elements are distinct, increment the count of valid subarrays.
- Why this approach comes to mind first: It's a straightforward, exhaustive method that considers all possibilities.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i; j < n; j++) {
            vector<int> subarray(nums.begin() + i, nums.begin() + j + 1);
            unordered_set<int> distinctElements(subarray.begin(), subarray.end());
            if (distinctElements.size() == subarray.size()) {
                long long sumOfSquares = 0;
                for (int num : subarray) {
                    sumOfSquares += (long long)num * num;
                }
                if (sumOfSquares <= k) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of `nums`. The outer two loops generate all subarrays ($O(n^2)$), and for each subarray, we potentially iterate over its elements to calculate the sum of squares and check for distinctness ($O(n)$).
> - **Space Complexity:** $O(n)$, for storing the subarray and the set of distinct elements.
> - **Why these complexities occur:** The brute force approach is inherently inefficient due to its exhaustive nature, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Utilize a sliding window approach to efficiently generate subarrays and a `unordered_set` to check for distinct elements. Additionally, maintain a running sum of squares to avoid recalculating for each subarray.
- Detailed breakdown of the approach:
  1. Initialize variables to keep track of the count of valid subarrays, the current sum of squares, and the start of the window.
  2. Iterate over `nums`, expanding the window to the right and updating the sum of squares.
  3. When a duplicate element is found or the sum of squares exceeds `k`, slide the window to the right by incrementing the start pointer and adjusting the sum of squares and the set of distinct elements accordingly.
- Proof of optimality: This approach minimizes the number of operations by avoiding the generation of all subarrays and the recalculation of sums for overlapping subarrays.

```cpp
int countSubarrays(vector<int>& nums, int k) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        unordered_set<int> distinctElements;
        long long sumOfSquares = 0;
        for (int j = i; j < n; j++) {
            if (!distinctElements.insert(nums[j]).second) break; // Break if not inserted (duplicate)
            sumOfSquares += (long long)nums[j] * nums[j];
            if (sumOfSquares > k) break; // Break if sum exceeds k
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the length of `nums`. The outer loop iterates over each element as a potential start of a subarray, and the inner loop expands the window to the right.
> - **Space Complexity:** $O(n)$, for storing the set of distinct elements in the current window.
> - **Optimality proof:** This is the best possible time complexity for this problem since we must at least consider each element as a potential start of a subarray, and for each start, we may need to consider all elements to its right.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window technique, use of `unordered_set` for efficient lookups and insertions.
- Problem-solving patterns identified: Breaking down complex problems into simpler, more manageable parts (e.g., considering each subarray individually).
- Optimization techniques learned: Avoiding redundant calculations (e.g., maintaining a running sum of squares), using data structures for efficient operations (e.g., `unordered_set` for distinct elements).

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases (e.g., empty input array, `k = 0`).
- Edge cases to watch for: Duplicate elements, sum of squares exceeding `k`, subarrays of length 1.
- Performance pitfalls: Using inefficient algorithms (e.g., brute force) for large inputs.
- Testing considerations: Thoroughly test with various inputs, including edge cases and large datasets, to ensure correctness and performance.