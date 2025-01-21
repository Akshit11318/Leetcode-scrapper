## Find All Anagrams in a String

**Problem Link:** https://leetcode.com/problems/find-all-anagrams-in-a-string/description

**Problem Statement:**
- Given two strings `s` and `p`, return all the start indices of `p`'s anagrams in `s`. 
- The input strings consist only of lowercase English letters.
- The length of both strings is in the range `[1, 10^5]`.
- Expected output format is a vector of integers representing the start indices of `p`'s anagrams in `s`.
- Key requirements and edge cases to consider include handling cases where `p` is longer than `s`, and when there are multiple anagrams of `p` in `s`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to generate all possible substrings of `s` with the same length as `p`, and then check each one to see if it's an anagram of `p`.
- Step-by-step breakdown:
  1. Generate all substrings of `s` with the same length as `p`.
  2. For each substring, sort its characters and compare with the sorted characters of `p`.
  3. If they are equal, it means the substring is an anagram of `p`, so add its start index to the result.

```cpp
vector<int> findAnagrams(string s, string p) {
    vector<int> result;
    int n = s.size(), m = p.size();
    if (m > n) return result;

    for (int i = 0; i <= n - m; i++) {
        string substr = s.substr(i, m);
        sort(substr.begin(), substr.end());
        sort(p.begin(), p.end());
        if (substr == p) {
            result.push_back(i);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m \log m)$, where $n$ is the length of `s` and $m$ is the length of `p`. The reason is that we are generating $n-m+1$ substrings, each of length $m$, and sorting each one, which takes $O(m \log m)$ time.
> - **Space Complexity:** $O(m)$, for storing the current substring and sorting it.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operation inside the loop, and the space complexity is due to the temporary storage needed for sorting.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a sliding window approach with a frequency count of characters in `p`.
- Detailed breakdown:
  1. Create a frequency count of characters in `p`.
  2. Initialize a sliding window of size `m` over `s`.
  3. For each position of the window, count the frequency of characters in the current window.
  4. Compare the frequency count of the current window with the frequency count of `p`.
  5. If they match, it means the current window is an anagram of `p`, so add its start index to the result.

```cpp
vector<int> findAnagrams(string s, string p) {
    vector<int> result;
    int n = s.size(), m = p.size();
    if (m > n) return result;

    vector<int> pCount(26), sCount(26);
    for (char c : p) pCount[c - 'a']++;

    for (int i = 0; i < n; i++) {
        sCount[s[i] - 'a']++;
        if (i >= m) sCount[s[i - m] - 'a']--;
        if (i >= m - 1 && pCount == sCount) {
            result.push_back(i - m + 1);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of `s`. The reason is that we are scanning `s` once.
> - **Space Complexity:** $O(1)$, as we are using a fixed-size array to store the frequency counts.
> - **Optimality proof:** This is optimal because we are only scanning `s` once and using a constant amount of space to store the frequency counts.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the sliding window technique and frequency counting.
- Problem-solving patterns identified include reducing the problem to a simpler one (e.g., comparing frequency counts instead of sorting).
- Optimization techniques learned include avoiding unnecessary computations (e.g., sorting) and using efficient data structures (e.g., arrays for frequency counts).
- Similar problems to practice include other string-related problems, such as finding the longest palindromic substring.

**Mistakes to Avoid:**
- Common implementation errors include not handling edge cases correctly (e.g., when `p` is longer than `s`) and not optimizing the solution (e.g., using sorting instead of frequency counting).
- Edge cases to watch for include when `p` is an empty string or when `s` contains only one unique character.
- Performance pitfalls include using inefficient algorithms (e.g., brute force) or data structures (e.g., linked lists instead of arrays).
- Testing considerations include testing the solution with different inputs, including edge cases, and verifying that the output is correct.