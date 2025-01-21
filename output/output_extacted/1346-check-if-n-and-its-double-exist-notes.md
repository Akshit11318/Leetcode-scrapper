## Check if N and Its Double Exist

**Problem Link:** https://leetcode.com/problems/check-if-n-and-its-double-exist/description

**Problem Statement:**
- Input format: An array of integers `arr`.
- Constraints: $1 \leq arr.length \leq 10^5$, $1 \leq arr[i] \leq 10^9$.
- Expected output format: A boolean indicating whether there exists an integer `n` such that both `n` and `2n` exist in the array.
- Key requirements: The solution should be efficient and scalable for large inputs.
- Edge cases to consider: Empty array, array with a single element, array with duplicate elements.
- Example test cases:
  - Input: `[10, 2, 5, 3]`, Output: `true` (10 and 20 are in the array, but the actual numbers are 10 and 2 * 5 = 10)
  - Input: `[7, 1, 14, 11]`, Output: `true` (7 and 14 are in the array)
  - Input: `[3, 1, 7, 11]`, Output: `false`

---

### Brute Force Approach

**Explanation:**
- The initial thought process involves checking every number in the array to see if its double exists.
- Step-by-step breakdown:
  1. Iterate over each number `n` in the array.
  2. For each `n`, iterate over the entire array again to check if `2n` exists.
  3. If `2n` is found, return `true`.
  4. If the loop completes without finding any `n` and `2n` pair, return `false`.

```cpp
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        for (int i = 0; i < arr.size(); i++) {
            for (int j = 0; j < arr.size(); j++) {
                if (i != j && arr[i] == 2 * arr[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the input array. This is because for each element, we potentially scan the entire array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the loop indices and do not use any data structures that scale with input size.
> - **Why these complexities occur:** The nested loop structure leads to the quadratic time complexity. The space complexity is constant because we do not allocate any additional space that scales with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a `unordered_set` to store the numbers we have seen so far. This allows us to check if a number's double (or half) exists in constant time.
- Detailed breakdown:
  1. Create an `unordered_set` to store the numbers.
  2. Iterate over the array. For each number:
    - Check if its double or half exists in the set.
    - If either exists, return `true`.
    - Add the current number to the set.
  3. If the loop completes without finding any pair, return `false`.

```cpp
class Solution {
public:
    bool checkIfExist(vector<int>& arr) {
        unordered_set<int> seen;
        for (int num : arr) {
            if (seen.find(num * 2) != seen.end() || (num % 2 == 0 && seen.find(num / 2) != seen.end())) {
                return true;
            }
            seen.insert(num);
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we perform a constant amount of work for each element.
> - **Space Complexity:** $O(n)$, as in the worst case, we might store every element in the set.
> - **Optimality proof:** This is optimal because we must at least look at each element once to determine if a pair exists, and the set operations (insertion and lookup) are constant time on average, making the overall time complexity linear.

---

### Final Notes

**Learning Points:**
- Using data structures like `unordered_set` for fast lookup.
- Reducing time complexity by avoiding unnecessary iterations.
- Importance of considering all edge cases.

**Mistakes to Avoid:**
- Not checking for `0` or handling division by `2` correctly for even numbers.
- Not using the most efficient data structures for the problem.
- Failing to consider all possible scenarios for the input data.