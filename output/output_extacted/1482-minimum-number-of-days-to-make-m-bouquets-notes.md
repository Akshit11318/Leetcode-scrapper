## Minimum Number of Days to Make m Bouquets
**Problem Link:** https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/description

**Problem Statement:**
- Input: `n` (number of flowers), `m` (number of bouquets), `bloomDay` (array of bloom days for each flower)
- Constraints: `1 <= n <= 10^5`, `1 <= m <= n`
- Expected output: The minimum number of days to make `m` bouquets, or `-1` if it's impossible.
- Key requirements: Find the minimum number of days to make `m` bouquets.
- Edge cases: Consider cases where it's impossible to make `m` bouquets.

**Example Test Cases:**
- `n = 3`, `m = 1`, `bloomDay = [1, 2, 3]`, output: `2`
- `n = 3`, `m = 2`, `bloomDay = [1, 2, 3]`, output: `3`
- `n = 3`, `m = 3`, `bloomDay = [1, 2, 3]`, output: `3`

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of days and check if it's possible to make `m` bouquets on each day.
- Step-by-step breakdown:
  1. Iterate over all possible days from the minimum bloom day to the maximum bloom day.
  2. For each day, iterate over the `bloomDay` array and count the number of flowers that have bloomed.
  3. If the number of bloomed flowers is greater than or equal to `m`, update the minimum number of days.

```cpp
int minDays(int n, int m, vector<int>& bloomDay) {
    int minDay = INT_MAX;
    for (int day = 1; day <= 100000; day++) {
        int bloomed = 0;
        for (int i = 0; i < n; i++) {
            if (bloomDay[i] <= day) {
                bloomed++;
            }
        }
        if (bloomed >= m) {
            minDay = min(minDay, day);
        }
    }
    return minDay == INT_MAX ? -1 : minDay;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot 10^5)$, where $n$ is the number of flowers. This is because we iterate over all possible days and for each day, we iterate over the `bloomDay` array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum number of days.
> - **Why these complexities occur:** The time complexity is high because we try all possible combinations of days, and the space complexity is low because we only use a constant amount of space.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a binary search approach to find the minimum number of days.
- Detailed breakdown:
  1. Initialize the minimum and maximum possible days.
  2. Perform a binary search between the minimum and maximum possible days.
  3. For each mid-day, count the number of flowers that have bloomed.
  4. If the number of bloomed flowers is greater than or equal to `m`, update the minimum possible day.

```cpp
int minDays(int n, int m, vector<int>& bloomDay) {
    if (n < m) return -1;
    int low = *min_element(bloomDay.begin(), bloomDay.end());
    int high = *max_element(bloomDay.begin(), bloomDay.end());
    while (low < high) {
        int mid = low + (high - low) / 2;
        int bloomed = 0;
        for (int i = 0; i < n; i++) {
            if (bloomDay[i] <= mid) {
                bloomed++;
            }
        }
        if (bloomed < m) {
            low = mid + 1;
        } else {
            high = mid;
        }
    }
    return low;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log k)$, where $n$ is the number of flowers and $k$ is the maximum possible day. This is because we perform a binary search between the minimum and maximum possible days, and for each mid-day, we iterate over the `bloomDay` array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the minimum and maximum possible days.
> - **Optimality proof:** This is the optimal solution because we use a binary search approach to find the minimum number of days, which reduces the time complexity from $O(n \cdot 10^5)$ to $O(n \log k)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: binary search, counting.
- Problem-solving patterns identified: using binary search to find the minimum or maximum value.
- Optimization techniques learned: reducing the time complexity by using a binary search approach.

**Mistakes to Avoid:**
- Common implementation errors: not handling edge cases, not using a binary search approach.
- Edge cases to watch for: cases where it's impossible to make `m` bouquets.
- Performance pitfalls: using a brute force approach, not optimizing the time complexity.
- Testing considerations: testing the function with different inputs, including edge cases.