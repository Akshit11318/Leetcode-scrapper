## Permutation Sequence
**Problem Link:** https://leetcode.com/problems/permutation-sequence/description

**Problem Statement:**
- Input format and constraints: Given integers `n` and `k`, return the `k`th permutation sequence of `n` numbers, where the numbers are from 1 to `n`.
- Expected output format: A string representing the `k`th permutation sequence.
- Key requirements and edge cases to consider: `1 <= n <= 9`, `1 <= k <= n!`, where `n!` denotes the factorial of `n`.
- Example test cases with explanations:
  - Input: `n = 3`, `k = 3`
  - Output: `"213"`
  - Explanation: The permutation sequences of `3` numbers are `"123"`, `"132"`, `"213"`, `"231"`, `"312"`, `"321"`. The `3`rd permutation sequence is `"213"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible permutations of `n` numbers, then return the `k`th permutation sequence.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of `n` numbers using a recursive function or an iterative approach.
  2. Store the permutations in a data structure such as a vector or an array.
  3. Return the `k`th permutation sequence from the stored permutations.
- Why this approach comes to mind first: It is a straightforward and intuitive approach, but it is not efficient for large values of `n` due to the factorial time complexity.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

void generatePermutations(std::vector<int>& nums, int start, int end, std::vector<std::string>& permutations) {
    if (start == end) {
        std::string permutation;
        for (int num : nums) {
            permutation += std::to_string(num);
        }
        permutations.push_back(permutation);
    } else {
        for (int i = start; i <= end; i++) {
            std::swap(nums[start], nums[i]);
            generatePermutations(nums, start + 1, end, permutations);
            std::swap(nums[start], nums[i]);
        }
    }
}

std::string getPermutation(int n, int k) {
    std::vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        nums[i] = i + 1;
    }
    std::vector<std::string> permutations;
    generatePermutations(nums, 0, n - 1, permutations);
    std::sort(permutations.begin(), permutations.end());
    return permutations[k - 1];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n!$ is the number of permutations and $n$ is the time complexity of generating each permutation.
> - **Space Complexity:** $O(n! \cdot n)$, where $n!$ is the number of permutations and $n$ is the space complexity of storing each permutation.
> - **Why these complexities occur:** The brute force approach generates all permutations, which has a factorial time complexity. The space complexity is also high due to the storage of all permutations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use the factorial number system to directly calculate the `k`th permutation sequence without generating all permutations.
- Detailed breakdown of the approach:
  1. Calculate the factorial of `n` and store it in an array `factorials`.
  2. Create a vector `nums` to store the numbers from 1 to `n`.
  3. Initialize an empty string `permutation` to store the result.
  4. Iterate from `n - 1` to `0`, and for each iteration:
    - Calculate the index `i` of the current number in the `nums` vector using the formula `i = (k - 1) / factorials[n - 1 - j]`.
    - Append the `i`th number from the `nums` vector to the `permutation` string.
    - Remove the `i`th number from the `nums` vector.
    - Update `k` to be `k - i * factorials[n - 1 - j]`.
  5. Return the `permutation` string.
- Proof of optimality: The optimal approach has a linear time complexity and uses a constant amount of space, making it the most efficient solution.

```cpp
std::string getPermutation(int n, int k) {
    std::vector<int> factorials(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        factorials[i] = factorials[i - 1] * i;
    }
    std::vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        nums[i] = i + 1;
    }
    std::string permutation;
    k--;
    for (int i = n - 1; i >= 0; i--) {
        int index = k / factorials[i];
        k %= factorials[i];
        permutation += std::to_string(nums[index]);
        nums.erase(nums.begin() + index);
    }
    return permutation;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of iterations.
> - **Space Complexity:** $O(n)$, where $n` is the space complexity of storing the `factorials` array and the `nums` vector.
> - **Optimality proof:** The optimal approach has a linear time complexity and uses a constant amount of space, making it the most efficient solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Factorial number system, permutation generation.
- Problem-solving patterns identified: Using mathematical insights to optimize solutions.
- Optimization techniques learned: Reducing time complexity from factorial to linear.
- Similar problems to practice: Permutation-related problems, such as generating all permutations or finding the next permutation in lexicographic order.

**Mistakes to Avoid:**
- Common implementation errors: Incorrect calculation of the `k`th permutation sequence, incorrect use of the factorial number system.
- Edge cases to watch for: Handling large values of `n` and `k`, ensuring correct calculation of the permutation sequence.
- Performance pitfalls: Using inefficient algorithms or data structures, such as generating all permutations instead of using the factorial number system.
- Testing considerations: Testing the solution with different values of `n` and `k`, ensuring correct output for edge cases.