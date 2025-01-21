## Single Number III

**Problem Link:** https://leetcode.com/problems/single-number-iii/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: Each element in `nums` appears twice except for two elements which appear only once. The size of `nums` is greater than 2.
- Expected output format: Return the two elements that appear only once in the form of a vector of two integers.
- Key requirements and edge cases to consider: The input array will have at least 3 elements. The two single numbers will not be the same.
- Example test cases:
  - Input: `nums = [1,2,1,3,2,5]`, Output: `[3,5]`.
  - Input: `nums = [-1,-2,-3,-4,-5]`, Output: `[-1,-2]` or `[-2,-1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Use a frequency counter to count the occurrences of each number in the array.
- Step-by-step breakdown of the solution:
  1. Initialize an empty hashmap `freq` to store the frequency of each number.
  2. Iterate through the array `nums`, for each number `num`, increment its frequency in `freq`.
  3. Initialize an empty vector `result` to store the numbers that appear only once.
  4. Iterate through the hashmap `freq`, for each number `num` with frequency 1, add it to `result`.
  5. Return `result`.
- Why this approach comes to mind first: It's straightforward and easy to implement.

```cpp
vector<int> singleNumber(vector<int>& nums) {
    unordered_map<int, int> freq;
    for (int num : nums) {
        freq[num]++;
    }
    vector<int> result;
    for (auto& pair : freq) {
        if (pair.second == 1) {
            result.push_back(pair.first);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in `nums`. We iterate through `nums` twice, once to count frequencies and once to find single numbers.
> - **Space Complexity:** $O(n)$ because in the worst case, we might need to store every number in the hashmap.
> - **Why these complexities occur:** The brute force approach requires iterating through the entire array to count frequencies and then again to find the single numbers, leading to linear time complexity. The space complexity is also linear because we use a hashmap to store the frequency of each number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use bitwise operations to find the two single numbers. The XOR operation (`^`) has the property that `a ^ a = 0` and `a ^ 0 = a`, so if we XOR all numbers in the array, the numbers that appear twice will cancel out, leaving the XOR of the two single numbers.
- Detailed breakdown of the approach:
  1. Calculate the XOR of all numbers in the array, `xor_all`.
  2. Find the rightmost set bit in `xor_all`, `rightmost_set_bit`.
  3. Partition the numbers in the array into two groups based on whether the rightmost set bit is set or not.
  4. Calculate the XOR of each group, `xor_group1` and `xor_group2`.
  5. `xor_group1` and `xor_group2` are the two single numbers.
- Why further optimization is impossible: This approach has the best possible time complexity for this problem because we must at least read the input array once.

```cpp
vector<int> singleNumber(vector<int>& nums) {
    int xor_all = 0;
    for (int num : nums) {
        xor_all ^= num;
    }
    int rightmost_set_bit = xor_all & -xor_all;
    int xor_group1 = 0, xor_group2 = 0;
    for (int num : nums) {
        if (num & rightmost_set_bit) {
            xor_group1 ^= num;
        } else {
            xor_group2 ^= num;
        }
    }
    return {xor_group1, xor_group2};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in `nums`. We iterate through `nums` twice.
> - **Space Complexity:** $O(1)$ because we use a constant amount of space to store the XOR results and the rightmost set bit.
> - **Optimality proof:** This approach is optimal because it only requires two passes through the input array, and each pass is necessary to find the two single numbers.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Bitwise operations, specifically XOR, and partitioning based on bit manipulation.
- Problem-solving patterns identified: Using XOR to find single numbers in an array, and partitioning to separate numbers based on certain properties.
- Optimization techniques learned: Reducing space complexity by using bitwise operations instead of a hashmap.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating the XOR of all numbers, or incorrectly partitioning the numbers.
- Edge cases to watch for: Empty input array, or input array with less than 3 elements.
- Performance pitfalls: Using a hashmap when the input array is very large, leading to high space complexity.
- Testing considerations: Test the function with different input arrays, including edge cases.