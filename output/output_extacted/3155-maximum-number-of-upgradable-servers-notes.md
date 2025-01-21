## Maximum Number of Upgradable Servers
**Problem Link:** https://leetcode.com/problems/maximum-number-of-upgradable-servers/description

**Problem Statement:**
- Input format: An array of integers `servers` where `servers[i]` is the capacity of the i-th server and a list of available upgrades `upgrades` where `upgrades[j]` is the capacity increase of the j-th upgrade.
- Constraints: Each upgrade can only be used once, and each server can only be upgraded once.
- Expected output format: The maximum number of servers that can be upgraded.
- Key requirements and edge cases to consider: The number of upgrades is not necessarily equal to the number of servers, and some servers may already have a higher capacity than what can be achieved with the available upgrades.
- Example test cases with explanations:
  - Example 1: `servers = [1, 0, 2]`, `upgrades = [2, 0, 3]`, Expected output: `2`.
  - Example 2: `servers = [2, 4, 3, 2]`, `upgrades = [5, 2, 0]`, Expected output: `3`.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Try all possible combinations of upgrades and servers to find the maximum number of upgradable servers.
- Step-by-step breakdown of the solution:
  1. Sort the `servers` array in ascending order.
  2. Sort the `upgrades` array in descending order.
  3. Use a recursive function to try all possible combinations of upgrades and servers.
  4. In each recursive call, try to upgrade the current server with the current upgrade.
  5. If the upgrade can be applied, recursively call the function with the next server and the next upgrade.
  6. Keep track of the maximum number of upgradable servers found so far.
- Why this approach comes to mind first: It is a straightforward approach that tries all possible combinations, but it is not efficient for large inputs.

```cpp
#include <vector>
#include <algorithm>

int maximumUpgradableServers(std::vector<int>& servers, std::vector<int>& upgrades) {
    std::sort(servers.begin(), servers.end());
    std::sort(upgrades.rbegin(), upgrades.rend());
    int maxUpgradable = 0;
    std::function<void(int, int, int)> tryUpgrades = [&](int serverIndex, int upgradeIndex, int upgradableCount) {
        if (serverIndex == servers.size() || upgradeIndex == upgrades.size()) {
            maxUpgradable = std::max(maxUpgradable, upgradableCount);
            return;
        }
        // Try to upgrade the current server with the current upgrade
        if (servers[serverIndex] + upgrades[upgradeIndex] > 0) {
            tryUpgrades(serverIndex + 1, upgradeIndex + 1, upgradableCount + 1);
        }
        // Try not to upgrade the current server with the current upgrade
        tryUpgrades(serverIndex + 1, upgradeIndex + 1, upgradableCount);
    };
    tryUpgrades(0, 0, 0);
    return maxUpgradable;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(2^{n+m})$, where $n$ is the number of servers and $m$ is the number of upgrades, because we try all possible combinations of upgrades and servers.
> - **Space Complexity:** $O(n+m)$, because we need to store the recursive call stack.
> - **Why these complexities occur:** The brute force approach tries all possible combinations of upgrades and servers, which leads to exponential time complexity.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a greedy approach to solve this problem. We should always try to upgrade the server with the smallest capacity first, because it has the highest chance of being upgradable.
- Detailed breakdown of the approach:
  1. Sort the `servers` array in ascending order.
  2. Sort the `upgrades` array in descending order.
  3. Initialize two pointers, one for the `servers` array and one for the `upgrades` array.
  4. Iterate through the `servers` array and try to upgrade each server with the current upgrade.
  5. If the upgrade can be applied, move to the next server and the next upgrade.
- Proof of optimality: This approach is optimal because it always tries to upgrade the server with the smallest capacity first, which has the highest chance of being upgradable.

```cpp
#include <vector>
#include <algorithm>

int maximumUpgradableServers(std::vector<int>& servers, std::vector<int>& upgrades) {
    std::sort(servers.begin(), servers.end());
    std::sort(upgrades.rbegin(), upgrades.rend());
    int upgradableCount = 0;
    int serverIndex = 0;
    int upgradeIndex = 0;
    while (serverIndex < servers.size() && upgradeIndex < upgrades.size()) {
        if (servers[serverIndex] + upgrades[upgradeIndex] > 0) {
            upgradableCount++;
            serverIndex++;
            upgradeIndex++;
        } else {
            serverIndex++;
        }
    }
    return upgradableCount;
}
```

> Complexity Analysis:
> - **Time Complexity:** $O(n \log n + m \log m)$, where $n$ is the number of servers and $m$ is the number of upgrades, because we sort the `servers` and `upgrades` arrays.
> - **Space Complexity:** $O(1)$, because we only use a constant amount of space.
> - **Optimality proof:** This approach is optimal because it always tries to upgrade the server with the smallest capacity first, which has the highest chance of being upgradable.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Greedy algorithm, sorting.
- Problem-solving patterns identified: Always try to upgrade the server with the smallest capacity first.
- Optimization techniques learned: Using a greedy approach to solve the problem.
- Similar problems to practice: Other problems that involve upgrading or assigning resources.

**Mistakes to Avoid:**
- Common implementation errors: Not sorting the `servers` and `upgrades` arrays, not initializing the pointers correctly.
- Edge cases to watch for: The number of upgrades is not necessarily equal to the number of servers, and some servers may already have a higher capacity than what can be achieved with the available upgrades.
- Performance pitfalls: Using a brute force approach to solve the problem.
- Testing considerations: Test the function with different inputs, including edge cases.