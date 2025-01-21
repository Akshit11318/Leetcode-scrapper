## Valid Triangle Number

**Problem Link:** https://leetcode.com/problems/valid-triangle-number/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Output: The number of unique triplets `(i, j, k)` such that `i < j < k` and `nums[i] + nums[j] > nums[k]`, `nums[i] + nums[k] > nums[j]`, and `nums[j] + nums[k] > nums[i]`.
- Key requirements and edge cases to consider: The input array `nums` can contain duplicate elements, and the indices `i`, `j`, and `k` must be distinct.
- Example test cases with explanations:
  - For `nums = [2,2,3,4]`, there are 3 unique triplets that satisfy the conditions: `(0, 1, 2)`, `(0, 1, 3)`, and `(1, 2, 3)`.
  - For `nums = [4,2,3,4]`, there are 4 unique triplets that satisfy the conditions: `(0, 2, 3)`, `(0, 3, 1)`, `(1, 2, 3)`, and `(2, 3, 1)`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check all possible triplets of indices `(i, j, k)` and verify if the corresponding elements satisfy the triangle inequality conditions.
- Step-by-step breakdown of the solution:
  1. Generate all possible triplets of indices `(i, j, k)` such that `i < j < k`.
  2. For each triplet, check if the elements `nums[i]`, `nums[j]`, and `nums[k]` satisfy the conditions `nums[i] + nums[j] > nums[k]`, `nums[i] + nums[k] > nums[j]`, and `nums[j] + nums[k] > nums[i]`.
  3. Count the number of triplets that satisfy the conditions.

```cpp
int triangleNumber(vector<int>& nums) {
    int n = nums.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (nums[i] + nums[j] > nums[k] && nums[i] + nums[k] > nums[j] && nums[j] + nums[k] > nums[i]) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array `nums`. This is because we have three nested loops that iterate over the array.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the count of valid triplets.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it checks all possible triplets of indices, resulting in a cubic number of iterations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: We can use a two-pointer technique to reduce the time complexity.
- Detailed breakdown of the approach:
  1. Sort the input array `nums` in ascending order.
  2. Iterate over the array and fix the largest side of the triangle, which is `nums[k]`.
  3. Use two pointers, `i` and `j`, to find the number of pairs `(nums[i], nums[j])` such that `nums[i] + nums[j] > nums[k]`.
  4. The number of valid triplets is the sum of the counts of such pairs for each `k`.

```cpp
int triangleNumber(vector<int>& nums) {
    int n = nums.size();
    sort(nums.begin(), nums.end());
    int count = 0;
    for (int k = 2; k < n; k++) {
        int i = 0, j = k - 1;
        while (i < j) {
            if (nums[i] + nums[j] > nums[k]) {
                count += j - i;
                j--;
            } else {
                i++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array `nums`. This is because we have two nested loops: one for iterating over the array and fixing the largest side, and another for finding the number of pairs using the two-pointer technique.
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the count of valid triplets and the indices.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity from $O(n^3)$ to $O(n^2)$ by using the two-pointer technique, which is the best possible time complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: two-pointer technique, sorting, and iteration.
- Problem-solving patterns identified: reducing time complexity by using efficient algorithms and data structures.
- Optimization techniques learned: using sorting and two-pointer technique to reduce time complexity.
- Similar problems to practice: other problems that involve finding valid triplets or pairs in an array, such as the 3Sum problem.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, such as an empty input array or duplicate elements.
- Edge cases to watch for: handling duplicate elements and ensuring that the indices `i`, `j`, and `k` are distinct.
- Performance pitfalls: using brute force approaches or inefficient algorithms that result in high time complexities.
- Testing considerations: testing the solution with different input arrays, including edge cases and large inputs.