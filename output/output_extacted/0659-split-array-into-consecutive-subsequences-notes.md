## Split Array into Consecutive Subsequences

**Problem Link:** https://leetcode.com/problems/split-array-into-consecutive-subsequences/description

**Problem Statement:**
- Input: A non-empty array of integers `nums`.
- Constraints: `1 <= nums.length <= 10^4`, `1 <= nums[i] <= 10^4`.
- Expected output: `true` if the array can be split into consecutive subsequences, `false` otherwise.
- Key requirements and edge cases to consider:
  - Handling duplicate numbers.
  - Ensuring each number is used exactly once.
  - Checking for sequences that can be formed from the array.
- Example test cases:
  - `[1, 2, 3, 3, 4, 5]`: Returns `true` because `[1, 2, 3]` and `[3, 4, 5]` are consecutive subsequences.
  - `[1, 2, 4, 5]`: Returns `false` because there is no way to form consecutive subsequences.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of subsequences.
- Step-by-step breakdown of the solution:
  1. Generate all possible subsequences of the input array.
  2. For each subsequence, check if it is consecutive.
  3. If a consecutive subsequence is found, remove its elements from the original array.
  4. Repeat steps 2-3 until all elements are used or no more consecutive subsequences can be found.
- Why this approach comes to mind first: It's a straightforward way to ensure all possibilities are considered.

```cpp
#include <vector>
#include <iostream>

bool isPossible(std::vector<int>& nums) {
    // Sort the array to make it easier to find consecutive subsequences
    std::sort(nums.begin(), nums.end());
    
    // Initialize variables to keep track of the current sequence and its length
    int currentNum = nums[0];
    int sequenceLength = 1;
    
    // Iterate over the sorted array
    for (int i = 1; i < nums.size(); i++) {
        // If the current number is consecutive to the previous one, increment the sequence length
        if (nums[i] == currentNum + 1) {
            sequenceLength++;
            currentNum = nums[i];
        } 
        // If the current number is the same as the previous one, it could be the start of a new sequence
        else if (nums[i] == currentNum) {
            // Check if there's a sequence of the same length that can be formed with the remaining numbers
            int tempNum = nums[i];
            int tempSequenceLength = 1;
            for (int j = i + 1; j < nums.size(); j++) {
                if (nums[j] == tempNum + 1) {
                    tempSequenceLength++;
                    tempNum = nums[j];
                }
            }
            // If a sequence of the same length can be formed, update the current sequence
            if (tempSequenceLength >= sequenceLength) {
                sequenceLength = tempSequenceLength;
                currentNum = tempNum;
            }
        } 
        // If the current number is not consecutive to the previous one and not the same, return false
        else {
            return false;
        }
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the array. This is because in the worst case, for each element, we might have to iterate over the rest of the array to find a consecutive sequence.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input array, because we only use a constant amount of space to store variables.
> - **Why these complexities occur:** The nested loops in the brute force approach cause the high time complexity. The space complexity is low because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: Using a `HashMap` to store the frequency of each number and another `HashMap` to store the length of the longest consecutive subsequence ending at each number.
- Detailed breakdown of the approach:
  1. Count the frequency of each number in the array.
  2. For each number, check if it can be the start of a new sequence. If so, try to extend the sequence as long as possible.
  3. After trying to extend the sequence, update the frequency of the numbers used in the sequence.
- Proof of optimality: This approach ensures that each number is used exactly once and that we try to form the longest possible sequences, which is optimal.

```cpp
#include <vector>
#include <unordered_map>

bool isPossible(std::vector<int>& nums) {
    std::unordered_map<int, int> freq;
    std::unordered_map<int, int> sequences;
    
    // Count the frequency of each number
    for (int num : nums) {
        freq[num]++;
    }
    
    // Try to form sequences
    for (int num : nums) {
        if (freq[num] == 0) continue; // Skip numbers that have been used
        freq[num]--;
        
        // Try to extend the sequence as long as possible
        int currentNum = num;
        while (freq.find(currentNum + 1) != freq.end() && freq[currentNum + 1] > 0) {
            freq[currentNum + 1]--;
            currentNum++;
        }
        
        // Update the length of the longest sequence ending at the last number
        sequences[currentNum]++;
    }
    
    // Check if all numbers have been used
    for (auto& pair : freq) {
        if (pair.second > 0) return false;
    }
    
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the array. This is because we make two passes over the data: one to count frequencies and another to try to form sequences.
> - **Space Complexity:** $O(n)$, because in the worst case, we might need to store every number in the `HashMap`.
> - **Optimality proof:** This approach is optimal because it ensures that each number is used exactly once and that we try to form the longest possible sequences, which minimizes the number of sequences needed.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using `HashMap` for frequency counting and sequence tracking.
- Problem-solving patterns identified: Trying to form the longest possible sequences and using frequency counting to ensure each number is used exactly once.
- Optimization techniques learned: Using a single pass to try to form sequences after counting frequencies.
- Similar problems to practice: Other problems involving sequence formation and frequency counting.

**Mistakes to Avoid:**
- Common implementation errors: Not updating the frequency of numbers correctly after forming a sequence.
- Edge cases to watch for: Handling duplicate numbers and ensuring each number is used exactly once.
- Performance pitfalls: Using nested loops or not optimizing the sequence formation process.
- Testing considerations: Testing with arrays of different lengths and with different distributions of numbers.