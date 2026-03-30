# Task 1: System Input and Data Representation [cite: 372, 376]
def bankers_algorithm():
    # Defining processes and resources [cite: 378]
    n_p = 3  
    n_r = 3
    
    # Input Matrices [cite: 379, 380, 381]
    processes = ["P0", "P1", "P2"]
    allocation = [[1, 0, 0], [2, 1, 1], [2, 2, 2]]
    maximum = [[4, 3, 3], [3, 2, 2], [9, 3, 2]]
    available = [3, 3, 2]

    print("--- TASK 1: SYSTEM INPUT & DATA REPRESENTATION ---")
    print("Process\tAllocation\tMaximum\t\tAvailable")
    for i in range(n_p):
        avail_str = str(available) if i == 0 else ""
        print(f"{processes[i]}\t{allocation[i]}\t{maximum[i]}\t{avail_str}")

    # Task 2: Need Matrix Calculation [cite: 385, 389]
    # Formula: Need = Maximum - Allocation 
    need = []
    for i in range(n_p):
        row = [maximum[i][j] - allocation[i][j] for j in range(n_r)]
        need.append(row)

    print("\n--- TASK 2: NEED MATRIX CALCULATION (Max - Alloc) ---")
    print("Process\tNeed Matrix")
    for i in range(n_p):
        print(f"{processes[i]}\t{need[i]}")

    # Task 3 & 4: Safety Algorithm & Safe Sequence [cite: 397, 411]
    finish = [False] * n_p
    safe_seq = []
    work = list(available) # Work = Available 

    print("\n--- TASK 3 & 4: EXECUTION STEPS & SAFE SEQUENCE ---")
    while len(safe_seq) < n_p:
        found = False
        for i in range(n_p):
            if not finish[i]:
                # Check if Need <= Work [cite: 405]
                if all(need[i][j] <= work[j] for j in range(n_r)):
                    print(f"Checking {processes[i]}: Need {need[i]} <= Work {work} -> YES")
                    # Update Work: Work = Work + Allocation [cite: 406]
                    for j in range(n_r):
                        work[j] += allocation[i][j]
                    finish[i] = True
                    safe_seq.append(processes[i])
                    print(f"Allocating resources... New Work: {work}")
                    found = True
        
        if not found:
            break

    # Task 5: Result Analysis [cite: 422, 428]
    print("\n--- TASK 5: RESULT ANALYSIS ---")
    if len(safe_seq) == n_p:
        print("RESULT: System is in a SAFE STATE.")
        print("SAFE SEQUENCE:", " -> ".join(safe_seq))
    else:
        print("RESULT: System is in an UNSAFE STATE (Potential Deadlock).")

if __name__ == "__main__":
    bankers_algorithm()