## Minimum Swaps to Group All 1s Together II
**Problem Link:** https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together-ii/description

**Problem Statement:**
- Input: A binary array `data`.
- Output: The minimum number of swaps required to group all `1`s together.
- Constraints: The input array `data` contains only `0`s and `1`s.
- Key Requirements: Find the minimum number of swaps to group all `1`s together in the array.
- Edge Cases: Handle cases where there are no `1`s in the array or when all elements are `1`s.

**Example Test Cases:**
- Input: `data = [1,0,1,0,1]`
  Output: `1`
  Explanation: We can swap the first and the third element to get `[1,1,0,0,1]`.
- Input: `data = [1,0,1,0,1,0,0,1,1,0,1]`
  Output: `3`
  Explanation: We need at least 3 swaps to group all `1`s together.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of swaps and check if all `1`s are grouped together.
- This approach involves generating all permutations of the array and checking each permutation to see if it satisfies the condition.

```cpp
class Solution {
public:
    int minSwaps(vector<int>& data) {
        int n = data.size();
        int ones = 0;
        // Count the number of ones in the array
        for (int i = 0; i < n; i++) {
            if (data[i] == 1) ones++;
        }
        
        // Generate all permutations and check each one
        int minSwaps = INT_MAX;
        do {
            int swaps = 0;
            bool grouped = true;
            for (int i = 0; i < ones; i++) {
                if (data[i] == 0) {
                    swaps++;
                }
            }
            minSwaps = min(minSwaps, swaps);
        } while (next_permutation(data.begin(), data.end()));
        
        return minSwaps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n!)$, where $n$ is the size of the input array. This is because we are generating all permutations of the array.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Why these complexities occur:** The brute force approach involves trying all possible permutations, which leads to an exponential time complexity.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use a sliding window approach to find the minimum number of swaps required to group all `1`s together.
- We maintain a window of size equal to the number of `1`s in the array and slide it over the array to find the minimum number of swaps.

```cpp
class Solution {
public:
    int minSwaps(vector<int>& data) {
        int n = data.size();
        int ones = 0;
        // Count the number of ones in the array
        for (int i = 0; i < n; i++) {
            if (data[i] == 1) ones++;
        }
        
        int minSwaps = INT_MAX;
        int windowOnes = 0;
        // Initialize the window
        for (int i = 0; i < ones; i++) {
            windowOnes += data[i];
        }
        
        minSwaps = min(minSwaps, ones - windowOnes);
        
        // Slide the window over the array
        for (int i = ones; i < n + ones; i++) {
            windowOnes -= data[i - ones];
            windowOnes += data[i % n];
            minSwaps = min(minSwaps, ones - windowOnes);
        }
        
        return minSwaps;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of the input array. This is because we are sliding a window of fixed size over the array.
> - **Space Complexity:** $O(1)$, as we are not using any extra space that scales with input size.
> - **Optimality proof:** This approach is optimal because it considers all possible positions of the window that contains all `1`s and finds the minimum number of swaps required.

---

### Final Notes
**Learning Points:**
- The problem demonstrates the use of the sliding window technique to find the minimum number of swaps required to group all `1`s together.
- It highlights the importance of counting the number of `1`s in the array and using this count to determine the size of the window.
- The problem also shows how to optimize the brute force approach by using a more efficient algorithm.

**Mistakes to Avoid:**
- Not counting the number of `1`s in the array before trying to group them together.
- Not using a sliding window approach to find the minimum number of swaps required.
- Not considering all possible positions of the window that contains all `1`s.