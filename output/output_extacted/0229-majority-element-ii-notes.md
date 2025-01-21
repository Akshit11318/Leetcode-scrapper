## Majority Element II
**Problem Link:** https://leetcode.com/problems/majority-element-ii/description

**Problem Statement:**
- Input format: An array of integers `nums`.
- Constraints: The length of `nums` is at least 1 and at most $10^5$.
- Expected output format: All the elements that appear more than $\frac{n}{3}$ times, where $n$ is the size of `nums`.
- Key requirements and edge cases to consider: Handling arrays with multiple elements that meet the criteria, arrays with no elements meeting the criteria, and arrays with elements that exactly meet the $\frac{n}{3}$ threshold.
- Example test cases:
  - `nums = [3,2,3]`: The output should be `[3]`.
  - `nums = [1,1,1,3,3,2,2,2]`: The output should be `[1,2]`.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Count the occurrences of each number in the array and compare it to $\frac{n}{3}$.
- Step-by-step breakdown of the solution:
  1. Create a map to store the count of each number.
  2. Iterate through the array, incrementing the count for each number in the map.
  3. Iterate through the map, checking each number's count against $\frac{n}{3}$.
- Why this approach comes to mind first: It directly addresses the problem by counting occurrences and comparing them to the threshold.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

vector<int> majorityElement(vector<int>& nums) {
    unordered_map<int, int> countMap;
    int n = nums.size();
    
    // Count occurrences of each number
    for (int num : nums) {
        if (countMap.find(num) != countMap.end()) {
            countMap[num]++;
        } else {
            countMap[num] = 1;
        }
    }
    
    vector<int> result;
    // Check counts against n/3
    for (auto& pair : countMap) {
        if (pair.second > n / 3) {
            result.push_back(pair.first);
        }
    }
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the size of `nums`, because we make two passes through the data: one to count occurrences and one to check those counts against the threshold.
> - **Space Complexity:** $O(n)$, because in the worst case, every element in `nums` could be unique, requiring a map of size $n$.
> - **Why these complexities occur:** The brute force approach requires iterating through all elements to count their occurrences and then iterating through the map to find elements that meet the criteria, leading to linear time complexity. The space complexity is due to the potential need to store every unique element in the map.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: The Boyer-Moore Voting Algorithm can be adapted to find elements that occur more than $\frac{n}{3}$ times by maintaining two counters for two potential candidates.
- Detailed breakdown of the approach:
  1. Initialize two counters and two candidate variables.
  2. Iterate through the array, updating the counters and candidates based on the current element.
  3. After the first pass, the candidates are the potential majority elements. Perform a second pass to confirm their counts exceed $\frac{n}{3}$.
- Proof of optimality: This approach is optimal because it only requires two passes through the data, resulting in a linear time complexity, and it uses a constant amount of space to store the counters and candidates.

```cpp
vector<int> majorityElement(vector<int>& nums) {
    int count1 = 0, count2 = 0, candidate1 = 0, candidate2 = 1;
    int n = nums.size();
    
    // First pass to find candidates
    for (int num : nums) {
        if (num == candidate1) {
            count1++;
        } else if (num == candidate2) {
            count2++;
        } else if (count1 == 0) {
            candidate1 = num;
            count1 = 1;
        } else if (count2 == 0) {
            candidate2 = num;
            count2 = 1;
        } else {
            count1--;
            count2--;
        }
    }
    
    // Reset counters for second pass
    count1 = count2 = 0;
    
    // Second pass to confirm candidates
    for (int num : nums) {
        if (num == candidate1) count1++;
        else if (num == candidate2) count2++;
    }
    
    vector<int> result;
    if (count1 > n / 3) result.push_back(candidate1);
    if (count2 > n / 3) result.push_back(candidate2);
    
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, because we make two passes through the data.
> - **Space Complexity:** $O(1)$, because we use a constant amount of space to store the counters and candidates.
> - **Optimality proof:** This solution is optimal because it achieves linear time complexity with constant space usage, which is the best possible for this problem given the need to examine each element at least once.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The Boyer-Moore Voting Algorithm and its adaptation for finding elements that occur more than $\frac{n}{3}$ times.
- Problem-solving patterns identified: The use of counters and candidate variables to efficiently find potential majority elements.
- Optimization techniques learned: Reducing space complexity by using a constant amount of space for counters and candidates.
- Similar problems to practice: Finding the majority element in an array (which occurs more than $\frac{n}{2}$ times), and other problems involving the Boyer-Moore Voting Algorithm.

**Mistakes to Avoid:**
- Common implementation errors: Incorrectly updating counters or not resetting them properly for the second pass.
- Edge cases to watch for: Handling arrays with no elements meeting the criteria, and arrays with elements that exactly meet the $\frac{n}{3}$ threshold.
- Performance pitfalls: Using data structures that lead to higher time or space complexity than necessary.
- Testing considerations: Thoroughly testing the function with various inputs, including edge cases and large datasets.