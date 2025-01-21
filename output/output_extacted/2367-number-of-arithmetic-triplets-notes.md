## Number of Arithmetic Triplets
**Problem Link:** https://leetcode.com/problems/number-of-arithmetic-triplets/description

**Problem Statement:**
- Input: An integer array `nums` and an integer `diff`.
- Constraints: `3 <= nums.length <= 10^4`, `0 <= nums[i] <= 10^4`, and `1 <= diff <= 10^4`.
- Expected Output: The number of arithmetic triplets in `nums` with difference `diff`.
- Key Requirements:
  - An arithmetic triplet is a sequence of three numbers where the difference between the first two numbers is the same as the difference between the last two numbers.
  - The sequence should be in ascending order and the numbers should be distinct.
- Example Test Cases:
  - `nums = [1, 2, 3, 4], diff = 1` returns `3` because there are three arithmetic triplets: `[1, 2, 3]`, `[1, 2, 4]`, and `[2, 3, 4]`.
  - `nums = [1, 2, 3, 4, 5], diff = 2` returns `2` because there are two arithmetic triplets: `[1, 3, 5]` and `[2, 4, 6]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to check every possible combination of three numbers in the array.
- We generate all possible triplets from the array and check if each triplet forms an arithmetic sequence with difference `diff`.
- This approach comes to mind first because it directly addresses the problem statement by checking all possibilities.

```cpp
int countArithmeticTriplets(vector<int>& nums, int diff) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (nums[j] - nums[i] == diff && nums[k] - nums[j] == diff) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the number of elements in `nums`, because we have three nested loops iterating over `nums`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and loop indices.
> - **Why these complexities occur:** The brute force approach is inherently inefficient due to the cubic time complexity from checking all possible triplets, making it impractical for large inputs.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to recognize that for any given number in the array, we can calculate the next two numbers that would form an arithmetic sequence with difference `diff`.
- We then check if these calculated numbers exist in the array.
- This approach is optimal because it reduces the time complexity by directly calculating potential triplets instead of checking all combinations.

```cpp
int countArithmeticTriplets(vector<int>& nums, int diff) {
    int count = 0;
    int n = nums.size();
    for (int i = 0; i < n; i++) {
        if (binary_search(nums.begin(), nums.end(), nums[i] + diff) &&
            binary_search(nums.begin(), nums.end(), nums[i] + 2 * diff)) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of elements in `nums`, because we use binary search for each element.
> - **Space Complexity:** $O(1)$, assuming the input array is already sorted or we can sort it in-place.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find all arithmetic triplets by leveraging binary search for efficient lookup.

---

### Final Notes
**Learning Points:**
- The importance of recognizing patterns and applying mathematical insights to reduce computational complexity.
- The use of binary search to efficiently find elements in a sorted array.
- The trade-off between brute force simplicity and optimal algorithmic efficiency.

**Mistakes to Avoid:**
- Not considering the constraints and characteristics of the input data.
- Failing to recognize opportunities for optimization, such as using binary search.
- Not validating the input and handling edge cases properly.

**Similar Problems to Practice:**
- Finding pairs or sequences with specific properties in arrays or lists.
- Optimizing algorithms for searching and matching patterns in data structures.
- Applying mathematical insights to solve computational problems efficiently.