## Statistics from a Large Sample
**Problem Link:** https://leetcode.com/problems/statistics-from-a-large-sample/description

**Problem Statement:**
- Input format and constraints: The problem takes an array of integers as input and returns an array of integers representing the count of numbers less than, equal to, and greater than the given number.
- Expected output format: An array of three integers, where the first integer represents the count of numbers less than the given number, the second integer represents the count of numbers equal to the given number, and the third integer represents the count of numbers greater than the given number.
- Key requirements and edge cases to consider: The input array can contain duplicate elements, and the given number can be present in the array.
- Example test cases with explanations:
  - Example 1: Input: `nums = [1, 2, 3, 4, 5]`, `n = 3`. Output: `[2, 1, 2]`. Explanation: There are 2 numbers less than 3 (1, 2), 1 number equal to 3 (3), and 2 numbers greater than 3 (4, 5).
  - Example 2: Input: `nums = [1, 1, 1, 1, 1]`, `n = 1`. Output: `[0, 5, 0]`. Explanation: There are 0 numbers less than 1, 5 numbers equal to 1 (all elements in the array), and 0 numbers greater than 1.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves iterating through the input array and comparing each element with the given number.
- Step-by-step breakdown of the solution:
  1. Initialize three counters: `lessThan`, `equalTo`, and `greaterThan`, to store the count of numbers less than, equal to, and greater than the given number, respectively.
  2. Iterate through the input array.
  3. For each element, compare it with the given number.
  4. If the element is less than the given number, increment the `lessThan` counter.
  5. If the element is equal to the given number, increment the `equalTo` counter.
  6. If the element is greater than the given number, increment the `greaterThan` counter.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, as it involves a simple iteration through the input array and comparison of each element with the given number.

```cpp
vector<int> countLessEqualGreater(vector<int>& nums, int n) {
    int lessThan = 0;
    int equalTo = 0;
    int greaterThan = 0;
    for (int num : nums) {
        if (num < n) {
            lessThan++;
        } else if (num == n) {
            equalTo++;
        } else {
            greaterThan++;
        }
    }
    return {lessThan, equalTo, greaterThan};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of elements in the input array. This is because we iterate through the input array once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the counters.
> - **Why these complexities occur:** The time complexity occurs because we iterate through the input array once, and the space complexity occurs because we use a constant amount of space to store the counters.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution involves using the same approach as the brute force solution, as it is already optimal.
- Detailed breakdown of the approach:
  1. Initialize three counters: `lessThan`, `equalTo`, and `greaterThan`, to store the count of numbers less than, equal to, and greater than the given number, respectively.
  2. Iterate through the input array.
  3. For each element, compare it with the given number.
  4. If the element is less than the given number, increment the `lessThan` counter.
  5. If the element is equal to the given number, increment the `equalTo` counter.
  6. If the element is greater than the given number, increment the `greaterThan` counter.
- Proof of optimality: This approach is optimal because it involves a single pass through the input array, which is necessary to count the numbers less than, equal to, and greater than the given number.
- Why further optimization is impossible: Further optimization is impossible because we must iterate through the input array at least once to count the numbers less than, equal to, and greater than the given number.

```cpp
vector<int> countLessEqualGreater(vector<int>& nums, int n) {
    int lessThan = 0;
    int equalTo = 0;
    int greaterThan = 0;
    for (int num : nums) {
        if (num < n) {
            lessThan++;
        } else if (num == n) {
            equalTo++;
        } else {
            greaterThan++;
        }
    }
    return {lessThan, equalTo, greaterThan};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m)$, where $m$ is the number of elements in the input array. This is because we iterate through the input array once.
> - **Space Complexity:** $O(1)$, as we use a constant amount of space to store the counters.
> - **Optimality proof:** The time complexity occurs because we iterate through the input array once, and the space complexity occurs because we use a constant amount of space to store the counters.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The problem demonstrates the use of counters to count the numbers less than, equal to, and greater than a given number.
- Problem-solving patterns identified: The problem involves a simple iteration through the input array and comparison of each element with the given number.
- Optimization techniques learned: The problem does not require any optimization techniques beyond the brute force solution.
- Similar problems to practice: Similar problems include counting the number of elements in an array that satisfy a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to initialize the counters or to increment them incorrectly.
- Edge cases to watch for: Edge cases include an empty input array or an input array with duplicate elements.
- Performance pitfalls: A performance pitfall is to iterate through the input array multiple times, which can increase the time complexity.
- Testing considerations: Testing considerations include testing the function with an empty input array, an input array with duplicate elements, and an input array with a large number of elements.