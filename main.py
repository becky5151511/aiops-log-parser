from parser import parse_log_line
import csv

# 打开日志文件
with open("sample.log", "r") as f:
    lines = f.readlines()

# 解析所有日志
parsed_logs = [parse_log_line(line) for line in lines if parse_log_line(line)]

# 输出到终端（可选）
for log in parsed_logs:
    print(log)

# 写入 CSV 文件
with open("parsed_output.csv", "w", newline='') as csvfile:
    fieldnames = ["timestamp", "level", "message"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(parsed_logs)

print("\n✅ 结果已写入 parsed_output.csv")
