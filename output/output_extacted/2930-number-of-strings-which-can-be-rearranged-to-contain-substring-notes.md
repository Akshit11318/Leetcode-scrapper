## Number of Strings Which Can Be Rearranged to Contain Substring
**Problem Link:** https://leetcode.com/problems/number-of-strings-which-can-be-rearranged-to-contain-substring/description

**Problem Statement:**
- Input: An array of strings `strings` and a target substring `target`.
- Constraints: Each string in `strings` consists of lowercase English letters. The length of `target` is between 2 and 5. The length of each string in `strings` is between 2 and 100.
- Expected Output: The number of strings which can be rearranged to contain the `target` substring.
- Key Requirements: Determine the number of strings that can be rearranged to contain the `target` substring, considering all possible permutations of characters in each string.
- Example Test Cases:
  - Input: `strings = ["abc","bac","cab","bca","xyc","yxc"]`, `target = "abc"`
    Output: `3`
  - Input: `strings = ["ab","ab","abc"]`, `target = "ab"`
    Output: `3`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves generating all permutations of each string and checking if the `target` substring is present in any permutation.
- This approach is straightforward but inefficient due to the large number of permutations for longer strings.
- Step-by-step breakdown:
  1. For each string in the input array, generate all permutations of its characters.
  2. For each permutation, check if the `target` substring is present.
  3. Count the number of strings for which at least one permutation contains the `target` substring.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

// Function to generate all permutations of a string
void permute(string str, int start, int end, vector<string>& permutations) {
    if (start == end) {
        permutations.push_back(str);
    } else {
        for (int i = start; i <= end; i++) {
            swap(str[start], str[i]);
            permute(str, start + 1, end, permutations);
            swap(str[start], str[i]); // backtrack
        }
    }
}

int numStrings(vector<string>& strings, string target) {
    int count = 0;
    for (const auto& str : strings) {
        vector<string> permutations;
        permute(str, 0, str.size() - 1, permutations);
        bool found = false;
        for (const auto& perm : permutations) {
            if (perm.find(target) != string::npos) {
                found = true;
                break;
            }
        }
        if (found) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<string> strings = {"abc","bac","cab","bca","xyc","yxc"};
    string target = "abc";
    cout << numStrings(strings, target) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M!)$, where $N$ is the number of strings and $M$ is the maximum length of a string. This is because we generate all permutations of each string.
> - **Space Complexity:** $O(M!)$ for storing all permutations of a single string.
> - **Why these complexities occur:** The brute force approach involves generating all permutations of each string, leading to a factorial time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves sorting the characters in each string and checking if the sorted string contains the sorted `target` substring.
- This approach is efficient because it avoids generating all permutations of each string.
- Step-by-step breakdown:
  1. Sort the characters in the `target` substring.
  2. For each string in the input array, sort its characters.
  3. Check if the sorted string contains the sorted `target` substring.
  4. Count the number of strings for which the sorted string contains the sorted `target` substring.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

int numStrings(vector<string>& strings, string target) {
    sort(target.begin(), target.end());
    int count = 0;
    for (const auto& str : strings) {
        string sortedStr = str;
        sort(sortedStr.begin(), sortedStr.end());
        if (sortedStr.find(target) != string::npos) {
            count++;
        }
    }
    return count;
}

int main() {
    vector<string> strings = {"abc","bac","cab","bca","xyc","yxc"};
    string target = "abc";
    cout << numStrings(strings, target) << endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \cdot M \log M)$, where $N$ is the number of strings and $M$ is the maximum length of a string. This is because we sort each string.
> - **Space Complexity:** $O(M)$ for sorting each string.
> - **Optimality proof:** This approach is optimal because it avoids generating all permutations of each string, reducing the time complexity from factorial to polynomial.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting, substring searching.
- Problem-solving patterns identified: avoiding unnecessary permutations, using sorting to simplify the problem.
- Optimization techniques learned: reducing the time complexity by avoiding unnecessary operations.

**Mistakes to Avoid:**
- Common implementation errors: not sorting the `target` substring, not checking for the presence of the sorted `target` substring in the sorted string.
- Edge cases to watch for: empty strings, strings with repeated characters.
- Performance pitfalls: generating all permutations of each string, using inefficient sorting algorithms.
- Testing considerations: testing with different input sizes, testing with different character sets.