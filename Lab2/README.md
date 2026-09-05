## 1. Triangle Pattern

**Aim:** Prompt the user for the number of rows and display a centered triangle pattern using stars.

**Logic:** Iterate through each row using a loop, printing leading spaces to center the shape while progressively increasing the number of stars in each row.

**Sample Input / Output:**

```text
Enter number of rows: 5

    *
   * *
  * * *
 * * * *
* * * * *
```

---

## 2. Square Pattern

**Aim:** Prompt the user for the side size and print a square grid pattern using stars.

**Logic:** Iterate through the specified number of rows, printing an equal number of stars on every line matching the input size.

**Sample Input / Output:**

```text
Enter size: 5

* * * * *
* * * * *
* * * * *
* * * * *
* * * * *
```

---

## 3. Right Angle Triangle

**Aim:** Prompt the user for the number of rows and display a right-angled triangle pattern using stars.

**Logic:** Iterate through each row, increasing the star count on each line by one for every successive row.

**Sample Input / Output:**

```text
Enter number of rows: 5

*
* *
* * *
* * * *
* * * * *
```

---

## 4. Inverse Triangle

**Aim:** Prompt the user for the number of rows and display an inverted triangle pattern using stars.

**Logic:** Iterate downwards from the given row count to one, decreasing the star count on each line by one step.

**Sample Input / Output:**

```text
Enter number of rows: 5

* * * * *
* * * *
* * *
* *
*
```

---

## 5. Rhombus Pattern

**Aim:** Prompt the user for the number of rows and display a slanted rhombus pattern using stars.

**Logic:** Loop through each row, printing a constant number of stars per line while prepending decreasing leading spaces to create a rhombus slope.

**Sample Input / Output:**

```text
Enter number of rows: 5

    * * * * *
   * * * * *
  * * * * *
 * * * * *
* * * * *
```

---

## 6. Number Pattern

**Aim:** Prompt the user for an integer `n` and render a symmetric concentric number pattern using nested loops.

**Logic:** Use nested `for` loops to generate grid rows and columns. Calculate each element's distance from the boundaries to print values that step down towards the center and expand symmetrically outward.

**Sample Input / Output:**

```text
Enter n: 4

4 4 4 4 4 4 4
4 3 3 3 3 3 4
4 3 2 2 2 3 4
4 3 2 1 2 3 4
4 3 2 2 2 3 4
4 3 3 3 3 3 4
4 4 4 4 4 4 4
```