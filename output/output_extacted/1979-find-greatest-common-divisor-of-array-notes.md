## Find Greatest Common Divisor of Array
**Problem Link:** https://leetcode.com/problems/find-greatest-common-divisor-of-array/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: `2 <= nums.length <= 1000`, `1 <= nums[i] <= 1000`.
- Expected Output: The greatest common divisor of all the numbers in the array.
- Key Requirements: The solution should efficiently find the greatest common divisor (GCD) of all numbers in the array.
- Edge Cases: The array may contain duplicate numbers, and the GCD may be 1.

**Example Test Cases:**
- Input: `nums = [2,4,6,8]`
- Output: `2`
- Explanation: The GCD of 2, 4, 6, and 8 is 2.
- Input: `nums = [7,5,6,8,3]`
- Output: `1`
- Explanation: The GCD of 7, 5, 6, 8, and 3 is 1.

---

### Brute Force Approach
**Explanation:**
- Initial thought process: Use the Euclidean algorithm to find the GCD of two numbers and then apply it to all pairs of numbers in the array.
- Step-by-step breakdown:
  1. Define a helper function `gcd(a, b)` to calculate the GCD of two numbers using the Euclidean algorithm.
  2. Initialize the result with the first number in the array.
  3. Iterate through the array, updating the result by calculating the GCD of the current result and the next number in the array.
- Why this approach comes to mind first: The Euclidean algorithm is a well-known method for finding the GCD of two numbers, and applying it to all pairs of numbers in the array seems like a straightforward solution.

```cpp
int gcdOfArray(vector<int>& nums) {
    int result = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        result = gcd(result, nums[i]);
    }
    return result;
}

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log \min(nums))$, where $n$ is the length of the array and $\min(nums)$ is the smallest number in the array. This is because the Euclidean algorithm takes $O(\log \min(a, b))$ time to calculate the GCD of two numbers $a$ and $b$, and we apply it to all $n$ numbers in the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result and the current number being processed.
> - **Why these complexities occur:** The time complexity is dominated by the repeated application of the Euclidean algorithm, which takes logarithmic time in the size of the input numbers. The space complexity is constant because we only use a fixed amount of space to store the result and the current number being processed.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: The Euclidean algorithm is already optimal for finding the GCD of two numbers, so we can simply apply it to all pairs of numbers in the array without any further optimization.
- Detailed breakdown: The optimal approach is the same as the brute force approach, as the Euclidean algorithm is already optimal for finding the GCD of two numbers.
- Proof of optimality: The Euclidean algorithm has a time complexity of $O(\log \min(a, b))$, which is optimal because we must at least read the input numbers to calculate their GCD.

```cpp
int gcdOfArray(vector<int>& nums) {
    int result = nums[0];
    for (int i = 1; i < nums.size(); i++) {
        result = gcd(result, nums[i]);
    }
    return result;
}

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log \min(nums))$, where $n$ is the length of the array and $\min(nums)$ is the smallest number in the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the result and the current number being processed.
> - **Optimality proof:** The Euclidean algorithm is already optimal for finding the GCD of two numbers, so applying it to all pairs of numbers in the array without any further optimization is also optimal.

---

### Final Notes
**Learning Points:**
- Key algorithmic concepts demonstrated: The Euclidean algorithm for finding the GCD of two numbers.
- Problem-solving patterns identified: Applying a known algorithm to all pairs of numbers in an array to solve a problem.
- Optimization techniques learned: None, as the Euclidean algorithm is already optimal.
- Similar problems to practice: Finding the least common multiple (LCM) of an array of numbers, finding the GCD of a matrix of numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not handling the base case of the Euclidean algorithm correctly (i.e., when $b = 0$).
- Edge cases to watch for: The array may contain duplicate numbers, and the GCD may be 1.
- Performance pitfalls: Not using the Euclidean algorithm, which can lead to exponential time complexity.
- Testing considerations: Test the solution with arrays containing duplicate numbers and arrays with a GCD of 1.