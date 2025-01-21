## Set Mismatch
**Problem Link:** https://leetcode.com/problems/set-mismatch/description

**Problem Statement:**
- Input: An array of integers `nums` containing `n + 1` integers where each integer is in the range `[1, n]`.
- Output: An array of two integers that represent the duplicate number and the missing number.
- Key requirements: The input array contains a duplicate and a missing number.
- Example test cases: 
    - Input: `nums = [1, 2, 2, 4]`
      Output: `[2, 3]`
    - Input: `nums = [1, 1]`
      Output: `[1, 2]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can use two passes through the array to find the duplicate and missing numbers. The first pass can count the occurrences of each number, and the second pass can identify the duplicate and missing numbers.
- Step-by-step breakdown of the solution:
    1. Create a frequency array `freq` of size `n + 1` to store the count of each number in the input array.
    2. Iterate through the input array and increment the corresponding count in the frequency array.
    3. Iterate through the frequency array to find the duplicate number (count greater than 1) and the missing number (count equal to 0).
- Why this approach comes to mind first: It is a straightforward solution that uses a frequency array to count the occurrences of each number.

```cpp
vector<int> findErrorNums(vector<int>& nums) {
    int n = nums.size();
    vector<int> freq(n + 1, 0);
    for (int num : nums) {
        freq[num]++;
    }
    int duplicate = 0, missing = 0;
    for (int i = 1; i <= n; i++) {
        if (freq[i] == 0) {
            missing = i;
        } else if (freq[i] > 1) {
            duplicate = i;
        }
    }
    return {duplicate, missing};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array, because we make two passes through the array.
> - **Space Complexity:** $O(n)$, because we use a frequency array of size $n + 1$.
> - **Why these complexities occur:** The time complexity is linear because we iterate through the input array twice, and the space complexity is linear because we use a frequency array to store the counts of each number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use the input array itself to mark the presence of each number, instead of using a separate frequency array.
- Detailed breakdown of the approach:
    1. Iterate through the input array and mark the presence of each number by negating the value at the corresponding index.
    2. Iterate through the input array again to find the duplicate number (index with a non-negative value) and the missing number (index with a positive value).
- Proof of optimality: This approach has the same time complexity as the brute force approach but uses less space because we do not need a separate frequency array.

```cpp
vector<int> findErrorNums(vector<int>& nums) {
    int n = nums.size();
    int duplicate = 0, missing = 0;
    for (int i = 0; i < n; i++) {
        int index = abs(nums[i]);
        if (nums[index - 1] < 0) {
            duplicate = index;
        } else {
            nums[index - 1] *= -1;
        }
    }
    for (int i = 0; i < n; i++) {
        if (nums[i] > 0) {
            missing = i + 1;
        }
    }
    return {duplicate, missing};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array, because we make two passes through the array.
> - **Space Complexity:** $O(1)$, because we use the input array itself to mark the presence of each number.
> - **Optimality proof:** This approach is optimal because it has the same time complexity as the brute force approach but uses less space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: frequency arrays, in-place marking.
- Problem-solving patterns identified: using the input array itself to reduce space complexity.
- Optimization techniques learned: reducing space complexity by using the input array.
- Similar problems to practice: problems involving frequency arrays and in-place marking.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not checking for duplicate numbers.
- Edge cases to watch for: empty input array, input array with only one element.
- Performance pitfalls: using unnecessary data structures, not optimizing space complexity.
- Testing considerations: testing with different input sizes, testing with different types of input data.