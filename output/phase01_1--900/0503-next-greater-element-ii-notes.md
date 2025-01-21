## Next Greater Element II
**Problem Link:** https://leetcode.com/problems/next-greater-element-ii/description

**Problem Statement:**
- Input: A circular array `nums` of integers.
- Constraints: `1 <= nums.length <= 10^5`, `0 <= nums[i] <= 10^8`.
- Expected Output: An array `ans` of the same length as `nums`, where `ans[i]` is the next greater element to `nums[i]` in the circular array. If there is no greater element, the answer is `-1`.
- Key Requirements: The array is circular, meaning that after the last element, we consider the elements from the start again.
- Example Test Cases:
  - Input: `nums = [1,2,1]`
    Output: `[2,-1,2]`
  - Input: `nums = [1,2,3,4,3]`
    Output: `[2,3,4,-1,4]`

---

### Brute Force Approach
**Explanation:**
- The initial thought process involves iterating through the array for each element to find the next greater element in a circular manner.
- For each element `nums[i]`, we start checking from `nums[i+1]` up to the end of the array, and then from the start of the array up to `nums[i-1]` (in a circular sense) to find the first element greater than `nums[i]`.
- If no greater element is found, we mark the answer as `-1`.

```cpp
#include <vector>
using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, -1);
    for (int i = 0; i < n; i++) {
        for (int j = (i + 1) % n; j != i; j = (j + 1) % n) {
            if (nums[j] > nums[i]) {
                ans[i] = nums[j];
                break;
            }
        }
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array, because for each element, we potentially scan the entire array.
> - **Space Complexity:** $O(n)$, for storing the result.
> - **Why these complexities occur:** The brute force approach involves nested loops, leading to quadratic time complexity. The space complexity is linear because we need to store the result for each element.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a stack to keep track of the indices of the elements we have seen so far but have not yet found a greater element for.
- We iterate through the array twice (to simulate the circular nature) and for each element, we pop all the elements from the stack that are smaller than the current element, updating their next greater element in the `ans` array.
- We then push the current index onto the stack.
- This approach ensures that we only need to make one pass through the array (considering its circular nature), reducing the time complexity significantly.

```cpp
#include <vector>
#include <stack>
using namespace std;

vector<int> nextGreaterElements(vector<int>& nums) {
    int n = nums.size();
    vector<int> ans(n, -1);
    stack<int> st;
    for (int i = 0; i < 2 * n; i++) {
        while (!st.empty() && nums[st.top()] < nums[i % n]) {
            ans[st.top()] = nums[i % n];
            st.pop();
        }
        st.push(i % n);
    }
    return ans;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because each element is pushed and popped from the stack exactly once.
> - **Space Complexity:** $O(n)$, for the stack in the worst case (when all elements are in increasing order).
> - **Optimality proof:** This is optimal because we only need to visit each element twice (once to potentially push it onto the stack and once to potentially pop it), and we use the stack to efficiently keep track of elements that still need a greater element found.

---

### Final Notes
**Learning Points:**
- The use of a stack to keep track of elements that need a greater element found.
- The importance of simulating the circular nature of the array by iterating twice.
- The optimization of reducing time complexity from $O(n^2)$ to $O(n)$ by avoiding nested loops.

**Mistakes to Avoid:**
- Not considering the circular nature of the array.
- Using a brute force approach that leads to high time complexity.
- Not utilizing a stack to efficiently manage elements that need a greater element found.

---