import couchdb
import csv
import sys
import json

# result.csv

url = 'http://openwhisk:openwhisk@127.0.0.1:5984/'
server = couchdb.Server(url)
inter = server['inter_results']
intra = server['intra_results']

print('Begin Reading Database...')
inter_data = {}
print(len(inter))
for id in inter:
    inter_data[id] = dict(inter[id])
print('Read End')

dir = sys.argv[1]

rows = []
for id in intra:
    intra_doc = dict(intra[id])
    if id not in inter_data:
        print(intra_doc['action_name'])
        continue
    inter_doc = dict(inter_data[id])
    row = { 'id': id, 'action': intra_doc['action_name'], 'intra_latency': intra_doc['intra_latency'], 'start_way': intra_doc['start_way'], 'container_attr': intra_doc['container_attr'], \
        'container_way': intra_doc['container_way'], 'queue_time': intra_doc['queue_time'], \
        'create_time': intra_doc['create_time'], 'rent_time': intra_doc['rent_time'], \
        'inter_start': inter_doc['start'], 'inter_end': inter_doc['end'], \
        'end-to-end': inter_doc['end-to-end'], 'container_start': intra_doc['start_time'], \
            'container_end': intra_doc['end_time'], 'exeuction': intra_doc['duration']}
    rows.append(row)
rows = sorted(rows, key = lambda i: (i['inter_start'], i['inter_end']))

start = float(rows[0]['inter_start'])

new_rows = []
for row in rows:
    if row['container_way'] == 'create' or row['container_way'] == 'rent' or row['container_way'] == 'prewarm':
        new_rows.append({'action': row['action'], 'start': row['start_way'], 'container': row['container_way'], 'create_time': row['create_time'], 'rent_time': row['rent_time'], 'end2end latency': row['intra_latency'], 'time_from_system_start': float(row['inter_start']) - start})

file_name = dir + '/result.csv'
with open(file_name, mode='w') as csv_file:
    fieldnames = ['action', 'start', 'container', 'create_time', 'rent_time', 'end2end latency', 'time_from_system_start']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for row in new_rows:
        writer.writerow(row)


print('Begin Reading Memory...')
memory = server['memory']
print(len(memory))
print('Read End')
# Memory.csv
datas = []
for time_id in memory:
     datas.append({'time': memory[time_id]['time'], 'mem_used':memory[time_id]['mem_used'] , 'mem_total':memory[time_id]['mem_total'], 'mem_load':memory[time_id]['mem_load'], 'cpu_load':memory[time_id]['cpu_load']})
datas = sorted(datas, key = lambda i: (i['time']))
file_name = sys.argv[1] + '/Memory.csv'
with open(file_name, mode='w') as csv_file:
    fieldnames = ['time', 'mem_used', 'mem_total', 'mem_load', 'cpu_load']
    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    writer.writeheader()
    for data in datas:
        writer.writerow(data)


# file_name = sys.argv[1] + '/results.csv'
# with open(file_name, mode='w') as csv_file:
#     fieldnames = ['id', 'action', 'intra_latency', 'start_way', 'container_attr', 'container_way', \
#         'queue_time', 'create_time', 'rent_time', 'inter_start', \
#         'inter_end', 'end-to-end', 'container_start', 'container_end', 'exeuction']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in rows:
#         writer.writerow(row)

# # statistic.csv
# data = {}
# for row in rows:
#     action = row['action']
#     if action not in data:
#         data[action] = {'action': action, 'cold': 0, 'warm': 0, 'prewarm': 0, 'create': 0, 'rent': 0, 'queue': 0}
#     data[action][row['start_way']] += 1
#     data[action][row['container_way']] += 1

# file_name = sys.argv[1] + '/statistic.csv'
# with open(file_name, mode='w') as csv_file:
#     fieldnames = ['action', 'cold', 'warm', 'prewarm', 'create', 'rent', 'queue']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for (k, v) in data.items():
#         writer.writerow(v)


# # lender_info.csv
# lend_info = server['lend_info']

# rows = []
# for id in lend_info:
#     doc = dict(lend_info[id])
#     row = {'id': id, 'time': doc['time'], 'action': doc['action'], 'lender_pool': doc['lender_pool'], 'type': doc['type']}
#     rows.append(row)
# rows = sorted(rows, key = lambda i: (i['time']))

# file_name = sys.argv[1] + '/lender_info.csv'
# with open(file_name, mode='w') as csv_file:
#     fieldnames = ['id', 'time', 'action', 'lender_pool', 'type']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in rows:
#         writer.writerow(row)


# # renter_lender_info.csv
# rent_info = server['renter_lender_info']
# rows = []
# for id in rent_info:
#     doc = dict(rent_info[id])
#     row = {'id': id, 'time': doc['time'], 'lender': doc['lender'], 'renter': doc['renter']}
#     rows.append(row)
# rows = sorted(rows, key = lambda i: (i['time']))

# file_name = sys.argv[1] + '/renter_lender_info.csv'
# with open(file_name, mode='w') as csv_file:
#     fieldnames = ['id', 'time', 'lender', 'renter']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in rows:
#         writer.writerow(row)

# # memory = server['overhead']
# # rows = []
# # for id in memory:
# #     doc = dict(memory[id])
# #     row = {'id': id, 'time': doc['time'], 'inter_memory': doc['inter_memory'], 'intra_memory': doc['intra_memory'], 'inter_cpu': doc['inter_cpu'], 'intra_cpu': doc['intra_cpu']}
# #     rows.append(row)
# # file_name = sys.argv[1] + '/overhead.csv'
# # with open(file_name, mode='w') as csv_file:
# #     fieldnames = ['id', 'time', 'inter_memory', 'intra_memory', 'inter_cpu', 'intra_cpu']
# #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
# #     writer.writeheader()
# #     for row in rows:
# #         writer.writerow(row)

# memory = server['container']
# rows = []
# for id in memory:
#     doc = dict(memory[id])
#     row = {'id': id, 'action': doc['action'], 'time': doc['time'], 'exec': doc['exec'], 'lender': doc['lender'], 'renter': doc['renter']}
#     rows.append(row)
# file_name = sys.argv[1] + '/container.csv'
# with open(file_name, mode='w') as csv_file:
#     fieldnames = ['id', 'action', 'time', 'exec', 'lender', 'renter']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in rows:
#         writer.writerow(row)

# memory = server['zygote_time']
# rows = []
# for id in memory:
#     doc = dict(memory[id])
#     row = {'id': id, 'action': doc['action'], 'time': doc['time'], 'zygote_time': doc['zygote_time']}
#     rows.append(row)
# file_name = sys.argv[1] + '/zygote_time.csv'
# with open(file_name, mode='w') as csv_file:
#     fieldnames = ['id', 'action', 'time', 'zygote_time']
#     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
#     writer.writeheader()
#     for row in rows:
#         writer.writerow(row)

# repack = server['repack_info']
# repack_info = {}
# for id in repack:
#     doc = dict(repack[id])
#     repack_info[id] = doc
# file_name = sys.argv[1] + '/repack_info.json'
# f = open(file_name, 'w', encoding = 'utf-8')
# json.dump(repack_info, f, sort_keys = False, indent = 4)