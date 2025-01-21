## Random Pick with Blacklist
**Problem Link:** https://leetcode.com/problems/random-pick-with-blacklist/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `N` and a list of integers `blacklist` which represents the blacklisted numbers, implement a class `Solution` with the following methods:
  - `Solution(int N, vector<int>& blacklist)`: Initializes the object with the given `N` and `blacklist`.
  - `int pick()`: Returns a random integer from `1` to `N` (inclusive) which is not in the `blacklist`.
- Expected output format: A random integer between `1` and `N` (inclusive) that is not in the `blacklist`.
- Key requirements and edge cases to consider: 
  - The `blacklist` is sorted in ascending order.
  - `1 <= N <= 10^9`
  - `0 <= blacklist.length <= min(10^5, N - 1)`
- Example test cases with explanations: 
  - `Solution solution(3, [1]); solution.pick(); // It should return either 2 or 3 randomly.`
  - `Solution solution(4, [2]); solution.pick(); // It should return either 1, 3 or 4 randomly.`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: To solve this problem, one might think of creating a list of all numbers from `1` to `N` and then removing the numbers in the `blacklist`. Then, we can pick a random number from this list.
- Step-by-step breakdown of the solution: 
  - Create a list of all numbers from `1` to `N`.
  - Remove the numbers in the `blacklist` from the list.
  - Use a random number generator to pick a number from the list.
- Why this approach comes to mind first: This approach is straightforward and directly addresses the problem statement.

```cpp
class Solution {
public:
    vector<int> valid;
    Solution(int N, vector<int>& blacklist) {
        for (int i = 1; i <= N; i++) {
            bool found = false;
            for (int num : blacklist) {
                if (i == num) {
                    found = true;
                    break;
                }
            }
            if (!found) {
                valid.push_back(i);
            }
        }
    }

    int pick() {
        int index = rand() % valid.size();
        return valid[index];
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(N \times M)$ where $N$ is the given number and $M$ is the size of the `blacklist`. This is because in the worst case, we are iterating over all numbers from `1` to `N` and for each number, we are checking if it exists in the `blacklist`.
> - **Space Complexity:** $O(N)$ as in the worst case, we might have to store all numbers from `1` to `N` in the `valid` list.
> - **Why these complexities occur:** These complexities occur because we are using a brute force approach that involves iterating over all numbers and checking each number against the `blacklist`.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of removing the blacklisted numbers from the list, we can use a hash set to store the blacklisted numbers and then use a random number generator to generate a number between `1` and `N`. If the generated number is in the hash set, we can generate another number.
- Detailed breakdown of the approach: 
  - Create a hash set to store the blacklisted numbers.
  - Use a random number generator to generate a number between `1` and `N`.
  - If the generated number is in the hash set, generate another number.
- Proof of optimality: This approach is optimal because it has a time complexity of $O(1)$ for the `pick` operation and a space complexity of $O(M)$ where $M$ is the size of the `blacklist`.

```cpp
class Solution {
public:
    unordered_set<int> blacklist;
    int N;
    Solution(int N, vector<int>& blacklist) {
        this->N = N;
        for (int num : blacklist) {
            this->blacklist.insert(num);
        }
    }

    int pick() {
        int num;
        do {
            num = rand() % N + 1;
        } while (blacklist.find(num) != blacklist.end());
        return num;
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for the `pick` operation. However, in the worst case, the `pick` operation might have to generate multiple numbers before finding a valid one, so the average time complexity is $O(1)$ but the worst-case time complexity is $O(N)$.
> - **Space Complexity:** $O(M)$ where $M$ is the size of the `blacklist`.
> - **Optimality proof:** This approach is optimal because it has a time complexity of $O(1)$ for the `pick` operation and a space complexity of $O(M)$.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash sets, random number generation.
- Problem-solving patterns identified: Using a hash set to store blacklisted numbers and generating random numbers.
- Optimization techniques learned: Using a hash set to reduce the time complexity of the `pick` operation.
- Similar problems to practice: Problems that involve generating random numbers and checking against a list of blacklisted numbers.

**Mistakes to Avoid:**
- Common implementation errors: Not checking if the generated number is in the hash set before returning it.
- Edge cases to watch for: The `blacklist` is sorted in ascending order, but this is not used in the optimal solution.
- Performance pitfalls: Using a brute force approach that involves iterating over all numbers and checking each number against the `blacklist`.
- Testing considerations: Testing the `pick` operation with different inputs and checking that it returns a valid number.