## Count Substrings That Can Be Rearranged to Contain a String II

**Problem Link:** https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-ii/description

**Problem Statement:**
- Input format and constraints: Given a string `s` and a string `target`, return the number of substrings in `s` that can be rearranged to contain `target`.
- Expected output format: The count of substrings that can be rearranged to contain `target`.
- Key requirements and edge cases to consider: 
    - The string `s` can contain any lowercase English letters.
    - The string `target` can contain any lowercase English letters.
    - The function should return the count of substrings that can be rearranged to contain `target`, not the substrings themselves.
- Example test cases with explanations:
    - Example 1: 
        - Input: `s = "ab", target = "ba"`
        - Output: `1`
        - Explanation: The only substring in `s` that can be rearranged to contain `target` is `"ab"`.
    - Example 2: 
        - Input: `s = "abc", target = "abc"`
        - Output: `1`
        - Explanation: The only substring in `s` that can be rearranged to contain `target` is `"abc"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate over all substrings of `s` and check if they can be rearranged to contain `target`.
- Step-by-step breakdown of the solution:
    1. Generate all substrings of `s`.
    2. For each substring, generate all permutations.
    3. Check if `target` is a subsequence of any permutation.
- Why this approach comes to mind first: It is a straightforward approach to generate all possible substrings and check if they can be rearranged to contain `target`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int countSubstrings(string s, string target) {
    int count = 0;
    for (int i = 0; i < s.size(); i++) {
        for (int j = i + 1; j <= s.size(); j++) {
            string substring = s.substr(i, j - i);
            sort(substring.begin(), substring.end());
            sort(target.begin(), target.end());
            if (substring.size() >= target.size()) {
                string temp = substring;
                for (char c : target) {
                    auto it = find(temp.begin(), temp.end(), c);
                    if (it == temp.end()) break;
                    temp.erase(it);
                }
                if (temp.size() == substring.size() - target.size()) count++;
            }
        }
    }
    return count;
}

int main() {
    string s = "ab";
    string target = "ba";
    cout << countSubstrings(s, target) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 * m \log m)$ where $n$ is the length of `s` and $m$ is the length of `target`. The time complexity is due to the generation of all substrings, sorting each substring and `target`, and checking if `target` is a subsequence of any permutation.
> - **Space Complexity:** $O(n + m)$ for storing the substrings and permutations.
> - **Why these complexities occur:** The brute force approach generates all substrings and permutations, which results in a high time complexity. The space complexity is due to the storage of the substrings and permutations.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a sliding window approach to check if a substring can be rearranged to contain `target`.
- Detailed breakdown of the approach:
    1. Initialize a frequency array for `target`.
    2. Initialize a frequency array for the current window.
    3. Iterate over the string `s` using a sliding window approach.
    4. For each character in the window, update the frequency array.
    5. Check if the frequency array of the window is a superset of the frequency array of `target`.
- Why further optimization is impossible: The optimal approach has a time complexity of $O(n * m)$, which is the minimum required to check all substrings.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

int countSubstrings(string s, string target) {
    int count = 0;
    unordered_map<char, int> target_freq;
    for (char c : target) {
        target_freq[c]++;
    }
    for (int i = 0; i < s.size(); i++) {
        unordered_map<char, int> window_freq;
        for (int j = i; j < s.size(); j++) {
            window_freq[s[j]]++;
            bool is_superset = true;
            for (auto& pair : target_freq) {
                if (window_freq[pair.first] < pair.second) {
                    is_superset = false;
                    break;
                }
            }
            if (is_superset) count++;
        }
    }
    return count;
}

int main() {
    string s = "ab";
    string target = "ba";
    cout << countSubstrings(s, target) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n * m)$ where $n$ is the length of `s` and $m` is the length of `target`. The time complexity is due to the iteration over the string `s` and the update of the frequency array.
> - **Space Complexity:** $O(m)$ for storing the frequency array of `target`.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n * m)$, which is the minimum required to check all substrings.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sliding window approach, frequency array.
- Problem-solving patterns identified: Using a frequency array to check if a substring can be rearranged to contain `target`.
- Optimization techniques learned: Using a sliding window approach to reduce the time complexity.
- Similar problems to practice: Counting substrings that contain a certain pattern.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the frequency array correctly, not checking if the frequency array of the window is a superset of the frequency array of `target`.
- Edge cases to watch for: Empty strings, strings with only one character.
- Performance pitfalls: Using a brute force approach, not optimizing the time complexity.
- Testing considerations: Testing with different inputs, testing with edge cases.