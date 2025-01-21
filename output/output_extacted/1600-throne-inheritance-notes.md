## Throne Inheritance

**Problem Link:** https://leetcode.com/problems/throne-inheritance/description

**Problem Statement:**
- Input format: The problem involves a `ThroneInheritance` class with methods to add a `name` and a `parent`, and to get the `inheritanceOrder` after a `king` dies.
- Expected output format: The output should be the order of inheritance.
- Key requirements and edge cases to consider: The king can die at any time, and the inheritance order should be updated accordingly.
- Example test cases with explanations:
  - `ThroneInheritance king("king")`
  - `king.birth("king", "andy")`
  - `king.birth("king", "bob")`
  - `king.birth("andy", "matthew")`
  - `king.birth("bob", "alex")`
  - `king.birth("bob", "asha")`
  - `king.death("andy")`
  - `king.getInheritanceOrder()`

---

### Brute Force Approach

**Explanation:**
- Initial thought process: Create a class `ThroneInheritance` with methods to add a `name` and a `parent`, and to get the `inheritanceOrder` after a `king` dies.
- Step-by-step breakdown of the solution:
  1. Create a `map` to store the children of each person.
  2. Create a `set` to store the dead people.
  3. When a person dies, add them to the `set` of dead people.
  4. When getting the inheritance order, use a depth-first search (DFS) to traverse the family tree, skipping the dead people.
- Why this approach comes to mind first: It's a straightforward approach that uses basic data structures to store the family relationships.

```cpp
class ThroneInheritance {
public:
    map<string, vector<string>> familyTree;
    set<string> deadPeople;
    
    ThroneInheritance(string kingName) {
        familyTree[kingName] = {};
    }
    
    void birth(string parentName, string childName) {
        familyTree[parentName].push_back(childName);
        familyTree[childName] = {};
    }
    
    void death(string name) {
        deadPeople.insert(name);
    }
    
    vector<string> getInheritanceOrder() {
        vector<string> order;
        dfs("king", order);
        return order;
    }
    
    void dfs(string name, vector<string>& order) {
        if (deadPeople.find(name) == deadPeople.end()) {
            order.push_back(name);
        }
        for (string child : familyTree[name]) {
            dfs(child, order);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of family relationships, because we use a DFS to traverse the family tree.
> - **Space Complexity:** $O(n + m)$, because we store the family relationships in a `map` and the dead people in a `set`.
> - **Why these complexities occur:** The DFS traversal and the storage of family relationships cause these complexities.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: We can use a similar approach to the brute force solution, but with a more efficient data structure, such as a `unordered_map` and a `unordered_set`.
- Detailed breakdown of the approach:
  1. Create a `unordered_map` to store the children of each person.
  2. Create a `unordered_set` to store the dead people.
  3. When a person dies, add them to the `set` of dead people.
  4. When getting the inheritance order, use a DFS to traverse the family tree, skipping the dead people.
- Proof of optimality: This approach has the same time and space complexity as the brute force solution, but with a more efficient data structure.

```cpp
class ThroneInheritance {
public:
    unordered_map<string, vector<string>> familyTree;
    unordered_set<string> deadPeople;
    
    ThroneInheritance(string kingName) {
        familyTree[kingName] = {};
    }
    
    void birth(string parentName, string childName) {
        familyTree[parentName].push_back(childName);
        familyTree[childName] = {};
    }
    
    void death(string name) {
        deadPeople.insert(name);
    }
    
    vector<string> getInheritanceOrder() {
        vector<string> order;
        dfs("king", order);
        return order;
    }
    
    void dfs(string name, vector<string>& order) {
        if (deadPeople.find(name) == deadPeople.end()) {
            order.push_back(name);
        }
        for (string child : familyTree[name]) {
            dfs(child, order);
        }
    }
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(n + m)$, where $n$ is the number of people and $m$ is the number of family relationships, because we use a DFS to traverse the family tree.
> - **Space Complexity:** $O(n + m)$, because we store the family relationships in a `map` and the dead people in a `set`.
> - **Optimality proof:** The use of a `unordered_map` and a `unordered_set` makes this approach more efficient than the brute force solution, while maintaining the same time and space complexity.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: DFS traversal, use of `map` and `set` data structures.
- Problem-solving patterns identified: Using a more efficient data structure can improve the performance of the solution.
- Optimization techniques learned: Using a `unordered_map` and a `unordered_set` can improve the performance of the solution.
- Similar problems to practice: Problems that involve traversing a tree or graph, such as finding the shortest path or the minimum spanning tree.

**Mistakes to Avoid:**
- Common implementation errors: Not checking for dead people when getting the inheritance order.
- Edge cases to watch for: When a person dies, we need to add them to the `set` of dead people.
- Performance pitfalls: Using a less efficient data structure, such as a `map` instead of a `unordered_map`.
- Testing considerations: We should test the solution with different family relationships and death scenarios to ensure that it works correctly.