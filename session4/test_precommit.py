import os
import const


def switch_to_dev_account():
    for name, value in os.environ.items():
        if name.startswith(const.DEV):
            os.environ[name[4:]] = value

def switch_to_cicd_account():
    for name, value in os.environ.items():
        if name.startswith(const.CICD):
            os.environ[name[5:]] = value