## Next Greater Element III
**Problem Link:** https://leetcode.com/problems/next-greater-element-iii/description

**Problem Statement:**
- Input format and constraints: Given a positive integer `n`, find the smallest integer which is greater than `n` and has the same digits as `n`.
- Expected output format: The smallest integer greater than `n` with the same digits, or `-1` if no such integer exists.
- Key requirements and edge cases to consider: 
  - The input integer `n` is in the range `[1, 10^9]`.
  - The integer `n` may have repeated digits.
  - If no greater integer with the same digits exists, return `-1`.
- Example test cases with explanations:
  - Input: `n = 12`, Output: `21`
  - Input: `n = 21`, Output: `12`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible permutations of the digits of `n` and check if any permutation is greater than `n`.
- Step-by-step breakdown of the solution:
  1. Convert the integer `n` to a string `s` to easily access and manipulate its digits.
  2. Generate all permutations of the string `s`.
  3. For each permutation, convert it back to an integer and check if it is greater than `n`.
  4. Keep track of the smallest integer greater than `n` with the same digits.
- Why this approach comes to mind first: It is a straightforward approach that involves generating all possible permutations and checking each one.

```cpp
#include <algorithm>
#include <string>
using namespace std;

int nextGreaterElement(int n) {
    string s = to_string(n);
    int min_greater = INT_MAX;
    do {
        int perm = stoi(s);
        if (perm > n && perm < min_greater) {
            min_greater = perm;
        }
    } while (next_permutation(s.begin(), s.end()));
    return min_greater == INT_MAX ? -1 : min_greater;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k!)$ where $k$ is the number of digits in $n$, because we generate all permutations of the digits.
> - **Space Complexity:** $O(k)$ for storing the string `s`, where $k$ is the number of digits in $n`.
> - **Why these complexities occur:** The time complexity is due to generating all permutations, and the space complexity is due to storing the string `s`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of generating all permutations, we can use a single pass through the digits of `n` to find the next greater element.
- Detailed breakdown of the approach:
  1. Convert the integer `n` to a string `s` to easily access and manipulate its digits.
  2. Find the first digit from the right that is smaller than the digit to its right. If no such digit exists, there is no greater integer with the same digits.
  3. Find the smallest digit to the right of the found digit that is greater than it.
  4. Swap the found digit with the smallest greater digit.
  5. Reverse the digits to the right of the found digit to get the smallest possible integer.
- Proof of optimality: This approach is optimal because it only requires a single pass through the digits of `n` and uses a minimal amount of extra space.

```cpp
int nextGreaterElement(int n) {
    string s = to_string(n);
    int i = s.size() - 2;
    while (i >= 0 && s[i] >= s[i + 1]) {
        i--;
    }
    if (i < 0) {
        return -1;
    }
    int j = s.size() - 1;
    while (s[j] <= s[i]) {
        j--;
    }
    swap(s[i], s[j]);
    reverse(s.begin() + i + 1, s.end());
    long long res = stoll(s);
    return res > INT_MAX ? -1 : res;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(k)$ where $k$ is the number of digits in $n$, because we only need to make a single pass through the digits.
> - **Space Complexity:** $O(k)$ for storing the string `s`, where $k$ is the number of digits in $n`.
> - **Optimality proof:** This approach is optimal because it only requires a single pass through the digits of `n` and uses a minimal amount of extra space.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Permutations, string manipulation, and optimization techniques.
- Problem-solving patterns identified: Using a single pass through the data to find the optimal solution.
- Optimization techniques learned: Avoiding unnecessary computations and using minimal extra space.
- Similar problems to practice: Finding the next smaller element, finding the largest permutation, and other permutation-related problems.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as when the input integer `n` has repeated digits or when no greater integer with the same digits exists.
- Edge cases to watch for: Handling the case when the input integer `n` is already the largest possible integer with its digits.
- Performance pitfalls: Using unnecessary computations or extra space, such as generating all permutations of the digits.
- Testing considerations: Testing the function with different inputs, including edge cases and large integers.