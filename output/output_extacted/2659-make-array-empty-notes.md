## Make Array Empty

**Problem Link:** https://leetcode.com/problems/make-array-empty/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums`, return `true` if you can make the array empty by removing all the elements in pairs. Each pair must satisfy the condition `nums[i] == nums[j]` and `i < j`. If you cannot make the array empty, return `false`.
- Expected output format: A boolean value indicating whether the array can be made empty.
- Key requirements and edge cases to consider:
  - The array can contain duplicate elements.
  - The array can be empty.
  - The array can contain only one element.
- Example test cases with explanations:
  - Input: `nums = [1, 2, 3, 1, 2, 3]`
    Output: `true`
    Explanation: You can remove the elements in pairs as follows: `(1, 1), (2, 2), (3, 3)`.
  - Input: `nums = [1, 1]`
    Output: `true`
    Explanation: You can remove the elements in pairs as follows: `(1, 1)`.
  - Input: `nums = [1]`
    Output: `false`
    Explanation: You cannot remove the only element in the array.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To make the array empty by removing all the elements in pairs, we can try all possible pairs of elements and check if they are equal.
- Step-by-step breakdown of the solution:
  1. Generate all possible pairs of elements in the array.
  2. Check if each pair has equal elements.
  3. If a pair has equal elements, remove them from the array.
  4. Repeat steps 1-3 until no more pairs can be found.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible pairs of elements.

```cpp
class Solution {
public:
    bool canMakeEmpty(vector<int>& nums) {
        bool foundPair = true;
        while (foundPair) {
            foundPair = false;
            for (int i = 0; i < nums.size(); i++) {
                for (int j = i + 1; j < nums.size(); j++) {
                    if (nums[i] == nums[j]) {
                        nums.erase(nums.begin() + i);
                        nums.erase(nums.begin() + j - 1);
                        foundPair = true;
                        break;
                    }
                }
                if (foundPair) break;
            }
        }
        return nums.empty();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ where $n$ is the number of elements in the array. This is because we are generating all possible pairs of elements and removing them from the array, which takes $O(n)$ time. We repeat this process until no more pairs can be found, which takes $O(n)$ time in the worst case. The inner loop takes $O(n)$ time.
> - **Space Complexity:** $O(1)$ if we ignore the space required for the input and output, as we are modifying the input array in place.
> - **Why these complexities occur:** The time complexity occurs because we are using nested loops to generate all possible pairs of elements and remove them from the array. The space complexity occurs because we are modifying the input array in place.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to keep track of the elements in the array. If we encounter an element that is equal to the top element of the stack, we can pop the top element from the stack. Otherwise, we can push the element onto the stack.
- Detailed breakdown of the approach:
  1. Initialize an empty stack.
  2. Iterate through the array. For each element, check if it is equal to the top element of the stack.
  3. If the element is equal to the top element of the stack, pop the top element from the stack.
  4. Otherwise, push the element onto the stack.
  5. After iterating through the entire array, check if the stack is empty. If it is, return `true`. Otherwise, return `false`.
- Proof of optimality: This approach is optimal because it uses a stack to keep track of the elements in the array, which allows us to efficiently check if an element is equal to the top element of the stack. This approach has a time complexity of $O(n)$, which is the best possible time complexity for this problem.

```cpp
class Solution {
public:
    bool canMakeEmpty(vector<int>& nums) {
        stack<int> s;
        for (int num : nums) {
            if (!s.empty() && s.top() == num) {
                s.pop();
            } else {
                s.push(num);
            }
        }
        return s.empty();
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of elements in the array. This is because we are iterating through the array once and using a stack to keep track of the elements.
> - **Space Complexity:** $O(n)$ if we ignore the space required for the input and output, as we are using a stack to keep track of the elements.
> - **Optimality proof:** This approach is optimal because it uses a stack to keep track of the elements in the array, which allows us to efficiently check if an element is equal to the top element of the stack.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a stack to keep track of elements in an array.
- Problem-solving patterns identified: Using a stack to efficiently check if an element is equal to the top element of the stack.
- Optimization techniques learned: Using a stack to reduce the time complexity of the algorithm.
- Similar problems to practice: Problems that involve using a stack to keep track of elements in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the stack is empty before popping an element from the stack.
- Edge cases to watch for: The array can be empty or contain only one element.
- Performance pitfalls: Using a nested loop to generate all possible pairs of elements, which can result in a high time complexity.
- Testing considerations: Test the algorithm with different inputs, including edge cases such as an empty array or an array with only one element.