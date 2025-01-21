## Sum of Consecutive Subsequences
**Problem Link:** https://leetcode.com/problems/sum-of-consecutive-subsequences/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The length of `nums` is between 1 and 100, and each integer is between 1 and 100.
- Expected output format: The sum of all subsequences of consecutive numbers in the given array.
- Key requirements and edge cases to consider: Handling arrays with duplicate numbers, arrays with negative numbers, and empty arrays.
- Example test cases with explanations: For `nums = [2, 3, 6, 7]`, the subsequences of consecutive numbers are `[2, 3]`, `[6, 7]`, so the sum is `2 + 3 + 6 + 7 = 18`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible subsequences and check if they are consecutive.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the given array.
  2. For each subsequence, check if the numbers are consecutive.
  3. If the numbers are consecutive, add them to the total sum.
- Why this approach comes to mind first: It's a straightforward approach that checks all possibilities.

```cpp
#include <iostream>
#include <vector>

int sumOfConsecutiveSubsequences(std::vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    for (int mask = 1; mask < (1 << n); mask++) {
        std::vector<int> subsequence;
        for (int i = 0; i < n; i++) {
            if ((mask & (1 << i)) != 0) {
                subsequence.push_back(nums[i]);
            }
        }
        if (isConsecutive(subsequence)) {
            totalSum += sumSubsequence(subsequence);
        }
    }
    return totalSum;
}

bool isConsecutive(std::vector<int>& subsequence) {
    if (subsequence.size() <= 1) return true;
    for (int i = 1; i < subsequence.size(); i++) {
        if (subsequence[i] - subsequence[i - 1] != 1) {
            return false;
        }
    }
    return true;
}

int sumSubsequence(std::vector<int>& subsequence) {
    int sum = 0;
    for (int num : subsequence) {
        sum += num;
    }
    return sum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$, where $n$ is the length of the input array. This is because we generate all possible subsequences and check each one for consecutiveness.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we store each subsequence in memory.
> - **Why these complexities occur:** The brute force approach has high time complexity because it generates all possible subsequences, which is an exponential operation. The space complexity is linear because we store each subsequence in memory.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the array to find all subsequences of consecutive numbers.
- Detailed breakdown of the approach:
  1. Initialize an empty vector to store the subsequences of consecutive numbers.
  2. Iterate through the array, checking if the current number is consecutive with the previous number.
  3. If the numbers are consecutive, add the current number to the current subsequence.
  4. If the numbers are not consecutive, add the current subsequence to the list of subsequences and start a new subsequence with the current number.
- Proof of optimality: This approach has a time complexity of $O(n)$, where $n$ is the length of the input array, because we only make a single pass through the array.

```cpp
int sumOfConsecutiveSubsequences(std::vector<int>& nums) {
    int n = nums.size();
    int totalSum = 0;
    int currentSum = nums[0];
    int currentLength = 1;
    for (int i = 1; i < n; i++) {
        if (nums[i] - nums[i - 1] == 1) {
            currentSum += nums[i];
            currentLength++;
        } else {
            totalSum += currentSum;
            currentSum = nums[i];
            currentLength = 1;
        }
    }
    totalSum += currentSum;
    return totalSum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we only make a single pass through the array.
> - **Space Complexity:** $O(1)$, where $n$ is the length of the input array. This is because we only use a constant amount of space to store the current subsequence and the total sum.
> - **Optimality proof:** This approach is optimal because it has a linear time complexity and uses a constant amount of space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a single pass through the array to find all subsequences of consecutive numbers.
- Problem-solving patterns identified: Looking for ways to reduce the time complexity of an algorithm by avoiding unnecessary operations.
- Optimization techniques learned: Using a single pass through the array instead of generating all possible subsequences.
- Similar problems to practice: Finding the sum of all subsequences of a given array, finding the longest subsequence of consecutive numbers in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty array or an array with a single element.
- Edge cases to watch for: Handling arrays with duplicate numbers, arrays with negative numbers, and empty arrays.
- Performance pitfalls: Using an exponential-time algorithm instead of a linear-time algorithm.
- Testing considerations: Testing the algorithm with a variety of input cases, including edge cases and large inputs.