# Introduction to Python

## Introduction

This repository documents my journey of learning Python from the basics through hands-on practice.

When I first started learning Python, I tried the traditional approach of following tutorials, watching YouTube videos, and referring to books. While these resources are useful and contain a lot of information, I found that simply following a video or reading through a chapter was not the most effective way for me to learn.

I often found myself understanding a concept while watching or reading it, but struggling to actually remember it or use it when I had to write code on my own. I wanted a learning process that was more interactive and focused on actually understanding why something worked rather than simply remembering how to write it.

Because of this, I decided to approach learning Python differently.

Instead of following a fixed course from beginning to end, I created my own checklist of concepts that I felt I needed to learn. I then worked through these concepts one at a time, using ChatGPT as an interactive learning companion. Rather than simply asking for explanations, I used it to ask questions, clarify things I did not understand, work through examples, create small coding challenges, and troubleshoot code when I got stuck.

The focus was on **practice and understanding rather than note-taking**.

For each topic, the goal was to write code myself, experiment with it, make mistakes, figure out why those mistakes happened, and then try again. This approach helped me turn individual Python concepts into something I could actually use rather than just recognize from a tutorial.

The repository therefore contains a mixture of simple exercises, experiments, challenges, and small programs. Not every program here is intended to be a polished project. Some exist simply because they helped me understand a particular concept.

The purpose of this repository is to document that learning process and the progression from Python fundamentals toward being able to build useful programs independently.

### Learning Approach

The general approach I followed was:

1. Create a checklist of Python concepts I wanted to learn.
2. Learn one concept at a time.
3. Ask questions whenever something was unclear.
4. Write the code myself instead of copying examples.
5. Practice the concept through small challenges.
6. Experiment with different approaches.
7. Debug mistakes and understand why they occurred.
8. Move on only after I felt comfortable using the concept.

This repository is therefore less about presenting perfect code and more about documenting the process of **learning by doing**.
# Stage 1 — Python Fundamentals

Stage 1 focuses on rebuilding my Python fundamentals through hands-on practice. The goal of this stage was not to memorize Python syntax, but to become comfortable writing small programs and understanding how Python behaves when different concepts are combined.

Each concept was practiced through individual Python files, small experiments, and coding challenges. Some of the programs are intentionally simple because they were created to understand a specific concept rather than to serve as complete projects.

## Topics Covered

### 1. Basic Python Syntax

The stage began with the fundamentals of writing and executing a Python program.

Topics practiced included:

- `print()`
- Basic Python syntax
- Comments
- Simple expressions
- Running Python programs from the terminal

The initial programs were intentionally simple and were used to become comfortable with the Python environment before moving into more complex concepts.

**File:** `hello.py`

---

### 2. Variables

Variables were introduced as a way of storing and working with data.

Topics practiced included:

- Creating variables
- Assigning values
- Strings
- Integers
- Using variables in expressions
- Combining multiple variables
- Understanding basic data types

Examples included storing information such as names, ages, and other personal or program-related data.

**File:** `variables.py`

---

### 3. User Input and Type Conversion

After working with predefined values, the next step was making programs interactive.

The `input()` function was practiced to allow programs to receive information from the user.

This stage also introduced type conversion using functions such as:

- `int()`
- `type()`

One important concept learned here was that `input()` returns a string by default, even when the user enters a number. This led to practicing the conversion of user input into integers when required.

**File:** `input.py`

---

### 4. Operators

Different types of Python operators were practiced through small experiments.

These included:

- Arithmetic operators
- Comparison operators
- Assignment and related operators
- Boolean expressions
- Remainder/modulus operations
- Exponentiation
- Floor division

The purpose was to understand how Python evaluates expressions and how operators can be used to create conditions and calculations.

**File:** `operators.py`

---

## 5. Conditional Statements

Conditional statements were introduced to allow programs to make decisions based on different conditions.

### `if`

The `if` statement was used to execute code when a condition evaluates to `True`.

### `else`

The `else` statement was used to provide an alternative when the `if` condition was not satisfied.

### `elif`

Multiple conditions were practiced using `elif`.

One of the exercises involved creating a grading system that assigned different grades depending on the marks entered by the user.

**Files:**

- `if_else.py`
- `elif.py`

---

## 6. Boolean Logic

Boolean values and logical operators were practiced to create more complex conditions.

The following were explored:

- `True`
- `False`
- `and`
- `or`
- `not`

The exercises focused on understanding how multiple conditions can be combined and how Boolean expressions evaluate to either `True` or `False`.

**Files:**

- `boolean_and.py`
- `boolean_or.py`
- `boolean_not.py`

---

# 7. Loops

Loops were introduced to allow programs to repeatedly execute code instead of writing the same instructions multiple times.

## `for` loops

The `for` loop was practiced for iterating through sequences and repeating code a specific number of times.

**File:** `for.py`

## `range()`

The `range()` function was explored alongside `for` loops to control the number and sequence of iterations.

Different forms of `range()` were practiced, including changing the starting value, ending value, and step.

**File:** `range.py`

## `while` loops

The `while` loop was practiced for situations where code needs to continue executing as long as a condition remains true.

**File:** `while.py`

---

# 8. Loop Control Statements

After learning the basic loops, loop-control statements were practiced.

### `break`

Used to immediately terminate a loop when a particular condition is met.

**File:** `break.py`

### `continue`

Used to skip the current iteration and move to the next iteration of a loop.

**File:** `continue.py`

### `pass`

The `pass` statement was explored as a placeholder that allows a block of code to remain syntactically valid without performing an operation.

**File:** `pass.py`

### `enumerate()`

`enumerate()` was practiced for iterating through a sequence while keeping track of the index of each element.

**File:** `enumerate.py`

---

# 9. Nested Loops

Nested loops were introduced after becoming comfortable with individual `for` and `while` loops.

The main concept practiced was placing one loop inside another loop and understanding how the inner loop executes completely for every iteration of the outer loop.

Examples included:

- Working with rows and columns
- Printing structured output
- Creating number patterns
- Creating star (`*`) patterns
- Understanding how the outer loop can control rows while the inner loop controls the contents of each row

**File:** `nested_loops.py`

This was also where concepts such as `print(..., end="")` were explored to control whether output moves to a new line.

---

# Stage 1 Summary

Stage 1 was primarily about building confidence with Python's core programming constructs.

By the end of this stage, I had practiced:

- Basic Python syntax
- `print()`
- Variables
- Basic data types
- User input
- Type conversion
- Operators
- Boolean values
- Boolean logic
- `if`
- `elif`
- `else`
- `for` loops
- `while` loops
- `range()`
- `break`
- `continue`
- `pass`
- `enumerate()`
- Nested loops
- Basic pattern problems

The most important part of this stage was not simply learning the syntax of each feature. It was learning how these features work together.

For example, a simple program could combine:

```text
input
  ↓
type conversion
  ↓
variable
  ↓
condition
  ↓
loop
  ↓
output
