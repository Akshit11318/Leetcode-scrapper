## Diet Plan Performance
**Problem Link:** https://leetcode.com/problems/diet-plan-performance/description

**Problem Statement:**
- Input: `int` array `calories`, `int` `k`, `int` `lower`, and `int` `upper`
- Constraints: `1 <= k <= calories.length <= 10^5`, `0 <= calories[i] <= 10^5`, `0 <= lower <= upper <= 10^9`
- Expected Output: The number of days when your total calories are in the range `[lower, upper]`
- Key Requirements: Calculate the total calories for each day and check if it falls within the given range
- Example Test Cases:
  - `calories = [1,2,3,4,5], k = 1, lower = 3, upper = 3`
  - `calories = [3,5], k = 2, lower = 1, upper = 5`

---

### Brute Force Approach

**Explanation:**
- Calculate the total calories for each day by summing up `k` consecutive days
- Check if the total calories fall within the given range `[lower, upper]`
- Count the number of days that satisfy the condition

```cpp
int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
    int n = calories.size();
    int count = 0;
    for (int i = 0; i <= n - k; i++) {
        int totalCalories = 0;
        for (int j = i; j < i + k; j++) {
            totalCalories += calories[j];
        }
        if (totalCalories >= lower && totalCalories <= upper) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot k)$, where $n$ is the length of the `calories` array and $k$ is the number of consecutive days
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the `count` variable
> - **Why these complexities occur:** The nested loops cause the time complexity to be quadratic, and the constant space usage results in a space complexity of $O(1)$

---

### Optimal Approach (Required)

**Explanation:**
- Use a sliding window approach to calculate the total calories for each day
- Maintain a running sum of `k` consecutive days and update it as we slide the window
- Check if the total calories fall within the given range `[lower, upper]` and count the number of days that satisfy the condition

```cpp
int dietPlanPerformance(vector<int>& calories, int k, int lower, int upper) {
    int n = calories.size();
    int count = 0;
    int windowSum = 0;
    for (int i = 0; i < n; i++) {
        windowSum += calories[i];
        if (i >= k) {
            windowSum -= calories[i - k];
        }
        if (i >= k - 1 && windowSum >= lower && windowSum <= upper) {
            count++;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the `calories` array
> - **Space Complexity:** $O(1)$, since we only use a constant amount of space to store the `count` and `windowSum` variables
> - **Optimality proof:** The sliding window approach allows us to calculate the total calories for each day in constant time, resulting in a linear time complexity

---

### Final Notes

**Learning Points:**
- The importance of using a sliding window approach to reduce time complexity
- How to maintain a running sum of `k` consecutive days and update it as we slide the window
- The benefits of using a single pass through the data to calculate the result

**Mistakes to Avoid:**
- Using nested loops to calculate the total calories for each day, resulting in a high time complexity
- Not updating the running sum correctly as we slide the window
- Not checking the edge cases where `i < k - 1` to avoid incorrect results

---