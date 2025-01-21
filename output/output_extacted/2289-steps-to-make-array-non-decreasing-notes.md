## Steps to Make Array Non-Decreasing
**Problem Link:** https://leetcode.com/problems/steps-to-make-array-non-decreasing/description

**Problem Statement:**
- Input: An integer array `nums`.
- Output: The minimum number of operations to make the array non-decreasing.
- Key Requirements:
  - An operation is defined as subtracting 1 from any element in the array.
  - The array should become non-decreasing after the operations, meaning for any two adjacent elements `a` and `b`, `a <= b`.
- Example Test Cases:
  - Input: `nums = [5,3,4,4,7,3,6,11,8,5,11]`
  - Output: `3`
  - Explanation: We can perform the following operations:
    1. Subtract 2 from the first element: `[3,3,4,4,7,3,6,11,8,5,11]`.
    2. Subtract 0 from the second element: `[3,3,4,4,7,3,6,11,8,5,11]`.
    3. Subtract 0 from the third element: `[3,3,4,4,7,3,6,11,8,5,11]`.
    We can see that after these operations, the array is non-decreasing.

### Brute Force Approach

**Explanation:**
- The initial thought process is to try all possible combinations of operations on the array.
- For each element in the array, we can try subtracting all possible values from it.
- We then check if the resulting array is non-decreasing.
- If it is, we count the number of operations performed.

```cpp
int minOperations(vector<int>& nums) {
    int minOps = INT_MAX;
    for (int i = 0; i < (1 << 30); i++) {
        vector<int> arr = nums;
        int ops = 0;
        for (int j = 0; j < arr.size(); j++) {
            if (j > 0 && arr[j] < arr[j-1]) {
                int diff = arr[j-1] - arr[j];
                arr[j] += diff;
                ops += diff;
            }
        }
        if (isNonDecreasing(arr)) {
            minOps = min(minOps, ops);
        }
    }
    return minOps;
}

bool isNonDecreasing(vector<int>& nums) {
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < nums[i-1]) {
            return false;
        }
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{30} \cdot n)$, where $n$ is the size of the input array. This is because we are trying all possible combinations of operations.
> - **Space Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we are creating a copy of the input array.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it tries all possible combinations of operations. The space complexity is relatively low because we only need to store a copy of the input array.

### Optimal Approach (Required)

**Explanation:**
- The key insight is that we only need to consider the minimum number of operations required to make the array non-decreasing.
- We can use a greedy approach to solve this problem. We iterate through the array from left to right, and for each element, we calculate the minimum number of operations required to make it greater than or equal to the previous element.
- We keep track of the minimum number of operations required so far.

```cpp
int minOperations(vector<int>& nums) {
    int ops = 0;
    for (int i = 1; i < nums.size(); i++) {
        if (nums[i] < nums[i-1]) {
            int diff = nums[i-1] - nums[i];
            ops += diff;
            nums[i] += diff;
        }
    }
    return ops;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we are iterating through the array once.
> - **Space Complexity:** $O(1)$, where $n$ is the size of the input array. This is because we are modifying the input array in place.
> - **Optimality proof:** The greedy approach is optimal because it always chooses the minimum number of operations required to make the array non-decreasing. This is because if we choose a larger number of operations, we would be making the array more non-decreasing than necessary, which would result in a larger number of operations overall.

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: greedy algorithms, dynamic programming.
- Problem-solving patterns identified: using a greedy approach to solve a problem.
- Optimization techniques learned: using a greedy approach to minimize the number of operations.
- Similar problems to practice: other problems that involve using a greedy approach to solve a problem.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not handling errors properly.
- Edge cases to watch for: empty input array, input array with a single element.
- Performance pitfalls: using a brute force approach to solve a problem, not optimizing the solution.
- Testing considerations: testing the solution with different input arrays, testing the solution with edge cases.