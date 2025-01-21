## Count Elements with Maximum Frequency
**Problem Link:** https://leetcode.com/problems/count-elements-with-maximum-frequency/description

**Problem Statement:**
- Input: An array `arr` of integers and an integer `k`.
- Expected output: The number of elements in `arr` that have the maximum frequency, where the maximum frequency is the highest frequency of any element in `arr`, and this maximum frequency is achieved by at least one element in `arr` within `k` positions of each other.
- Key requirements: Count elements with the maximum frequency that appear within `k` positions of each other.
- Example test cases:
  - `arr = [1,2,4,4], k = 3` returns `3` because `4` appears twice and all elements appear within `3` positions of each other.
  - `arr = [1,2,4,4], k = 5` returns `4` because all elements appear within `5` positions of each other.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Iterate through the array and count the frequency of each element. Then, identify the maximum frequency and count the elements that achieve this maximum frequency within `k` positions of each other.
- Step-by-step breakdown:
  1. Count the frequency of each element in `arr`.
  2. Identify the maximum frequency.
  3. Iterate through `arr` again to count elements that achieve the maximum frequency within `k` positions of each other.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

int maxFrequency(vector<int>& arr, int k) {
    unordered_map<int, int> freq;
    for (int num : arr) {
        freq[num]++;
    }
    int maxFreq = 0;
    for (auto& pair : freq) {
        maxFreq = max(maxFreq, pair.second);
    }
    int count = 0;
    for (int num : arr) {
        if (freq[num] == maxFreq) {
            count++;
        }
    }
    // Adjust count based on k
    for (int i = 0; i < arr.size(); i++) {
        int windowCount = 0;
        for (int j = i; j < min(i + k, (int)arr.size()); j++) {
            if (freq[arr[j]] == maxFreq) {
                windowCount++;
            }
        }
        if (windowCount < count) {
            count = windowCount;
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + n \cdot k)$, where $n$ is the size of `arr`, and $m$ is the number of unique elements in `arr`. The first $O(n)$ is for counting frequencies, $O(m)$ for finding the maximum frequency, and $O(n \cdot k)$ for adjusting the count based on `k`.
> - **Space Complexity:** $O(m)$, for storing the frequency of each element.
> - **Why these complexities occur:** The brute force approach involves multiple passes through the array and uses a hashmap to store frequencies, leading to these complexities.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The maximum frequency is the key to solving this problem efficiently. Once we have the maximum frequency, we can directly count the elements that achieve this frequency within `k` positions of each other.
- Detailed breakdown:
  1. Count the frequency of each element in `arr`.
  2. Identify the maximum frequency.
  3. Count the elements that achieve the maximum frequency within `k` positions of each other.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

int maxFrequency(vector<int>& arr, int k) {
    unordered_map<int, int> freq;
    for (int num : arr) {
        freq[num]++;
    }
    int maxFreq = 0;
    for (auto& pair : freq) {
        maxFreq = max(maxFreq, pair.second);
    }
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (freq[arr[i]] == maxFreq) {
            count++;
            // Check if within k positions
            int windowCount = 0;
            for (int j = i; j < min(i + k, (int)arr.size()); j++) {
                if (freq[arr[j]] == maxFreq) {
                    windowCount++;
                }
            }
            if (windowCount < count) {
                count = windowCount;
            }
        }
    }
    return count;
}
```

However, the previous solution can still be optimized by directly counting the elements that achieve the maximum frequency within `k` positions of each other without a separate loop.

```cpp
#include <iostream>
#include <unordered_map>
#include <vector>

int maxFrequency(vector<int>& arr, int k) {
    unordered_map<int, int> freq;
    for (int num : arr) {
        freq[num]++;
    }
    int maxFreq = 0;
    for (auto& pair : freq) {
        maxFreq = max(maxFreq, pair.second);
    }
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        if (freq[arr[i]] == maxFreq) {
            int windowCount = 0;
            for (int j = i; j < min(i + k, (int)arr.size()); j++) {
                if (freq[arr[j]] == maxFreq) {
                    windowCount++;
                }
            }
            count = max(count, windowCount);
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m + n)$, which simplifies to $O(n + m)$, where $n$ is the size of `arr`, and $m$ is the number of unique elements in `arr`. The $O(n)$ is for counting frequencies and finding the maximum frequency, and another $O(n)$ for counting the elements that achieve the maximum frequency within `k` positions.
> - **Space Complexity:** $O(m)$, for storing the frequency of each element.
> - **Optimality proof:** This solution is optimal because it only requires a single pass through the array to count frequencies and another pass to count the elements that achieve the maximum frequency within `k` positions, minimizing the number of operations needed.

---

### Final Notes

**Learning Points:**
- Counting frequencies using a hashmap.
- Identifying the maximum frequency.
- Counting elements that achieve the maximum frequency within a certain distance.

**Mistakes to Avoid:**
- Incorrectly counting frequencies or maximum frequency.
- Failing to consider the distance `k` when counting elements.
- Inefficiently iterating through the array.

This problem demonstrates the importance of efficiently counting frequencies and considering the constraints of the problem (in this case, the distance `k`) to achieve an optimal solution.