## Word Subsets
**Problem Link:** https://leetcode.com/problems/word-subsets/description

**Problem Statement:**
- Input: Two lists of strings, `A` and `B`, where each string consists of lowercase English letters.
- Constraints: 
  - `1 <= A.length <= 10^5`
  - `1 <= A[i].length <= 10`
  - `1 <= B.length <= 10^5`
  - `1 <= B[i].length <= 10`
- Expected Output: A list of strings from `A` that are `universal` superstrings. A string `x` from `A` is a universal superstring if for every string `y` in `B`, the frequency of every character in `y` is less than or equal to the frequency of the same character in `x`.
- Key Requirements: Identify all universal superstrings in `A` that can cover every string in `B`.

### Example Test Cases:
- Input: `A = ["amazon","apple","facebook","google","leetcode"]`, `B = ["e","o"]`
- Output: `["facebook","google","leetcode"]`
- Explanation: Each string in the output can cover all strings in `B`.

### Brute Force Approach
**Explanation:**
- The initial thought process involves checking each string in `A` against every string in `B`.
- For each string `x` in `A`, we compare its character frequency with that of every string `y` in `B`.
- We only include `x` in the result if it can cover all strings in `B`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
    vector<string> result;
    for (const string& x : A) {
        bool universal = true;
        for (const string& y : B) {
            unordered_map<char, int> freqX, freqY;
            for (char c : x) freqX[c]++;
            for (char c : y) freqY[c]++;
            
            bool covers = true;
            for (const auto& pair : freqY) {
                if (freqX[pair.first] < pair.second) {
                    covers = false;
                    break;
                }
            }
            if (!covers) {
                universal = false;
                break;
            }
        }
        if (universal) result.push_back(x);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(|A| \cdot |B| \cdot max(|x|, |y|))$, where $|A|$ and $|B|$ are the sizes of the input lists, and $max(|x|, |y|)$ is the maximum length of strings in `A` and `B`.
> - **Space Complexity:** $O(max(|x|, |y|))$, for storing the frequency maps of characters in strings from `A` and `B`.
> - **Why these complexities occur:** The brute force approach involves nested loops over the input lists and their string elements, leading to the time complexity. The space complexity is due to the storage needed for character frequencies.

### Optimal Approach (Required)
**Explanation:**
- Instead of comparing each string in `A` with every string in `B`, we can first find the maximum frequency of each character across all strings in `B`.
- Then, we compare each string in `A` with this maximum frequency map.
- If a string in `A` can cover this maximum frequency map, it can cover all strings in `B`.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

vector<string> wordSubsets(vector<string>& A, vector<string>& B) {
    vector<string> result;
    unordered_map<char, int> maxFreqB;
    
    // Find the maximum frequency of each character in B
    for (const string& y : B) {
        unordered_map<char, int> freqY;
        for (char c : y) freqY[c]++;
        for (const auto& pair : freqY) {
            maxFreqB[pair.first] = max(maxFreqB[pair.first], pair.second);
        }
    }
    
    for (const string& x : A) {
        unordered_map<char, int> freqX;
        for (char c : x) freqX[c]++;
        
        bool covers = true;
        for (const auto& pair : maxFreqB) {
            if (freqX[pair.first] < pair.second) {
                covers = false;
                break;
            }
        }
        if (covers) result.push_back(x);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(|B| \cdot max(|y|) + |A| \cdot max(|x|))$, where $|B|$ and $|A|$ are the sizes of the input lists, and $max(|y|)$ and $max(|x|)$ are the maximum lengths of strings in `B` and `A`, respectively.
> - **Space Complexity:** $O(max(|x|, |y|))$, for storing the frequency maps of characters.
> - **Optimality proof:** This approach is optimal because it reduces the number of comparisons needed by first computing the maximum frequency map for `B`, thus avoiding redundant comparisons.

### Final Notes

**Learning Points:**
- The importance of preprocessing data to reduce computational complexity.
- Using frequency maps to compare strings based on character occurrences.
- Optimizing nested loop structures by reducing the number of comparisons.

**Mistakes to Avoid:**
- Not considering the maximum frequency of characters across all strings in `B`.
- Failing to optimize the comparison process, leading to inefficient solutions.
- Not validating the input data for edge cases, such as empty strings or lists.