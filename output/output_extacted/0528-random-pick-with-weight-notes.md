## Random Pick with Weight

**Problem Link:** https://leetcode.com/problems/random-pick-with-weight/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `w` representing weights of different elements, we need to implement a solution that supports two operations: `init` and `pickIndex`. The `init` operation initializes the solution with the given weights, and the `pickIndex` operation returns a random index based on the given weights. The weights are non-negative, and the total sum of weights is guaranteed to be positive.
- Expected output format: The `pickIndex` operation should return a random index `i` such that the probability of picking index `i` is equal to `w[i] / sum(w)`.
- Key requirements and edge cases to consider: The solution should handle large inputs and support a large number of `pickIndex` operations.
- Example test cases with explanations:
    - Example 1: `init([1, 3])`, `pickIndex()`, `pickIndex()`, `pickIndex()`. The expected output is a random index, with index 0 having a 25% chance of being picked and index 1 having a 75% chance of being picked.
    - Example 2: `init([1])`, `pickIndex()`. The expected output is always index 0.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: One possible approach is to generate a random number between 0 and the total sum of weights minus 1, and then use this number to select an index based on the cumulative sum of weights.
- Step-by-step breakdown of the solution:
    1. Calculate the total sum of weights.
    2. Generate a random number between 0 and the total sum minus 1.
    3. Iterate through the weights and calculate the cumulative sum.
    4. Return the index where the cumulative sum exceeds the random number.
- Why this approach comes to mind first: This approach is straightforward and easy to understand, but it may not be the most efficient solution.

```cpp
class Solution {
public:
    vector<int> w;
    int sum;

    Solution(vector<int>& w) {
        this->w = w;
        sum = 0;
        for (int weight : w) {
            sum += weight;
        }
    }

    int pickIndex() {
        int randNum = rand() % sum;
        int cumulativeSum = 0;
        for (int i = 0; i < w.size(); i++) {
            cumulativeSum += w[i];
            if (cumulativeSum > randNum) {
                return i;
            }
        }
        return -1; // This should never happen
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$, where $n$ is the number of weights, because we need to iterate through the weights to calculate the cumulative sum.
> - **Space Complexity:** $O(1)$, because we only need a constant amount of space to store the total sum and the random number.
> - **Why these complexities occur:** The time complexity occurs because we need to iterate through the weights, and the space complexity occurs because we only need a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a binary search approach to find the index where the cumulative sum exceeds the random number.
- Detailed breakdown of the approach:
    1. Calculate the total sum of weights.
    2. Generate a random number between 0 and the total sum minus 1.
    3. Use binary search to find the index where the cumulative sum exceeds the random number.
- Proof of optimality: This approach is optimal because it reduces the time complexity from $O(n)$ to $O(\log n)$.
- Why further optimization is impossible: This approach is already optimal because it uses a binary search approach, which is the most efficient way to find an element in a sorted array.

```cpp
class Solution {
public:
    vector<int> w;
    vector<int> cumulativeSum;
    int sum;

    Solution(vector<int>& w) {
        this->w = w;
        cumulativeSum.resize(w.size());
        sum = 0;
        for (int i = 0; i < w.size(); i++) {
            sum += w[i];
            cumulativeSum[i] = sum;
        }
    }

    int pickIndex() {
        int randNum = rand() % sum;
        int left = 0;
        int right = w.size() - 1;
        while (left < right) {
            int mid = left + (right - left) / 2;
            if (cumulativeSum[mid] <= randNum) {
                left = mid + 1;
            } else {
                right = mid;
            }
        }
        return left;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(\log n)$, where $n$ is the number of weights, because we use a binary search approach.
> - **Space Complexity:** $O(n)$, because we need to store the cumulative sum.
> - **Optimality proof:** The time complexity is optimal because we use a binary search approach, and the space complexity is necessary to store the cumulative sum.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Binary search, cumulative sum.
- Problem-solving patterns identified: Using binary search to find an element in a sorted array.
- Optimization techniques learned: Reducing the time complexity by using a binary search approach.
- Similar problems to practice: Random Pick with Blacklist, Random Pick Index.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases, such as an empty input array.
- Edge cases to watch for: An empty input array, a single-element input array.
- Performance pitfalls: Not using a binary search approach, which can lead to a high time complexity.
- Testing considerations: Testing the solution with different input sizes, testing the solution with edge cases.