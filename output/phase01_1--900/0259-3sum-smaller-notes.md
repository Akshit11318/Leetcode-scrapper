## 3Sum Smaller

**Problem Link:** https://leetcode.com/problems/3sum-smaller/description

**Problem Statement:**
- Input format and constraints: Given an array of `n` integers `nums` and an integer `target`, find the number of triplets in the array that sum up to less than `target`.
- Expected output format: The function should return the count of such triplets.
- Key requirements and edge cases to consider: 
    - The input array can contain duplicates.
    - The input array can be empty or contain a single element.
    - The target value can be positive, negative, or zero.
- Example test cases with explanations:
    - Input: `nums = [-2,0,1,3]`, `target = 2`
      Output: `2`
      Explanation: There are two triplets whose sum is less than 2: `[-2,0,1]` and `[-2,0,3]` is not valid because it's greater than the target, but `[-2,0,1]` and `[-2,1,3]` is not valid because it's greater than the target, only `[-2,0,1]` is valid.
    - Input: `nums = []`, `target = 0`
      Output: `0`
      Explanation: There are no triplets in an empty array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The most straightforward approach to solve this problem is to generate all possible triplets from the given array and check if their sum is less than the target.
- Step-by-step breakdown of the solution:
    1. Generate all possible triplets from the array using three nested loops.
    2. For each triplet, calculate the sum of its elements.
    3. If the sum is less than the target, increment a counter to keep track of the number of such triplets.
- Why this approach comes to mind first: This approach is simple to understand and implement, but it has a high time complexity due to the three nested loops.

```cpp
int threeSumSmaller(vector<int>& nums, int target) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (nums[i] + nums[j] + nums[k] < target) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the input array. This is because we are using three nested loops to generate all possible triplets.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Why these complexities occur:** The time complexity is high because we are generating all possible triplets, which results in a cubic number of operations. The space complexity is constant because we are only using a fixed amount of space to store the count of triplets.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can sort the array first and then use a two-pointer technique to find the number of triplets that sum up to less than the target.
- Detailed breakdown of the approach:
    1. Sort the input array in ascending order.
    2. Iterate over the array with the first pointer `i`.
    3. For each `i`, use two pointers `j` and `k` starting from `i + 1` and `n - 1`, respectively.
    4. Move the `j` pointer to the right and the `k` pointer to the left based on the sum of the elements at the current positions of `i`, `j`, and `k`.
    5. If the sum is less than the target, increment the count by `k - j` because all elements between `j` and `k` will form a triplet with `i` that sums up to less than the target.
- Proof of optimality: This approach has a time complexity of $O(n^2)$, which is the best possible time complexity for this problem because we need to consider at least $n^2$ pairs of elements.

```cpp
int threeSumSmaller(vector<int>& nums, int target) {
    int count = 0;
    int n = nums.size();
    sort(nums.begin(), nums.end());
    for (int i = 0; i < n - 2; i++) {
        int j = i + 1;
        int k = n - 1;
        while (j < k) {
            if (nums[i] + nums[j] + nums[k] < target) {
                count += k - j;
                j++;
            } else {
                k--;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because we are using two nested loops to iterate over the array.
> - **Space Complexity:** $O(1)$, as we are not using any additional space that scales with the input size.
> - **Optimality proof:** The time complexity is optimal because we need to consider at least $n^2$ pairs of elements to find all triplets that sum up to less than the target.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, two-pointer technique, and iteration over the array.
- Problem-solving patterns identified: Using a two-pointer technique to find the number of triplets that sum up to less than the target.
- Optimization techniques learned: Sorting the array and using a two-pointer technique to reduce the time complexity from $O(n^3)$ to $O(n^2)$.
- Similar problems to practice: 3Sum, 3Sum Closest, and 4Sum.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the array before using the two-pointer technique.
- Edge cases to watch for: Empty array, array with a single element, and target value of zero.
- Performance pitfalls: Using a brute force approach with three nested loops, which results in a high time complexity.
- Testing considerations: Test the function with different input arrays and target values to ensure it works correctly for all edge cases.