## Custom Sort String
**Problem Link:** [https://leetcode.com/problems/custom-sort-string/description](https://leetcode.com/problems/custom-sort-string/description)

**Problem Statement:**
- Input format: Two strings `S` and `T`, where `S` represents the custom order and `T` is the string to be sorted.
- Constraints: `S` and `T` consist of lowercase letters only, and the length of `S` is less than or equal to 26.
- Expected output format: A string where characters from `T` are sorted based on the custom order provided in `S`, and characters not present in `S` are appended at the end in alphabetical order.
- Key requirements and edge cases to consider: Handling characters not present in `S`, maintaining the relative order of characters in `S`, and ensuring characters not in `S` are sorted alphabetically.

**Example Test Cases:**
- `S = "cba", T = "abcd"`: The output should be `"cbad"`.
- `S = "cba", T = "abcd"`, but `S` does not contain `d`: Characters not in `S` (like `d`) should be appended in alphabetical order.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through each character in `T` and find its position in `S` to determine its order. If a character is not found in `S`, append it at the end in alphabetical order.
- Step-by-step breakdown:
  1. Create a map to store the frequency of each character in `T`.
  2. Iterate through `S` and append characters from `T` that match the current character in `S`, based on their frequency.
  3. After iterating through `S`, append any remaining characters from `T` (not found in `S`) in alphabetical order.

```cpp
#include <iostream>
#include <string>
#include <unordered_map>
#include <algorithm>

string customSortString(string S, string T) {
    unordered_map<char, int> freq;
    for (char c : T) freq[c]++;
    
    string result = "";
    for (char c : S) {
        if (freq.find(c) != freq.end()) {
            result += string(freq[c], c);
            freq.erase(c);
        }
    }
    
    for (auto& pair : freq) {
        result += string(pair.second, pair.first);
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + k)$, where $n$ is the length of `S`, $m$ is the length of `T`, and $k$ is the number of unique characters in `T`. The reason is we iterate through `S` and `T` once, and then iterate through the map of unique characters in `T`.
> - **Space Complexity:** $O(m)$, for storing the frequency of characters in `T`.
> - **Why these complexities occur:** The iteration through `S` and `T`, and the map operations, contribute to these complexities.

---

### Optimal Approach (Required)
The provided brute force approach is already quite efficient for this problem, leveraging the use of an unordered map to track character frequencies in `T` and then constructing the result string based on the custom order provided by `S`. This approach ensures that characters are processed in the custom order and that characters not present in `S` are appended in alphabetical order due to the nature of the map's iteration.

However, the optimal approach can be slightly refined by directly appending characters to the result string without the need for an explicit erase operation from the map after appending, as we can simply decrement the count in the map and append when the count reaches zero or when we've processed all characters in `S`.

```cpp
string customSortString(string S, string T) {
    unordered_map<char, int> freq;
    for (char c : T) freq[c]++;
    
    string result = "";
    for (char c : S) {
        if (freq.find(c) != freq.end()) {
            result += string(freq[c], c);
            freq[c] = 0; // Mark as processed
        }
    }
    
    for (char c = 'a'; c <= 'z'; c++) {
        if (freq.find(c) != freq.end() && freq[c] > 0) {
            result += string(freq[c], c);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + 26)$, where $n$ is the length of `S`, $m` is the length of `T`, and the constant factor accounts for the iteration over all lowercase letters to append remaining characters.
> - **Space Complexity:** $O(m)$, for storing the frequency of characters in `T`.
> - **Optimality proof:** This approach is optimal because it processes each character in `S` and `T` exactly once, leveraging the map for efficient lookup and append operations, thus minimizing the number of operations required.

---

### Final Notes

**Learning Points:**
- Utilizing an unordered map for efficient character frequency tracking.
- Iterating through a custom order string to construct a result string based on that order.
- Appending remaining characters not in the custom order in alphabetical order.

**Mistakes to Avoid:**
- Not considering characters not present in the custom order string.
- Not maintaining the relative order of characters as specified in the custom order string.
- Inefficient use of data structures leading to higher time or space complexities.