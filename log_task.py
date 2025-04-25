import textwrap
import datetime

def log_task(max_line_length=80):
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")  

    task_description = input("What did you do today? ") 

    log_file_path = 'daily_log.txt'

    # Wrap the task description for readability
    wrapped_task = textwrap.fill(task_description, width=max_line_length)
    
    # Append the task with date, time, and a newline for readability
    with open(log_file_path, 'a') as log_file:
        log_file.write(f'[{timestamp}] {wrapped_task}\n\n')  # Newline for clear separation
        
    print("Task logged successfully!")

if __name__ == "__main__":
    log_task()
