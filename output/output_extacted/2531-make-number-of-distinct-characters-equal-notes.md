## Make Number of Distinct Characters Equal
**Problem Link:** https://leetcode.com/problems/make-number-of-distinct-characters-equal/description

**Problem Statement:**
- Input format and constraints: Given two strings `s` and `t` of length `n`, determine if it's possible to make the number of distinct characters in `s` and `t` equal by changing at most `k` characters in the string `s`. 
- Expected output format: Return `true` if it's possible to make the number of distinct characters in `s` and `t` equal by changing at most `k` characters in `s`, otherwise return `false`.
- Key requirements and edge cases to consider: 
    - `1 <= k <= n <= 10^5`
    - `s` and `t` consist only of lowercase English letters.
- Example test cases with explanations: 
    - If `s = "a"` and `t = "b"` and `k = 1`, the answer is `true` because we can change `s` to `"b"`.
    - If `s = "a"` and `t = "b"` and `k = 0`, the answer is `false` because we cannot change `s` to `"b"` without changing any characters.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Try all possible combinations of changing characters in `s` to match characters in `t` and check if the number of distinct characters in `s` and `t` becomes equal after each combination.
- Step-by-step breakdown of the solution:
    1. Generate all possible combinations of changing `k` characters in `s`.
    2. For each combination, change the corresponding characters in `s`.
    3. Calculate the number of distinct characters in `s` and `t`.
    4. Check if the number of distinct characters in `s` and `t` is equal.
- Why this approach comes to mind first: It's a straightforward approach to try all possible combinations and check if the condition is satisfied.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

bool makeEqual(string s, string t, int k) {
    int n = s.size();
    for (int i = 0; i < (1 << n); i++) {
        string temp = s;
        int count = 0;
        for (int j = 0; j < n; j++) {
            if ((i & (1 << j)) != 0) {
                if (temp[j] != t[j]) {
                    temp[j] = t[j];
                    count++;
                }
            }
        }
        if (count <= k) {
            set<char> setS(temp.begin(), temp.end());
            set<char> setT(t.begin(), t.end());
            if (setS.size() == setT.size()) {
                return true;
            }
        }
    }
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n \cdot n)$ because we generate all possible combinations of changing characters in `s` and for each combination, we calculate the number of distinct characters in `s` and `t`.
> - **Space Complexity:** $O(n)$ for the temporary string and sets to store distinct characters.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, which leads to an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Instead of trying all possible combinations, we can count the frequency of each character in `s` and `t` and then try to make the frequency of each character in `s` equal to the frequency of the same character in `t` by changing at most `k` characters in `s`.
- Detailed breakdown of the approach:
    1. Count the frequency of each character in `s` and `t`.
    2. Calculate the difference in frequency of each character between `s` and `t`.
    3. Try to make the frequency of each character in `s` equal to the frequency of the same character in `t` by changing at most `k` characters in `s`.
- Proof of optimality: This approach is optimal because it only tries to change the characters in `s` that are different from the corresponding characters in `t`, which minimizes the number of changes needed.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <set>
using namespace std;

bool makeEqual(string s, string t, int k) {
    int n = s.size();
    vector<int> countS(26, 0);
    vector<int> countT(26, 0);
    for (int i = 0; i < n; i++) {
        countS[s[i] - 'a']++;
        countT[t[i] - 'a']++;
    }
    int diff = 0;
    for (int i = 0; i < 26; i++) {
        diff += abs(countS[i] - countT[i]);
    }
    return diff <= 2 * k;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ because we count the frequency of each character in `s` and `t` and then calculate the difference in frequency.
> - **Space Complexity:** $O(1)$ because we use a fixed-size array to store the frequency of each character.
> - **Optimality proof:** This approach is optimal because it only tries to change the characters in `s` that are different from the corresponding characters in `t`, which minimizes the number of changes needed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: frequency counting, difference calculation.
- Problem-solving patterns identified: instead of trying all possible combinations, try to find the minimum number of changes needed to satisfy the condition.
- Optimization techniques learned: use a fixed-size array to store the frequency of each character instead of a dynamic data structure.

**Mistakes to Avoid:**
- Common implementation errors: not checking the boundary conditions, not handling the case when `k` is greater than `n`.
- Edge cases to watch for: when `s` and `t` are identical, when `k` is equal to `n`.
- Performance pitfalls: using a dynamic data structure to store the frequency of each character, trying all possible combinations instead of finding the minimum number of changes needed.