## Movie Rental Refactoring

A classic refactoring problem from Chapter 1 of
_Refactoring: Improving the Design of Existing Code_ by Martin Fowler.  

This repository contains Python code translated from the Java version.

The runnable `main.py` creates a customer and prints a statement.


## Instructions

See [Movie Rental Refactoring, Part 1](https://cpske.github.io/ISP/assignment/movierental/movierental-part1) for description of the code and what to do.

Before and after each refactoring you should **run the unit tests**.

## Resources

See [Resources](https://cpske.github.io/ISP/assignment/movierental/movierental-part1#resources) in the assignment description.

## Rationale

### 2.1 what refactoring signs (code smells) suggest this refactoring?

**Feature Envy** --
The `Rental` class calculates prices and points based on the `Movie` class's pricing code. This means that `Rental` depends on information from `Movie` that it should probably handle itself.
If we move the pricing code into `Rental`, it won't need to rely on `Movie` as much, and the code will be easier to understand.

### 2.2 what design principle suggests this refactoring? Why?

The **Single Responsibility Principle** (SRP) means that each class should do only one thing. The `Movie` class should only handle information about `movies`, but how much they cost should not include.
If we move the pricing information and calculations to the `Rental` class, each class will do its own job, making the code easier to understand and maintain.

### 5.2 Describe where you implement this method and the reasons for your choice.

I've placed `price_code_for_movie` as a top-level function as part of the rental module, which are aligns with 
* *Low Coupling* -- minimize their (`Movie`, `Rental`) dependencies.
* *High Cohesion* -- The rental.py module focuses on rental-related functionalities, including price code determination.
* *Flexibility* -- can potentially reuse `price_code_for_movie` in other parts of code if needed, further promoting loose coupling.