import json
from datetime import datetime

def filter_by_countdate(input_file, output_file, start_time, end_time):
    start_time = datetime.strptime(start_time, "%Y-%m-%d %H:%M:%S")
    end_time = datetime.strptime(end_time, "%Y-%m-%d %H:%M:%S")

    with open(input_file, 'r') as file:
        data = [json.loads(line) for line in file]

    filtered_data = [entry for entry in data if is_within_time_range(entry.get('countdate'), start_time, end_time)]

    with open(output_file, 'w') as file:
        for entry in filtered_data:
            json.dump(entry, file)
            file.write('\n')

def is_within_time_range(datetime_str, start_time, end_time):
    datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    return start_time <= datetime_obj <= end_time

if __name__ == "__main__":
    input_file_path = "D://countData.7.log"
    output_file_path = "D://filterCountData.log"
    start_time = "2023-11-23 16:30:00"
    end_time = "2023-11-23 19:15:00"

    filter_by_countdate(input_file_path, output_file_path, start_time, end_time)
    print("Filtering completed. Result written to", output_file_path)


