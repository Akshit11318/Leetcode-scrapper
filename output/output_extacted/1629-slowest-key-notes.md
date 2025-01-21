## Slowing Down the Key Presses
**Problem Link:** https://leetcode.com/problems/slowest-key/description

**Problem Statement:**
- Input format: A string `s` and an array of integers `releaseTimes` where `releaseTimes[i]` represents the time at which the key `s[i]` was released.
- Constraints: `2 <= s.length <= 10^5`, `s` consists only of lowercase English letters, `releaseTimes.length == s.length`, `0 <= releaseTimes[i] <= 10^9`.
- Expected output format: The character that was pressed for the longest duration.
- Key requirements and edge cases to consider:
  - Handling ties: If multiple keys are pressed for the same longest duration, return the one that appears earliest in the alphabet.
  - Edge case: All keys are pressed for the same duration.

**Example Test Cases:**
- Input: `s = "abc"`, `releaseTimes = [3, 2, 1]`
  Output: `"a"`
  Explanation: The key "a" was pressed for 3 seconds, "b" for 2 seconds, and "c" for 1 second.

### Brute Force Approach
**Explanation:**
- The initial thought process is to iterate through each character in the string and calculate the duration it was pressed.
- We then compare these durations to find the character that was pressed for the longest duration.

```cpp
class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string s) {
        int n = s.length();
        int maxDuration = 0;
        char slowestKey = s[0];
        
        for (int i = 0; i < n; i++) {
            int duration = (i == 0) ? releaseTimes[i] : releaseTimes[i] - releaseTimes[i - 1];
            if (duration > maxDuration || (duration == maxDuration && s[i] < slowestKey)) {
                maxDuration = duration;
                slowestKey = s[i];
            }
        }
        
        return slowestKey;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`. This is because we make a single pass through the string.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the maximum duration and the slowest key.
> - **Why these complexities occur:** The time complexity is linear because we process each character in the string once. The space complexity is constant because we do not use any data structures that grow with the input size.

### Optimal Approach (Required)
**Explanation:**
- The optimal approach is the same as the brute force approach because we must examine each character in the string at least once to determine the slowest key.
- The key insight is to maintain a running maximum duration and update it as we iterate through the string, comparing the current duration with the maximum found so far.
- This approach is optimal because it achieves the minimum required time complexity of $O(n)$.

```cpp
class Solution {
public:
    char slowestKey(vector<int>& releaseTimes, string s) {
        int n = s.length();
        int maxDuration = 0;
        char slowestKey = s[0];
        
        for (int i = 0; i < n; i++) {
            int duration = (i == 0) ? releaseTimes[i] : releaseTimes[i] - releaseTimes[i - 1];
            if (duration > maxDuration || (duration == maxDuration && s[i] < slowestKey)) {
                maxDuration = duration;
                slowestKey = s[i];
            }
        }
        
        return slowestKey;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the string `s`.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space.
> - **Optimality proof:** This is the optimal approach because we must process each character at least once, resulting in a lower bound of $O(n)$ time complexity.

### Final Notes

**Learning Points:**
- The importance of maintaining a running maximum or minimum when comparing elements in a sequence.
- How to handle ties in a comparison, particularly when there are additional criteria such as alphabetical order.
- The principle that sometimes the brute force approach can be optimal if it already achieves the minimum required time complexity.

**Mistakes to Avoid:**
- Failing to consider edge cases, such as when all keys are pressed for the same duration.
- Not handling ties correctly, particularly in terms of additional comparison criteria.
- Overcomplicating the solution by introducing unnecessary complexity or data structures.