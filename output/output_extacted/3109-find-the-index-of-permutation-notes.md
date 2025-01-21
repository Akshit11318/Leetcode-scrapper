## Find the Index of the Permutation
**Problem Link:** https://leetcode.com/problems/find-the-index-of-permutation/description

**Problem Statement:**
- Input format: A string `s` containing the permutation of numbers from 1 to `n` where `n` is the length of `s`.
- Constraints: `1 <= n <= 8`, `s` is a permutation of numbers from 1 to `n`.
- Expected output format: The index of the permutation in lexicographical order.
- Key requirements and edge cases to consider:
  - Handling permutations of varying lengths.
  - Correctly calculating the lexicographical index.
- Example test cases with explanations:
  - For `s = "21"`, the output should be `1` because the permutation `21` is the second lexicographically smallest permutation of `12`.
  - For `s = "123"`, the output should be `0` because `123` is the first lexicographically smallest permutation of `123`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of numbers from 1 to `n`, then find the index of the given permutation `s` in the sorted list of these permutations.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of numbers from 1 to `n`.
  2. Sort these permutations lexicographically.
  3. Find the index of the given permutation `s` in the sorted list.
- Why this approach comes to mind first: It directly addresses the problem by considering all possible permutations and then locating the given permutation among them.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

void permute(std::vector<int>& nums, int start, int end, std::vector<std::string>& permutations, std::string& current) {
    if (start == end) {
        std::string perm = "";
        for (char c : current) {
            perm += std::to_string(c);
        }
        permutations.push_back(perm);
    } else {
        for (int i = start; i <= end; i++) {
            std::swap(nums[start], nums[i]);
            current[start] = nums[start] + '0';
            permute(nums, start + 1, end, permutations, current);
            std::swap(nums[start], nums[i]);
        }
    }
}

int findIndex(std::string s) {
    int n = s.length();
    std::vector<int> nums(n);
    for (int i = 0; i < n; i++) {
        nums[i] = i + 1;
    }
    std::vector<std::string> permutations;
    std::string current(n, ' ');
    permute(nums, 0, n - 1, permutations, current);
    std::sort(permutations.begin(), permutations.end());
    for (int i = 0; i < permutations.size(); i++) {
        if (permutations[i] == s) {
            return i;
        }
    }
    return -1; // Should not reach here
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n \cdot \log(n!))$ due to generating all permutations ($O(n!)$), sorting them ($O(n! \cdot \log(n!))$), and finding the given permutation ($O(n!)$).
> - **Space Complexity:** $O(n! \cdot n)$ for storing all permutations.
> - **Why these complexities occur:** The brute force approach generates all permutations and sorts them, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations, calculate the index of the given permutation by considering the relative order of elements.
- Detailed breakdown of the approach:
  1. Initialize the index and a factorial array to store factorials of numbers up to `n`.
  2. Iterate through the given permutation from left to right.
  3. For each element, calculate how many smaller elements are to its right and update the index accordingly using the factorial array.
  4. Remove the current element from consideration for the next steps.
- Proof of optimality: This approach directly calculates the index without generating all permutations, reducing the time complexity significantly.

```cpp
int findIndex(std::string s) {
    int n = s.length();
    std::vector<int> factorial(n + 1, 1);
    for (int i = 1; i <= n; i++) {
        factorial[i] = i * factorial[i - 1];
    }
    std::vector<bool> used(n + 1, false);
    int index = 0;
    for (int i = 0; i < n; i++) {
        int digit = s[i] - '0';
        int smaller = 0;
        for (int j = 1; j < digit; j++) {
            if (!used[j]) {
                smaller++;
            }
        }
        index += smaller * factorial[n - i - 1];
        used[digit] = true;
    }
    return index;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ due to iterating through the permutation and checking smaller elements.
> - **Space Complexity:** $O(n)$ for storing the factorial array and used elements.
> - **Optimality proof:** This approach calculates the index directly without generating all permutations, making it significantly more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Factorial, permutation indexing.
- Problem-solving patterns identified: Calculating indices based on relative order.
- Optimization techniques learned: Avoiding unnecessary generation of permutations.
- Similar problems to practice: Permutation indexing, lexicographical order problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly calculating factorials or indices.
- Edge cases to watch for: Handling permutations of varying lengths, ensuring correct indexing.
- Performance pitfalls: Generating all permutations unnecessarily.
- Testing considerations: Thoroughly testing with different permutation lengths and values.