# Python OOP Implementation: Dragon, Wizard, Knight

**Author:** Zoë Finelli  
**Course:** A.B. Cognitive Science - CSCI1300  
**Date:** 29 October 2024

---

## 1. Project Overview

This project features a robust Object-Oriented Programming (OOP) implementation of a console-based strategy game, "Dragon, Wizard, Knight" (a variant of Rock, Paper, Scissors).

The primary objective of this development was to refactor a legacy procedural script—which relied heavily on global variables and linear flow—into a modular, class-based application. This architecture demonstrates core Computer Science principles, including inheritance, polymorphism, and encapsulation, resulting in a highly maintainable and extensible codebase.

### Game Phases
* **Standard Game:** The user competes against an AI opponent ("Sally") for a user-defined number of rounds using the standard interaction triangle (Dragon > Knight > Wizard > Dragon).
* **Bonus Round:** Victory in the standard game unlocks a "Boss Rush" mode. The player must defeat two AI opponents ("Sally" and "Bob") simultaneously. This phase introduces a new variable, the **Druid**, which carries unique high-risk/high-reward scoring rules.

---

## 2. Technical Architecture

The project structure moves away from functional programming towards a strict OOP hierarchy.

### Class Structure

* **`Player` (Base Class)**
    * Serves as the parent interface for all participants.
    * Encapsulates shared attributes (`name`, `points`) to adhere to the **DRY (Don't Repeat Yourself)** principle.
    * Defines an abstract method `choose_move()` to enforce structure in child classes.

* **`HumanPlayer` (Child Class)**
    * Inherits from `Player`.
    * **Polymorphism:** Overrides `choose_move()` to handle standard input (stdin) and implements robust input validation (filtering for valid characters D/W/K).

* **`RobotPlayer` (Child Class)**
    * Inherits from `Player`.
    * **Polymorphism:** Overrides `choose_move()` to implement AI logic (randomized decision-making using the `random` library).

* **`DragonWizardKnightGame` (Controller Class)**
    * Acts as the central engine, managing the entire lifecycle of the application.
    * **State Management:** Replaces global variables with instance attributes (`self.player`, `self.rounds_total`), preventing namespace pollution.
    * **Data-Driven Logic:** Utilizes Hash Maps (Dictionaries) for win/loss condition lookups (`{'d': 'k', ...}`), reducing algorithmic complexity compared to nested `if/else` statements.

---

## 3. Installation & Execution

This project depends only on the Python Standard Library. No external `pip` installations are required.

### Prerequisites
* Python 3.10 or higher

### How to Run
1.  Clone the repository or download the source file.
2.  Navigate to the directory in your terminal.
3.  Execute the script:

```bash
python dragon_wizard_knight.py
