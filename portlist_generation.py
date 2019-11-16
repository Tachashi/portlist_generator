# -*- coding: utf-8 -*-
from ttp import ttp
import json
import csv

# 各種ファイルのパスを定義
TEMPLATE = './catalyst2960_template_ttp.txt'
PORT_LIST = './port_list_hqaccess1_ttp.csv'
CONFIG_FILENAME = './config_hqaccess1.txt'
CSV_COLUMNS = ['port_no', 'speed', 'duplex', 'mode', 'vlan', 'portfast', 'status', 'description']


def parse_config(template_file, config_filename):
    with open(config_filename, 'rt') as fc:
        data_to_parse = fc.read()

    with open(template_file, 'rt') as ft:
        ttp_template = ft.read()

    # create parser object and parse data using template:
    parser = ttp(data=data_to_parse, template=ttp_template)
    parser.parse()

    # print result in JSON format
    results = parser.result(format='json')[0]
    return results

    # output result in csv format
    # csv_results = parser.result(format='csv')[0]
    # return csv_results


def write_dict_to_csv(port_list, csv_columns, results):
    with open(port_list, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=csv_columns)
        writer.writeheader()
        for data in results:
            writer.writerow(data)
    return            


def main():
    results = parse_config(TEMPLATE, CONFIG_FILENAME)
    print(results)
    results_dict = json.loads(results)
    write_dict_to_csv(PORT_LIST, CSV_COLUMNS, results_dict[0]['l2_interfaces'])


if __name__ == "__main__":
    main()
