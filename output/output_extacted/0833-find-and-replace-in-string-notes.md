## Find and Replace in String

**Problem Link:** https://leetcode.com/problems/find-and-replace-in-string/description

**Problem Statement:**
- Input: a string `s`, an array of indices `indices`, and an array of strings `sources` and `targets`.
- Constraints: `0 <= s.length <= 10^4`, `0 <= indices.length <= 10^4`, `0 <= sources.length <= 10^4`, `0 <= targets.length <= 10^4`, `sources[i].length > 0`, `targets[i].length > 0`, and `indices[i] < s.length`.
- Expected output: a string after replacing all occurrences of `sources[i]` with `targets[i]` at the specified `indices[i]`.
- Key requirements and edge cases to consider: 
  - Replacement should occur in the order specified by `indices`.
  - If a replacement causes a previous index to be out of bounds, it should be ignored.
- Example test cases with explanations:
  - `s = "abcd"`, `indices = [0, 2]`, `sources = ["a", "cd"]`, `targets = ["eee", "fff"]`. The expected output is `"eeebfff"`.
  - `s = "abcd"`, `indices = [0, 2]`, `sources = ["ab", "ec"]`, `targets = ["eee", "fff"]`. The expected output is `"eeecd"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through the `indices` array, and for each index, check if the substring starting at that index matches the corresponding `source`. If it does, replace it with the corresponding `target`.
- Step-by-step breakdown of the solution:
  1. Iterate through the `indices` array.
  2. For each index, extract the substring from `s` starting at that index with the length of the corresponding `source`.
  3. Compare the extracted substring with the `source`. If they match, replace the substring in `s` with the `target`.
- Why this approach comes to mind first: It directly follows the problem statement, replacing substrings as specified.

```cpp
string findReplaceString(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
    string result = s;
    for (int i = 0; i < indices.size(); i++) {
        string substr = s.substr(indices[i], sources[i].length());
        if (substr == sources[i]) {
            result.replace(indices[i], sources[i].length(), targets[i]);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \cdot k)$, where $n$ is the length of `s`, $m$ is the number of replacements, and $k$ is the average length of `sources` and `targets`. This is because for each replacement, we potentially scan the entire string.
> - **Space Complexity:** $O(n)$ for storing the result string.
> - **Why these complexities occur:** The brute force approach involves repeated scanning and replacement in the string, leading to high time complexity. The space complexity is due to the storage of the resulting string.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of modifying the string in-place, we can build the result string incrementally. We iterate through the `indices` and `sources` in sorted order of `indices`. For each index, we append the substring from the last processed index to the current index, followed by the `target` if the `source` matches.
- Detailed breakdown of the approach:
  1. Sort the `indices` along with their corresponding `sources` and `targets` based on `indices`.
  2. Initialize an empty result string.
  3. Iterate through the sorted `indices`. For each index:
     - Append the substring from the last processed index to the current index to the result.
     - If the `source` matches the substring starting at the current index, append the `target` instead.
  4. Finally, append any remaining substring from the last processed index to the end of `s`.
- Proof of optimality: This approach ensures that we only scan the string once and make replacements in a single pass, minimizing the time complexity.

```cpp
string findReplaceString(string s, vector<int>& indices, vector<string>& sources, vector<string>& targets) {
    vector<vector<string>> sorted;
    for (int i = 0; i < indices.size(); i++) {
        sorted.push_back({to_string(indices[i]), sources[i], targets[i]});
    }
    sort(sorted.begin(), sorted.end(), [](vector<string>& a, vector<string>& b) {
        return stoi(a[0]) < stoi(b[0]);
    });
    
    string result = "";
    int lastIdx = 0;
    for (auto& vec : sorted) {
        int idx = stoi(vec[0]);
        result += s.substr(lastIdx, idx - lastIdx);
        if (s.substr(idx, vec[1].length()) == vec[1]) {
            result += vec[2];
        } else {
            result += s.substr(idx, vec[1].length());
        }
        lastIdx = idx + vec[1].length();
    }
    result += s.substr(lastIdx);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m \log m)$, where $n$ is the length of `s` and $m` is the number of replacements. The sorting step dominates the complexity.
> - **Space Complexity:** $O(n + m)$ for storing the result string and the sorted indices.
> - **Optimality proof:** This approach is optimal because it minimizes the number of passes through the data, achieving a linear time complexity with respect to the input size after sorting.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Sorting, string manipulation, and incremental building of the result.
- Problem-solving patterns identified: Breaking down the problem into manageable parts (sorting and then iterating) and using data structures efficiently.
- Optimization techniques learned: Avoiding in-place modifications and using a single pass through the data.
- Similar problems to practice: Other string manipulation and replacement problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when the replacement causes a previous index to be out of bounds.
- Edge cases to watch for: Handling cases where the `source` does not match the substring at the specified index.
- Performance pitfalls: Using inefficient algorithms that result in high time complexity.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large datasets.