import datetime

# Function to log task with date and time
def log_task():
    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  # Format: YYYY-MM-DD HH:MM:SS

    # Ask for the task description
    task_description = input("What did you do today? ")

    # Path to the log file
    log_file_path = 'daily_log.txt'

    # Append the task with date, time, and a newline for readability
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'[{timestamp}] {task_description}\n\n')
        
    print("Task logged successfully!")

# Run the log task function
if __name__ == "__main__":
    log_task()
