## Contains Duplicate II
**Problem Link:** https://leetcode.com/problems/contains-duplicate-ii/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `k`.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= k <= 10^5`, and `0 <= nums[i] < 10^9`.
- Expected Output: A boolean indicating whether there exist two distinct indices `i` and `j` in the array such that `nums[i] == nums[j]` and `abs(i - j) <= k`.
- Key Requirements and Edge Cases:
  - The array can contain duplicate elements.
  - The condition `abs(i - j) <= k` must be satisfied for the two indices.
  - The function should return `true` as soon as it finds a pair satisfying the conditions.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through the array and compare each element with every other element that is within `k` distance.
- Step-by-step breakdown of the solution:
  1. Iterate through the array using a nested loop structure to compare each pair of elements.
  2. For each pair, check if the elements are equal and if their indices satisfy the condition `abs(i - j) <= k`.
  3. If such a pair is found, immediately return `true`.
  4. If no such pair is found after checking all elements, return `false`.

```cpp
bool containsNearbyDuplicate(vector<int>& nums, int k) {
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j <= i + k && j < n; j++) {
            if (nums[i] == nums[j]) {
                return true;
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(nk)$, where $n$ is the number of elements in the array. This is because for each element, we potentially check up to $k$ other elements.
> - **Space Complexity:** $O(1)$, not including the space required for the input array. This is because we only use a constant amount of space to store our indices and variables.
> - **Why these complexities occur:** The brute force approach involves checking every possible pair of elements within the distance $k$, leading to the $O(nk)$ time complexity. The space complexity is constant because we do not use any data structures that scale with the input size.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Use a hash set (or unordered set in C++) to keep track of the elements we have seen in the last `k` steps. This allows us to check if an element has been seen before in constant time.
- Detailed breakdown of the approach:
  1. Initialize an empty hash set.
  2. Iterate through the array. For each element:
     - Check if the element is already in the hash set. If it is, return `true`.
     - Add the element to the hash set.
     - If the size of the hash set exceeds `k`, remove the oldest element (the one that is no longer within `k` distance).
  3. If we finish iterating through the array without finding a duplicate within `k` distance, return `false`.

```cpp
bool containsNearbyDuplicate(vector<int>& nums, int k) {
    unordered_set<int> numSet;
    for (int i = 0; i < nums.size(); i++) {
        if (i > k) {
            numSet.erase(nums[i - k - 1]);
        }
        if (!numSet.insert(nums[i]).second) {
            return true;
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make a single pass through the array, and operations on the hash set (insertion and erasure) take constant time on average.
> - **Space Complexity:** $O(min(n, k))$, because in the worst case, our hash set will contain up to $k$ elements (when $k < n$), or up to $n$ elements (when $k \geq n$).
> - **Optimality proof:** This approach is optimal because it minimizes the time complexity by using a hash set to reduce the comparison time to constant, and it only makes a single pass through the array.

---

### Final Notes

**Learning Points:**
- Using hash sets to keep track of elements and reduce comparison time.
- The importance of considering the constraints of the problem (in this case, the distance `k`) when designing the solution.
- How to optimize a brute force solution by identifying and leveraging key insights (e.g., using a hash set to store recent elements).

**Mistakes to Avoid:**
- Not considering the constraints of the problem when designing the solution.
- Not optimizing the solution by leveraging data structures like hash sets.
- Not properly handling edge cases, such as when `k` is larger than the array size.