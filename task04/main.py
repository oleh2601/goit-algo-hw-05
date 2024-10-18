from pathlib import Path
import sys


def parse_log_line(line: str) -> dict:
    # Split the log 3 times for data, time, group
    # And pass the rest to the message
    date, time, group, message = line.split(' ', maxsplit=3)
    log_dict = {
        "date": date,
        "time": time,
        "group": group,
        "message": message,
        }
    return log_dict

def load_logs(file_path: str) -> list[dict]:
    try:    
        with open(file_path, 'r', encoding='utf-8') as file:
            log_dict_list = []
            for log_line in file:
                # Adding every log to a list of dictionaries 
                # Unless the log is empty
                if log_line.strip() != '':
                    log_dict_list.append(parse_log_line(log_line))
        return log_dict_list
    except IOError as e:
            print(f"File error: {e}")
            sys.exit(1)

def filter_logs_by_level(logs: list, level: str) -> list:
    # Using filter and go through all logs and selected only those who fit
    # The group that user has choosen
    filtered_log_list =  list(
        filter(lambda log:log['group'].upper() == level, logs)
        )
    # Using list comprehension to format each log into a string
    return [f"{log['date']} {log['time']} - {log['message']}" for log in filtered_log_list]


def count_logs_by_level(logs: list) -> dict:
    level_dict = {
        "INFO" : 0,
        "DEBUG" : 0,
        "ERROR" : 0,
        "WARNING" : 0,
    }
    # Counting up total amount of each log group messages
    for log in logs:
        level = log['group'].upper()
        if level in level_dict:
            level_dict[level] += 1
    return level_dict


def display_log_counts(counts: dict):
    # Priting it nicely so the output looks like a table
    print('Log Group  | Amount')
    print(f'{"-"*11}|{"-"*7}')
    for key, value in counts.items():
        print(f"{key:<11}|{value:<7}")


def main():
    # Check the number of arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Syntax: file name *optional*: log group")
        sys.exit(1)
    
    logfile_path = Path(sys.argv[1])

    # Check if file's name is incorrect or ti doesn't exist
    if not logfile_path.is_file():
        print("Incorrect file name or file doesn't exist") 
        sys.exit(1)
    log_list = load_logs(logfile_path)

    # if the level is provided, filter by that level
    if len(sys.argv) == 3:
        # Make sure the group name is valid
        level = sys.argv[2].upper()
        if level not in {'ERROR', 'DEBUG', 'INFO', 'WARNING'}:
            print('Incorrect group name')
            sys.exit(1)
        # If so filter by it
        filtered_log_list = filter_logs_by_level(log_list, level)
        # Displaying the log counts and filtered logs
        display_log_counts(count_logs_by_level(log_list))
        if filtered_log_list:
            print(f'Details of the logs for the level: "{level}": ')
            for log in filtered_log_list:
                print(log)     
        else:
            print(f"No logs found for level '{level}'")    
    else:
        # If there is no specific level requested
        # Just showing log counts
        display_log_counts(count_logs_by_level(log_list))




if __name__ == "__main__":
    main()