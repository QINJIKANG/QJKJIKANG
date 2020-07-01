"""
数据层
"""
import os
import pickle
from conf import settings


def save_info(obj):
    user_dir = os.path.join(settings.DB_PATH, obj.__class__.__name__)

    if not os.path.isdir(user_dir):
        os.mkdir(user_dir)

    user_path = os.path.join(user_dir, obj.name)

    with open(user_path, 'wb') as f:
        pickle.dump(obj, f)


# 查看数据
def select_info(cls, name):
    user_dir = os.path.join(settings.DB_PATH, cls.__name__, name)

    if os.path.exists(user_dir):

        with open(user_dir, 'rb') as f:

            obj = pickle.load(f)

            return obj




