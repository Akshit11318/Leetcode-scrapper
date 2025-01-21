## GCD Sort of an Array

**Problem Link:** https://leetcode.com/problems/gcd-sort-of-an-array/description

**Problem Statement:**
- Input: An array of integers `nums`.
- Constraints: The array contains at least one element and at most $10^5$ elements, with each element in the range $[1, 10^5]$.
- Expected output: Determine if it's possible to sort the array in ascending order such that the `gcd` of any two adjacent elements is greater than 1.
- Key requirements and edge cases to consider: The input array may not be sorted initially, and we need to check for the possibility of sorting it under the given condition. The `gcd` of two numbers greater than 1 implies they share a common divisor other than 1.
- Example test cases with explanations:
  - For `nums = [2,4,6,8]`, the answer is `true` because the array can be sorted as `[2,4,6,8]` and the `gcd` of any two adjacent numbers is greater than 1.
  - For `nums = [2,4,1]`, the answer is `false` because no matter how we sort the array, there will always be a pair of adjacent numbers with a `gcd` of 1 (e.g., `1` and any other number).

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Generate all permutations of the array and check each permutation to see if it satisfies the condition that the `gcd` of any two adjacent elements is greater than 1.
- Step-by-step breakdown of the solution:
  1. Generate all permutations of the input array `nums`.
  2. For each permutation, iterate through the array and calculate the `gcd` of each pair of adjacent elements.
  3. If the `gcd` of any pair of adjacent elements is 1, mark the permutation as invalid.
  4. If a permutation is found where all pairs of adjacent elements have a `gcd` greater than 1, return `true`.
- Why this approach comes to mind first: It's a straightforward, albeit inefficient, way to check all possible arrangements of the array.

```cpp
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int gcd(int a, int b) {
    if (b == 0) return a;
    return gcd(b, a % b);
}

bool gcdSortOfAnArrayBrute(vector<int>& nums) {
    sort(nums.begin(), nums.end());
    do {
        bool valid = true;
        for (int i = 0; i < nums.size() - 1; ++i) {
            if (gcd(nums[i], nums[i+1]) == 1) {
                valid = false;
                break;
            }
        }
        if (valid) return true;
    } while (next_permutation(nums.begin(), nums.end()));
    return false;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n! \cdot n)$, where $n$ is the number of elements in the array. This is because we generate all permutations of the array (which is $O(n!)$) and for each permutation, we check the `gcd` of adjacent elements (which takes $O(n)$ time).
> - **Space Complexity:** $O(1)$, not counting the space needed for the input and output, because we only use a constant amount of space to store the `gcd` of two numbers and the loop counters.
> - **Why these complexities occur:** The high time complexity comes from generating all permutations of the array, which grows factorially with the size of the input. The space complexity is low because we don't use any data structures that scale with the input size.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of checking all permutations, we can use the fact that if two numbers have a `gcd` greater than 1, they must share a common prime factor. Thus, we can group numbers by their prime factors and check if it's possible to arrange them such that adjacent numbers always share a prime factor.
- Detailed breakdown of the approach:
  1. Find all prime factors of each number in the array.
  2. Create a graph where each number is a node, and two nodes are connected if their corresponding numbers share a prime factor.
  3. Check if the graph is connected. If it is, then it's possible to arrange the numbers such that any two adjacent numbers share a prime factor (and thus have a `gcd` greater than 1).
- Proof of optimality: This approach is optimal because it directly addresses the condition required for the array to be sorted (i.e., adjacent elements having a `gcd` greater than 1) without unnecessarily exploring all permutations.

```cpp
#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;

vector<int> primeFactors(int n) {
    vector<int> factors;
    for (int i = 2; i * i <= n; ++i) {
        if (n % i == 0) {
            factors.push_back(i);
            while (n % i == 0) n /= i;
        }
    }
    if (n > 1) factors.push_back(n);
    return factors;
}

bool gcdSortOfAnArrayOptimal(vector<int>& nums) {
    unordered_map<int, vector<int>> graph;
    for (int num : nums) {
        vector<int> factors = primeFactors(num);
        for (int factor : factors) {
            if (graph.find(factor) == graph.end()) graph[factor] = {};
            graph[factor].push_back(num);
        }
    }
    
    for (auto& pair : graph) {
        sort(pair.second.begin(), pair.second.end());
    }
    
    for (int num : nums) {
        vector<int> factors = primeFactors(num);
        bool hasNeighbor = false;
        for (int factor : factors) {
            auto it = lower_bound(graph[factor].begin(), graph[factor].end(), num);
            if (it != graph[factor].end() && *it == num) {
                if (it > graph[factor].begin()) hasNeighbor = true;
                if (it + 1 < graph[factor].end()) hasNeighbor = true;
            } else if (it > graph[factor].begin()) hasNeighbor = true;
            else if (it < graph[factor].end()) hasNeighbor = true;
        }
        if (!hasNeighbor) return false;
    }
    return true;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \cdot \sqrt{m})$, where $n$ is the number of elements in the array and $m$ is the maximum value in the array. This is because for each number, we find its prime factors (which takes $O(\sqrt{m})$ time), and we do this for all $n$ numbers.
> - **Space Complexity:** $O(n + m)$, because in the worst case, we might store all numbers in the graph.
> - **Optimality proof:** This approach is optimal because it avoids the exponential time complexity of generating all permutations and directly focuses on the condition that allows the array to be sorted (adjacent elements having a `gcd` greater than 1).

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Prime factorization, graph theory.
- Problem-solving patterns identified: Using mathematical properties (like `gcd`) to reduce the problem space, applying graph theory to model relationships between elements.
- Optimization techniques learned: Avoiding brute force by identifying key properties of the problem that can be leveraged for efficiency.
- Similar problems to practice: Problems involving `gcd`, prime factorization, and graph theory.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases properly (e.g., an empty array, an array with a single element).
- Edge cases to watch for: Arrays with duplicate elements, arrays where all elements are prime numbers.
- Performance pitfalls: Using inefficient algorithms for finding prime factors or checking graph connectivity.
- Testing considerations: Thoroughly testing with various inputs, including edge cases and large inputs to ensure efficiency.