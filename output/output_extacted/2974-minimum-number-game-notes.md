## Minimum Number Game
**Problem Link:** https://leetcode.com/problems/minimum-number-game/description

**Problem Statement:**
- Input format: Two integers `num1` and `num2` representing two numbers.
- Constraints: `1 <= num1 <= 10^9`, `1 <= num2 <= 10^9`.
- Expected output format: The minimum number that can be obtained by removing `k` digits from the concatenation of `num1` and `num2`.
- Key requirements and edge cases to consider: The minimum number can be obtained by removing any `k` digits from the concatenation, where `k` is the number of digits in the concatenation minus the desired number of digits.
- Example test cases with explanations:
  - Example 1: `num1 = 10200`, `num2 = 47361`, `k = 5`. The concatenation is "1020047361". Removing 5 digits, we get "0".
  - Example 2: `num1 = 10`, `num2 = 25`, `k = 1`. The concatenation is "1025". Removing 1 digit, we get "025" or "105" or "125" or "102" or "120". The minimum number is "025".

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Generate all possible numbers by removing `k` digits from the concatenation of `num1` and `num2`, and then find the minimum number.
- Step-by-step breakdown of the solution:
  1. Concatenate `num1` and `num2`.
  2. Generate all possible numbers by removing `k` digits from the concatenation.
  3. Find the minimum number among the generated numbers.
- Why this approach comes to mind first: It is a straightforward approach to generate all possible numbers and find the minimum one.

```cpp
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string findMinNum(string num1, string num2, int k) {
    string concat = num1 + num2;
    vector<string> nums;
    vector<bool> visited(concat.size(), false);
    
    function<void(int, string)> generateNums = [&](int index, string num) {
        if (index == k) {
            nums.push_back(num);
            return;
        }
        
        for (int i = 0; i < concat.size(); i++) {
            if (!visited[i]) {
                visited[i] = true;
                generateNums(index + 1, num + concat[i]);
                visited[i] = false;
            }
        }
    };
    
    generateNums(0, "");
    
    string minNum = "9999999999999999999";
    for (auto& num : nums) {
        if (num.size() < minNum.size() || (num.size() == minNum.size() && num < minNum)) {
            minNum = num;
        }
    }
    
    return minNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n})$, where $n$ is the number of digits in the concatenation. This is because we generate all possible numbers by removing `k` digits.
> - **Space Complexity:** $O(2^{n})$, as we store all generated numbers in the `nums` vector.
> - **Why these complexities occur:** The brute force approach generates all possible numbers, resulting in exponential time and space complexity.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight that leads to optimal solution: We can use a priority queue to keep track of the minimum number that can be obtained by removing `k` digits.
- Detailed breakdown of the approach:
  1. Concatenate `num1` and `num2`.
  2. Use a priority queue to store the minimum number that can be obtained by removing `k` digits.
  3. Iterate through the concatenation and remove the largest digit that is greater than the current minimum number.
- Proof of optimality: This approach ensures that we always remove the largest digit that is greater than the current minimum number, resulting in the minimum number that can be obtained by removing `k` digits.
- Why further optimization is impossible: This approach has a time complexity of $O(n \log n)$, where $n$ is the number of digits in the concatenation. This is because we use a priority queue to store the minimum number.

```cpp
#include <iostream>
#include <string>
#include <queue>

using namespace std;

string findMinNum(string num1, string num2, int k) {
    string concat = num1 + num2;
    priority_queue<char> pq;
    
    for (char c : concat) {
        while (k > 0 && !pq.empty() && pq.top() > c) {
            pq.pop();
            k--;
        }
        pq.push(c);
    }
    
    while (k > 0 && !pq.empty()) {
        pq.pop();
        k--;
    }
    
    string minNum;
    while (!pq.empty()) {
        minNum = pq.top() + minNum;
        pq.pop();
    }
    
    return minNum;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n)$, where $n$ is the number of digits in the concatenation. This is because we use a priority queue to store the minimum number.
> - **Space Complexity:** $O(n)$, as we store the minimum number in the `minNum` string.
> - **Optimality proof:** This approach ensures that we always remove the largest digit that is greater than the current minimum number, resulting in the minimum number that can be obtained by removing `k` digits.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Priority queue, greedy algorithm.
- Problem-solving patterns identified: Using a priority queue to keep track of the minimum number.
- Optimization techniques learned: Using a priority queue to reduce time complexity.
- Similar problems to practice: Minimum number that can be obtained by removing `k` digits from a single number.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, such as when `k` is greater than the number of digits in the concatenation.
- Edge cases to watch for: When `k` is equal to the number of digits in the concatenation, the minimum number is "0".
- Performance pitfalls: Using a brute force approach, which results in exponential time and space complexity.
- Testing considerations: Test the function with different inputs, including edge cases, to ensure that it produces the correct output.