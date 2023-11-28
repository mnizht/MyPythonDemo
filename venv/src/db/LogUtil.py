import re


def extract_unids(log_file_path, output_file_path):
    # 定义正则表达式
    regex_pattern = r'\[.*\] \[.*\] \[.*\] \[.*\] ([a-f0-9-]+) .*数据写入错误.*$'

    # 用于存储提取的 unid
    extracted_unids = set()

    # 打开日志文件并逐行处理
    with open(log_file_path, 'r', encoding='utf-8', errors='ignore') as log_file:
        for line in log_file:
            match = re.search(regex_pattern, line)
            if match:
                unid = match.group(1)
                extracted_unids.add(unid)

    # 将提取的 unid 写入输出文件
    with open(output_file_path, 'w') as output_file:
        for unid in extracted_unids:
            output_file.write(unid + '\n')


if __name__ == "__main__":
    log_file_path = "D://vion//store//log-info.log"
    output_file_path = "D://93.txt"

    extract_unids(log_file_path, output_file_path)
    print("Extraction completed. Unids written to", output_file_path)
