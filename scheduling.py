class Process:
    def __init__(self, pid, arrival_time, burst_time):
        self.pid = pid
        self.at = arrival_time
        self.bt = burst_time
        self.ct = 0   # Completion Time
        self.tat = 0  # Turnaround Time
        self.wt = 0   # Waiting Time

def run_fcfs(processes):
    # Sort processes by Arrival Time
    processes.sort(key=lambda x: x.at)
    current_time = 0
    
    for p in processes:
        if current_time < p.at:
            current_time = p.at  # CPU is idle [cite: 64]
        
        current_time += p.bt
        p.ct = current_time
        p.tat = p.ct - p.at  # TAT = CT - AT [cite: 62]
        p.wt = p.tat - p.bt  # WT = TAT - BT [cite: 63]
    
    return processes

def run_sjf(processes):
    n = len(processes)
    completed = []
    current_time = 0
    # Copy list so we don't modify the original
    ready_pool = list(processes)
    
    while len(completed) < n:
        # Filter processes that have arrived [cite: 77]
        arrived = [p for p in ready_pool if p.at <= current_time]
        
        if not arrived:
            current_time += 1
            continue
            
        # Pick process with the shortest burst time [cite: 76]
        best_p = min(arrived, key=lambda x: x.bt)
        
        current_time += best_p.bt
        best_p.ct = current_time
        best_p.tat = best_p.ct - best_p.at
        best_p.wt = best_p.tat - best_p.bt
        
        completed.append(best_p)
        ready_pool.remove(best_p)
        
    return completed


def show_table(processes, title):
    print(f"\n--- {title} Results ---")
    print("PID\tAT\tBT\tCT\tTAT\tWT")
    for p in processes:
        print(f"{p.pid}\t{p.at}\t{p.bt}\t{p.ct}\t{p.tat}\t{p.wt}")

def print_gantt(processes):
    print("\nGantt Chart Sequence:")
    for p in processes:
        print(f"|  P{p.pid}  ", end="")
    print("|")

if __name__ == "__main__":
    n = int(input("How many processes? "))
    user_processes = []
    
    for i in range(n):
        print(f"\nProcess {i+1}:")
        at = int(input("  Arrival Time: "))
        bt = int(input("  Burst Time: "))
        user_processes.append(Process(i+1, at, bt))
    
    # Run FCFS
    fcfs_res = run_fcfs([Process(p.pid, p.at, p.bt) for p in user_processes])
    show_table(fcfs_res, "FCFS")
    print_gantt(fcfs_res)
    
    # Run SJF
    sjf_res = run_sjf([Process(p.pid, p.at, p.bt) for p in user_processes])
    show_table(sjf_res, "SJF")
    print_gantt(sjf_res)