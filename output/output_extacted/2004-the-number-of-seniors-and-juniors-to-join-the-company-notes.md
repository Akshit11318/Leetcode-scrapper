## The Number of Seniors and Juniors to Join the Company

**Problem Link:** https://leetcode.com/problems/the-number-of-seniors-and-juniors-to-join-the-company/description

**Problem Statement:**
- Input format: A list of integers representing the scores of senior and junior candidates.
- Constraints: Each score is between 0 and 100, and there are at most 100 candidates.
- Expected output format: The number of seniors and juniors to join the company.
- Key requirements and edge cases to consider: 
  - The `seniors` list contains the scores of senior candidates, and the `juniors` list contains the scores of junior candidates.
  - The company wants to hire `seniorsNeeded` seniors and `juniorsNeeded` juniors.
  - The `finalScore` is the minimum score a candidate can have to be hired.
- Example test cases with explanations:
  - Example 1: 
    - Input: `seniors = [10,20,30,40], juniors = [10,20,30,40], seniorsNeeded = 2, juniorsNeeded = 2, finalScore = 30`
    - Output: `4`
    - Explanation: The company hires the 2 seniors with the highest scores (30 and 40) and the 2 juniors with the highest scores (30 and 40).

### Brute Force Approach

**Explanation:**
- Initial thought process: The brute force approach involves sorting both the `seniors` and `juniors` lists in descending order and then selecting the top candidates until the required number of seniors and juniors is reached.
- Step-by-step breakdown of the solution:
  1. Sort the `seniors` list in descending order.
  2. Sort the `juniors` list in descending order.
  3. Initialize counters for seniors and juniors.
  4. Iterate over the sorted lists and select candidates until the required number of seniors and juniors is reached.

```cpp
int countSeniorsAndJuniors(vector<int>& seniors, vector<int>& juniors, int seniorsNeeded, int juniorsNeeded, int finalScore) {
    sort(seniors.rbegin(), seniors.rend());
    sort(juniors.rbegin(), juniors.rend());
    
    int seniorsCount = 0;
    int juniorsCount = 0;
    
    for (int i = 0; i < seniors.size(); i++) {
        if (seniorsCount < seniorsNeeded && seniors[i] >= finalScore) {
            seniorsCount++;
        }
    }
    
    for (int i = 0; i < juniors.size(); i++) {
        if (juniorsCount < juniorsNeeded && juniors[i] >= finalScore) {
            juniorsCount++;
        }
    }
    
    return seniorsCount + juniorsCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$, where $n$ is the number of seniors and $m$ is the number of juniors. This is because we are sorting both lists.
> - **Space Complexity:** $O(1)$, assuming the sorting is done in-place.
> - **Why these complexities occur:** The time complexity is dominated by the sorting operations, and the space complexity is constant because we are not using any additional space that scales with the input size.

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Instead of sorting the entire lists, we can use a two-pointer technique to find the required number of seniors and juniors.
- Detailed breakdown of the approach:
  1. Initialize two pointers, one for seniors and one for juniors, at the beginning of each list.
  2. Iterate over the lists and increment the pointers until the required number of seniors and juniors is reached.
- Proof of optimality: This approach is optimal because it avoids the unnecessary work of sorting the entire lists.

```cpp
int countSeniorsAndJuniors(vector<int>& seniors, vector<int>& juniors, int seniorsNeeded, int juniorsNeeded, int finalScore) {
    int seniorsCount = 0;
    int juniorsCount = 0;
    
    for (int i = 0; i < seniors.size(); i++) {
        if (seniors[i] >= finalScore) {
            seniorsCount++;
            if (seniorsCount == seniorsNeeded) break;
        }
    }
    
    for (int i = 0; i < juniors.size(); i++) {
        if (juniors[i] >= finalScore) {
            juniorsCount++;
            if (juniorsCount == juniorsNeeded) break;
        }
    }
    
    return seniorsCount + juniorsCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of seniors and $m$ is the number of juniors.
> - **Space Complexity:** $O(1)$, assuming we are not using any additional space that scales with the input size.
> - **Optimality proof:** This approach is optimal because it only iterates over the lists once and avoids the unnecessary work of sorting the entire lists.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Two-pointer technique, sorting.
- Problem-solving patterns identified: Avoiding unnecessary work, using optimal data structures.
- Optimization techniques learned: Using a two-pointer technique to avoid sorting the entire lists.
- Similar problems to practice: Problems that involve finding the required number of elements in a list.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for edge cases, not validating input.
- Edge cases to watch for: Empty lists, lists with a single element.
- Performance pitfalls: Using unnecessary data structures or algorithms.
- Testing considerations: Testing with different input sizes, testing with edge cases.