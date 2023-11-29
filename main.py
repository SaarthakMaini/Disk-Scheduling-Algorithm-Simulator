import matplotlib.pyplot as plt

class DiskSchedulerSimulator:
    def __init__(self, initial_position, requests):
        self.initial_position = initial_position
        self.requests = requests
        self.sequence_dict = {}

    def fcfs(self):
        self.sequence_dict['FCFS'] = self.requests.copy()

    def sstf(self):
        self.sequence_dict['SSTF'] = sorted(self.requests, key=lambda x: abs(x - self.initial_position))

    def scan(self):
        sorted_requests = sorted(self.requests)
        lower = [r for r in sorted_requests if r < self.initial_position]
        upper = [r for r in sorted_requests if r >= self.initial_position]
        self.sequence_dict['SCAN'] = lower + upper

    def c_scan(self):
        sorted_requests = sorted(self.requests)
        lower = [r for r in sorted_requests if r < self.initial_position]
        upper = [r for r in sorted_requests if r >= self.initial_position]
        self.sequence_dict['C-SCAN'] = upper + lower

    def look(self):
        sorted_requests = sorted(self.requests)
        lower = [r for r in sorted_requests if r < self.initial_position]
        upper = [r for r in sorted_requests if r > self.initial_position]
        self.sequence_dict['LOOK'] = lower + upper

    def c_look(self):
        sorted_requests = sorted(self.requests)
        lower = [r for r in sorted_requests if r < self.initial_position]
        upper = [r for r in sorted_requests if r > self.initial_position]
        self.sequence_dict['C-LOOK'] = upper + lower

    def visualize_all(self):
        plt.figure(figsize=(12, 6))
        for algorithm_name, sequence in self.sequence_dict.items():
            plt.step(range(len(sequence)), sequence, label=algorithm_name)

        plt.title('Disk Scheduling Algorithms Comparison')
        plt.xlabel('Request Order')
        plt.ylabel('Disk Position')
        plt.legend()
        plt.show()

initial_position = 50
requests_sequence = [82, 170, 43, 140, 24, 16, 190]

simulator = DiskSchedulerSimulator(initial_position, requests_sequence)

simulator.fcfs()
simulator.sstf()
simulator.scan()
simulator.c_scan()
simulator.look()
simulator.c_look()

simulator.visualize_all()
