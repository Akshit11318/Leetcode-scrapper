## Restore the Array
**Problem Link:** https://leetcode.com/problems/restore-the-array/description

**Problem Statement:**
- Input format: The problem provides two inputs: a string `s` and an integer `k`. The string `s` represents a sequence of digits where each digit is repeated a certain number of times. The integer `k` represents the length of the original sequence of digits before repetition.
- Expected output format: The task is to restore the original sequence of digits from the given string `s` and integer `k`.
- Key requirements and edge cases to consider:
  - Each digit in the string `s` is repeated a certain number of times, and we need to find the original sequence of digits before repetition.
  - The integer `k` represents the length of the original sequence of digits before repetition.
  - We need to consider all possible combinations of digits that satisfy the given conditions.
- Example test cases with explanations:
  - For example, if the input string is "231" and the integer `k` is 5, the original sequence of digits could be "21025" or "21052" or other combinations.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to generate all possible combinations of digits that satisfy the given conditions and check each combination to see if it matches the given string `s` and integer `k`.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of digits of length `k`.
  2. For each combination, repeat each digit the number of times specified in the string `s`.
  3. Check if the resulting sequence matches the given string `s` and integer `k`.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it can be inefficient for large inputs.

```cpp
#include <iostream>
#include <vector>
#include <string>

void restoreArray(string s, int k) {
    vector<string> res;
    int n = s.size();
    vector<int> counts;
    for (int i = 0; i < n; i += 2) {
        counts.push_back(s[i + 1] - '0');
    }
    vector<string> nums;
    string num = "";
    for (int i = 0; i < k; i++) {
        num += '0';
        nums.push_back(num);
        num += '0';
    }
    vector<bool> visited(k, false);
    backtrack(nums, counts, res, visited, 0);
    for (auto& x : res) {
        cout << x << endl;
    }
}

void backtrack(vector<string>& nums, vector<int>& counts, vector<string>& res, vector<bool>& visited, int idx) {
    if (idx == counts.size()) {
        string str = "";
        for (auto& x : nums) {
            str += x;
        }
        res.push_back(str);
        return;
    }
    for (int i = 0; i < nums.size(); i++) {
        if (visited[i]) continue;
        if (nums[i].size() < counts[idx]) {
            visited[i] = true;
            nums[i] += (char)('0' + idx);
            backtrack(nums, counts, res, visited, idx);
            visited[i] = false;
            nums[i].pop_back();
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n})$, where $n$ is the length of the input string `s`. This is because we are generating all possible combinations of digits.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we are storing the counts of each digit and the current combination of digits.
> - **Why these complexities occur:** The brute force approach generates all possible combinations of digits, which leads to an exponential time complexity. The space complexity is linear because we are storing a fixed amount of information for each digit.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The key insight is to use a backtracking approach with a more efficient way of generating combinations. We can use a recursive function to generate all possible combinations of digits.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes the current combination of digits, the counts of each digit, and the current index.
  2. If the current index is equal to the length of the counts array, add the current combination to the result.
  3. Otherwise, iterate over the possible digits and recursively call the function with the updated combination and index.
- Proof of optimality: The optimal approach has a time complexity of $O(2^{n})$, which is the best possible time complexity for this problem because we need to generate all possible combinations of digits.

```cpp
#include <iostream>
#include <vector>
#include <string>

void restoreArray(string s, int k) {
    int n = s.size();
    vector<int> counts;
    for (int i = 0; i < n; i += 2) {
        counts.push_back(s[i + 1] - '0');
    }
    vector<string> res;
    string num = "";
    for (int i = 0; i < k; i++) {
        num += '0';
    }
    vector<bool> visited(k, false);
    backtrack(num, counts, res, visited, 0);
    for (auto& x : res) {
        cout << x << endl;
    }
}

void backtrack(string& num, vector<int>& counts, vector<string>& res, vector<bool>& visited, int idx) {
    if (idx == counts.size()) {
        res.push_back(num);
        return;
    }
    for (int i = 0; i < num.size(); i++) {
        if (visited[i]) continue;
        if (num[i] == '0') {
            visited[i] = true;
            num[i] = (char)('0' + idx);
            backtrack(num, counts, res, visited, idx + 1);
            visited[i] = false;
            num[i] = '0';
        }
    }
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n})$, where $n$ is the length of the input string `s`. This is because we are generating all possible combinations of digits.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input string `s`. This is because we are storing the counts of each digit and the current combination of digits.
> - **Optimality proof:** The optimal approach has the same time complexity as the brute force approach, but it uses a more efficient way of generating combinations, which makes it more practical for large inputs.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, recursion.
- Problem-solving patterns identified: generating all possible combinations of digits.
- Optimization techniques learned: using a more efficient way of generating combinations.
- Similar problems to practice: other problems that involve generating all possible combinations of elements.

**Mistakes to Avoid:**
- Common implementation errors: not checking for edge cases, not handling recursive function calls correctly.
- Edge cases to watch for: empty input string, invalid input string.
- Performance pitfalls: using an inefficient way of generating combinations, not optimizing the recursive function calls.
- Testing considerations: testing the function with different input strings and lengths, checking for correctness and performance.