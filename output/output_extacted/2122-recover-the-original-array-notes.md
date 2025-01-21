## Recover the Original Array
**Problem Link:** https://leetcode.com/problems/recover-the-original-array/description

**Problem Statement:**
- Input: A sorted array `changed` of integers, representing the modified array, and an integer `x`, representing the change.
- Output: The original array `nums` if it exists, otherwise return an empty array.
- Key requirements and edge cases to consider:
  - The original array must have the same length as the changed array.
  - The original array must be non-empty.
- Example test cases with explanations:
  - Example 1: Input: `changed = [1,2,3,4], x = 1`, Output: `[0,1,2,3]`
  - Example 2: Input: `changed = [1,2,4,6], x = 1`, Output: `[]`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of `x` added or subtracted from each element in the changed array.
- Step-by-step breakdown of the solution:
  1. Generate all possible combinations of adding or subtracting `x` from each element in the changed array.
  2. Check if each combination results in a sorted array.
  3. If a combination results in a sorted array, check if the array can be recovered by adding or subtracting `x` from each element.
- Why this approach comes to mind first: It's a straightforward approach that tries all possible combinations.

```cpp
#include <vector>
#include <algorithm>

std::vector<int> recoverArray(std::vector<int>& changed, int x) {
    int n = changed.size();
    std::vector<int> original(n);
    std::vector<bool> visited(n);
    
    // Generate all possible combinations
    std::function<void(int)> dfs = [&](int index) {
        if (index == n) {
            // Check if the current combination results in a sorted array
            if (std::is_sorted(original.begin(), original.end())) {
                // Check if the array can be recovered
                std::vector<int> recovered;
                for (int i = 0; i < n; i++) {
                    if (original[i] + x == changed[i]) {
                        recovered.push_back(original[i]);
                    } else if (original[i] - x == changed[i]) {
                        recovered.push_back(original[i]);
                    }
                }
                if (recovered.size() == n) {
                    return;
                }
            }
        }
        
        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                original[index] = changed[i] + x;
                visited[i] = true;
                dfs(index + 1);
                visited[i] = false;
                
                original[index] = changed[i] - x;
                visited[i] = true;
                dfs(index + 1);
                visited[i] = false;
            }
        }
    };
    
    dfs(0);
    return {};
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^n)$, where $n$ is the length of the changed array. This is because we're trying all possible combinations of adding or subtracting `x` from each element.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the changed array. This is because we're storing the original array and the visited array.
> - **Why these complexities occur:** The brute force approach tries all possible combinations, resulting in exponential time complexity. The space complexity is linear because we're storing the original array and the visited array.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight: The problem can be solved by using a hash map to store the frequency of each number in the changed array.
- Detailed breakdown of the approach:
  1. Create a hash map to store the frequency of each number in the changed array.
  2. Iterate through the changed array and for each number, check if adding or subtracting `x` results in a valid number in the hash map.
  3. If a valid number is found, decrement its frequency in the hash map.
  4. If all numbers in the changed array can be recovered, return the original array.
- Proof of optimality: The optimal approach has a time complexity of $O(n)$, where $n$ is the length of the changed array, making it more efficient than the brute force approach.

```cpp
#include <vector>
#include <unordered_map>

std::vector<int> recoverArray(std::vector<int>& changed, int x) {
    int n = changed.size();
    std::unordered_map<int, int> freq;
    std::vector<int> original;
    
    // Create a hash map to store the frequency of each number
    for (int num : changed) {
        freq[num]++;
    }
    
    for (int num : changed) {
        if (freq[num] > 0) {
            freq[num]--;
            int curr = num;
            std::vector<int> temp;
            
            for (int i = 0; i < n - 1; i++) {
                temp.push_back(curr);
                if (freq.find(curr + x) != freq.end()) {
                    curr += x;
                    freq[curr]--;
                } else if (freq.find(curr - x) != freq.end()) {
                    curr -= x;
                    freq[curr]--;
                } else {
                    break;
                }
            }
            
            if (temp.size() == n) {
                original = temp;
                break;
            }
            
            // Backtrack
            for (int num : temp) {
                freq[num]++;
            }
        }
    }
    
    return original;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the length of the changed array. This is because we're iterating through the changed array and using a hash map to store the frequency of each number.
> - **Space Complexity:** $O(n)$, where $n$ is the length of the changed array. This is because we're storing the original array and the hash map.
> - **Optimality proof:** The optimal approach has a time complexity of $O(n)$, making it more efficient than the brute force approach.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash map, frequency counting, backtracking.
- Problem-solving patterns identified: Using a hash map to store frequency of numbers, iterating through the array to find valid numbers.
- Optimization techniques learned: Using a hash map to reduce time complexity, backtracking to avoid unnecessary computations.
- Similar problems to practice: Recovering the original array with multiple changes, finding the original array with a given change.

**Mistakes to Avoid:**
- Common implementation errors: Not using a hash map to store frequency of numbers, not backtracking correctly.
- Edge cases to watch for: Empty array, array with duplicate numbers.
- Performance pitfalls: Using a brute force approach, not optimizing the solution.
- Testing considerations: Test with different inputs, including edge cases and large inputs.