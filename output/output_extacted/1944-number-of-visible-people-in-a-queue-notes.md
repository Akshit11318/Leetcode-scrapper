## Number of Visible People in a Queue

**Problem Link:** https://leetcode.com/problems/number-of-visible-people-in-a-queue/description

**Problem Statement:**
- Input format and constraints: The problem takes a 2D array `heights` as input, where `heights[i]` is an array representing the heights of people standing in the `i-th` queue. Each `heights[i]` contains integers representing the heights of people in that queue.
- Expected output format: The function should return an array of integers where the `i-th` integer represents the number of people visible when looking at the `i-th` queue.
- Key requirements and edge cases to consider: A person is considered visible if there is no one in front of them who is taller or of the same height. We need to consider edge cases where a queue is empty or contains only one person.
- Example test cases with explanations:
  - Input: `heights = [[10,6,8,4],[3,2,5],[4,3],[5,2,3]]`
  - Output: `[2,1,1,2]`
  - Explanation: For the first queue, only the first and third people are visible. For the second queue, only the first person is visible. For the third queue, only the first person is visible. For the fourth queue, the first and third people are visible.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: We can iterate through each queue and for each person, check if there is anyone in front of them who is taller or of the same height. If not, we increment the count of visible people for that queue.
- Step-by-step breakdown of the solution:
  1. Initialize an array `visible` to store the count of visible people for each queue.
  2. Iterate through each queue in `heights`.
  3. For each queue, initialize a variable `count` to 0.
  4. Iterate through each person in the queue.
  5. For each person, check if there is anyone in front of them who is taller or of the same height. If not, increment `count`.
  6. After checking all people in the queue, store `count` in the corresponding index in `visible`.
- Why this approach comes to mind first: It is a straightforward approach that directly addresses the problem statement.

```cpp
vector<int> canSeePersonsCount(vector<vector<int>>& heights) {
    vector<int> visible(heights.size(), 0);
    for (int i = 0; i < heights.size(); i++) {
        int count = 0;
        for (int j = 0; j < heights[i].size(); j++) {
            bool isVisible = true;
            for (int k = 0; k < j; k++) {
                if (heights[i][k] >= heights[i][j]) {
                    isVisible = false;
                    break;
                }
            }
            if (isVisible) count++;
        }
        visible[i] = count;
    }
    return visible;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m^2)$, where $n$ is the number of queues and $m$ is the maximum number of people in a queue. This is because for each queue, we are iterating through each person and for each person, we are checking all the people in front of them.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queues. This is because we are storing the count of visible people for each queue in the `visible` array.
> - **Why these complexities occur:** The time complexity occurs because of the nested loops used to iterate through each person in each queue and check the people in front of them. The space complexity occurs because we need to store the count of visible people for each queue.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to keep track of the indices of people who are visible. We start from the end of the queue and iterate backwards. For each person, we pop all the people from the stack who are shorter than the current person and then push the current person onto the stack.
- Detailed breakdown of the approach:
  1. Initialize an array `visible` to store the count of visible people for each queue.
  2. Iterate through each queue in `heights`.
  3. For each queue, initialize a stack to store the indices of visible people.
  4. Iterate through each person in the queue from the end to the beginning.
  5. For each person, pop all the people from the stack who are shorter than the current person and increment the count of visible people for the current queue.
  6. After popping, push the current person onto the stack.
  7. After checking all people in the queue, store the count of visible people in the corresponding index in `visible`.
- Proof of optimality: This approach is optimal because we only need to iterate through each queue once and for each person, we only need to pop and push from the stack a constant number of times. This reduces the time complexity from $O(n \cdot m^2)$ to $O(n \cdot m)$.

```cpp
vector<int> canSeePersonsCount(vector<vector<int>>& heights) {
    vector<int> visible(heights.size(), 0);
    for (int i = 0; i < heights.size(); i++) {
        stack<int> st;
        for (int j = heights[i].size() - 1; j >= 0; j--) {
            while (!st.empty() && heights[i][st.top()] <= heights[i][j]) {
                st.pop();
                visible[i]++;
            }
            if (!st.empty()) visible[i]++;
            st.push(j);
        }
    }
    return visible;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of queues and $m$ is the maximum number of people in a queue. This is because we are iterating through each queue once and for each person, we are performing a constant amount of work.
> - **Space Complexity:** $O(n \cdot m)$, where $n$ is the number of queues and $m$ is the maximum number of people in a queue. This is because we are using a stack to store the indices of visible people for each queue.
> - **Optimality proof:** This approach is optimal because we are only iterating through each queue once and for each person, we are performing a constant amount of work. This reduces the time complexity from $O(n \cdot m^2)$ to $O(n \cdot m)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The use of stacks to keep track of visible people.
- Problem-solving patterns identified: The use of iteration from the end to the beginning to simplify the problem.
- Optimization techniques learned: The use of stacks to reduce the time complexity from $O(n \cdot m^2)$ to $O(n \cdot m)$.
- Similar problems to practice: Problems involving the use of stacks to keep track of visible or accessible elements.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for the case where the stack is empty before popping or pushing elements.
- Edge cases to watch for: The case where a queue is empty or contains only one person.
- Performance pitfalls: Using a brute force approach that has a time complexity of $O(n \cdot m^2)$.
- Testing considerations: Testing the function with different inputs, including edge cases, to ensure that it produces the correct output.