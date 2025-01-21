## Count Good Triplets
**Problem Link:** https://leetcode.com/problems/count-good-triplets/description

**Problem Statement:**
- Input: An array `arr` of integers and two integers `a` and `b`.
- Constraints: `3 <= arr.length <= 100`, `1 <= arr[i] <= 1000`, `0 <= a, b <= 100`.
- Expected output: The number of good triplets.
- Key requirements and edge cases to consider:
  - A triplet `(i, j, k)` is good if `i < j < k`, `arr[i] % a == 0`, `arr[j] % b == 0`, and `arr[k] % a == 0` and `arr[k] % b == 0`.
  - Example test cases: 
    - Input: `arr = [1,1,2,2,3], a = 1, b = 2`, Output: `4`.
    - Input: `arr = [3,1,4,3], a = 5, b = 2`, Output: `0`.

---

### Brute Force Approach

**Explanation:**
- The initial thought process is to check all possible triplets in the array to see if they satisfy the conditions.
- Step-by-step breakdown of the solution:
  1. Generate all possible triplets from the array.
  2. For each triplet, check if it satisfies the conditions `arr[i] % a == 0`, `arr[j] % b == 0`, and `arr[k] % a == 0` and `arr[k] % b == 0`.
  3. Count the number of good triplets.

```cpp
int countGoodTriplets(vector<int>& arr, int a, int b) {
    int count = 0;
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            for (int k = j + 1; k < n; k++) {
                if (arr[i] % a == 0 && arr[j] % b == 0 && arr[k] % a == 0 && arr[k] % b == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3)$, where $n$ is the size of the array, because we are generating all possible triplets.
> - **Space Complexity:** $O(1)$, because we are not using any extra space that scales with the input size.
> - **Why these complexities occur:** The time complexity occurs because we are using three nested loops to generate all possible triplets, and the space complexity is constant because we are only using a fixed amount of space to store the count.

---

### Optimal Approach (Required)

**Explanation:**
- The key insight that leads to the optimal solution is to use a single loop to iterate over the array and count the number of elements that satisfy the conditions for `a` and `b`.
- Detailed breakdown of the approach:
  1. Initialize counts for elements that satisfy `arr[i] % a == 0` and `arr[i] % b == 0`.
  2. Iterate over the array, updating the counts.
  3. Calculate the number of good triplets using the counts.

```cpp
int countGoodTriplets(vector<int>& arr, int a, int b) {
    int count_a = 0, count_b = 0, count_ab = 0;
    for (int num : arr) {
        if (num % a == 0) count_a++;
        if (num % b == 0) count_b++;
        if (num % a == 0 && num % b == 0) count_ab++;
    }
    int n = arr.size();
    int count = 0;
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] % a == 0 && arr[j] % b == 0) {
                count += count_ab;
            }
        }
    }
    return count;
}
```

However, the optimal solution above still has room for improvement because it uses two nested loops. 

Let's try a different approach. For each element, we can count how many elements to its right satisfy `arr[i] % a == 0` and `arr[i] % b == 0`. 

```cpp
int countGoodTriplets(vector<int>& arr, int a, int b) {
    int count = 0;
    int n = arr.size();
    for (int i = 0; i < n; i++) {
        if (arr[i] % a == 0) {
            for (int j = i + 1; j < n; j++) {
                if (arr[j] % b == 0) {
                    int count_ab = 0;
                    for (int k = j + 1; k < n; k++) {
                        if (arr[k] % a == 0 && arr[k] % b == 0) {
                            count_ab++;
                        }
                    }
                    count += count_ab;
                }
            }
        }
    }
    return count;
}
```

But this solution still uses three nested loops. 

A better solution is to use a hash map to store the frequency of elements that satisfy `arr[i] % a == 0` and `arr[i] % b == 0`.

However, there isn't a better solution than the brute force approach for this problem because we must check all possible triplets to count the good ones.

But let's try another approach.

```cpp
int countGoodTriplets(vector<int>& arr, int a, int b) {
    int count = 0;
    int n = arr.size();
    vector<int> count_ab(n);
    for (int i = n - 1; i >= 0; i--) {
        if (arr[i] % a == 0 && arr[i] % b == 0) {
            count_ab[i] = 1;
        }
        if (i < n - 1) {
            count_ab[i] += count_ab[i + 1];
        }
    }
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (arr[i] % a == 0 && arr[j] % b == 0) {
                if (j < n - 1) {
                    count += count_ab[j + 1];
                }
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the size of the array, because we are using two nested loops.
> - **Space Complexity:** $O(n)$, because we are using a vector to store the frequency of elements that satisfy `arr[i] % a == 0` and `arr[i] % b == 0`.
> - **Optimality proof:** This solution is optimal because we must check all possible pairs of elements to count the good triplets.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: counting, nested loops, hash maps.
- Problem-solving patterns identified: counting good triplets, using hash maps to store frequency.
- Optimization techniques learned: reducing the number of loops, using hash maps to store frequency.
- Similar problems to practice: counting good pairs, counting good quadruplets.

**Mistakes to Avoid:**
- Common implementation errors: using incorrect loop bounds, not updating counts correctly.
- Edge cases to watch for: empty arrays, arrays with a single element.
- Performance pitfalls: using too many loops, not using hash maps to store frequency.
- Testing considerations: testing with different inputs, testing with edge cases.