## Contains Duplicate

**Problem Link:** https://leetcode.com/problems/contains-duplicate/description

**Problem Statement:**
- Input format and constraints: Given an integer array `nums` of size `n`, return `true` if there are any duplicate elements in the array and `false` otherwise.
- Expected output format: A boolean value indicating the presence of duplicates.
- Key requirements and edge cases to consider: Empty arrays, arrays with a single element, arrays with duplicate elements, and arrays with all unique elements.
- Example test cases with explanations:
  - `nums = [1, 2, 3, 1]`, return `true` because there are duplicate elements.
  - `nums = [1, 2, 3, 4]`, return `false` because there are no duplicate elements.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Check every pair of elements in the array to see if there are any duplicates.
- Step-by-step breakdown of the solution: Iterate through the array with two nested loops, comparing each element with every other element.
- Why this approach comes to mind first: It's a straightforward, intuitive way to check for duplicates, but it's not efficient for large arrays.

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        int n = nums.size();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (nums[i] == nums[j]) {
                    return true;
                }
            }
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array, because we're using two nested loops to compare each pair of elements.
> - **Space Complexity:** $O(1)$, because we're not using any additional space that scales with the input size.
> - **Why these complexities occur:** The nested loops cause the quadratic time complexity, and the lack of additional data structures that scale with the input size results in constant space complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `unordered_set` to store unique elements as we iterate through the array, and return `true` as soon as we encounter a duplicate.
- Detailed breakdown of the approach: Iterate through the array, adding each element to the `unordered_set`. If an element is already in the set, return `true`.
- Proof of optimality: This approach has a time complexity of $O(n)$ because looking up an element in an `unordered_set` takes constant time on average.
- Why further optimization is impossible: We must examine each element at least once to determine if there are duplicates, so a time complexity better than $O(n)$ is not possible.

```cpp
class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> uniqueElements;
        for (int num : nums) {
            if (uniqueElements.find(num) != uniqueElements.end()) {
                return true;
            }
            uniqueElements.insert(num);
        }
        return false;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array, because we're doing a constant amount of work for each element.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store all elements in the `unordered_set`.
> - **Optimality proof:** We've achieved the best possible time complexity because we only examine each element once, and we use an `unordered_set` for constant-time lookups.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using a `unordered_set` for efficient lookups and avoiding unnecessary comparisons.
- Problem-solving patterns identified: Breaking down the problem into smaller, more manageable parts (in this case, checking for duplicates one element at a time).
- Optimization techniques learned: Using data structures that offer fast lookup times to reduce overall time complexity.
- Similar problems to practice: Other problems involving duplicate detection or set operations.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases (like empty arrays or arrays with a single element), and using inefficient data structures or algorithms.
- Edge cases to watch for: Empty arrays, arrays with a single element, and arrays with all unique elements.
- Performance pitfalls: Using nested loops or other inefficient algorithms for large inputs.
- Testing considerations: Thoroughly testing the solution with a variety of inputs, including edge cases, to ensure correctness.