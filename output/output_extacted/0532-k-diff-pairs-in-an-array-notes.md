## K-Diff Pairs in an Array

**Problem Link:** https://leetcode.com/problems/k-diff-pairs-in-an-array/description

**Problem Statement:**
- Input format: An array of integers `nums` and an integer `k`.
- Constraints: $1 \leq n \leq 10^5$, $1 \leq k \leq 10^9$, $-10^9 \leq nums[i] \leq 10^9$.
- Expected output format: The number of pairs of elements in the array that have a difference of `k`.
- Key requirements and edge cases to consider:
  - Handling duplicate pairs.
  - Considering pairs where the difference is exactly `k`.
- Example test cases with explanations:
  - Input: `nums = [3, 1, 4, 1, 5], k = 2`, Output: `2` (pairs: `(1, 3)`, `(3, 5)`).
  - Input: `nums = [1, 2, 3, 4, 5], k = 1`, Output: `4` (pairs: `(1, 2)`, `(2, 3)`, `(3, 4)`, `(4, 5)`).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all pairs of elements in the array and check if their difference is `k`.
- Step-by-step breakdown of the solution:
  1. Initialize a counter for the number of pairs with a difference of `k`.
  2. Iterate over the array using two nested loops to consider all pairs of elements.
  3. For each pair, calculate the absolute difference between the two elements.
  4. If the difference is `k`, increment the counter.
- Why this approach comes to mind first: It directly implements the problem statement without considering any optimizations.

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        int count = 0;
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (abs(nums[i] - nums[j]) == k) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because we are iterating over all pairs of elements using two nested loops.
> - **Space Complexity:** $O(1)$, excluding the input array, since we are only using a constant amount of space to store the count of pairs.
> - **Why these complexities occur:** The brute force approach has a high time complexity due to the nested loops, which results in checking all possible pairs of elements. The space complexity is low because we only need a single variable to keep track of the count.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using an unordered map to store the elements of the array as keys and their counts as values. This allows for efficient lookup of elements and their pairs.
- Detailed breakdown of the approach:
  1. Initialize an unordered map `countMap` to store the count of each element in the array.
  2. Initialize a set `uniquePairs` to store unique pairs of elements with a difference of `k`.
  3. Iterate over the array, and for each element, check if its pair (i.e., the element plus `k`) exists in the map.
  4. If the pair exists and `k` is not zero, add the pair to the set of unique pairs.
  5. If `k` is zero, we need to ensure we don't count duplicate pairs, so we only add the pair if the count of the element is more than one.
- Proof of optimality: This approach reduces the time complexity significantly by avoiding the need to check all pairs of elements. It achieves a time complexity of $O(n)$ because each element is processed once.

```cpp
class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_map<int, int> countMap;
        set<pair<int, int>> uniquePairs;
        
        for (int num : nums) {
            countMap[num]++;
        }
        
        for (auto& pair : countMap) {
            if (k == 0) {
                if (pair.second > 1) {
                    uniquePairs.insert({pair.first, pair.first});
                }
            } else {
                if (countMap.find(pair.first + k) != countMap.end()) {
                    uniquePairs.insert({min(pair.first, pair.first + k), max(pair.first, pair.first + k)});
                }
            }
        }
        
        return uniquePairs.size();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we are iterating over the array once to populate the map and then once more to find the pairs.
> - **Space Complexity:** $O(n)$, because in the worst case, we might store every element in the map and every pair in the set.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find all unique pairs with a difference of `k`. It does so by leveraging the efficiency of hash-based data structures for lookup and storage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hashing, efficient lookup, and avoiding duplicate pairs.
- Problem-solving patterns identified: Using data structures to optimize the solution, handling edge cases like `k == 0`.
- Optimization techniques learned: Reducing time complexity by avoiding nested loops, using sets to store unique pairs.
- Similar problems to practice: Other problems involving pairs or unique elements, such as finding pairs with a given sum or finding unique elements in an array.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to handle edge cases like `k == 0`, not checking for duplicate pairs.
- Edge cases to watch for: `k` being zero, duplicate elements in the array, negative numbers.
- Performance pitfalls: Using inefficient data structures or algorithms, not optimizing for the given constraints.
- Testing considerations: Thoroughly testing with different inputs, including edge cases and large datasets.