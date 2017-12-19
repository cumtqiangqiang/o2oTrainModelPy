import  pandas as pd
from constants import  *
from  datetime import  datetime
import numpy as np
from sklearn.model_selection import train_test_split

def add_label(data):
    received_date = data["Date_received"]
    consume_date = data["Date"]

    label_frame = pd.Series(list(map(lambda x,y: 1. if get_time_diff(x,y) else 0.,
                               received_date,consume_date )))
    label_frame.name = 'label'

    data = data.join(label_frame)

    return data

def get_time_diff(start,end):

    if start != 'null' and end != 'null':
        date_format = '%Y%m%d'
        start_date = datetime.strptime(start, date_format)
        end_date = datetime.strptime(end, date_format)
        if (end_date - start_date).days <= 15 :
            return  True
    else:
        return  False

if __name__ == '__main__':
    # raw_offline_data =  pd.read_csv(TRAIN_OFFLINE_DATA_PATH)
    # data = add_label(raw_offline_data)
    #
    # data.to_csv('Resource/trainLabelData/train_label_data.csv',index=False)
    label_data = pd.read_csv('Resource/trainLabelData/train_label_data.csv')
    offline_user_feature = pd.read_csv('Resource/features/offline/trainUserFeature/user_feature.csv')
    offline_mer_feature = pd.read_csv('Resource/features/offline/trainMerFeature/merchant_feature.csv')
    offline_user_mer_feature = pd.read_csv('Resource/features/offline/trainUserMerFeature/user_merchant_feature.csv')

    online_user_feature = pd.read_csv('Resource/features/online/trainUserFeature/user_feature.csv')
    online_mer_feature = pd.read_csv('Resource/features/online/trainMerFeature/merchant_feature.csv')
    online_user_mer_feature = pd.read_csv('Resource/features/online/trainUserMerFeature/user_merchant_feature.csv')

    user_feature = pd.merge(online_user_feature,on='User_id',how='outer')
    user_feature.tocsv('Resource/features/user_features.csv')
    merchant_feature = pd.merge(online_mer_feature,on='Merchant_id',how='outer')

    merchant_feature.tocsv('Resource/features/mer_features.csv')
















