#!/usr/bin/env python3

import re
import operator
import csv
import numpy as np

per_user = {}
info_dict = {}
error_dict = {}
error2 = {"Error": 20}

f = open("log.txt", "r")
lines = f.read()
print(lines)

Error = re.findall(r"ERROR ([\w ]*)", lines)
print(Error)

for Error in Error:
  error_count = lines.count(Error)
  error2[Error] = error_count
  error2 = dict(sorted(error2.items(), key=operator.itemgetter(1), reverse=True))

error2["Error"] = "Count"

print(error2)

# data = re.findall(r"ticky: ([A-Z]*)?([\w+ ]*)?(\[[#][1-9]*\] )?(\(\w+\))", lines)
#
# print(data)

info_regex = r"ticky: INFO([\w+ ]*)?(\[[#][1-9]*\] )?(\(\w+\))"
error_regex = r"ticky: ERROR ([\w+ ]*)?(\(\w+\))"

info_list = re.findall(info_regex, lines)
error_list = re.findall(error_regex, lines)

print(info_list)
print(error_list)



# print(info_dict)
# print(error_dict)

# rows = data.shape[0]
# cols = data.shape[1]
#
# i = 0
# for i in range(0, data[i]):
#         j = 0
#         if data[i][j] == "INFO":
#             j = 3
#             info_dict[data[i][j]] = data.count(data[i][j])
#         if data[i][j] == "ERROR":
#             j = 3
#             error_dict[data[i][j]] = data.count(data[i][j])



# print(info_dict)
# print(error_dict)
