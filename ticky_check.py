#!/usr/bin/env python3

import re
import operator
import csv


per_user = {}
error = {}
info_dict = {}
error_dict = {}

f = open("log.txt", "r")
lines = f.read()
print(lines)

Info = re.findall(r"INFO ([\w ]*)", lines)


Error = re.findall(r"ERROR ([\w ]*)", lines)

print(Info)
print(Error)

usernames = re.findall(r"\(\w+\)", lines)
print(usernames)

for Error in Error:
  Error_count = lines.count(Error)
  error["Error"] = 20
  error[Error] = Error_count
  error = dict(sorted(error.items(), key=operator.itemgetter(1), reverse=True))

for key, value in error.items():
    # do something with value
    if key == "Error":
      error[key] = "Count"
    else:
      error[key] = str(value)

print(error)

list_lines = lines.split("\n")
print(list_lines)

Info_all = re.findall(r"INFO ([\w ]*\[#\d+\] \(\w+\))", lines)
Error_all = re.findall(r"ERROR ([\w ]*\(\w+\))", lines)

Info_count = len(Info)
Error_count = len(Error)

print(Info_count, Error_count)

Info_text = re.findall(r"INFO", lines)
Error_text = re.findall(r"ERROR", lines)


Info_sub = re.sub("INFO ([\w+ ]*\[#\d+\])", "INFO", lines)
Error_sub = re.sub("ERROR ([\w+ ']*)", "ERROR ", Info_sub)

Error_sub.strip("()", )
print(Error_sub)

Info_count = Error_sub.count("INFO")
Error_count = Error_sub.count("ERROR")

info_finder = re.findall(r"INFO \(\w+\)", Error_sub)
error_finder = re.findall(r"ERROR \(\w+\)", Error_sub)
print(len(info_finder))
print(len(error_finder))

print(info_finder)
print(error_finder)

info_finder = list(map(lambda st: str.replace(st, "(", ""), info_finder))
info_finder = list(map(lambda st: str.replace(st, ")", ""), info_finder))

error_finder = list(map(lambda st: str.replace(st, "(", ""), error_finder))
error_finder = list(map(lambda st: str.replace(st, ")", ""), error_finder))

print(info_finder)
print(error_finder)
#
info_list = [word for line in info_finder for word in line.split()]
error_list = [word for line in error_finder for word in line.split()]
#
print(info_list)
print(error_list)
#
print(len(info_list))
print(len(error_list))
#
info_dict = {x:info_list.count(x) for x in info_list}
error_dict = {x:error_list.count(x) for x in error_list}
#
#
print(info_dict)
print(error_dict)
#
#
#
#
for key,value in info_dict.items():
  if key == "INFO":
    info_dict = {"ab_Username": "INFO"}
    # info_dict = {value:key}
    # info_dict[key] = "Username
  else:
    info_dict[key] = str(value)

for key,value in error_dict.items():
  if key == "ERROR":
    error_dict = {"ab_Username": "ERROR"}
    # error_dict = {value:key}
    # error_dict[key] = "Username"
  else:
    error_dict[key] = str(value)
#
info_dict = dict(sorted(info_dict.items(), key=lambda x: x[0].lower()))
error_dict = dict(sorted(error_dict.items(), key=lambda x: x[0].lower()))

print(info_dict)
print(error_dict)
#
for key, value in info_dict.items():
  if key == "ab_Username":
    info_dict = {"Username": "INFO"}
    # del info_dict[oldkey]
  else:
    info_dict[key] = str(value)

for key, value in error_dict.items():
  if key == "ab_Username":
    error_dict = {"Username": "ERROR"}
    # del info_dict[oldkey]
  else:
    error_dict[key] = str(value)

print(error)
print(info_dict)
print(error_dict)
#
for key, value in error_dict.items():
    if key not in info_dict:
      info_dict[key] = "0"
    else:
      pass

print(info_dict)
print(error_dict)
#
for key, value in info_dict.items():
  if key == "Username":
    info_dict = {"ab_Username": "INFO"}
  else:
    info_dict[key] = value
#
info_dict = dict(sorted(info_dict.items(), key=lambda x: x[0].lower()))
# #
for key, value in info_dict.items():
  if key == "ab_Username":
    info_dict = {"Username": "INFO"}
  else:
    info_dict[key] = value
#
print(error)
print(info_dict)
print(error_dict)
#
for key in (info_dict.keys() | error_dict.keys()):
    if key in info_dict: per_user.setdefault(key, []).append(info_dict[key])
    if key in error_dict: per_user.setdefault(key, []).append(error_dict[key])


per_user['(ab_Username)'] = per_user.pop('Username')
per_user = dict(sorted(per_user.items(), key=lambda x: x[0].lower()))

for key, value in per_user.items():
  if key == "(ab_Username)":
    per_user = {"Username": ["INFO", "ERROR"]}
  else:
    per_user[key] = value

print(error)
print(per_user)
#
with open('error_message.csv', 'w') as f:
  for key in error.keys():
    f.write("%s,%s\n" % (key, error[key]))

with open('user_statistics.csv', 'w') as f:
  for key, value in per_user.items():
    if value[0] and value[1] in per_user[key]:
      f.write("%s,%s,%s\n" % (key, value[0], value[1]))
