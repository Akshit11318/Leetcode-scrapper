## Asteroid Collision
**Problem Link:** https://leetcode.com/problems/asteroid-collision/description

**Problem Statement:**
- Input format and constraints: The input is a list of integers representing asteroids, where a positive integer denotes the size of an asteroid moving to the right and a negative integer denotes the size of an asteroid moving to the left. The list can contain at most 10,000 asteroids, and the size of each asteroid is in the range [1, 10000].
- Expected output format: The function should return a list of integers representing the final state of the asteroids after all collisions have occurred.
- Key requirements and edge cases to consider:
  - Two asteroids of equal size collide and both are destroyed.
  - A larger asteroid moving to the right collides with a smaller asteroid moving to the left, and the larger asteroid continues moving to the right.
  - A smaller asteroid moving to the right collides with a larger asteroid moving to the left, and the smaller asteroid is destroyed.
- Example test cases with explanations:
  - Input: `[5,10,-5]`, Output: `[5,10]`
  - Input: `[8,-8]`, Output: `[]`
  - Input: `[10,2,-5]`, Output: `[10]`
  - Input: `[-2,-1,1,2]`, Output: `[-2,-1,1,2]`

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Simulate the collision process by iterating through the list of asteroids and checking for collisions between adjacent asteroids.
- Step-by-step breakdown of the solution:
  1. Initialize an empty stack to store the asteroids that have not been destroyed.
  2. Iterate through the list of asteroids.
  3. For each asteroid, check if it collides with the asteroid at the top of the stack.
  4. If the asteroid collides with the top asteroid, compare their sizes and handle the collision accordingly.
  5. If the asteroid does not collide with the top asteroid, push it onto the stack.
- Why this approach comes to mind first: It is a straightforward approach that simulates the collision process.

```cpp
vector<int> asteroidCollision(vector<int>& asteroids) {
    stack<int> st;
    for (int asteroid : asteroids) {
        bool destroyed = false;
        while (!st.empty() && asteroid < 0 && st.top() > 0) {
            if (st.top() < -asteroid) {
                st.pop();
                continue;
            } else if (st.top() == -asteroid) {
                st.pop();
            }
            destroyed = true;
            break;
        }
        if (!destroyed) {
            st.push(asteroid);
        }
    }
    vector<int> result;
    while (!st.empty()) {
        result.push_back(st.top());
        st.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of asteroids. This is because in the worst case, we need to iterate through the stack for each asteroid.
> - **Space Complexity:** $O(n)$, where $n$ is the number of asteroids. This is because in the worst case, we need to store all asteroids in the stack.
> - **Why these complexities occur:** The time complexity occurs because of the nested loop structure, where we iterate through the list of asteroids and the stack. The space complexity occurs because we need to store the asteroids that have not been destroyed in the stack.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a stack to store the asteroids that have not been destroyed and handle collisions in a single pass.
- Detailed breakdown of the approach:
  1. Initialize an empty stack to store the asteroids that have not been destroyed.
  2. Iterate through the list of asteroids.
  3. For each asteroid, check if it collides with the asteroid at the top of the stack.
  4. If the asteroid collides with the top asteroid, compare their sizes and handle the collision accordingly.
  5. If the asteroid does not collide with the top asteroid, push it onto the stack.
- Proof of optimality: This approach has a time complexity of $O(n)$, where $n$ is the number of asteroids, because we only need to iterate through the list of asteroids once. The space complexity is also $O(n)$, where $n$ is the number of asteroids, because in the worst case, we need to store all asteroids in the stack.

```cpp
vector<int> asteroidCollision(vector<int>& asteroids) {
    stack<int> st;
    for (int asteroid : asteroids) {
        bool destroyed = false;
        while (!st.empty() && asteroid < 0 && st.top() > 0) {
            if (st.top() < -asteroid) {
                st.pop();
                continue;
            } else if (st.top() == -asteroid) {
                st.pop();
            }
            destroyed = true;
            break;
        }
        if (!destroyed) {
            st.push(asteroid);
        }
    }
    vector<int> result;
    while (!st.empty()) {
        result.push_back(st.top());
        st.pop();
    }
    reverse(result.begin(), result.end());
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of asteroids. This is because we only need to iterate through the list of asteroids once.
> - **Space Complexity:** $O(n)$, where $n$ is the number of asteroids. This is because in the worst case, we need to store all asteroids in the stack.
> - **Optimality proof:** This approach is optimal because we only need to iterate through the list of asteroids once, and we use a stack to store the asteroids that have not been destroyed. This approach has the best possible time and space complexity for this problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Stack data structure, collision detection, and handling.
- Problem-solving patterns identified: Using a stack to store and handle collisions between asteroids.
- Optimization techniques learned: Reducing the time complexity from $O(n^2)$ to $O(n)$ by using a stack to handle collisions in a single pass.
- Similar problems to practice: Other problems that involve collision detection and handling, such as [https://leetcode.com/problems/interval-list-intersections/](https://leetcode.com/problems/interval-list-intersections/).

**Mistakes to Avoid:**
- Common implementation errors: Not handling the case where an asteroid collides with the top asteroid and both are destroyed.
- Edge cases to watch for: Handling the case where the input list is empty or contains only one asteroid.
- Performance pitfalls: Using a nested loop structure that results in a time complexity of $O(n^2)$.
- Testing considerations: Testing the function with different input cases, including edge cases and large inputs.