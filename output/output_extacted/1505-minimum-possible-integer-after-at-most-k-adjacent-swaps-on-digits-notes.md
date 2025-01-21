## Minimum Possible Integer After At Most K Adjacent Swaps On Digits
**Problem Link:** https://leetcode.com/problems/minimum-possible-integer-after-at-most-k-adjacent-swaps-on-digits/description

**Problem Statement:**
- Input format: A string `num` representing a non-negative integer and an integer `k`.
- Constraints: `1 <= num.length <= 10^5`, `0 <= k <= 10^5`, and `num` consists of digits.
- Expected output format: The minimum possible integer after at most `k` adjacent swaps on digits.
- Key requirements and edge cases to consider: The number of swaps should not exceed `k`, and we aim to minimize the integer.
- Example test cases:
  - `num = "432", k = 4`: The output is `"124"`.
  - `num = "100", k = 1`: The output is `"010"`.
  - `num = "11112", k = 4`: The output is `"11112"`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible swaps and find the minimum integer.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input string.
  2. For each permutation, count the number of swaps needed to achieve it from the original string.
  3. If the number of swaps is less than or equal to `k`, update the minimum integer if the current permutation is smaller.
- Why this approach comes to mind first: It's a straightforward, exhaustive approach.

```cpp
#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

void swap(string& num, int i, int j) {
    char temp = num[i];
    num[i] = num[j];
    num[j] = temp;
}

int countSwaps(const string& num, const string& target) {
    int swaps = 0;
    string temp = num;
    for (int i = 0; i < target.size(); ++i) {
        int j = temp.find(target[i], i);
        if (j != i) {
            swap(temp, i, j);
            swaps++;
        }
    }
    return swaps;
}

string minimumInteger(string num, int k) {
    string minNum = num;
    do {
        if (countSwaps(num, minNum) <= k) {
            minNum = min(minNum, num);
        }
        next_permutation(num.begin(), num.end());
    } while (!next_permutation(num.begin(), num.end()));
    return minNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$ where $n$ is the length of the input string. This is because we generate all permutations and for each permutation, we count the number of swaps.
> - **Space Complexity:** $O(n)$ for storing the input string and temporary strings.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of the input string, which results in a factorial time complexity. The space complexity is linear due to the storage of strings.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to minimize the integer. We start from the leftmost digit and try to swap it with the smallest possible digit on its right.
- Detailed breakdown of the approach:
  1. Initialize an empty result string.
  2. Iterate through the input string from left to right.
  3. For each digit, try to find the smallest possible digit on its right within the range of `k` swaps.
  4. If a smaller digit is found, swap it with the current digit and update the result string.
  5. Repeat steps 3-4 until no more swaps are possible or `k` swaps have been made.
- Proof of optimality: This approach ensures that we minimize the integer by always choosing the smallest possible digit for each position.

```cpp
string minimumInteger(string num, int k) {
    for (int i = 0; i < num.size(); ++i) {
        int minIdx = i;
        for (int j = i + 1; j <= min(i + k, (int)num.size() - 1); ++j) {
            if (num[j] < num[minIdx]) {
                minIdx = j;
            }
        }
        if (minIdx != i) {
            for (int j = minIdx; j > i; --j) {
                swap(num[j], num[j - 1]);
                k--;
            }
            if (k == 0) break;
        }
    }
    return num;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$ where $n$ is the length of the input string. This is because we iterate through the input string and for each digit, we try to find the smallest possible digit on its right within the range of `k` swaps.
> - **Space Complexity:** $O(n)$ for storing the input string.
> - **Optimality proof:** This approach ensures that we minimize the integer by always choosing the smallest possible digit for each position, resulting in an optimal solution.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy approach, swapping, and string manipulation.
- Problem-solving patterns identified: Minimizing a value by choosing the smallest possible option at each step.
- Optimization techniques learned: Using a greedy approach to minimize the integer.
- Similar problems to practice: Other problems involving string manipulation and minimization.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty input string or `k` being greater than the length of the input string.
- Edge cases to watch for: Handling cases where `k` is 0 or the input string is already minimized.
- Performance pitfalls: Using an inefficient algorithm, such as the brute force approach, for large inputs.
- Testing considerations: Testing the solution with different inputs, including edge cases, to ensure its correctness.