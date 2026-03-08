# Time Complexity of While Loops

The **time complexity of a `while` loop** depends on **how many times the loop executes**.

Time Complexity = **Number of iterations × Work inside the loop**

---

## 1. Increment by 1

```python
i = 0
while i < n:
    i += 1
```

**Explanation**

The value of `i` increases by 1 each iteration.

```
0 → 1 → 2 → 3 → ... → n
```

Number of iterations = **n**

**Time Complexity**

```
O(n)
```

---

## 2. Multiplying by 2

```python
i = 1
while i < n:
    i *= 2
```

**Explanation**

The value doubles each time.

```
1 → 2 → 4 → 8 → 16 → ... → n
```

Number of iterations ≈ **log₂(n)**

**Time Complexity**

```
O(log n)
```

---

## 3. Dividing by 2

```python
n = 100
while n > 0:
    n = n // 2
```

**Explanation**

The value becomes half each iteration.

```
100 → 50 → 25 → 12 → 6 → 3 → 1
```

Number of iterations ≈ **log₂(n)**

**Time Complexity**

```
O(log n)
```

---

## 4. Nested While Loops

```python
i = 0
while i < n:
    j = 0
    while j < n:
        j += 1
    i += 1
```

Outer loop runs **n times**
Inner loop runs **n times**

Total operations:

```
n × n = n²
```

**Time Complexity**

```
O(n²)
```

---

## 5. Removing Digits Example

```python
num = 1234
while num > 0:
    num = num // 10
```

Each step removes one digit.

```
1234 → 123 → 12 → 1 → 0
```

Number of iterations = **number of digits**

Digits of `n` ≈ **log₁₀(n)**

**Time Complexity**

```
O(log n)
```

---

# Summary

| Loop Pattern           | Time Complexity |
| ---------------------- | --------------- |
| `i += 1`               | O(n)            |
| `i *= 2`               | O(log n)        |
| `i //= 2`              | O(log n)        |
| Nested loops           | O(n²)           |
| Digit removal (`//10`) | O(log n)        |

---

# Key Rule

* **Linear growth → O(n)**
* **Halving / Doubling → O(log n)**
* **Nested loops → O(n²)**
