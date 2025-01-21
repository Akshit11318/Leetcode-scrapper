## Apples or Oranges
**Problem Link:** https://leetcode.com/problems/apples-oranges/description

**Problem Statement:**
- Input format and constraints: The problem takes in a list of integers representing the positions of apples and oranges on a number line, along with the positions of two houses. The task is to count the number of apples and oranges that fall within the range of each house.
- Expected output format: The output should be two separate counts, one for the number of apples that fall within the range of the first house and one for the number of oranges that fall within the range of the second house.
- Key requirements and edge cases to consider: The positions of the apples, oranges, and houses are given as integers, and the ranges are inclusive.
- Example test cases with explanations:
  - If the positions of the apples are [2, 3, 4], the positions of the oranges are [3, -4, -1], the position of the first house is 1, the position of the second house is 10, and the distance from the house is 2, then the number of apples that fall within the range of the first house is 1 (since 2 is within the range [1 - 2, 1 + 2]), and the number of oranges that fall within the range of the second house is 1 (since 3 is within the range [10 - 2, 10 + 2]).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we need to calculate the number of apples and oranges that fall within the range of each house. We can do this by iterating through the list of apples and oranges and checking if each one falls within the range of the corresponding house.
- Step-by-step breakdown of the solution:
  1. Calculate the range for the first house by subtracting and adding the distance from the house's position.
  2. Iterate through the list of apples and check if each apple's position falls within the range of the first house. If it does, increment the count of apples.
  3. Calculate the range for the second house by subtracting and adding the distance from the house's position.
  4. Iterate through the list of oranges and check if each orange's position falls within the range of the second house. If it does, increment the count of oranges.
- Why this approach comes to mind first: This approach is straightforward and easy to understand. It involves simple iteration and comparison, making it a natural first step in solving the problem.

```cpp
#include <vector>
#include <iostream>

std::vector<int> countApplesAndOranges(int s, int t, int a, int b, std::vector<int>& apples, std::vector<int>& oranges) {
    int m = apples.size();
    int n = oranges.size();
    int countApples = 0;
    int countOranges = 0;

    for (int i = 0; i < m; i++) {
        if (apples[i] + a >= s && apples[i] + a <= t) {
            countApples++;
        }
    }

    for (int i = 0; i < n; i++) {
        if (oranges[i] + b >= s && oranges[i] + b <= t) {
            countOranges++;
        }
    }

    std::vector<int> result = {countApples, countOranges};
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, where m is the number of apples and n is the number of oranges. This is because we are iterating through each list once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output vectors. This is because we are using a constant amount of space to store the counts.
> - **Why these complexities occur:** The time complexity is linear because we are doing a constant amount of work for each apple and orange. The space complexity is constant because we are not using any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The optimal solution is the same as the brute force approach, as we must check each apple and orange to determine if it falls within the range of the corresponding house.
- Detailed breakdown of the approach:
  1. Calculate the range for the first house by subtracting and adding the distance from the house's position.
  2. Iterate through the list of apples and check if each apple's position falls within the range of the first house. If it does, increment the count of apples.
  3. Calculate the range for the second house by subtracting and adding the distance from the house's position.
  4. Iterate through the list of oranges and check if each orange's position falls within the range of the second house. If it does, increment the count of oranges.
- Proof of optimality: This approach is optimal because we must check each apple and orange at least once to determine if it falls within the range of the corresponding house.
- Why further optimization is impossible: Further optimization is impossible because we must do at least a constant amount of work for each apple and orange, resulting in a time complexity of $O(m + n)$.

```cpp
#include <vector>
#include <iostream>

std::vector<int> countApplesAndOranges(int s, int t, int a, int b, std::vector<int>& apples, std::vector<int>& oranges) {
    int m = apples.size();
    int n = oranges.size();
    int countApples = 0;
    int countOranges = 0;

    for (int i = 0; i < m; i++) {
        if (apples[i] + a >= s && apples[i] + a <= t) {
            countApples++;
        }
    }

    for (int i = 0; i < n; i++) {
        if (oranges[i] + b >= s && oranges[i] + b <= t) {
            countOranges++;
        }
    }

    std::vector<int> result = {countApples, countOranges};
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(m + n)$, where m is the number of apples and n is the number of oranges. This is because we are iterating through each list once.
> - **Space Complexity:** $O(1)$, excluding the space needed for the input and output vectors. This is because we are using a constant amount of space to store the counts.
> - **Optimality proof:** This approach is optimal because we must check each apple and orange at least once to determine if it falls within the range of the corresponding house.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: iteration, comparison.
- Problem-solving patterns identified: checking each element in a list to determine if it meets a certain condition.
- Optimization techniques learned: none, as the problem requires checking each element at least once.
- Similar problems to practice: other problems involving iteration and comparison.

**Mistakes to Avoid:**
- Common implementation errors: off-by-one errors when calculating the range of the houses.
- Edge cases to watch for: when the range of a house is empty (i.e., the distance is 0).
- Performance pitfalls: none, as the problem requires checking each element at least once.
- Testing considerations: test with different inputs, including edge cases, to ensure the solution is correct.