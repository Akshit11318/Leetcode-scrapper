## Odd String Difference

**Problem Link:** https://leetcode.com/problems/odd-string-difference/description

**Problem Statement:**
- Input format and constraints: Given an array of strings `words`, return the `odd` string from the array. The `odd` string is the string that differs from every other string by exactly one character. If there is no `odd` string, return an empty string.
- Expected output format: A string representing the `odd` string, or an empty string if no such string exists.
- Key requirements and edge cases to consider:
  - All strings in the input array have the same length.
  - The `odd` string differs from every other string by exactly one character.
  - If there are multiple `odd` strings, return any one of them.
- Example test cases with explanations:
  - `words = ["abc","abc","abc"]`: No `odd` string exists, return an empty string.
  - `words = ["abc","abd","abe","abf"]`: The `odd` string is `"abc"`, return `"abc"`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Compare each string with every other string to find the `odd` string.
- Step-by-step breakdown of the solution:
  1. Iterate over each string in the input array.
  2. For each string, compare it with every other string in the array.
  3. Count the number of different characters between the two strings.
  4. If the number of different characters is exactly one, mark the string as a potential `odd` string.
  5. After comparing all strings, return the first string that is marked as an `odd` string.

```cpp
class Solution {
public:
    string oddString(vector<string>& words) {
        for (int i = 0; i < words.size(); i++) {
            bool isOdd = true;
            for (int j = 0; j < words.size(); j++) {
                if (i == j) continue;
                int diff = 0;
                for (int k = 0; k < words[i].size(); k++) {
                    if (words[i][k] != words[j][k]) diff++;
                }
                if (diff != 1) {
                    isOdd = false;
                    break;
                }
            }
            if (isOdd) return words[i];
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of strings in the input array and $m$ is the length of each string. This is because we compare each string with every other string, and for each comparison, we iterate over the characters of the strings.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the indices and the `isOdd` flag.
> - **Why these complexities occur:** The time complexity is high because we use nested loops to compare all strings, and the space complexity is low because we only use a few variables to store the indices and the `isOdd` flag.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of comparing each string with every other string, we can compare the differences between the strings. If a string is `odd`, its differences with other strings will be different from the differences of other strings.
- Detailed breakdown of the approach:
  1. Initialize an empty map to store the differences between the strings.
  2. Iterate over each string in the input array.
  3. For each string, iterate over every other string in the array.
  4. Calculate the differences between the two strings.
  5. Store the differences in the map.
  6. After storing all differences, iterate over the map and find the string that has a different difference with every other string.
  7. Return the `odd` string.

```cpp
class Solution {
public:
    string oddString(vector<string>& words) {
        unordered_map<string, int> diffCount;
        for (int i = 0; i < words.size(); i++) {
            for (int j = i + 1; j < words.size(); j++) {
                string diff;
                for (int k = 0; k < words[i].size(); k++) {
                    if (words[i][k] != words[j][k]) {
                        diff += to_string(words[i][k] - words[j][k]);
                    }
                }
                diffCount[diff]++;
            }
        }
        for (int i = 0; i < words.size(); i++) {
            for (int j = i + 1; j < words.size(); j++) {
                string diff;
                for (int k = 0; k < words[i].size(); k++) {
                    if (words[i][k] != words[j][k]) {
                        diff += to_string(words[i][k] - words[j][k]);
                    }
                }
                if (diffCount[diff] == 1) return words[i];
            }
        }
        return "";
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot m)$, where $n$ is the number of strings in the input array and $m$ is the length of each string. This is because we compare each string with every other string, and for each comparison, we iterate over the characters of the strings.
> - **Space Complexity:** $O(n \cdot m)$, as we use a map to store the differences between the strings.
> - **Optimality proof:** The time complexity is still high because we compare each string with every other string. However, we reduce the number of comparisons by storing the differences in a map and reusing them. The space complexity is higher because we use a map to store the differences.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: string comparison, difference calculation, and map usage.
- Problem-solving patterns identified: using a map to store and reuse differences between strings.
- Optimization techniques learned: reducing the number of comparisons by storing and reusing differences.
- Similar problems to practice: string comparison and difference calculation problems.

**Mistakes to Avoid:**
- Common implementation errors: incorrect string comparison, incorrect difference calculation, and incorrect map usage.
- Edge cases to watch for: empty input array, strings with different lengths, and strings with no differences.
- Performance pitfalls: high time complexity due to nested loops and high space complexity due to map usage.
- Testing considerations: test cases with different input arrays, strings with different lengths, and strings with no differences.