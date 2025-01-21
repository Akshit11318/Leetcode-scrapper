## Elements in Array After Removing and Replacing Elements

**Problem Link:** https://leetcode.com/problems/elements-in-array-after-removing-and-replacing-elements/description

**Problem Statement:**
- Input format and constraints: The problem takes two arrays, `nums` and `replacements`, where `nums` is the original array and `replacements` is an array of pairs, each pair containing a value to remove from `nums` and a value to replace it with.
- Expected output format: The output should be the modified `nums` array after applying all replacements.
- Key requirements and edge cases to consider: The replacements should be applied in the order they appear in the `replacements` array. If a value to be removed does not exist in `nums`, the replacement should not occur.
- Example test cases with explanations: For example, given `nums = [1, 2, 3]` and `replacements = [[1, 3], [2, 4]]`, the output should be `[3, 4, 3]` because we first replace `1` with `3` and then `2` with `4`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The first approach that comes to mind is to iterate through each replacement pair and apply the replacement to the `nums` array.
- Step-by-step breakdown of the solution: 
  1. Iterate through each replacement pair in the `replacements` array.
  2. For each pair, find all occurrences of the value to be removed in the `nums` array and replace them with the replacement value.
- Why this approach comes to mind first: It directly follows the problem statement's requirements and is straightforward to implement.

```cpp
#include <vector>
using namespace std;

vector<int> replaceElements(vector<int>& nums, vector<vector<int>>& replacements) {
    for (auto& replacement : replacements) {
        int valToRemove = replacement[0];
        int replacementVal = replacement[1];
        for (int i = 0; i < nums.size(); ++i) {
            if (nums[i] == valToRemove) {
                nums[i] = replacementVal;
            }
        }
    }
    return nums;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `nums` and $m$ is the size of `replacements`. This is because for each replacement, we potentially iterate through all elements of `nums`.
> - **Space Complexity:** $O(1)$, not counting the space needed for the input and output arrays, as we modify the input array in-place.
> - **Why these complexities occur:** The time complexity is due to the nested loop structure, where for each replacement, we potentially scan the entire `nums` array. The space complexity is constant because we do not use any additional data structures that scale with input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The problem can be solved more efficiently by recognizing that we only need to replace the values in `nums` once for each replacement pair, without needing to scan the entire array for each replacement.
- Detailed breakdown of the approach: 
  1. Create a copy of the `nums` array to avoid modifying the original array until all replacements are processed.
  2. Iterate through the `replacements` array. For each replacement pair, find all occurrences of the value to be removed in the copy of `nums` and replace them with the replacement value.
  3. After all replacements are applied, return the modified array.
- Proof of optimality: This approach remains $O(n \cdot m)$ in the worst case but is more efficient in practice because it avoids unnecessary scans and modifications of the original array.

```cpp
#include <vector>
using namespace std;

vector<int> replaceElements(vector<int>& nums, vector<vector<int>>& replacements) {
    vector<int> numsCopy = nums;
    for (auto& replacement : replacements) {
        int valToRemove = replacement[0];
        int replacementVal = replacement[1];
        for (int i = 0; i < numsCopy.size(); ++i) {
            if (numsCopy[i] == valToRemove) {
                numsCopy[i] = replacementVal;
            }
        }
    }
    return numsCopy;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the size of `nums` and $m$ is the size of `replacements`.
> - **Space Complexity:** $O(n)$, because we create a copy of the `nums` array.
> - **Optimality proof:** While the time complexity remains the same as the brute force approach, this solution is more efficient in practice due to reduced overhead from avoiding in-place modification until necessary. However, for very large inputs, the space complexity might be a consideration.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Array manipulation, in-place modification, and the importance of considering the practical efficiency of algorithms.
- Problem-solving patterns identified: Recognizing the need to minimize unnecessary scans and modifications of data structures.
- Optimization techniques learned: Creating temporary copies of data to avoid modifying the original data until necessary.
- Similar problems to practice: Problems involving array or string manipulation, where efficiency and minimizing unnecessary operations are key.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as an empty `nums` or `replacements` array.
- Edge cases to watch for: Handling cases where the value to be removed does not exist in `nums`, or where the replacement value is the same as the value to be removed.
- Performance pitfalls: Using inefficient data structures or algorithms that lead to high time or space complexity.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases, to ensure correctness and efficiency.