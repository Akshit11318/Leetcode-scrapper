## Letter Combinations of a Phone Number
**Problem Link:** https://leetcode.com/problems/letter-combinations-of-a-phone-number/description

**Problem Statement:**
- Input format: a string `digits` containing digits from 2 to 9.
- Constraints: `0 <= digits.length <= 4`.
- Expected output format: a list of all possible letter combinations that the number could represent.
- Key requirements and edge cases to consider: 
  - The mapping between digits and letters is given as follows:
    - `2`: `abc`
    - `3`: `def`
    - `4`: `ghi`
    - `5`: `jkl`
    - `6`: `mno`
    - `7`: `pqrs`
    - `8`: `tuv`
    - `9`: `wxyz`
  - If the input is empty, return an empty list.
- Example test cases with explanations:
  - Input: `digits = "23"`
    - Output: `["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]`
  - Input: `digits = ""`
    - Output: `[]`
  - Input: `digits = "2"`
    - Output: `["a", "b", "c"]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: One straightforward way to solve this problem is to manually list all possible combinations for each digit and then combine them.
- Step-by-step breakdown of the solution:
  1. Define a mapping between digits and their corresponding letters.
  2. Iterate through each digit in the input string.
  3. For each digit, generate all possible combinations with the letters associated with the previous digits.
  4. Store these combinations in a list.
- Why this approach comes to mind first: It's a simple, intuitive way to ensure all possible combinations are considered.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector<string> letterCombinations(string digits) {
    if (digits.empty()) return {};
    
    unordered_map<char, string> phone = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    
    vector<string> result;
    vector<string> temp;
    temp.push_back("");
    
    for (char digit : digits) {
        vector<string> newTemp;
        for (string str : temp) {
            for (char c : phone[digit]) {
                newTemp.push_back(str + c);
            }
        }
        temp = newTemp;
    }
    
    result = temp;
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, where $n$ is the number of digits. This is because in the worst case, each digit can have up to 4 letters (e.g., `7` and `9`), and we generate all combinations.
> - **Space Complexity:** $O(4^n)$, as we store all generated combinations in memory.
> - **Why these complexities occur:** The brute force approach generates all possible combinations, leading to exponential time and space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Using a backtracking approach, we can efficiently generate all combinations without storing intermediate results unnecessarily.
- Detailed breakdown of the approach:
  1. Define a recursive function that takes the current digit index and the current combination.
  2. If the current index is equal to the length of the input string, add the current combination to the result list.
  3. Otherwise, for each letter associated with the current digit, recursively call the function with the next index and the updated combination.
- Proof of optimality: This approach ensures that all possible combinations are generated while minimizing unnecessary computations and memory usage.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

void backtrack(string digits, int index, string current, vector<string>& result, unordered_map<char, string>& phone) {
    if (index == digits.size()) {
        result.push_back(current);
        return;
    }
    
    for (char c : phone[digits[index]]) {
        backtrack(digits, index + 1, current + c, result, phone);
    }
}

vector<string> letterCombinations(string digits) {
    if (digits.empty()) return {};
    
    unordered_map<char, string> phone = {
        {'2', "abc"},
        {'3', "def"},
        {'4', "ghi"},
        {'5', "jkl"},
        {'6', "mno"},
        {'7', "pqrs"},
        {'8', "tuv"},
        {'9', "wxyz"}
    };
    
    vector<string> result;
    backtrack(digits, 0, "", result, phone);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(4^n)$, where $n$ is the number of digits. This is because in the worst case, each digit can have up to 4 letters, and we generate all combinations.
> - **Space Complexity:** $O(4^n)$, as we store all generated combinations in memory.
> - **Optimality proof:** This approach is optimal because it generates all possible combinations while minimizing unnecessary computations and memory usage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: backtracking, recursion.
- Problem-solving patterns identified: using a recursive function to generate all combinations.
- Optimization techniques learned: minimizing unnecessary computations and memory usage.
- Similar problems to practice: generating permutations, subsets.

**Mistakes to Avoid:**
- Common implementation errors: forgetting to handle edge cases (e.g., empty input string).
- Edge cases to watch for: input strings with different lengths, empty input string.
- Performance pitfalls: using inefficient data structures or algorithms.
- Testing considerations: testing with different input lengths, edge cases.