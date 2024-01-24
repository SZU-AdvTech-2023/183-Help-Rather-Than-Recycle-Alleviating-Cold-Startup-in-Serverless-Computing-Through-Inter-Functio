import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
# from brokenaxes import brokenaxes
from matplotlib import gridspec

matplotlib.rcParams['font.sans-serif'] = ['SimHei']

# generate Fig.2
data = pd.read_csv('aws_result/cold_start.csv')

# names = ['cs_bot', 'ep_users_sign_up', 'ep_products_table_update', 'ep_orders_create_order', 'ep_products_validate',
#          'ep_delivery_on_package_created',
#          'ep_payment_validate', 'ep_warehouse_on_order_events', 'ep_warehouse_table_update',
#          'ep_payment_cancel_payment', 'ep_delivery_table_requests', 'ep_payment_process_payment',
#          'ep_orders_on_event', 'ep_orders_table_update', 'ep_payment_update_payment', 'df_union', 'eo_athenarunner',
#          'eo_gluerunner', 'eo_ons3objectcreated', 'fmp_twitter_streaming',
#          'fmp_twitterddb', 'fmp_comparefaces', 'fp_notification', 'fp_conversion', 'fp_sentiment', 't_payment_method',
#          't_ddb_encrypt_item', 'sc_add_to_cart', 'sc_update_cart',
#          'sc_list_cart', 'sc_migrate_cart', 'sc_checkout_cart', 'sc_delete_from_cart', 'tcp_download_podcast',
#          'tcp_check_transcribe', 'tcp_process_podcast_rss', 'tcp_upload_to_elasticsearch', 'cer_lambda', ]
names = ['cs_bot', 't_payment_method','t_ddb_encrypt_item', 'eo_athenarunner','eo_gluerunner', 'eo_ons3objectcreated','df_union',
         'fmp_twitter_streaming','fmp_twitterddb', 'fmp_comparefaces','cer_lambda',
         'fp_notification', 'fp_conversion', 'fp_sentiment',
         'tcp_download_podcast','tcp_check_transcribe', 'tcp_process_podcast_rss', 'tcp_upload_to_elasticsearch',
         'sc_add_to_cart', 'sc_update_cart','sc_list_cart', 'sc_migrate_cart', 'sc_checkout_cart', 'sc_delete_from_cart',
         'ep_users_sign_up', 'ep_products_table_update', 'ep_orders_create_order', 'ep_products_validate','ep_delivery_on_package_created',
         'ep_payment_validate', 'ep_warehouse_on_order_events', 'ep_warehouse_table_update',
         'ep_payment_cancel_payment', 'ep_delivery_table_requests', 'ep_payment_process_payment',
         'ep_orders_on_event', 'ep_orders_table_update', 'ep_payment_update_payment', ]
# tick_labels = ['bot', ' ', ' ', ' ', ' ', ' ',
#                ' ', 'eco', ' ', ' ', ' ', ' ',
#                ' ', ' ', ' ', 'ddns', ' ', 'etl', ' ', ' ',
#                'rek', ' ', ' ', 'file', ' ', '   tok', ' ', ' ', ' ',
#                ' ', 'cart', ' ', ' ', ' ', '      pod', ' ', ' ', 'rep']
tick_labels = ['bot', '   tok', ' ', ' ', 'etl', ' ',
               'ddns', ' ', 'rek', ' ', 'rep', ' ',
               'file', ' ', ' ', '   pod', ' ', ' ', ' ', ' ',
               '   cart', ' ', ' ', ' ', ' ',  ' ', ' ', ' ',' ',
               ' ', '', 'eco', ' ', ' ', ' ', ' ', ' ', ' ']

pagurus = list(data['pagurus'].values)
prewarm = list(data['prewarm'].values)
sock = list(data['sock'].values)
openwhisk = list(data['openwhisk'].values)

fig, ax = plt.subplots()
# width = 0.23  # the width of the bars: can also be len(x) sequence
fig.set_size_inches(30, 15)
plt.rcParams.update({'font.size': 28})
x = np.arange(38)

# ax.axvline(x=0.5, color='tab:gray', linestyle='--', linewidth=3)
# ax.axvline(x=14.5, color='tab:gray', linestyle='--', linewidth=3)
# ax.axvline(x=15.5, color='tab:gray', linestyle='--', linewidth=3)
# ax.axvline(x=18.5, color='tab:gray', linestyle='--', linewidth=3)
# ax.axvline(x=21.5, color='tab:gray', linestyle='--', linewidth=3)
# ax.axvline(x=24.5, color='tab:gray', linestyle='--', linewidth=3)
# ax.axvline(x=26.5, color='tab:gray', linestyle='--', linewidth=3)
# ax.axvline(x=32.5, color='tab:gray', linestyle='--', linewidth=3)
# ax.axvline(x=36.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=0.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=2.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=5.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=6.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=9.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=10.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=13.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=17.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axvline(x=23.5, color='tab:gray', linestyle='--', linewidth=3)
ax.axhline(y=3.67, color='tab:red', linestyle='--', linewidth=3)

ax.set_ylim(-0.2, 5.0)
ax.set_yticks([0, 2,3.67, 4 , 6, 8, 10])
ax.set_yticklabels(["0","2.0", "3.67","4.0","6.0","8.0","10.0"], fontsize=28)
ax.set_xlim(-0.8, 37.5)
ax.set_xticklabels(tick_labels, fontsize=28)
plt.xticks(x, tick_labels)


ax.plot(x, openwhisk, color='#DA70D6',linewidth=3,label='OpenWhisk(禁用预热)',marker='x', ms=12)
ax.plot(x, prewarm, color='#C0C0C0',linewidth=3,label='OpenWhisk(启用预热)',marker='*', ms=12)
# ax.plot(x, random, color='#c82423',linewidth=3,label='Pagurus-WRS',marker='s', ms=12)
ax.plot(x, pagurus, color='#87CEEB',linewidth=3,label='Pagurus',marker='o', ms=12)
ax.plot(x, sock, color='#90EE90',linewidth=3,label='SOCK',marker='^', ms=12)

plt.xlabel('应用程序名称', fontsize=30)
plt.ylabel('平均冷启动次数', fontsize=30)
ax.legend(ncol=2, fontsize=24,loc = 'upper left',handlelength=1.5)


# plt.show()
fig.savefig("aws_result/fig_2.pdf", bbox_inches='tight')
