from CyberSource import *
import os
from importlib.machinery import SourceFileLoader
config_file = os.getcwd() + "\\data\\Configuration.py"
configuration = SourceFileLoader("module.name", config_file).load_module()

def get_user_information():
    try:
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        user_management_obj = UserManagementApi(details_dict1)

        return_data, status, body= user_management_obj.get_users(organization_id="testrest")
        print(status)
        print(body)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    get_user_information()
