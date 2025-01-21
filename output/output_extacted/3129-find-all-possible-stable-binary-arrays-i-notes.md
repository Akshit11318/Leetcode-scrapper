## Find All Possible Stable Binary Arrays I
**Problem Link:** https://leetcode.com/problems/find-all-possible-stable-binary-arrays-i/description

**Problem Statement:**
- Given a binary array `arr` of length `n`, find all possible stable binary arrays of length `n`.
- A binary array is stable if for every `i` in the range `[0, n-2]`, `arr[i] >= arr[i+1]`.
- Input format: a binary array `arr` of length `n`.
- Constraints: `1 <= n <= 20`.
- Expected output format: a list of all possible stable binary arrays of length `n`.
- Key requirements and edge cases to consider: the input array `arr` may contain both `0`s and `1`s, and the output should include all possible stable binary arrays, not just those that can be obtained by modifying the input array.
- Example test cases with explanations:
  - Input: `arr = [1,1,1]`, Output: `[[1,1,1],[1,1,0],[1,0,0],[0,0,0]]`
  - Input: `arr = [0,0,0]`, Output: `[[0,0,0]]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to generate all possible binary arrays of length `n` and then filter out those that are not stable.
- Step-by-step breakdown of the solution:
  1. Generate all possible binary arrays of length `n` using a recursive function or bit manipulation.
  2. For each generated array, check if it is stable by iterating over the array and verifying that each element is greater than or equal to the next element.
  3. If the array is stable, add it to the result list.

```cpp
#include <vector>
using namespace std;

void generateStableArrays(vector<vector<int>>& result, vector<int>& current, int n, int index) {
    if (index == n) {
        result.push_back(current);
        return;
    }
    for (int i = 0; i <= 1; i++) {
        if (index == 0 || i <= current[index - 1]) {
            current[index] = i;
            generateStableArrays(result, current, n, index + 1);
        }
    }
}

vector<vector<int>> findAllPossibleStableBinaryArrays(int n) {
    vector<vector<int>> result;
    vector<int> current(n);
    generateStableArrays(result, current, n, 0);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the input array, because we generate all possible binary arrays of length $n$.
> - **Space Complexity:** $O(2^n \cdot n)$, because we store all stable binary arrays of length $n$ in the result list.
> - **Why these complexities occur:** The time complexity occurs because we generate all possible binary arrays of length $n$, and the space complexity occurs because we store all stable binary arrays of length $n$ in the result list.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight that leads to the optimal solution is to generate only stable binary arrays of length `n` directly, without generating all possible binary arrays and then filtering out those that are not stable.
- Step-by-step breakdown of the approach:
  1. Initialize an empty result list to store all stable binary arrays of length `n`.
  2. Define a recursive function `generateStableArrays` that generates all stable binary arrays of length `n` directly.
  3. In the recursive function, iterate over all possible values for the current element (0 or 1), and recursively generate all stable binary arrays for the remaining elements.
  4. If the current element is 1, only consider 1 or 0 for the next element. If the current element is 0, only consider 0 for the next element.

```cpp
#include <vector>
using namespace std;

void generateStableArrays(vector<vector<int>>& result, vector<int>& current, int n, int index) {
    if (index == n) {
        result.push_back(current);
        return;
    }
    for (int i = 0; i <= 1; i++) {
        if (index == 0 || i <= current[index - 1]) {
            current[index] = i;
            generateStableArrays(result, current, n, index + 1);
        }
    }
}

vector<vector<int>> findAllPossibleStableBinaryArrays(int n) {
    vector<vector<int>> result;
    vector<int> current(n);
    generateStableArrays(result, current, n, 0);
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the input array, because we generate all stable binary arrays of length $n$ directly.
> - **Space Complexity:** $O(2^n \cdot n)$, because we store all stable binary arrays of length $n$ in the result list.
> - **Optimality proof:** The time complexity is optimal because we must generate all stable binary arrays of length `n`, and the space complexity is optimal because we must store all stable binary arrays of length `n` in the result list.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: recursive function, bit manipulation, and filtering.
- Problem-solving patterns identified: generating all possible solutions and then filtering out those that do not meet the conditions.
- Optimization techniques learned: generating only stable binary arrays directly, without generating all possible binary arrays and then filtering out those that are not stable.
- Similar problems to practice: generating all possible permutations of a given array, generating all possible subsets of a given array.

**Mistakes to Avoid:**
- Common implementation errors: not initializing the result list, not checking the base case in the recursive function.
- Edge cases to watch for: handling the case where `n` is 0 or 1, handling the case where the input array is empty.
- Performance pitfalls: generating all possible binary arrays of length `n` and then filtering out those that are not stable, which has a time complexity of $O(2^n)$.
- Testing considerations: testing the function with different input values, testing the function with edge cases.