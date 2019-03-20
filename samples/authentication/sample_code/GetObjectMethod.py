from lib.sampleapiclient.controller.ApiController import *
from Get_Generate_Headers import *
from authenticationsdk.util.PropertiesUtil import *
from importlib.machinery import SourceFileLoader

request_file = os.path.join(os.getcwd(), "samples/authentication/data", "Configuration.py")
config_data = SourceFileLoader("module.name", request_file).load_module()

class GetObjectMethod:
    def __init__(self):
        # UNIQUE GET ID [EDITABLE]
        self.get_id = "5530001234136115003003"
        # REQUEST TARGET [EDITABLE]
        self.request_target = "/pts/v2/payments/" + self.get_id
        # REQUEST-TYPE [NOT-EDITABLE]
        self.request_type = "GET"
        # give the URL path to where the data needs to be authenticated
        self.url = GlobalLabelParameters.HTTP_URL_PREFIX

    def get_object_method(self):
        try:
            configuration = config_data.Configuration()
            details_dict1 = configuration.get_configuration()
            
            mconfig = MerchantConfiguration()
            mconfig.set_merchantconfig(details_dict1)
            
            mconfig.validate_merchant_details(details_dict1, mconfig)
            
            mconfig.request_type_method = self.request_type
            mconfig.request_target = self.request_target
            mconfig.url = self.url + mconfig.request_host + mconfig.request_target
            
            self.process(mconfig)
        except ApiException as e:
            print(e)
        except IOError as e:
            print(GlobalLabelParameters.FILE_NOT_FOUND + str(e.filename))
        except KeyError as e:
            print(GlobalLabelParameters.NOT_ENTERED + str(e))
        except Exception as e:
            print(e)

    # noinspection PyMethodMayBeStatic
    def process(self, mconfig):
        api_controller = ApiController()
        
        api_controller.payment_get(mconfig)
        
        print(" URL                : " + mconfig.url)
        print(" Response Code      : " + str(mconfig.response_code))
        print(" V-C-Corealation ID : " + mconfig.v_c_correlation_id)
        print(" Response Message   : " + mconfig.response_message.decode("utf-8"))

if __name__ == "__main__":
    sample_obj = GetObjectMethod()
    sample_obj.get_object_method()
