## Maximize the Confusion of an Exam

**Problem Link:** https://leetcode.com/problems/maximize-the-confusion-of-an-exam/description

**Problem Statement:**
- Input format and constraints: The input is an array of answers where `answers[i]` is the answer to the i-th question.
- Expected output format: The maximum number of confused students.
- Key requirements and edge cases to consider: The maximum number of confused students is achieved when the most frequent answer is chosen as the correct answer for each question.
- Example test cases with explanations:
  - Example 1: Input: `answers = [1,2,3,4,5,6,7,8,9,10]`, Output: `5`
  - Example 2: Input: `answers = [1,1,1,1,1,1,1,1,1,1]`, Output: `10`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To maximize the confusion, we need to find the answer that appears most frequently in the array.
- Step-by-step breakdown of the solution:
  1. Create a frequency map of the answers.
  2. Find the maximum frequency.
  3. The maximum number of confused students is equal to the maximum frequency.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int maxConfusion(std::vector<int>& answers) {
    // Create a frequency map of the answers
    std::unordered_map<int, int> frequencyMap;
    for (int answer : answers) {
        frequencyMap[answer]++;
    }
    
    // Find the maximum frequency
    int maxFrequency = 0;
    for (auto& pair : frequencyMap) {
        maxFrequency = std::max(maxFrequency, pair.second);
    }
    
    // The maximum number of confused students is equal to the maximum frequency
    return maxFrequency;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of answers. We iterate over the answers twice: once to create the frequency map and once to find the maximum frequency.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique answers. We use an unordered map to store the frequency of each answer.
> - **Why these complexities occur:** The time complexity is linear because we iterate over the answers a constant number of times. The space complexity is linear because we store the frequency of each answer in the unordered map.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a single pass over the answers to find the maximum frequency.
- Detailed breakdown of the approach:
  1. Create a frequency map of the answers.
  2. Keep track of the maximum frequency as we iterate over the answers.
- Proof of optimality: This approach is optimal because we only iterate over the answers once, resulting in a time complexity of $O(n)$.
- Why further optimization is impossible: We must iterate over the answers at least once to find the maximum frequency, so the time complexity cannot be improved.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

int maxConfusion(std::vector<int>& answers) {
    // Create a frequency map of the answers and keep track of the maximum frequency
    std::unordered_map<int, int> frequencyMap;
    int maxFrequency = 0;
    for (int answer : answers) {
        frequencyMap[answer]++;
        maxFrequency = std::max(maxFrequency, frequencyMap[answer]);
    }
    
    // The maximum number of confused students is equal to the maximum frequency
    return maxFrequency;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of answers. We iterate over the answers once to create the frequency map and find the maximum frequency.
> - **Space Complexity:** $O(n)$, where $n$ is the number of unique answers. We use an unordered map to store the frequency of each answer.
> - **Optimality proof:** The time complexity is optimal because we only iterate over the answers once. The space complexity is also optimal because we must store the frequency of each answer to find the maximum frequency.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency maps, maximum frequency.
- Problem-solving patterns identified: Using a single pass over the data to find the maximum frequency.
- Optimization techniques learned: Reducing the number of iterations over the data.
- Similar problems to practice: Other problems involving frequency maps and maximum frequency.

**Mistakes to Avoid:**
- Common implementation errors: Forgetting to initialize the frequency map or the maximum frequency.
- Edge cases to watch for: Empty input arrays or arrays with a single element.
- Performance pitfalls: Using a nested loop to find the maximum frequency, resulting in a time complexity of $O(n^2)$.
- Testing considerations: Testing the function with different input arrays, including edge cases.