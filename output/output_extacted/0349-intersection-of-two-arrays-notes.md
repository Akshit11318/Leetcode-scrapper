## Intersection of Two Arrays
**Problem Link:** https://leetcode.com/problems/intersection-of-two-arrays/description

**Problem Statement:**
- Input format: Two integer arrays `nums1` and `nums2`.
- Constraints: $1 \leq nums1.length, nums2.length \leq 1000$ and $1 \leq nums1[i], nums2[i] \leq 1000$.
- Expected output format: An array of distinct integers that are present in both `nums1` and `nums2`.
- Key requirements: The output should not contain duplicates.
- Edge cases to consider: Empty input arrays, arrays with no common elements.
- Example test cases:
  - Input: `nums1 = [1,2,2,1]`, `nums2 = [2,2]`. Output: `[2]`.
  - Input: `nums1 = [4,9,5]`, `nums2 = [9,4,9,8,4]`. Output: `[4,9]`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to use nested loops to compare each element of `nums1` with every element of `nums2`.
- Step-by-step breakdown:
  1. Initialize an empty set or list to store unique common elements.
  2. Iterate over each element in `nums1`.
  3. For each element in `nums1`, iterate over each element in `nums2`.
  4. If an element from `nums1` matches an element in `nums2` and it's not already in the result set, add it.
- This approach comes to mind first because it directly addresses the problem statement without requiring additional data structures or complex algorithms.

```cpp
#include <vector>
#include <unordered_set>

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    unordered_set<int> result;
    for (int num1 : nums1) {
        for (int num2 : nums2) {
            if (num1 == num2 && result.find(num1) == result.end()) {
                result.insert(num1);
            }
        }
    }
    vector<int> finalResult(result.begin(), result.end());
    return finalResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \times m)$, where $n$ and $m$ are the sizes of `nums1` and `nums2`, respectively. This is because for each element in `nums1`, we potentially iterate over all elements in `nums2`.
> - **Space Complexity:** $O(min(n, m))$, as in the worst case, we might store all elements from the smaller array in the result set.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity, while the use of a set for storing unique elements leads to the space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Using a set to store elements from one array allows for constant time lookup, significantly reducing the overall time complexity.
- Detailed breakdown:
  1. Convert one of the input arrays into a set for $O(n)$ time complexity.
  2. Iterate over the second array, checking if each element exists in the set. If it does and it's not already in the result set, add it.
- Proof of optimality: This approach minimizes the number of operations by leveraging the constant time complexity of set lookups, making it more efficient than the brute force approach.

```cpp
#include <vector>
#include <unordered_set>

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    unordered_set<int> set1(nums1.begin(), nums1.end());
    unordered_set<int> result;
    for (int num2 : nums2) {
        if (set1.find(num2) != set1.end() && result.find(num2) == result.end()) {
            result.insert(num2);
        }
    }
    vector<int> finalResult(result.begin(), result.end());
    return finalResult;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ and $m$ are the sizes of `nums1` and `nums2`, respectively. Creating the set takes $O(n)$ time, and iterating over `nums2` takes $O(m)$ time.
> - **Space Complexity:** $O(n + m)$, as we store elements from both arrays in sets.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the intersection by leveraging the efficiency of set operations.

---

### Alternative Approach
**Explanation:**
- Different perspective: Instead of using sets, we can sort both arrays and then use two pointers to find common elements.
- Unique trade-offs: This approach avoids the use of extra space for sets but requires sorting the arrays, which can be beneficial if the arrays are already sorted or if memory is a concern.
- Scenarios where this approach might be preferred: When memory is limited, or the input arrays are already sorted.

```cpp
#include <vector>
#include <algorithm>

vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
    sort(nums1.begin(), nums1.end());
    sort(nums2.begin(), nums2.end());
    vector<int> result;
    int i = 0, j = 0;
    while (i < nums1.size() && j < nums2.size()) {
        if (nums1[i] < nums2[j]) i++;
        else if (nums1[i] > nums2[j]) j++;
        else {
            if (result.empty() || result.back() != nums1[i]) {
                result.push_back(nums1[i]);
            }
            i++; j++;
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$ due to the sorting operations.
> - **Space Complexity:** $O(1)$ if we ignore the space needed for the output, as we only use a constant amount of extra space for the pointers.
> - **Trade-off analysis:** This approach is beneficial when memory is a concern or the input arrays are large and already sorted. However, the time complexity is generally higher than the set-based approach due to the sorting step.

---

### Final Notes

**Learning Points:**
- **Set operations** can significantly reduce time complexity in problems involving unique elements or fast lookup.
- **Sorting** can be an alternative approach when memory is a concern or the input is already sorted.
- **Trade-off analysis** is crucial in choosing the most appropriate algorithm based on the specific constraints of the problem.

**Mistakes to Avoid:**
- **Not considering edge cases**, such as empty input arrays or arrays with no common elements.
- **Ignoring the possibility of duplicate elements** in the input arrays.
- **Not optimizing for time and space complexity** based on the problem's constraints and requirements.
- **Failing to test the solution** thoroughly with various input scenarios.