## Missing Number in Arithmetic Progression

**Problem Link:** https://leetcode.com/problems/missing-number-in-arithmetic-progression/description

**Problem Statement:**
- Input format: An array of integers `nums` representing an arithmetic progression with one missing number.
- Constraints: The array will contain between 2 and 100 elements, with values ranging from 0 to 10^9.
- Expected output format: The missing number in the arithmetic progression.
- Key requirements and edge cases to consider: The input array is guaranteed to be an arithmetic progression with one missing number, and the missing number can be anywhere in the sequence.
- Example test cases with explanations:
  - For `nums = [1, 2, 3, 5]`, the missing number is `4`.
  - For `nums = [1, 3, 5, 7, 9]`, the missing number is `5` if we consider the progression `1, 2, 3, 4, 5, 6, 7, 8, 9`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all possible arithmetic progressions that could fit the given array and check which one has a missing number.
- Step-by-step breakdown of the solution:
  1. Determine the possible common differences (`d`) for the arithmetic progression by calculating the differences between consecutive elements in the array.
  2. For each possible `d`, generate the complete arithmetic progression starting from the first element of the array.
  3. Compare the generated progression with the input array to find the missing number.
- Why this approach comes to mind first: It's a straightforward method that involves generating all possible progressions and checking for the missing number.

```cpp
#include <vector>
#include <set>
#include <algorithm>

int findMissingNumber(vector<int>& nums) {
    int n = nums.size();
    set<int> possibleDifferences;
    
    // Calculate possible common differences
    for (int i = 1; i < n; i++) {
        possibleDifferences.insert(nums[i] - nums[i-1]);
    }
    
    // Try each possible common difference
    for (int d : possibleDifferences) {
        vector<int> progression;
        progression.push_back(nums[0]);
        
        // Generate the progression
        while (progression.back() <= nums.back() + d) {
            progression.push_back(progression.back() + d);
        }
        
        // Check for the missing number
        for (int i = 0; i < progression.size(); i++) {
            if (find(nums.begin(), nums.end(), progression[i]) == nums.end()) {
                return progression[i];
            }
        }
    }
    
    // If no progression fits, return an error or a default value
    return -1; // This should not happen according to the problem statement
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of elements in the input array and $m$ is the average length of the generated progressions. This is because for each possible common difference, we generate a progression and compare it with the input array.
> - **Space Complexity:** $O(n + m)$, as we store the input array and the generated progression.
> - **Why these complexities occur:** The brute force approach involves generating multiple progressions and comparing them with the input array, leading to high time and space complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The missing number in an arithmetic progression can be found by calculating the difference between the sum of the complete progression and the sum of the given array.
- Detailed breakdown of the approach:
  1. Calculate the common difference (`d`) of the progression by finding the most frequent difference between consecutive elements in the array.
  2. Calculate the sum of the complete arithmetic progression using the formula for the sum of an arithmetic series: $S = \frac{n}{2} \cdot (a_1 + a_n)$, where $n$ is the number of terms, $a_1$ is the first term, and $a_n$ is the last term.
  3. Calculate the sum of the given array.
  4. The missing number is the difference between the sum of the complete progression and the sum of the given array.
- Proof of optimality: This approach is optimal because it directly calculates the missing number without generating all possible progressions, reducing the time complexity to $O(n)$.

```cpp
#include <vector>
#include <algorithm>

int findMissingNumber(vector<int>& nums) {
    int n = nums.size();
    int firstTerm = nums[0];
    int lastTerm = nums.back();
    
    // Calculate the common difference
    int d = 0;
    int maxCount = 0;
    map<int, int> differences;
    for (int i = 1; i < n; i++) {
        int diff = nums[i] - nums[i-1];
        differences[diff]++;
        if (differences[diff] > maxCount) {
            maxCount = differences[diff];
            d = diff;
        }
    }
    
    // Calculate the sum of the complete progression
    int completeSum = (n + 1) * (firstTerm + lastTerm + d) / 2;
    
    // Calculate the sum of the given array
    int arraySum = 0;
    for (int num : nums) {
        arraySum += num;
    }
    
    // The missing number is the difference between the two sums
    return completeSum - arraySum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we make a single pass through the array to calculate the common difference and the sums.
> - **Space Complexity:** $O(n)$, for storing the input array and the map of differences.
> - **Optimality proof:** This approach is optimal because it directly calculates the missing number without generating all possible progressions, reducing the time complexity to $O(n)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Arithmetic progressions, calculating sums of series, and optimizing brute force approaches.
- Problem-solving patterns identified: Looking for patterns in the input data and using mathematical formulas to simplify the problem.
- Optimization techniques learned: Reducing the number of iterations and using mathematical formulas to calculate the solution directly.
- Similar problems to practice: Finding missing numbers in sequences, calculating sums of series, and optimizing brute force approaches.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array or an array with a single element.
- Edge cases to watch for: Input arrays with duplicate elements or arrays with a large number of elements.
- Performance pitfalls: Using brute force approaches that have high time complexities.
- Testing considerations: Testing the solution with different input arrays, including edge cases and large inputs.