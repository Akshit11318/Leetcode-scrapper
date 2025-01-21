## Simple Bank System
**Problem Link:** https://leetcode.com/problems/simple-bank-system/description

**Problem Statement:**
- Input format and constraints: The problem involves designing a simple bank system with a given number of accounts, each with an initial balance. The system should support two operations: `deposit` and `withdraw`. The `deposit` operation adds a specified amount to an account, while the `withdraw` operation subtracts a specified amount from an account if sufficient funds are available.
- Expected output format: The system should return a boolean value indicating whether the operation was successful.
- Key requirements and edge cases to consider:
  - Handle invalid account numbers.
  - Handle insufficient funds for withdrawal.
  - Ensure thread safety for concurrent operations.
- Example test cases with explanations:
  - Creating a bank system with multiple accounts and performing deposit and withdrawal operations.

---

### Brute Force Approach

**Explanation:**
- Initial thought process: The simplest approach is to use a `std::map` to store the account balances, where each account number is a key.
- Step-by-step breakdown of the solution:
  1. Create a `std::map` to store the account balances.
  2. Implement the `deposit` operation by adding the specified amount to the account balance.
  3. Implement the `withdraw` operation by checking if sufficient funds are available and then subtracting the specified amount from the account balance.
- Why this approach comes to mind first: It is the most straightforward way to implement the required functionality.

```cpp
class Bank {
public:
    Bank(vector<long long>& balance) {
        for (int i = 0; i < balance.size(); i++) {
            accounts[i + 1] = balance[i];
        }
    }
    
    bool transfer(int account1, int account2, long long money) {
        if (account1 < 1 || account1 > accounts.size() || account2 < 1 || account2 > accounts.size()) {
            return false;
        }
        if (accounts[account1] < money) {
            return false;
        }
        accounts[account1] -= money;
        accounts[account2] += money;
        return true;
    }
    
    bool deposit(int account, long long money) {
        if (account < 1 || account > accounts.size()) {
            return false;
        }
        accounts[account] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if (account < 1 || account > accounts.size()) {
            return false;
        }
        if (accounts[account] < money) {
            return false;
        }
        accounts[account] -= money;
        return true;
    }

private:
    unordered_map<int, long long> accounts;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for deposit and withdrawal operations, as we are simply updating the account balance.
> - **Space Complexity:** $O(n)$, where n is the number of accounts, as we need to store the account balances.
> - **Why these complexities occur:** The time complexity is constant because we are using a hash map to store the account balances, allowing for constant-time lookups and updates. The space complexity is linear because we need to store the account balances for all accounts.

---

### Optimal Approach (Required)

**Explanation:**
- Key insight that leads to optimal solution: Using an `unordered_map` to store the account balances provides the most efficient way to implement the required functionality.
- Detailed breakdown of the approach:
  1. Create an `unordered_map` to store the account balances.
  2. Implement the `deposit` operation by adding the specified amount to the account balance.
  3. Implement the `withdraw` operation by checking if sufficient funds are available and then subtracting the specified amount from the account balance.
- Proof of optimality: This approach is optimal because it provides constant-time operations for deposit and withdrawal, and it uses the minimum amount of space required to store the account balances.

```cpp
class Bank {
public:
    Bank(vector<long long>& balance) {
        for (int i = 0; i < balance.size(); i++) {
            accounts[i + 1] = balance[i];
        }
    }
    
    bool transfer(int account1, int account2, long long money) {
        if (account1 < 1 || account1 > accounts.size() || account2 < 1 || account2 > accounts.size()) {
            return false;
        }
        if (accounts[account1] < money) {
            return false;
        }
        accounts[account1] -= money;
        accounts[account2] += money;
        return true;
    }
    
    bool deposit(int account, long long money) {
        if (account < 1 || account > accounts.size()) {
            return false;
        }
        accounts[account] += money;
        return true;
    }
    
    bool withdraw(int account, long long money) {
        if (account < 1 || account > accounts.size()) {
            return false;
        }
        if (accounts[account] < money) {
            return false;
        }
        accounts[account] -= money;
        return true;
    }

private:
    unordered_map<int, long long> accounts;
};
```

> Complexity Analysis:
> - **Time Complexity:** $O(1)$ for deposit and withdrawal operations.
> - **Space Complexity:** $O(n)$, where n is the number of accounts.
> - **Optimality proof:** This approach is optimal because it provides the most efficient way to implement the required functionality, with constant-time operations and minimal space usage.

---

### Final Notes

**Learning Points:**
- Key algorithmic concepts demonstrated: Hash maps, constant-time operations.
- Problem-solving patterns identified: Using data structures to optimize operations.
- Optimization techniques learned: Minimizing space usage while maintaining efficient operations.
- Similar problems to practice: Implementing other types of bank systems or financial transactions.

**Mistakes to Avoid:**
- Common implementation errors: Failing to handle edge cases, such as invalid account numbers or insufficient funds.
- Edge cases to watch for: Invalid account numbers, insufficient funds, concurrent operations.
- Performance pitfalls: Using inefficient data structures or algorithms.
- Testing considerations: Thoroughly testing the implementation with various input scenarios and edge cases.