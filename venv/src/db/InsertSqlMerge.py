def merge_inserts(sql_file, chunk_size, output_file):
    with open(sql_file, 'r', encoding='UTF-8') as file:
        lines = file.readlines()

    merged_queries = []
    values_list = []

    for line in lines:
        if line.startswith('INSERT'):
            values_start = line.find('VALUES') + len('VALUES')
            values_end = line.rfind(';')
            values = line[values_start:values_end].strip()
            values_list.append(values)

        if len(values_list) >= chunk_size:
            merged_values = ',\n'.join(values_list)
            merged_query = lines[0].split('VALUES')[0] + 'VALUES \n' + merged_values + ';'
            merged_queries.append(merged_query)
            values_list = []

    # 处理剩余的 INSERT 语句
    if values_list:
        merged_values = ',\n'.join(values_list)
        merged_query = lines[0].split('VALUES')[0] + 'VALUES \n' + merged_values + ';'
        merged_queries.append(merged_query)

    # 将合并后的 INSERT 语句写入新的 SQL 文件中
    with open(output_file, 'w', encoding='UTF-8') as out_file:
        for query in merged_queries:
            out_file.write(query + '\n')

if __name__ == '__main__':
    sql_file = 'D:/Data/b_table.sql'
    chunk_size = 100  # 可配置的变量值，表示合并的条数
    output_file = 'D:/Data/merged.sql'
    merged_queries = merge_inserts(sql_file, chunk_size, output_file)

