## Daily Temperatures
**Problem Link:** https://leetcode.com/problems/daily-temperatures/description

**Problem Statement:**
- Input format and constraints: Given an array of integers representing daily temperatures, where `temperatures[i]` represents the temperature on the `i-th` day, and the length of the array is in the range `[1, 30,000]`. The temperature is an integer in the range `[-10^8, 10^8]`.
- Expected output format: Return an array `answer` such that `answer[i]` is the number of days until a warmer temperature for each day.
- Key requirements and edge cases to consider: 
    * If there is no future day with a warmer temperature, the answer is `0`.
    * The input array is non-empty and contains at least one element.
- Example test cases with explanations: 
    * Example 1: Input: `temperatures = [73,74,75,71,69,72,76,73]`, Output: `[1,1,4,2,1,1,0,0]`.
    * Example 2: Input: `temperatures = [10,20,30,40,50,60]`, Output: `[1,1,1,1,1,0]`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: For each day, we can check all future days to find the first day with a warmer temperature.
- Step-by-step breakdown of the solution:
    1. Iterate over each day in the input array.
    2. For each day, iterate over all future days to find the first day with a warmer temperature.
    3. If a warmer temperature is found, calculate the number of days until that warmer temperature.
    4. If no warmer temperature is found, set the answer to `0`.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> answer(n, 0);
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (temperatures[j] > temperatures[i]) {
                answer[i] = j - i;
                break;
            }
        }
    }
    return answer;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of days. This is because we have a nested loop structure, where the outer loop iterates over each day, and the inner loop iterates over all future days.
> - **Space Complexity:** $O(n)$, where $n$ is the number of days. This is because we need to store the answer for each day in the output array.
> - **Why these complexities occur:** The time complexity occurs because of the nested loop structure, and the space complexity occurs because of the need to store the output array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to keep track of the indices of the days for which we have not yet found a warmer temperature. When we encounter a day with a warmer temperature, we can pop the indices from the stack and calculate the answer for those days.
- Detailed breakdown of the approach:
    1. Initialize an empty stack to store the indices of the days.
    2. Iterate over each day in the input array.
    3. If the stack is not empty and the current day's temperature is greater than the temperature of the day at the top of the stack, pop the top index from the stack and calculate the answer for that day.
    4. Push the current index onto the stack.
- Proof of optimality: This approach is optimal because we only need to iterate over the input array once, and we use a stack to efficiently keep track of the indices of the days for which we have not yet found a warmer temperature.

```cpp
vector<int> dailyTemperatures(vector<int>& temperatures) {
    int n = temperatures.size();
    vector<int> answer(n, 0);
    stack<int> st;
    for (int i = 0; i < n; i++) {
        while (!st.empty() && temperatures[i] > temperatures[st.top()]) {
            int idx = st.top();
            st.pop();
            answer[idx] = i - idx;
        }
        st.push(i);
    }
    return answer;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of days. This is because we only need to iterate over the input array once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of days. This is because in the worst case, we may need to push all indices onto the stack.
> - **Optimality proof:** This approach is optimal because we only need to iterate over the input array once, and we use a stack to efficiently keep track of the indices of the days for which we have not yet found a warmer temperature.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Stack data structure, iteration over an array.
- Problem-solving patterns identified: Using a stack to keep track of indices, iterating over an array to find a warmer temperature.
- Optimization techniques learned: Using a stack to reduce the time complexity from $O(n^2)$ to $O(n)$.
- Similar problems to practice: Problems involving iteration over an array and using a stack to keep track of indices.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the stack is empty before popping an element, not updating the answer array correctly.
- Edge cases to watch for: Handling the case where the input array is empty, handling the case where there is no future day with a warmer temperature.
- Performance pitfalls: Using a nested loop structure, which can lead to a time complexity of $O(n^2)$.
- Testing considerations: Testing the function with different input arrays, including edge cases such as an empty array or an array with a single element.