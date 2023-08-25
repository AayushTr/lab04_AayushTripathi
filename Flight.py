class FlightProcess:
    def __init__(self, p_id, process, start_time, priority):
        self.p_id = p_id
        self.process = process
        self.start_time = start_time
        self.priority = priority

class FlightTable:
    def __init__(self):
        self.processes = []

    def add_process(self, process):
        self.processes.append(process)

    def sort_by_pid(self):
        self.processes.sort(key=lambda x: x.p_id)

    def sort_by_start_time(self):
        self.processes.sort(key=lambda x: x.start_time)

    def sort_by_priority(self):
        priority_order = {"High": 1, "MID": 2, "Low": 3}
        self.processes.sort(key=lambda x: priority_order[x.priority])

    def print_table(self):
        print("P_ID  Process   Start Time  Priority")
        for process in self.processes:
            print(f"{process.p_id}    {process.process}    {process.start_time}       {process.priority}")

def main():
    flight_table = FlightTable()

    flight_table.add_process(FlightProcess("P1", "VSCode", 100, "MID"))
    flight_table.add_process(FlightProcess("P23", "Eclipse", 234, "MID"))
    flight_table.add_process(FlightProcess("P93", "Chrome", 189, "High"))
    flight_table.add_process(FlightProcess("P42", "JDK", 9, "High"))
    flight_table.add_process(FlightProcess("P9", "CMD", 7, "High"))
    flight_table.add_process(FlightProcess("P87", "NotePad", 23, "Low"))

    print("Sorting Options:")
    print("1. Sort by P_ID")
    print("2. Sort by Start Time")
    print("3. Sort by Priority")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        flight_table.sort_by_pid()
    elif choice == 2:
        flight_table.sort_by_start_time()
    elif choice == 3:
        flight_table.sort_by_priority()

    flight_table.print_table()

if __name__ == "__main__":
    main()
