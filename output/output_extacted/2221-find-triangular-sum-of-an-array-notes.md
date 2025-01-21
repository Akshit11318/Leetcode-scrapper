## Find Triangular Sum of an Array
**Problem Link:** https://leetcode.com/problems/find-triangular-sum-of-an-array/description

**Problem Statement:**
- Input format and constraints: You are given a 1D `array` of integers, and you need to find the triangular sum of this array. The triangular sum is calculated by taking the sum of the elements in each row of a triangular array, where the first row is the input array, and each subsequent row is formed by taking the sum of adjacent elements from the previous row.
- Expected output format: The final sum of the last row.
- Key requirements and edge cases to consider: The input array can be empty, and the array can have a single element.
- Example test cases with explanations: 
    - Input: `[1,2,3,4]`
    - Output: `7`
    - Explanation: The first row is `[1,2,3,4]`. The second row is `[3,5,7]`. The third row is `[8,12]`. The fourth row is `[20]`. The sum of the last row is `20`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, we need to generate the triangular array and then calculate the sum of the last row.
- Step-by-step breakdown of the solution: 
    1. Initialize the first row with the input array.
    2. Generate each subsequent row by taking the sum of adjacent elements from the previous row.
    3. Continue this process until we have generated all rows.
    4. Calculate the sum of the last row.
- Why this approach comes to mind first: This approach is straightforward and directly follows the problem description.

```cpp
vector<int> getRow(vector<int>& prevRow) {
    vector<int> row;
    for (int i = 0; i < prevRow.size() - 1; i++) {
        row.push_back(prevRow[i] + prevRow[i + 1]);
    }
    return row;
}

int triangularSum(vector<int>& nums) {
    vector<int> currentRow = nums;
    while (currentRow.size() > 1) {
        currentRow = getRow(currentRow);
    }
    return currentRow[0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the input array. This is because we are generating a triangular array, and the number of operations is proportional to the sum of the first $n$ natural numbers.
> - **Space Complexity:** $O(n)$, where $n$ is the number of elements in the input array. This is because we need to store the current row, which can have up to $n$ elements.
> - **Why these complexities occur:** The time complexity occurs because we are generating a triangular array, and the space complexity occurs because we need to store the current row.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: The triangular sum can be calculated using the properties of the triangular array. Specifically, the $i^{th}$ element of the $j^{th}$ row is the sum of the $i^{th}$ and $(i + 1)^{th}$ elements of the $(j - 1)^{th}$ row.
- Detailed breakdown of the approach: 
    1. Initialize the first row with the input array.
    2. Generate each subsequent row using the properties of the triangular array.
    3. Continue this process until we have generated all rows.
    4. Calculate the sum of the last row.
- Proof of optimality: This approach is optimal because it has the same time complexity as the brute force approach but with a more efficient implementation.
- Why further optimization is impossible: This approach is already optimal because it has a time complexity of $O(n^2)$, which is the minimum required to generate the triangular array.

```cpp
int triangularSum(vector<int>& nums) {
    int n = nums.size();
    for (int i = n - 2; i >= 0; i--) {
        for (int j = 0; j <= i; j++) {
            nums[j] = (nums[j] + nums[j + 1]) % 10;
        }
    }
    return nums[0];
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of elements in the input array. This is because we are generating a triangular array, and the number of operations is proportional to the sum of the first $n$ natural numbers.
> - **Space Complexity:** $O(1)$, where $n$ is the number of elements in the input array. This is because we are modifying the input array in place.
> - **Optimality proof:** This approach is optimal because it has the same time complexity as the brute force approach but with a more efficient implementation.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: The triangular sum problem demonstrates the use of dynamic programming to solve problems that have overlapping subproblems.
- Problem-solving patterns identified: The problem-solving pattern used in this problem is to identify the base case and the recursive case, and to use dynamic programming to store the results of subproblems.
- Optimization techniques learned: The optimization technique used in this problem is to use dynamic programming to avoid redundant calculations.
- Similar problems to practice: Similar problems to practice include the `House Robber` problem and the `Climbing Stairs` problem.

**Mistakes to Avoid:**
- Common implementation errors: A common implementation error is to forget to initialize the base case or to forget to update the dynamic programming table.
- Edge cases to watch for: An edge case to watch for is when the input array is empty or has a single element.
- Performance pitfalls: A performance pitfall is to use a naive recursive approach that has an exponential time complexity.
- Testing considerations: A testing consideration is to test the function with different input arrays, including edge cases and large inputs.