# CPU Scheduling Algorithms

This repository contains simulation programs for CPU scheduling algorithms, specifically:

- **First-Come, First-Served (FCFS)**
- **Longest-Completed-So-Far (LCSF)**

## Description

CPU scheduling is a core concept in operating systems, determining the order in which processes are executed. This repository provides Python implementations for FCFS and LCSF scheduling algorithms.

The programs simulate CPU scheduling using randomly generated process data and calculate average turnaround and waiting times.

## How to Use

1. Clone or download this repository to your local machine.
2. Each algorithm is implemented in a separate Python file:
   - `fcfs.py`: Simulates the First-Come, First-Served scheduling algorithm.
   - `lcsf.py`: Simulates the Longest-Completed-So-Far scheduling algorithm.

3. Simply run the Python script of your choice to see the results. Example:

   To run FCFS:
   ```bash
   python fcfs.py
   ```
   To run LCSF:
   ```bash
   python lcsf.py
   ```

## Output
The programs will generate example data and print the results, including:
- **Average turnaround time**
- **Average waiting time**

The data used in these simulations is randomly generated, and the results will vary each time you run the program.
