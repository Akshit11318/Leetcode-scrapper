## Minimum Runes to Add to Cast Spell

**Problem Link:** https://leetcode.com/problems/minimum-runes-to-add-to-cast-spell/description

**Problem Statement:**
- Given a string `spell`, representing the spell you want to cast, and a string `pos`, representing the runes you have, find the minimum number of runes you need to add to `pos` to cast the spell.
- The input string `spell` and `pos` consist of lowercase English letters.
- The spell can only be cast if you have all the required runes in `pos`.
- Return the minimum number of runes you need to add to `pos` to cast the spell.

**Example Test Cases:**

* Input: `spell = "hello", pos = "hello"` Output: `0` (You already have all the required runes)
* Input: `spell = "hello", pos = "helo"` Output: `1` (You need to add one more 'l' to cast the spell)
* Input: `spell = "hello", pos = "ll"` Output: `3` (You need to add 'h', 'e', and 'o' to cast the spell)

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to iterate through each character in the `spell` string and check if it exists in the `pos` string.
- If a character is found in `pos`, decrement its count in `pos`.
- If a character is not found in `pos`, increment the count of runes to be added.
- This approach is straightforward but has a high time complexity due to the repeated iteration through the `pos` string.

```cpp
int minRunesToCastSpell(string spell, string pos) {
    int runes_to_add = 0;
    for (char c : spell) {
        bool found = false;
        for (int i = 0; i < pos.size(); i++) {
            if (pos[i] == c) {
                found = true;
                pos.erase(i, 1);
                break;
            }
        }
        if (!found) {
            runes_to_add++;
        }
    }
    return runes_to_add;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the length of the `spell` string and $m$ is the length of the `pos` string. This is because for each character in `spell`, we potentially iterate through the entire `pos` string.
> - **Space Complexity:** $O(m)$, where $m$ is the length of the `pos` string. This is because we modify the `pos` string by erasing characters from it.
> - **Why these complexities occur:** These complexities occur due to the nested loop structure and the modification of the `pos` string.

---

### Optimal Approach (Required)

**Explanation:**
- The optimal approach involves using a frequency map to count the occurrences of each character in the `spell` and `pos` strings.
- We then iterate through the frequency map of `spell` and subtract the corresponding count from the frequency map of `pos`.
- If the count in `pos` is less than the count in `spell`, we add the difference to the count of runes to be added.
- This approach reduces the time complexity significantly by avoiding the nested loop structure.

```cpp
int minRunesToCastSpell(string spell, string pos) {
    unordered_map<char, int> spell_count, pos_count;
    for (char c : spell) spell_count[c]++;
    for (char c : pos) pos_count[c]++;
    
    int runes_to_add = 0;
    for (auto& pair : spell_count) {
        char c = pair.first;
        int count = pair.second;
        if (pos_count.find(c) == pos_count.end() || pos_count[c] < count) {
            runes_to_add += max(0, count - pos_count[c]);
        }
    }
    return runes_to_add;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the length of the `spell` string and $m$ is the length of the `pos` string. This is because we iterate through each string once to build the frequency maps and then iterate through the frequency map of `spell`.
> - **Space Complexity:** $O(n + m)$, where $n$ is the length of the `spell` string and $m$ is the length of the `pos` string. This is because we store the frequency maps for both strings.
> - **Optimality proof:** This approach is optimal because it reduces the time complexity to linear, avoiding the nested loop structure of the brute force approach. It also minimizes the space complexity by using frequency maps.

---

### Final Notes

**Learning Points:**
- Using frequency maps to count character occurrences can significantly reduce time complexity.
- Avoiding nested loop structures can improve performance.
- Modifying input strings can lead to higher space complexity.

**Mistakes to Avoid:**
- Not considering edge cases, such as empty input strings.
- Not validating input strings for correct format.
- Not optimizing the solution for performance.

**Similar Problems to Practice:**
- **_Minimum Window Substring_**: Finding the minimum window that contains all characters of a given string.
- **_Subarray Sum Equals K_**: Finding the number of subarrays with a sum equal to a given target.