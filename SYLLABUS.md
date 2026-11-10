# Course Syllabus — Introduction to Python Programming

## Course Information

| Item | Description |
| --- | --- |
| Course title | Introduction to Python Programming |
| Level | Beginner |
| Prerequisites | No prior programming experience required |
| Course length | Seven instructional modules and four applied projects; contact hours may be adapted to the institution's schedule |
| Main environment | Python 3.12+, PyCharm, `uv`, pytest, Ruff, NumPy, and Pandas |

## Course Description

This course introduces programming through Python. Students first learn how
Python source code is translated and executed, then progressively develop the
skills required to structure, validate, and test small applications.

The course combines concise reference notes with practical exercises. Concepts
are applied through command-line projects that increase in scope, from basic
control flow to object-oriented design.

Particular attention is given to code readability, separation of
responsibilities, type annotations, error handling, debugging, and the use of
professional development tools.

## Target Audience

The course is intended for students who are new to programming or who need a
structured introduction to Python before progressing to software development,
data analysis, automation, or machine learning courses.

## Learning Outcomes

By the end of the course, students will be able to:

1. explain, at an introductory level, how Python source code, bytecode, the
   CPython interpreter, machine instructions, and memory interact;
2. create and run an isolated Python project using `uv` and declared
   dependencies;
3. use Python's fundamental types, operators, input/output functions, imports,
   and debugging tools;
4. decompose a problem into small functions with clear responsibilities and
   type annotations;
5. use positional arguments, keyword arguments, `*args`, `**kwargs`, and simple
   recursive functions appropriately;
6. implement decision-making and repetition with Boolean expressions,
   `if`/`elif`/`else`, `match`, and loops;
7. select and manipulate appropriate collections, including lists, tuples,
   dictionaries, sets, strings, and generators;
8. explain mutability, references, hashing, memory layout, and the practical
   impact of collection choices;
9. raise, catch, and handle built-in exceptions without hiding unexpected
   failures;
10. design small programs using classes, dataclasses, enums, instance methods,
    class methods, and static methods;
11. use NumPy arrays for vectorized numerical operations and Pandas objects for
    basic tabular data manipulation;
12. distinguish vectorization from parallel execution and explain why NumPy
    arrays can outperform Python lists for numerical workloads;
13. format, lint, debug, and verify Python code using Ruff, PyCharm, and pytest;
14. represent a program before implementation using flowcharts, finite-state
    machines, decision tables, and trace tables;
15. implement a complete small application from a functional specification.

## Course Content

### Module 1 — Python Fundamentals and Execution Model

- From source code to Python bytecode and CPython execution
- Interpreter, machine code, and processor execution
- Modules, packages, dependencies, and imports
- Virtual environments and dependency management with `uv`
- Fundamental types: integers, floats, strings, Booleans, and `None`
- Variables as references to objects
- Mutability, object identity, memory use, and execution-time implications
- Input/output, conversions, basic operators, and common runtime errors
- Inspecting variables with the PyCharm debugger

### Module 2 — Functions and Decomposition

- Defining and calling functions
- Parameters, return values, scope, and type annotations
- Type hints as development support rather than runtime validation
- Positional and keyword arguments
- `*args` and `**kwargs`
- Naming and readability
- Single-responsibility functions
- Splitting and reusing code
- Recursive functions and base cases

### Module 3 — Control Flow

- Boolean values and truthiness
- Comparison and logical operators
- `if`, `elif`, and `else`
- Pattern matching with `match`
- `while` loops
- Combining control flow with functions

### Module 4 — Collections and Iteration

- Lists, tuples, dictionaries, sets, strings, and generators
- Iteration with `for`
- Indexing, slicing, membership, and collection operations
- Mutable and immutable objects
- Lists as arrays of references
- Dictionaries and sets as hash-table-based structures
- Average constant-time lookup and memory trade-offs
- Memory fragmentation and cache locality
- List and dictionary comprehensions
- Generator expressions and lazy evaluation

### Module 5 — Exceptions

- Reading tracebacks and identifying error types
- `try`, `except`, `else`, and `finally`
- Catching specific exceptions
- Raising errors with `raise`
- Validating user input and business rules
- Separating expected errors from programming errors

### Module 6 — Object-Oriented Programming

- Objects, classes, instances, attributes, and methods
- Constructors and instance state
- Encapsulation and separation of responsibilities
- Dataclasses for structured heterogeneous data
- Dataclasses compared with dictionaries
- Typed dictionaries for dictionary-shaped structured data
- Enums for constrained states and choices
- Instance methods, `@classmethod`, and `@staticmethod`
- Choosing functions instead of classes when no object state is required
- Object-oriented design without unnecessary inheritance

### Module 7 — NumPy and Pandas

- Python lists compared with homogeneous NumPy arrays
- Array shape, dimensions, data types, indexing, and slicing
- Vectorized arithmetic and Boolean masks
- Aggregations and the `axis` argument
- Broadcasting
- NumPy views and copies
- Vectorization, compiled loops, SIMD, the GIL, and parallelism
- Pandas `Series` and `DataFrame`
- Column selection, `.loc`, `.iloc`, and filtering
- Derived columns and vectorized transformations
- Missing values
- Grouping and aggregation with `groupby`

## Practical Work

### Guided Exercises

Each module includes pytest-based exercises. Students complete missing code and
use assertions as an immediate description of the expected behavior. Exercises
are corrected collaboratively during class rather than distributed with a
separate answer repository.

Typical activities include:

- inspecting and transforming variables;
- implementing small functions;
- evaluating conditions and loops;
- manipulating collections and generators;
- validating inputs with exceptions;
- creating classes and dataclasses;
- performing vectorized NumPy and Pandas operations.

### Applied Projects

Before coding each project, students submit a flow document describing the
nominal path, error branches, loops, responsibilities, and—where relevant—the
state transitions. This preliminary design may combine a flowchart, a
finite-state machine, a decision table, and a trace table.

1. **Mini ATM** — authentication, menus, input validation, balances, and
   transaction history.
2. **StockFlow** — stock management, dictionaries, sets, exceptions, movement
   history, and statistics.
3. **MediaFlow** — object-oriented modeling, enums, dataclasses, dictionaries,
   sets, comprehensions, search, and simple loan rules.
4. **Typed Stack-Based Virtual Machine** — final take-home assessment completed
   in groups of one to three students. Students represent typed values,
   instructions, constants, and stack state, then execute simple programs.
   Evaluation includes undisclosed instruction sequences to verify general
   correctness.

Project specifications describe required behavior. Suggested interfaces are
provided only in a final help section so students may first design their own
solution.

## Teaching and Learning Methods

- Short instructor explanations and reference notes
- Live demonstrations in Python and PyCharm
- Guided debugging and code reading
- Incremental pytest exercises
- Individual and collaborative problem solving
- Instructor-led corrections and refactoring discussions
- Applied command-line projects
- A final take-home group assessment
