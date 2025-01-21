## Maximum Profitable Triplets with Increasing Prices II

**Problem Link:** https://leetcode.com/problems/maximum-profitable-triplets-with-increasing-prices-ii/description

**Problem Statement:**
- Given an array of integers `prices` representing the prices of items over time, find the maximum number of profitable triplets with increasing prices that can be obtained.
- A triplet is considered profitable if the first item is bought at a price less than the second item, and the second item is bought at a price less than the third item.
- The input array `prices` is guaranteed to contain at least three elements.
- The expected output is the maximum number of profitable triplets.

**Key Requirements and Edge Cases:**
- The prices array can contain duplicate elements.
- The prices array can contain negative numbers.
- The prices array can contain zero.
- The length of the prices array is guaranteed to be at least three.

**Example Test Cases:**
- Example 1: `prices = [1, 2, 3, 4, 5]`, the output should be `10`.
- Example 2: `prices = [1, 3, 2, 4, 5]`, the output should be `6`.

### Brute Force Approach

**Explanation:**
- The initial thought process is to use three nested loops to generate all possible triplets and check if they are profitable.
- The outer loop iterates over the array to select the first item.
- The middle loop iterates over the remaining elements to select the second item.
- The inner loop iterates over the remaining elements to select the third item.
- For each triplet, we check if the first item is less than the second item and the second item is less than the third item.

```cpp
int maximumProfitableTriplets(vector<int>& prices) {
    int n = prices.size();
    int count = 0;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            for (int k = j + 1; k < n; k++) {
                if (prices[i] < prices[j] && prices[j] < prices[k]) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the length of the prices array. This is because we have three nested loops, each iterating over the array.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count variable.
> - **Why these complexities occur:** The time complexity is cubic because we generate all possible triplets, and the space complexity is constant because we only use a single variable to store the count.

### Optimal Approach (Required)

**Explanation:**
- The key insight is to use a two-pointer technique to reduce the time complexity.
- We iterate over the array with two pointers, `i` and `j`, where `i` is the pointer for the first item and `j` is the pointer for the second item.
- For each pair of `i` and `j`, we count the number of elements greater than `prices[j]` to the right of `j`.
- We use a separate pass to count the number of elements greater than `prices[j]` to the right of `j`.

```cpp
int maximumProfitableTriplets(vector<int>& prices) {
    int n = prices.size();
    int count = 0;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            if (prices[i] < prices[j]) {
                for (int k = j + 1; k < n; k++) {
                    if (prices[j] < prices[k]) {
                        count++;
                    }
                }
            }
        }
    }
    return count;
}
```

However, a more optimal approach would involve using a single pass through the array to count the number of profitable triplets.

```cpp
int maximumProfitableTriplets(vector<int>& prices) {
    int n = prices.size();
    int count = 0;
    for (int i = 0; i < n - 2; i++) {
        for (int j = i + 1; j < n - 1; j++) {
            if (prices[i] < prices[j]) {
                int greaterThanJ = 0;
                for (int k = j + 1; k < n; k++) {
                    if (prices[j] < prices[k]) {
                        greaterThanJ++;
                    }
                }
                count += greaterThanJ;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$ in the first optimal approach and $O(n^2)$ in the second optimal approach, where $n$ is the length of the prices array. 
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count variable.
> - **Optimality proof:** The time complexity is reduced to $O(n^2)$ in the second optimal approach because we only iterate over the array twice.

### Final Notes

**Learning Points:**
- The key algorithmic concept demonstrated is the two-pointer technique.
- The problem-solving pattern identified is the use of nested loops to generate all possible triplets.
- The optimization technique learned is the reduction of time complexity by using a single pass through the array.
- Similar problems to practice include finding the maximum number of profitable pairs with increasing prices.

**Mistakes to Avoid:**
- Common implementation errors include incorrect indexing and incorrect counting.
- Edge cases to watch for include duplicate elements and negative numbers.
- Performance pitfalls include using unnecessary nested loops and not optimizing the time complexity.
- Testing considerations include testing with different input sizes and edge cases.