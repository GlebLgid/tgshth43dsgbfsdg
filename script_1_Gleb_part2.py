import re

def parse_logs(log_file_path):
    with open(log_file_path, 'r') as file:
        logs = file.readlines()

    parsed_logs = []
    for log in logs:
        attacker_ip = re.search(r'Attacker IP: \*\*(.*?)\*\*', log).group(1)
        target = re.search(r'Target: \*\*(.*?)\*\*', log).group(1)
        attack_name = re.search(r'Attack type: \*\*(.*?)\*\*', log).group(1)
        parsed_logs.append((attacker_ip, target, attack_name))

    return parsed_logs

def save_parsed_logs(parsed_logs, output_file_path):
    with open(output_file_path, 'w') as file:
        for log in parsed_logs:
            file.write(f'{log[0]}, {log[1]}, {log[2]}\n')

def main():
    log_file_path = 'log_1.txt'
    output_file_path = 'parsed_logs.csv'
    parsed_logs = parse_logs(log_file_path)
    save_parsed_logs(parsed_logs, output_file_path)

if name == "__main__":
    main()