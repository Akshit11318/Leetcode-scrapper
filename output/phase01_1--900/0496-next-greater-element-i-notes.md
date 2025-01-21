## Next Greater Element I
**Problem Link:** https://leetcode.com/problems/next-greater-element-i/description

**Problem Statement:**
- Given two arrays `nums1` and `nums2`, find the next greater element for each element in `nums1`. The next greater element for a number `x` in `nums1` is the first greater number to its right in `nums2`. If there is no such element, return `-1` for this number.
- Input format and constraints: `nums1` and `nums2` are non-empty arrays with distinct elements.
- Expected output format: An array with the same length as `nums1`, where each element is the next greater element for the corresponding element in `nums1`.
- Key requirements and edge cases to consider: 
  - Handling elements in `nums1` that do not exist in `nums2`.
  - Finding the next greater element for each element in `nums1` within `nums2`.
  - Returning `-1` for elements in `nums1` that do not have a next greater element in `nums2`.
- Example test cases with explanations:
  - For `nums1 = [4, 1, 2]` and `nums2 = [1, 3, 4, 2]`, the output should be `[-1, 3, -1]`.
  - For `nums1 = [2, 4]` and `nums2 = [1, 2, 3, 4]`, the output should be `[4, -1]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate through each element in `nums1` and find its next greater element in `nums2` by iterating through `nums2` from left to right.
- Step-by-step breakdown of the solution:
  1. Create an empty result array to store the next greater elements for `nums1`.
  2. Iterate through each element `x` in `nums1`.
  3. For each `x`, iterate through `nums2` from left to right to find the first element greater than `x`.
  4. If such an element is found, append it to the result array; otherwise, append `-1`.
- Why this approach comes to mind first: It directly addresses the problem statement by checking each element in `nums1` against all elements in `nums2` to find the next greater element.

```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    vector<int> result;
    for (int x : nums1) {
        bool found = false;
        for (int y : nums2) {
            if (x == y) {
                found = true;
            } else if (found && y > x) {
                result.push_back(y);
                break;
            }
        }
        if (!found || result.size() != nums1.size()) {
            result.push_back(-1);
        }
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n*m)$, where $n$ is the size of `nums1` and $m$ is the size of `nums2`, because for each element in `nums1`, we potentially iterate through all elements in `nums2`.
> - **Space Complexity:** $O(n)$, where $n$ is the size of `nums1`, because we create a result array of the same size as `nums1`.
> - **Why these complexities occur:** The nested loop structure leads to the time complexity, and the result array leads to the space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Use a stack to keep track of the indices of elements in `nums2` that do not have a next greater element yet. Iterate through `nums2`, and for each element, pop all elements from the stack that are smaller than the current element, updating their next greater element. This way, we ensure that for each element in `nums1`, we can find its next greater element in `nums2` in a single pass.
- Detailed breakdown of the approach:
  1. Create a hash map `map` to store the next greater element for each element in `nums2`.
  2. Initialize an empty stack.
  3. Iterate through `nums2`. For each element `y`:
    - While the stack is not empty and the top element of the stack is less than `y`, pop the top element and update its next greater element in `map`.
    - Push `y` onto the stack.
  4. Create the result array by looking up each element of `nums1` in `map`. If an element is not found, set its result to `-1`.
- Proof of optimality: This approach ensures that we only iterate through `nums2` once and use a constant amount of time to look up the next greater element for each element in `nums1`, leading to a significant improvement over the brute force approach.

```cpp
vector<int> nextGreaterElement(vector<int>& nums1, vector<int>& nums2) {
    unordered_map<int, int> map;
    stack<int> st;
    for (int y : nums2) {
        while (!st.empty() && st.top() < y) {
            map[st.top()] = y;
            st.pop();
        }
        st.push(y);
    }
    vector<int> result;
    for (int x : nums1) {
        result.push_back(map.count(x) ? map[x] : -1);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the size of `nums1` and $m` is the size of `nums2`, because we make a single pass through `nums2` and then look up each element of `nums1` in constant time.
> - **Space Complexity:** $O(n + m)$, because in the worst case, the stack and the hash map could contain all elements from `nums2`, and the result array has the size of `nums1`.
> - **Optimality proof:** This approach is optimal because it minimizes the number of operations required to find the next greater element for each element in `nums1` within `nums2`, achieving a linear time complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to efficiently find the next greater element in an array.
- Problem-solving patterns identified: The importance of iterating through data structures in a way that minimizes unnecessary comparisons.
- Optimization techniques learned: Applying a stack-based approach to reduce the time complexity of finding the next greater element.
- Similar problems to practice: Finding the next smaller element, implementing a stack-based solution for other array or string manipulation problems.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly handling edge cases, such as when an element in `nums1` does not exist in `nums2`.
- Edge cases to watch for: Ensuring that the solution correctly handles arrays with duplicate elements or when `nums1` and `nums2` have different sizes.
- Performance pitfalls: Failing to optimize the solution, leading to high time complexities for large inputs.
- Testing considerations: Thoroughly testing the solution with various input scenarios, including edge cases and large inputs.