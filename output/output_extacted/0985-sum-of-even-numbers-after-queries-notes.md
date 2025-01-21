## Sum of Even Numbers After Queries
**Problem Link:** https://leetcode.com/problems/sum-of-even-numbers-after-queries/description

**Problem Statement:**
- Input: An array `A` of integers and an array `queries` where each query is of the form `[value, index]`.
- Constraints: `1 <= A.length <= 10000`, `1 <= queries.length <= 10000`, `0 <= value <= 10000`, `0 <= index < A.length`.
- Expected Output: An array where each element at index `i` represents the sum of all even numbers in `A` after applying the first `i` queries.
- Key Requirements: Update the array `A` according to each query and calculate the sum of even numbers after each query.

**Example Test Cases:**
- Input: `A = [1,2,3,4]`, `queries = [[1,0],[-3,1],[-4,0],[2,3]]`
- Output: `[8,6,2,4]`
- Explanation: 
    1. Initially, `A = [1,2,3,4]`, sum of even numbers is `2 + 4 = 6`.
    2. After first query, `A = [2,2,3,4]`, sum of even numbers is `2 + 2 + 4 = 8`.
    3. After second query, `A = [2,-1,3,4]`, sum of even numbers is `2 + 4 = 6`.
    4. After third query, `A = [-2,-1,3,4]`, sum of even numbers is `-2 + 4 = 2`.
    5. After fourth query, `A = [-2,-1,3,6]`, sum of even numbers is `-2 + 6 = 4`.

---

### Brute Force Approach

**Explanation:**
- Iterate through each query and update the array `A` accordingly.
- After each update, calculate the sum of all even numbers in `A`.
- Store each sum in a separate array to return as the result.

```cpp
#include <vector>

std::vector<int> sumEvenAfterQueries(std::vector<int>& A, std::vector<std::vector<int>>& queries) {
    std::vector<int> result;
    for (const auto& query : queries) {
        int value = query[0];
        int index = query[1];
        A[index] += value;
        
        int sum = 0;
        for (int num : A) {
            if (num % 2 == 0) {
                sum += num;
            }
        }
        result.push_back(sum);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot m)$, where $n$ is the number of queries and $m$ is the number of elements in `A`. This is because for each query, we potentially scan all elements of `A`.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queries. We store the sum after each query in the `result` vector.
> - **Why these complexities occur:** The brute force approach involves scanning the entire array `A` for each query to calculate the sum of even numbers, leading to a higher time complexity.

---

### Optimal Approach

**Explanation:**
- Instead of recalculating the sum of all even numbers after each query, maintain a running sum of even numbers in `A`.
- For each query, check if the value being added to `A` is even or odd, and if the element at the index in `A` is even or odd before the addition.
- Update the running sum based on these conditions.

```cpp
#include <vector>

std::vector<int> sumEvenAfterQueries(std::vector<int>& A, std::vector<std::vector<int>>& queries) {
    int evenSum = 0;
    for (int num : A) {
        if (num % 2 == 0) {
            evenSum += num;
        }
    }
    
    std::vector<int> result;
    for (const auto& query : queries) {
        int value = query[0];
        int index = query[1];
        
        // Check if the current element at index is even
        if (A[index] % 2 == 0) {
            evenSum -= A[index];
        }
        
        // Update the element at index
        A[index] += value;
        
        // Check if the new element at index is even
        if (A[index] % 2 == 0) {
            evenSum += A[index];
        }
        
        result.push_back(evenSum);
    }
    return result;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of queries and $m$ is the number of elements in `A`. This is because we make a single pass through `A` to calculate the initial sum of even numbers, and then for each query, we perform a constant amount of work.
> - **Space Complexity:** $O(n)$, where $n$ is the number of queries. We store the sum after each query in the `result` vector.
> - **Optimality proof:** This approach is optimal because it minimizes the amount of work done for each query by only considering the elements that change, rather than recalculating the sum of all even numbers.

---

### Final Notes

**Learning Points:**
- The importance of maintaining a running sum or count to avoid redundant calculations.
- How to update the running sum based on the conditions of the problem (e.g., even or odd numbers).
- The trade-off between the brute force approach (simple but inefficient) and the optimal approach (more complex but efficient).

**Mistakes to Avoid:**
- Failing to consider the initial state of the array `A` and the impact of each query on the sum of even numbers.
- Not updating the running sum correctly based on the conditions of the problem.
- Overlooking the potential for optimizing the calculation of the sum after each query.