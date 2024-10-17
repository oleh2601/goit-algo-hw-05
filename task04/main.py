from pathlib import Path
import sys
from collections import Counter

def parse_log_line(line: str) -> dict:
    line_list = line.split(' ')
    log_dict = {
        "date" : line_list[0],
        "time" : line_list[1],
        "group" : line_list[2],
        "message" : ' '.join([line_list[line] for line in range(3, len(line_list))])
        }
    return log_dict

def load_logs(file_path: str) -> list:
    with open(file_path, 'r', encoding='utf-8') as file:
        log_dict_list = []
        for log_line in file:
            log_line = log_line.strip()
            log_dict_list.append(parse_log_line(log_line))
        return log_dict_list

def filter_logs_by_level(logs: list, level: str) -> list:
    filtered_log_list = []
    for log in logs:
        if log.count(level) > 0:
            filtered_log_list.append(log)
    return filtered_log_list


def count_logs_by_level(logs: list) -> dict:
    level_dict = {
        "INFO" : 0,
        "DEBUG" : 0,
        "ERROR" : 0,
        "WARNING" : 0,
    }
    print(logs)
    for log in logs:
        level = log.split(',')[2].strip()
        if level in level_dict:
            level_dict[level] += 1
    return level_dict


def display_log_counts(counts: dict):
    print('Log Group  | Amount')
    print(f'{"-"*11}|{"-"*7}')
    for key, value in counts.items():
        print(f"{key:<11}|{value:<7}")


def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Wrong amount of args")
    elif len(sys.argv) == 2:
        logfile_path = Path(sys.argv[1])
        log_list = load_logs(logfile_path)
        level_counter = Counter()
        for log in log_list:
            level_counter.update(count_logs_by_level(log))
            log_dict = parse_log_line()
        level_dict = dict(level_counter)
        display_log_counts(level_dict)
        
    elif len(sys.argv) == 3:
        logfile_path = Path(sys.argv[1])
        log_list = load_logs(logfile_path)
        level = sys.argv[2].upper()
        filtered_log_list = filter_logs_by_level(log_list, level)
        print('Details of the logs for the level: "{level}": ')
        for log in filtered_log_list:
            print(log)
        




if __name__ == "__main__":
    main()