from lib.sampleapiclient.controller.ApiController import *
from Get_Generate_Headers import *
from authenticationsdk.util.PropertiesUtil import *
from pathlib import Path

class GetMethod:
    def __init__(self):
        # UNIQUE GET ID [EDITABLE]
        self.get_id = "5529992481426498103002"
        # REQUEST TARGET [EDITABLE]
        self.request_target = "/pts/v2/payments/" + self.get_id
        # REQUEST-TYPE [NOT-EDITABLE]
        self.request_type = "GET"
        # give the URL path to where the data needs to be authenticated
        self.url = GlobalLabelParameters.HTTP_URL_PREFIX

    def get_method(self):
        try:
            util_obj = PropertiesUtil()
            util_obj.cybs_path = os.path.join(os.getcwd(), "samples/authentication/Resources", "cybs.json")
            details_dict1 = util_obj.properties_util()

            mconfig = MerchantConfiguration()
            mconfig.set_merchantconfig(details_dict1)

            mconfig.validate_merchant_details(details_dict1, mconfig)

            mconfig.request_type_method = self.request_type
            mconfig.request_target = self.request_target
            mconfig.url = self.url + mconfig.request_host + mconfig.request_target

            self.process(mconfig)
            write_log_audit(200)
        except ApiException as e:
            print(e)
            write_log_audit(400)
        except IOError as e:
            print(GlobalLabelParameters.FILE_NOT_FOUND + str(e.filename))
            write_log_audit(400)
        except KeyError as e:
            print(GlobalLabelParameters.NOT_ENTERED + str(e))
            write_log_audit(400)
        except Exception as e:
            print(e)
            write_log_audit(400)

    # noinspection PyMethodMayBeStatic
    def process(self, mconfig):
        api_controller = ApiController()

        api_controller.payment_get(mconfig)

        print(" URL                : " + mconfig.url)
        print(" Response Code      : " + str(mconfig.response_code))
        print(" V-C-Correlation ID : " + mconfig.v_c_correlation_id)
        print(" Response Message   : " + mconfig.response_message.decode("utf-8"))

def write_log_audit(status):
    print(f"[Sample Code Testing] [{Path(__file__).stem}] {status}")

if __name__ == "__main__":
    sample_obj = GetMethod()
    sample_obj.get_method()
