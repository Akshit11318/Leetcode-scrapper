## Friends of Appropriate Ages
**Problem Link:** https://leetcode.com/problems/friends-of-appropriate-ages/description

**Problem Statement:**
- Input: An array of integers `ages` representing the ages of people.
- Constraints: $1 \leq ages.length \leq 50$, $1 \leq ages[i] \leq 120$.
- Expected output: The number of pairs of friends of appropriate ages.
- Key requirements: Count the number of pairs where the age of one person is less than or equal to $0.5 * age$ of the other person plus $7$.
- Example test cases:
  - Input: `[16,16]`
    - Output: `2`
    - Explanation: Both people can be friends with each other.
  - Input: `[16,17,18]`
    - Output: `2`
    - Explanation: The person with age $16$ can be friends with the person of age $17$ but not $18$.

---

### Brute Force Approach
**Explanation:**
- The initial thought process is to compare each person's age with every other person's age to see if they can be friends.
- Step-by-step breakdown:
  1. Initialize a variable to store the count of pairs of friends.
  2. Iterate over the `ages` array for each person.
  3. For each person, iterate over the `ages` array again to compare with every other person.
  4. Check if the age condition is met for each pair.
  5. If the condition is met, increment the count of pairs.
- Why this approach comes to mind first: It is straightforward and directly addresses the problem statement.

```cpp
int numFriendRequests(vector<int>& ages) {
    int count = 0;
    for (int i = 0; i < ages.size(); i++) {
        for (int j = 0; j < ages.size(); j++) {
            if (i != j && ages[j] <= 0.5 * ages[i] + 7 && ages[i] > ages[j]) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$, where $n$ is the number of people, because we are using nested loops to compare each person with every other person.
> - **Space Complexity:** $O(1)$, because we are using a constant amount of space to store the count of pairs.
> - **Why these complexities occur:** The time complexity is high because of the nested loops, and the space complexity is low because we only need a single variable to store the count.

---

### Optimal Approach (Required)
**Explanation:**
- Key insight: Instead of comparing each person with every other person, we can observe that the condition for being friends is based on the age of the person and can be generalized.
- Detailed breakdown:
  1. Initialize a variable to store the count of pairs of friends.
  2. Iterate over the `ages` array for each person.
  3. For each person, calculate the lower bound of age that can be a friend based on the condition $0.5 * age + 7$.
  4. Count the number of people whose age is less than or equal to this lower bound and not equal to the current person's age.
  5. Add this count to the total count of pairs.
- Proof of optimality: This approach is optimal because it reduces the number of comparisons needed by directly calculating the potential friends for each person instead of comparing with every other person.

```cpp
int numFriendRequests(vector<int>& ages) {
    int count = 0;
    for (int i = 0; i < ages.size(); i++) {
        int lowerBound = 0.5 * ages[i] + 7;
        for (int j = 0; j < ages.size(); j++) {
            if (i != j && ages[j] <= lowerBound && ages[i] > ages[j]) {
                count++;
            }
        }
    }
    return count;
}
```

However, the above code still has a time complexity of $O(n^2)$ because of the nested loops. To optimize further, we can use a frequency array to store the count of each age and then iterate over the frequency array to calculate the count of pairs.

```cpp
int numFriendRequests(vector<int>& ages) {
    int count = 0;
    int freq[121] = {0}; // Frequency array for ages from 1 to 120
    for (int age : ages) {
        freq[age]++;
    }
    for (int ageA = 1; ageA <= 120; ageA++) {
        if (freq[ageA] == 0) continue; // Skip if no one has this age
        for (int ageB = 1; ageB <= 120; ageB++) {
            if (ageB <= 0.5 * ageA + 7 && ageA > ageB) {
                count += freq[ageA] * freq[ageB];
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m^2)$, where $n$ is the number of people and $m$ is the range of ages (in this case, $m = 120$), because we first iterate over the people to fill the frequency array and then iterate over the possible ages to calculate the count of pairs.
> - **Space Complexity:** $O(m)$, because we use a frequency array of size $m$ to store the count of each age.
> - **Optimality proof:** This is the optimal solution because it minimizes the number of comparisons needed by using a frequency array to reduce the number of iterations.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Using frequency arrays to reduce the number of comparisons.
- Problem-solving patterns identified: Breaking down the problem into smaller sub-problems and using insights to optimize the solution.
- Optimization techniques learned: Reducing the number of iterations by using a frequency array.

**Mistakes to Avoid:**
- Common implementation errors: Not handling edge cases properly, such as when the input array is empty.
- Edge cases to watch for: When the age of one person is exactly equal to the lower bound calculated for another person.
- Performance pitfalls: Using nested loops without optimizing the inner loop.
- Testing considerations: Testing the function with different input arrays, including edge cases like an empty array or an array with duplicate ages.