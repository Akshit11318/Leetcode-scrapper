## Constructing Two Increasing Arrays
**Problem Link:** https://leetcode.com/problems/constructing-two-increasing-arrays/description

**Problem Statement:**
- Input: An array of integers `target` and an array of integers `arr`.
- Constraints: Both arrays are non-empty and contain only integers.
- Expected Output: Determine if it's possible to construct two increasing arrays from the given arrays.
- Key Requirements: The two arrays should be increasing, and we can select elements from `arr` to form these arrays.
- Edge Cases: Handle cases where `arr` or `target` is empty, or when it's impossible to form two increasing arrays.

**Example Test Cases:**
- Example 1: `target = [2, 3, 1, 3, 4, 0, 2, 2]`, `arr = [2, 3, 2, 2, 0, 1, 3, 4]`. The output is `true` because we can construct two increasing arrays: `[2, 3, 4]` and `[2, 3, 1, 0, 2]`.
- Example 2: `target = [1, 3, 5, 7, 9]`, `arr = [3, 1, 5, 7, 9]`. The output is `true` because we can construct two increasing arrays: `[1, 3, 5, 7, 9]` and an empty array.

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves trying all possible combinations of elements from `arr` to form two increasing arrays.
- We generate all permutations of `arr` and check each permutation to see if it can be split into two increasing arrays that satisfy the conditions.
- This approach comes to mind first because it guarantees finding a solution if one exists, but it's inefficient due to the large number of permutations.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

bool isIncreasing(const vector<int>& arr) {
    for (int i = 1; i < arr.size(); ++i) {
        if (arr[i] <= arr[i - 1]) return false;
    }
    return true;
}

bool constructArrays(vector<int> target, vector<int> arr) {
    sort(arr.begin(), arr.end());
    do {
        vector<int> first, second;
        for (int i = 0; i < arr.size(); ++i) {
            if (first.empty() || arr[i] > first.back()) {
                first.push_back(arr[i]);
            } else if (second.empty() || arr[i] > second.back()) {
                second.push_back(arr[i]);
            } else {
                break;
            }
        }
        if (first.size() + second.size() == arr.size() && isIncreasing(first) && isIncreasing(second)) {
            return true;
        }
    } while (next_permutation(arr.begin(), arr.end()));
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$ due to generating all permutations of `arr`, where $n$ is the size of `arr`.
> - **Space Complexity:** $O(n)$ for storing the permutations and the two potential increasing arrays.
> - **Why these complexities occur:** The brute force approach involves generating all permutations, which leads to a factorial time complexity. The space complexity is linear because we only need to store the current permutation and the two arrays being constructed.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use two pointers to track the current position in `target` and `arr`, ensuring that we construct two increasing arrays efficiently.
- We maintain two vectors, `first` and `second`, to store the elements of the two increasing arrays.
- We iterate through `target` and `arr` simultaneously, using the two pointers to decide which array to add each element to, ensuring that both arrays remain increasing.
- This approach is optimal because it avoids unnecessary permutations and directly constructs the arrays in a single pass.

```cpp
#include <iostream>
#include <vector>

using namespace std;

bool constructArrays(vector<int>& target, vector<int>& arr) {
    vector<int> first, second;
    int i = 0, j = 0;
    while (i < target.size() && j < arr.size()) {
        if (arr[j] == target[i]) {
            if (first.empty() || arr[j] > first.back()) {
                first.push_back(arr[j]);
                i++;
            } else if (second.empty() || arr[j] > second.back()) {
                second.push_back(arr[j]);
                i++;
            } else {
                return false;
            }
            j++;
        } else {
            j++;
        }
    }
    return i == target.size();
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `target` and $m$ is the size of `arr`, because we make a single pass through both arrays.
> - **Space Complexity:** $O(n + m)$ for storing the two increasing arrays.
> - **Optimality proof:** This approach is optimal because it directly constructs the two increasing arrays in a single pass through the input arrays, avoiding unnecessary permutations and comparisons.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated include the use of two pointers for efficient array traversal and the construction of increasing arrays.
- Problem-solving patterns identified include the importance of maintaining sorted or increasing sequences and the use of pointers for efficient iteration.
- Optimization techniques learned include avoiding unnecessary permutations and using single-pass algorithms.

**Mistakes to Avoid:**
- Common implementation errors include failing to handle edge cases, such as empty input arrays, and not properly maintaining the increasing order of the arrays.
- Performance pitfalls include using brute force approaches that lead to high time complexities.
- Testing considerations include thoroughly testing the function with various input scenarios, including edge cases and large input sizes.