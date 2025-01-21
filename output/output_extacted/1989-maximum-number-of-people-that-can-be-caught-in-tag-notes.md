## Maximum Number of People That Can Be Caught in Tag

**Problem Link:** https://leetcode.com/problems/maximum-number-of-people-that-can-be-caught-in-tag/description

**Problem Statement:**
- Input: An array of `distances` representing the distance each person is from the tagger, and an array of `speeds` representing the speed of each person.
- Constraints: The length of `distances` and `speeds` is the same, and the lengths are between $1$ and $10^5$.
- Expected Output: The maximum number of people that can be caught in tag.
- Key Requirements: To find the maximum number of people that can be caught, we need to consider the time it takes for the tagger to catch each person and the time it takes for the person to be caught.
- Example Test Cases: 
  - `distances = [1,2,3,4], speeds = [1,1,1,1]`, the output should be `4`.
  - `distances = [1,2,3,4], speeds = [1,2,3,4]`, the output should be `1`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to calculate the time it takes for the tagger to catch each person and sort these times.
- Then, we can iterate through the sorted times and count the number of people that can be caught.
- This approach comes to mind first because it directly addresses the problem statement by considering the time it takes to catch each person.

```cpp
class Solution {
public:
    int catchMaximumAmountOfPeople(vector<int>& distances, vector<int>& speeds) {
        int n = distances.size();
        vector<double> times;
        
        // Calculate the time it takes for the tagger to catch each person
        for (int i = 0; i < n; i++) {
            times.push_back((double)distances[i] / speeds[i]);
        }
        
        // Sort the times
        sort(times.begin(), times.end());
        
        int count = 0;
        double currentTime = 0;
        
        // Iterate through the sorted times and count the number of people that can be caught
        for (int i = 0; i < n; i++) {
            if (currentTime <= times[i]) {
                count++;
                currentTime = times[i];
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(n)$ for storing the times.
> - **Why these complexities occur:** The sorting operation dominates the time complexity, and the space complexity is due to the additional space needed to store the times.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to realize that we only need to consider the time it takes for the tagger to catch each person and the fact that the tagger can catch a person if the tagger's time to catch is less than or equal to the person's time to be caught.
- This approach is optimal because it directly addresses the problem statement with the minimum number of operations required.
- The proof of optimality is that any other approach would require more operations, such as sorting or iterating through the times multiple times.

```cpp
class Solution {
public:
    int catchMaximumAmountOfPeople(vector<int>& distances, vector<int>& speeds) {
        int n = distances.size();
        vector<double> times;
        
        // Calculate the time it takes for the tagger to catch each person
        for (int i = 0; i < n; i++) {
            times.push_back((double)distances[i] / speeds[i]);
        }
        
        // Sort the times
        sort(times.begin(), times.end());
        
        int count = 0;
        double currentTime = 0;
        
        // Iterate through the sorted times and count the number of people that can be caught
        for (int i = 0; i < n; i++) {
            if (currentTime <= times[i]) {
                count++;
                currentTime = times[i];
            }
        }
        
        return count;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$ due to the sorting operation.
> - **Space Complexity:** $O(n)$ for storing the times.
> - **Optimality proof:** This approach is optimal because it directly addresses the problem statement with the minimum number of operations required.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: sorting and iterating through times.
- Problem-solving patterns identified: considering the time it takes for the tagger to catch each person and the fact that the tagger can catch a person if the tagger's time to catch is less than or equal to the person's time to be caught.
- Optimization techniques learned: using the minimum number of operations required to solve the problem.
- Similar problems to practice: problems that involve sorting and iterating through times, such as scheduling problems.

**Mistakes to Avoid:**
- Common implementation errors: not considering the time it takes for the tagger to catch each person, or not sorting the times correctly.
- Edge cases to watch for: cases where the distances or speeds are zero, or cases where the times are equal.
- Performance pitfalls: using more operations than necessary to solve the problem, such as sorting the times multiple times.
- Testing considerations: testing the solution with different inputs, such as different distances and speeds, and testing the edge cases.