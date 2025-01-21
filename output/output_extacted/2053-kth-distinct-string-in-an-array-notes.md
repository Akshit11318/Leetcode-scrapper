## Kth Distinct String in an Array

**Problem Link:** https://leetcode.com/problems/kth-distinct-string-in-an-array/description

**Problem Statement:**
- Input format and constraints: Given an array of strings `arr` and an integer `k`, find the `kth` distinct string in the array.
- Expected output format: Return the `kth` distinct string if it exists, otherwise return an empty string.
- Key requirements and edge cases to consider:
  - Handle cases where `k` is larger than the number of distinct strings.
  - Consider the possibility of empty strings in the array.
- Example test cases with explanations:
  - Input: `arr = ["d","b","c","b","c","a"], k = 2`, Output: `"a"`
  - Input: `arr = ["aaa","aa","a"], k = 1`, Output: `"aaa"`
  - Input: `arr = ["a","b","a"], k = 3`, Output: `""`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Count the occurrences of each string and store them in a data structure, then find the `kth` distinct string.
- Step-by-step breakdown of the solution:
  1. Create a frequency map to store the count of each string.
  2. Iterate through the array to populate the frequency map.
  3. Filter out the strings that appear more than once.
  4. Sort the remaining strings.
  5. Return the `kth` string if it exists, otherwise return an empty string.
- Why this approach comes to mind first: It's a straightforward way to solve the problem, but it might not be the most efficient.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>
#include <algorithm>

using namespace std;

string kthDistinct(vector<string>& arr, int k) {
    unordered_map<string, int> freqMap;
    for (const auto& str : arr) {
        freqMap[str]++;
    }

    vector<string> distinctStrs;
    for (const auto& pair : freqMap) {
        if (pair.second == 1) {
            distinctStrs.push_back(pair.first);
        }
    }

    sort(distinctStrs.begin(), distinctStrs.end());
    if (k <= distinctStrs.size()) {
        return distinctStrs[k - 1];
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of distinct strings. This is because we sort the distinct strings.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of strings in the array. This is because we store the frequency map and the distinct strings.
> - **Why these complexities occur:** The sorting step dominates the time complexity, and the space complexity is due to the storage of the frequency map and the distinct strings.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass through the array to count the occurrences of each string and store them in a data structure.
- Detailed breakdown of the approach:
  1. Create a frequency map to store the count of each string.
  2. Iterate through the array to populate the frequency map.
  3. Filter out the strings that appear more than once and store the distinct strings in a vector.
  4. Return the `kth` string if it exists, otherwise return an empty string.
- Proof of optimality: This approach has a linear time complexity, which is the best we can achieve for this problem.

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

string kthDistinct(vector<string>& arr, int k) {
    unordered_map<string, int> freqMap;
    for (const auto& str : arr) {
        freqMap[str]++;
    }

    vector<string> distinctStrs;
    for (const auto& pair : freqMap) {
        if (pair.second == 1) {
            distinctStrs.push_back(pair.first);
        }
    }

    if (k <= distinctStrs.size()) {
        sort(distinctStrs.begin(), distinctStrs.end());
        return distinctStrs[k - 1];
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ in the worst case, where $n$ is the number of distinct strings. However, if we can find a way to avoid sorting, we can achieve $O(n)$ time complexity.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of strings in the array.
> - **Optimality proof:** We can achieve $O(n)$ time complexity by using a vector to store the distinct strings and then iterating through it to find the $kth$ string.

To achieve $O(n)$ time complexity, we can modify the approach as follows:

```cpp
string kthDistinct(vector<string>& arr, int k) {
    unordered_map<string, int> freqMap;
    for (const auto& str : arr) {
        freqMap[str]++;
    }

    vector<string> distinctStrs;
    for (const auto& pair : freqMap) {
        if (pair.second == 1) {
            distinctStrs.push_back(pair.first);
        }
    }

    if (k <= distinctStrs.size()) {
        sort(distinctStrs.begin(), distinctStrs.end());
        return distinctStrs[k - 1];
    }
    return "";
}
```

However, we can further optimize this by using a single pass through the array and the frequency map to find the $kth$ distinct string:

```cpp
string kthDistinct(vector<string>& arr, int k) {
    unordered_map<string, int> freqMap;
    for (const auto& str : arr) {
        freqMap[str]++;
    }

    int count = 0;
    for (const auto& pair : freqMap) {
        if (pair.second == 1) {
            count++;
            if (count == k) {
                return pair.first;
            }
        }
    }
    return "";
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the total number of strings in the array.
> - **Space Complexity:** $O(n)$, where $n$ is the total number of strings in the array.
> - **Optimality proof:** This approach has a linear time complexity, which is the best we can achieve for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: frequency counting, sorting, and iteration.
- Problem-solving patterns identified: using a single pass through the array and the frequency map to find the $kth$ distinct string.
- Optimization techniques learned: avoiding sorting and using a single pass through the array and the frequency map.
- Similar problems to practice: finding the $kth$ smallest element in an array, finding the $kth$ largest element in an array.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, such as an empty array or an invalid value of $k$.
- Edge cases to watch for: an empty array, an invalid value of $k$, and a large array with many distinct strings.
- Performance pitfalls: using sorting unnecessarily, which can increase the time complexity to $O(n \log n)$.
- Testing considerations: testing the function with different inputs, including edge cases and large arrays.