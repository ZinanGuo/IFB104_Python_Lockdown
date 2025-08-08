# IFB104 — Infectious Disease Lockdown Simulation (Python Turtle)

![No Usage Allowed](https://img.shields.io/badge/Usage-No%20Usage%20Allowed-red)

A Python-based simulation and visualisation tool developed for the **IFB104 Building IT Systems** course assessment 1.  
The program models how two biological entities move and interact under lockdown conditions, displaying infection spread in real time using **Turtle** graphics.

---

## Features
- **Custom Entity Graphics** — Two unique characters, each with distinct *healthy* and *unwell* states (Part A).
- **Grid-Based Movement** — An 8×8 “lockdown area” with hard state borders (no leaving the grid).
- **Local Government Areas (LGA)** — Left half = LGA A (cols 1–4), right half = LGA B (cols 5–8).
- **Infection Rule** — A healthy entity becomes unwell immediately upon entering the LGA of an unwell entity.
- **Action-Driven Simulation** — Reads a list of actions (initialisation + movements) from a provided `entity_data` module.
- **Overwriting When Co-located** — Later drawings overwrite earlier ones in the same cell (as per spec).

---

## How It Works
1. Draw the grid and place both entities in their **home cells** (marked by dots).
2. Read a dataset (list of actions) from `entity_data.actions()`:
   - **Initialisation** — Starting health for left and right entities.
   - **Movements** — Which entity moves, direction, and number of cells.
3. Enforce rules:
   - Prevent crossing the outer border of the grid.
   - Apply infection as soon as a healthy entity enters the other LGA that currently has an unwell entity.
4. Draw the entity image in **every cell traversed** during movement.

---

## Tech Stack
- Python 3.x
- Built-in `turtle` graphics
- `entity_data.py` (provided for the assessment; **not included** in this repo)

---

## How to Run
> Make sure the program file and `entity_data.py` are in the **same folder**.

```bash
python Assessment_1_Lockdown_Z_G.py
```

> If your file name is different, replace it accordingly.

---

## Reproducible Testing (Fixed Seeds)
By default, each run generates a **new random dataset**.  
For testing or demo purposes, you can pass a fixed **seed** to `actions()` **in the main program** so the same dataset is produced every time (e.g., known “escape”, “cross-LGA infection” scenarios):

```python
# Example inside the main program (for development/demo only):
data = actions(9)  # known scenario; produces identical data each run
```

> When submitting the final program (per brief), **remove the seed** so it works for any random dataset.

---

## Example Scenarios
- **Double Escape Attempt** — Both entities try to leave the grid, but are blocked by borders.
- **Cross-LGA Infection** — A healthy entity becomes unwell upon entering the other LGA.
- **Peaceful Travel** — Both entities remain healthy while moving across LGAs.

---

## Project Context
This solution was delivered in two parts:
- **Part A**: Draw four images (two entities × two states: healthy/unwell) with Turtle; fit precisely in grid cells; include captions; avoid hard-coded absolute coordinates.
- **Part B**: Implement the full movement + infection simulation driven by datasets from `entity_data.actions()`; enforce borders and LGA infection rules.

---

## License & Usage Restrictions
Copyright © 2025 Zinan Guo 
All rights reserved.  

This repository is provided **for viewing purposes only**.  
You may **not** copy, modify, distribute, or use any part of this code for any purpose without the **explicit written permission** of the author.
