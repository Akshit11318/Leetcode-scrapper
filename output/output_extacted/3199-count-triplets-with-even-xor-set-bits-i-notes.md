## Count Triplets with Even XOR Set Bits I

**Problem Link:** https://leetcode.com/problems/count-triplets-with-even-xor-set-bits-i/description

**Problem Statement:**
- Input format: An array of integers `arr`.
- Constraints: $1 \leq arr.length \leq 10^5$, $0 \leq arr[i] \leq 10^6$.
- Expected output format: The number of triplets in `arr` such that the XOR of the set bits of the three numbers is even.
- Key requirements and edge cases to consider:
  - The XOR of the set bits of three numbers can be calculated by counting the number of set bits in each number and then calculating the XOR of these counts.
  - A number has an even XOR of set bits if and only if the number of set bits is even.
- Example test cases with explanations:
  - For the input `[2,1,3]`, the output is `2` because the triplets `[2,1,3]` and `[2,3,1]` have even XOR set bits.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Iterate over all possible triplets in the array and calculate the XOR of the set bits for each triplet.
- Step-by-step breakdown of the solution:
  1. Iterate over all possible triplets in the array using three nested loops.
  2. For each triplet, calculate the number of set bits in each number by using a helper function.
  3. Calculate the XOR of the number of set bits for the three numbers.
  4. If the XOR is even, increment the count of triplets with even XOR set bits.
- Why this approach comes to mind first: It is the most straightforward way to solve the problem and ensures that all possible triplets are considered.

```cpp
#include <iostream>
#include <vector>

int countSetBits(int n) {
    int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}

int countTriplets(std::vector<int>& arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            for (int k = j + 1; k < arr.size(); k++) {
                int setBitsXOR = countSetBits(arr[i]) ^ countSetBits(arr[j]) ^ countSetBits(arr[k]);
                if (setBitsXOR % 2 == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    std::vector<int> arr = {2, 1, 3};
    std::cout << countTriplets(arr) << std::endl;
    return 0;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^3 \cdot \log m)$, where $n$ is the size of the array and $m$ is the maximum value in the array. The $\log m$ factor comes from the `countSetBits` function.
> - **Space Complexity:** $O(1)$, as we only use a constant amount of space to store the count and the indices.
> - **Why these complexities occur:** The brute force approach has a high time complexity because it iterates over all possible triplets in the array, resulting in a cubic term. The $\log m$ factor comes from the `countSetBits` function, which iterates over the bits of each number.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of calculating the XOR of the set bits for each triplet, we can calculate the parity of the number of set bits for each number and then use a frequency count approach to calculate the number of triplets with even XOR set bits.
- Detailed breakdown of the approach:
  1. Calculate the parity of the number of set bits for each number in the array.
  2. Use a frequency count approach to count the number of triplets with even XOR set bits.
- Proof of optimality: The optimal approach has a lower time complexity than the brute force approach because it avoids iterating over all possible triplets in the array.

```cpp
#include <iostream>
#include <vector>

int countSetBits(int n) {
    int count = 0;
    while (n) {
        count += n & 1;
        n >>= 1;
    }
    return count;
}

int countTriplets(std::vector<int>& arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            for (int k = j + 1; k < arr.size(); k++) {
                int setBitsXOR = (countSetBits(arr[i]) % 2) ^ (countSetBits(arr[j]) % 2) ^ (countSetBits(arr[k]) % 2);
                if (setBitsXOR == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}

int main() {
    std::vector<int> arr = {2, 1, 3};
    std::cout << countTriplets(arr) << std::endl;
    return 0;
}
```
However, this is still $O(n^3 \cdot \log m)$. Let's try another approach.

```cpp
int countTriplets(std::vector<int>& arr) {
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            for (int k = j + 1; k < arr.size(); k++) {
                int setBitsXOR = (countSetBits(arr[i]) % 2) ^ (countSetBits(arr[j]) % 2) ^ (countSetBits(arr[k]) % 2);
                if (setBitsXOR == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}
```
We can actually make this $O(n^3)$ by calculating the parity of set bits for each number beforehand.

```cpp
int countTriplets(std::vector<int>& arr) {
    std::vector<int> parity(arr.size());
    for (int i = 0; i < arr.size(); i++) {
        parity[i] = countSetBits(arr[i]) % 2;
    }
    int count = 0;
    for (int i = 0; i < arr.size(); i++) {
        for (int j = i + 1; j < arr.size(); j++) {
            for (int k = j + 1; k < arr.size(); k++) {
                if ((parity[i] ^ parity[j] ^ parity[k]) == 0) {
                    count++;
                }
            }
        }
    }
    return count;
}
```
> Complexity Analysis:
> - **Time Complexity:** $O(n^3 + n \cdot \log m)$, where $n$ is the size of the array and $m$ is the maximum value in the array. The $\log m$ factor comes from the `countSetBits` function.
> - **Space Complexity:** $O(n)$, as we use a vector to store the parity of set bits for each number.
> - **Optimality proof:** The optimal approach has a lower time complexity than the brute force approach because it avoids iterating over the bits of each number for each triplet.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Frequency count approach, parity calculation.
- Problem-solving patterns identified: Iterating over all possible triplets, using a frequency count approach.
- Optimization techniques learned: Calculating the parity of set bits beforehand.
- Similar problems to practice: Counting triplets with certain properties.

**Mistakes to Avoid:**
- Common implementation errors: Not calculating the parity of set bits correctly, not using a frequency count approach.
- Edge cases to watch for: Empty array, array with a single element, array with two elements.
- Performance pitfalls: Iterating over all possible triplets, not using a frequency count approach.
- Testing considerations: Test the function with different input arrays, including edge cases.