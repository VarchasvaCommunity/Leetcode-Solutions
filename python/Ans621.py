# LeetCode_Solution_For_621_Task_Scheduler
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Count the frequency of each task
        counter = Counter(tasks)

        # Sort the frequencies in ascending order
        freq = sorted(list(counter.values()))

        # Get the maximum frequency (most common task)
        max_idle = freq.pop()

        # Calculate the total idle time needed
        total = (max_idle - 1) * n

        # Distribute other tasks within idle time
        while freq and total > 0:
            # Use the minimum between max_idle - 1 and the next most common task
            total = total - min(max_idle - 1, freq.pop())

        # Ensure total idle time is non-negative
        total = max(0, total)

        # Add the length of the tasks to the total
        return len(tasks) + total