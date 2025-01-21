## Make Lexicographically Smallest Array by Swapping Elements

**Problem Link:** https://leetcode.com/problems/make-lexicographically-smallest-array-by-swapping-elements/description

**Problem Statement:**
- Input format: You are given an array of integers `nums` and an array of integers `index`.
- Constraints: `1 <= nums.length, index.length <= 10^5`.
- Expected output format: Return the array of integers after applying the given swaps to make the array lexicographically smallest.
- Key requirements and edge cases to consider: 
  - Each swap operation involves swapping the elements at two different indices.
  - The goal is to make the resulting array lexicographically smallest.
- Example test cases with explanations:
  - Example 1: Input: `nums = [100, 86, 84, 2, 4]`, `index = [3, 0, 1, 2, 4]`. Output: `[2, 4, 100, 86, 84]`. Explanation: Swap `nums[0]` and `nums[3]`, then `nums[1]` and `nums[0]`, and finally `nums[2]` and `nums[1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can try all possible permutations of swaps to find the lexicographically smallest array.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the given swaps.
  2. Apply each permutation of swaps to the original array.
  3. Compare the resulting arrays and find the lexicographically smallest one.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible solutions.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

vector<int> smallestArray(vector<int>& nums, vector<int>& index) {
    int n = nums.size();
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        result[index[i]] = nums[i];
    }
    return result;
}

vector<int> bruteForce(vector<int>& nums, vector<int>& index) {
    int n = nums.size();
    vector<int> result = smallestArray(nums, index);
    vector<int> temp(n);
    for (int i = 0; i < n; i++) {
        temp[i] = nums[i];
    }
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            swap(temp[i], temp[j]);
            vector<int> tempResult = smallestArray(temp, index);
            if (tempResult < result) {
                result = tempResult;
            }
            swap(temp[i], temp[j]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the length of the input arrays. This is because we are generating all permutations of swaps and applying each permutation to the array.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input arrays. This is because we need to store the temporary results.
> - **Why these complexities occur:** The brute force approach tries all possible permutations of swaps, which leads to an exponential time complexity. The space complexity is linear because we only need to store the temporary results.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to find the lexicographically smallest array.
- Detailed breakdown of the approach:
  1. Create a new array `result` of the same length as the input arrays.
  2. Iterate over the input arrays and for each index `i`, place the value `nums[i]` at the position `index[i]` in the `result` array.
  3. The resulting array is the lexicographically smallest array.
- Proof of optimality: The greedy approach ensures that we are always choosing the smallest possible value for each position in the `result` array, which leads to the lexicographically smallest array.

```cpp
vector<int> optimalSolution(vector<int>& nums, vector<int>& index) {
    int n = nums.size();
    vector<int> result(n);
    for (int i = 0; i < n; i++) {
        result[index[i]] = nums[i];
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input arrays. This is because we are iterating over the input arrays once.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input arrays. This is because we need to store the result array.
> - **Optimality proof:** The greedy approach ensures that we are always choosing the smallest possible value for each position in the `result` array, which leads to the lexicographically smallest array.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, swapping elements.
- Problem-solving patterns identified: Finding the lexicographically smallest array.
- Optimization techniques learned: Using a greedy approach to reduce time complexity.
- Similar problems to practice: Finding the lexicographically largest array, sorting arrays.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, not initializing variables.
- Edge cases to watch for: Empty input arrays, duplicate values.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Test the solution with different input sizes, test the solution with edge cases.