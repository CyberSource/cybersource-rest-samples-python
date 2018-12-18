from CyberSource import *
import os
from importlib.machinery import SourceFileLoader

config_file = os.path.join(os.getcwd(), "data", "Configuration.py")
configuration = SourceFileLoader("module.name", config_file).load_module()


def get_user_information():
    try:
        # Reading Merchant details from Configuration file
        config_obj = configuration.Configuration()
        details_dict1 = config_obj.get_configuration()
        user_management_obj = UserManagementApi(details_dict1)

        return_data, status, body = user_management_obj.get_users(organization_id="testrest")
        print("API RESPONSE CODE : ", status)
        print("API RESPONSE BODY : ", body)
    except Exception as e:
        print("Exception when calling UserManagementApi->get_users: %s\n" % e)


if __name__ == "__main__":
    get_user_information()
