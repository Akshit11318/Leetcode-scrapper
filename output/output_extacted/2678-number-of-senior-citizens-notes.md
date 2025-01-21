## Number of Senior Citizens

**Problem Link:** https://leetcode.com/problems/number-of-senior-citizens/description

**Problem Statement:**
- Input format: A list of integers representing the ages of people
- Constraints: The list will contain at least one element and at most 100 elements. Each age will be between 0 and 150.
- Expected output format: The number of people who are 60 years old or older
- Key requirements and edge cases to consider: The function should handle empty lists, lists with a single element, and lists with multiple elements. It should also handle cases where there are no senior citizens and cases where all people are senior citizens.
- Example test cases with explanations:
  - Input: `[65, 45, 59, 60, 70]`
    - Output: `3`
    - Explanation: The people with ages 65, 60, and 70 are senior citizens.
  - Input: `[59, 59, 59]`
    - Output: `0`
    - Explanation: There are no senior citizens in the list.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We need to iterate through the list of ages and count the number of people who are 60 years old or older.
- Step-by-step breakdown of the solution:
  1. Initialize a counter variable to 0.
  2. Iterate through the list of ages.
  3. For each age, check if it is 60 or older.
  4. If it is, increment the counter.
  5. After iterating through the entire list, return the counter.
- Why this approach comes to mind first: It is a straightforward solution that directly addresses the problem statement.

```cpp
int countSeniors(vector<int>& ages) {
    int count = 0;
    for (int age : ages) {
        if (age >= 60) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the list, because we are iterating through the list once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the counter variable.
> - **Why these complexities occur:** The time complexity is linear because we are performing a constant amount of work for each element in the list. The space complexity is constant because we are not using any data structures that grow with the size of the input.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The brute force approach is already optimal because we need to examine each element in the list at least once to determine if it is a senior citizen.
- Detailed breakdown of the approach: The optimal approach is the same as the brute force approach.
- Proof of optimality: We cannot do better than $O(n)$ time complexity because we need to examine each element in the list at least once.
- Why further optimization is impossible: We are already using the minimum amount of time and space necessary to solve the problem.

```cpp
int countSeniors(vector<int>& ages) {
    int count = 0;
    for (int age : ages) {
        if (age >= 60) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the list, because we are iterating through the list once.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the counter variable.
> - **Optimality proof:** The time complexity is optimal because we need to examine each element in the list at least once. The space complexity is optimal because we are not using any data structures that grow with the size of the input.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Iteration, conditional statements, and counter variables.
- Problem-solving patterns identified: Directly addressing the problem statement and using a brute force approach.
- Optimization techniques learned: Recognizing when a brute force approach is already optimal.
- Similar problems to practice: Other problems that involve iterating through a list and counting elements that meet a certain condition.

**Mistakes to Avoid:**
- Common implementation errors: Off-by-one errors, incorrect conditional statements, and forgetting to initialize variables.
- Edge cases to watch for: Empty lists, lists with a single element, and lists with multiple elements.
- Performance pitfalls: Using data structures that grow with the size of the input when a constant amount of space is sufficient.
- Testing considerations: Testing the function with different types of input, including edge cases, to ensure it works correctly.