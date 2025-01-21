## Count Good Meals
**Problem Link:** https://leetcode.com/problems/count-good-meals/description

**Problem Statement:**
- Input format and constraints: Given a list of integers `meal_costs` where each integer represents the cost of a meal, and an integer `k`, find the number of pairs of meals that have a total cost equal to `k`.
- Expected output format: The number of pairs of meals that have a total cost equal to `k`.
- Key requirements and edge cases to consider: 
  - The list of meals can be empty.
  - The list of meals can contain duplicate costs.
  - The cost `k` can be any positive integer.
- Example test cases with explanations: 
  - For `meal_costs = [10, 20, 30, 40, 50]` and `k = 90`, the output should be `1` because there is only one pair of meals with a total cost equal to `90`, which is `(40, 50)`.
  - For `meal_costs = [15, 15, 15, 15, 15]` and `k = 30`, the output should be `10` because there are `10` pairs of meals with a total cost equal to `30`, which are `(15, 15)` for each pair of indices.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest way to solve this problem is to use a brute force approach by checking every pair of meals and counting the number of pairs that have a total cost equal to `k`.
- Step-by-step breakdown of the solution: 
  1. Initialize a variable `count` to `0` to store the number of pairs of meals with a total cost equal to `k`.
  2. Iterate over the list of meals using two nested loops to generate all possible pairs of meals.
  3. For each pair of meals, check if the total cost is equal to `k`. If it is, increment the `count` variable.
  4. After checking all pairs of meals, return the `count` variable.

```cpp
int countPairs(vector<int>& meal_costs, int k) {
    int count = 0;
    int n = meal_costs.size();
    for (int i = 0; i < n; i++) {
        for (int j = i + 1; j < n; j++) {
            if (meal_costs[i] + meal_costs[j] == k) {
                count++;
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n^2)$ where $n$ is the number of meals. This is because we are using two nested loops to generate all possible pairs of meals.
> - **Space Complexity:** $O(1)$ because we are only using a constant amount of space to store the `count` variable.
> - **Why these complexities occur:** The time complexity is $O(n^2)$ because we are checking every pair of meals, and the space complexity is $O(1)$ because we are only using a constant amount of space.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a `unordered_map` to store the frequency of each meal cost, and then iterate over the map to count the number of pairs of meals with a total cost equal to `k`.
- Detailed breakdown of the approach: 
  1. Initialize an `unordered_map` `freq` to store the frequency of each meal cost.
  2. Iterate over the list of meals and update the frequency of each meal cost in the `freq` map.
  3. Initialize a variable `count` to `0` to store the number of pairs of meals with a total cost equal to `k`.
  4. Iterate over the `freq` map and for each meal cost `x`, check if `k - x` is also in the map. If it is, increment the `count` variable by the product of the frequencies of `x` and `k - x`.
  5. After checking all meal costs, return the `count` variable.

```cpp
int countPairs(vector<int>& meal_costs, int k) {
    unordered_map<int, int> freq;
    for (int cost : meal_costs) {
        freq[cost]++;
    }
    int count = 0;
    for (auto& pair : freq) {
        int x = pair.first;
        int y = k - x;
        if (y >= x && freq.find(y) != freq.end()) {
            if (x == y) {
                count += freq[x] * (freq[x] - 1) / 2;
            } else {
                count += freq[x] * freq[y];
            }
        }
    }
    return count;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n)$ where $n$ is the number of meals. This is because we are iterating over the list of meals once to update the frequency map, and then iterating over the map once to count the number of pairs of meals.
> - **Space Complexity:** $O(n)$ because we are using an `unordered_map` to store the frequency of each meal cost.
> - **Optimality proof:** This is the optimal solution because we are only iterating over the list of meals once and then iterating over the map once, which reduces the time complexity from $O(n^2)$ to $O(n)$.