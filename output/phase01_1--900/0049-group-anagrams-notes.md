## Group Anagrams
**Problem Link:** [https://leetcode.com/problems/group-anagrams/description](https://leetcode.com/problems/group-anagrams/description)

**Problem Statement:**
- Input format: A list of strings `strs`.
- Constraints: $1 \leq strs.length \leq 10^4$, $0 \leq strs[i].length \leq 100$, `strs[i]` consists of lowercase English letters.
- Expected output format: A list of lists of strings, where each sublist contains anagrams.
- Key requirements and edge cases to consider: Handle cases where input list is empty or contains only one element. Also, ensure that the anagram grouping is case-sensitive as per the problem constraints.
- Example test cases with explanations:
  - Input: `strs = ["eat","tea","tan","ate","nat","bat"]`, Output: `[["eat","tea","ate"],["tan","nat"],["bat"]]`.
  - Input: `strs = [""]`, Output: `[[""]]`.
  - Input: `strs = ["a"]`, Output: `[["a"]]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Compare each string with every other string to check for anagrams.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of each string.
  2. Compare the sorted version of each string with the sorted version of every other string to determine anagrams.
- Why this approach comes to mind first: It directly addresses the problem by comparing strings, but it's inefficient due to the high number of comparisons and permutations.

```cpp
#include <vector>
#include <string>
#include <algorithm>

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    vector<vector<string>> result;
    for (const auto& str : strs) {
        bool found = false;
        for (auto& group : result) {
            if (isAnagram(str, group[0])) {
                group.push_back(str);
                found = true;
                break;
            }
        }
        if (!found) {
            result.push_back({str});
        }
    }
    return result;
}

bool isAnagram(const string& s1, const string& s2) {
    string sortedS1 = s1;
    string sortedS2 = s2;
    sort(sortedS1.begin(), sortedS1.end());
    sort(sortedS2.begin(), sortedS2.end());
    return sortedS1 == sortedS2;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(NMlogM + NM)$, where $N$ is the number of strings and $M$ is the maximum length of a string. The $NMlogM$ term comes from sorting each string, and the $NM$ term comes from comparing each string with others.
> - **Space Complexity:** $O(NM)$, for storing the result and sorting strings.
> - **Why these complexities occur:** The brute force approach involves sorting and comparing each string, leading to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: Use a hashmap to group anagrams based on their sorted characters.
- Detailed breakdown of the approach:
  1. Create a hashmap where the key is the sorted version of a string and the value is a list of anagrams.
  2. Iterate through each string in the input list, sort its characters, and use this sorted string as a key in the hashmap.
  3. Add the original string to the list of values for the corresponding key in the hashmap.
- Proof of optimality: This approach minimizes the number of comparisons and operations by directly mapping anagrams to their sorted versions.

```cpp
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

vector<vector<string>> groupAnagrams(vector<string>& strs) {
    unordered_map<string, vector<string>> anagrams;
    for (const auto& str : strs) {
        string sortedStr = str;
        sort(sortedStr.begin(), sortedStr.end());
        anagrams[sortedStr].push_back(str);
    }
    vector<vector<string>> result;
    for (const auto& pair : anagrams) {
        result.push_back(pair.second);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(NMlogM)$, where $N$ is the number of strings and $M$ is the maximum length of a string. This comes from sorting each string.
> - **Space Complexity:** $O(NM)$, for storing the result and hashmap.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations by directly grouping anagrams based on their sorted versions, avoiding unnecessary comparisons.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: Hashmap usage, string sorting, and anagram detection.
- Problem-solving patterns identified: Using sorted strings as keys to group anagrams efficiently.
- Optimization techniques learned: Minimizing comparisons and operations by leveraging hashmap lookups.
- Similar problems to practice: Other string and hashmap-based problems, such as finding duplicates or counting frequencies.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as empty strings or single-character strings.
- Edge cases to watch for: Handling lists with a single element, empty lists, and lists containing only anagrams or no anagrams.
- Performance pitfalls: Using inefficient algorithms for sorting or comparing strings.
- Testing considerations: Thoroughly testing with various input cases, including edge cases and large inputs.