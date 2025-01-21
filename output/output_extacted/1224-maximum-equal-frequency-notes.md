## Maximum Equal Frequency
**Problem Link:** https://leetcode.com/problems/maximum-equal-frequency/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: `1 <= nums.length <= 2 * 10^5`, `1 <= nums[i] <= 10^9`.
- Expected output format: The maximum length of the array that can be achieved by changing at most one element.
- Key requirements and edge cases to consider: The frequency of each number must be the same, and at most one element can be changed to achieve this.

Example test cases:
- `nums = [2,2,1,1,5,3,3,5]`, expected output: `7`.
- `nums = [1,1,1,2,2,2,3,3,3,4,4,4,5]`, expected output: `13`.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to try all possible combinations of changing one element and check if the resulting array has equal frequencies for all numbers.
- Step-by-step breakdown:
  1. Iterate over all possible indices in the array.
  2. For each index, try all possible values for the element at that index.
  3. After changing the element, count the frequency of each number in the array.
  4. Check if all frequencies are the same.
  5. If they are, update the maximum length if the current length is greater.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int maxEqualFreq(std::vector<int>& nums) {
    int n = nums.size();
    int maxLen = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 1; j <= 1000000000; j++) {
            nums[i] = j;
            std::unordered_map<int, int> freq;
            for (int k = 0; k < n; k++) {
                freq[nums[k]]++;
            }
            bool allSame = true;
            int firstFreq = -1;
            for (auto& it : freq) {
                if (firstFreq == -1) {
                    firstFreq = it.second;
                } else if (it.second != firstFreq) {
                    allSame = false;
                    break;
                }
            }
            if (allSame && n > maxLen) {
                maxLen = n;
            }
            nums[i] = j - 1;
        }
    }
    return maxLen;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2 \cdot 10^9)$, where $n$ is the length of the input array. This is because we are trying all possible combinations of changing one element and checking the frequencies.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are using an unordered map to store the frequencies of the numbers.
> - **Why these complexities occur:** The brute force approach has high time complexity due to the nested loops and the checking of frequencies for each combination.

---

### Optimal Approach (Required)
**Explanation:**
- The key insight is to use an unordered map to store the frequencies of the numbers and another unordered map to store the count of each frequency.
- We then iterate over the array and update the frequencies and the count of each frequency.
- If the count of each frequency is at most 2, we can make the frequencies equal by changing at most one element.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int maxEqualFreq(std::vector<int>& nums) {
    int n = nums.size();
    std::unordered_map<int, int> freq;
    std::unordered_map<int, int> count;
    for (int num : nums) {
        freq[num]++;
    }
    for (auto& it : freq) {
        count[it.second]++;
    }
    for (int i = n; i > 0; i--) {
        if (count.size() == 1) {
            return i;
        }
        if (count.size() == 2) {
            int maxFreq = -1;
            int minFreq = -1;
            for (auto& it : count) {
                if (maxFreq == -1) {
                    maxFreq = it.first;
                } else if (minFreq == -1) {
                    minFreq = it.first;
                } else {
                    break;
                }
            }
            if (maxFreq - minFreq == 1 && count[maxFreq] == 1) {
                return i;
            }
            if (minFreq == 1 && count[minFreq] == 1) {
                return i;
            }
        }
        for (int num : nums) {
            if (freq[num] == 1) {
                freq.erase(num);
                break;
            } else {
                freq[num]--;
                if (freq[num] == 0) {
                    freq.erase(num);
                }
            }
        }
        for (auto& it : freq) {
            count[it.second]++;
        }
    }
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are iterating over the array once and updating the frequencies and the count of each frequency.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the input array. This is because we are using two unordered maps to store the frequencies and the count of each frequency.
> - **Optimality proof:** This is the optimal solution because we are using the minimum amount of space and time required to solve the problem. We are iterating over the array once and updating the frequencies and the count of each frequency, which is the most efficient way to solve the problem.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using unordered maps to store frequencies and the count of each frequency.
- Problem-solving patterns identified: Iterating over the array and updating the frequencies and the count of each frequency.
- Optimization techniques learned: Using the minimum amount of space and time required to solve the problem.
- Similar problems to practice: Problems involving frequencies and counts, such as finding the most frequent element in an array.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as an empty array.
- Edge cases to watch for: An array with only one element, an array with all elements being the same.
- Performance pitfalls: Using a brute force approach, which can result in high time complexity.
- Testing considerations: Testing the solution with different inputs, such as an array with all elements being the same, an array with only one element.