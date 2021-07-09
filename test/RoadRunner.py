import json
import unittest
import os
import time
from importlib import import_module
from importlib.machinery import SourceFileLoader

class Test(unittest.TestCase):
    def recurse(self, return_data, fieldpath):
        field_list = fieldpath.split('.')
        #Creating a copy of the dictionary passed as param
        return_data_copy = return_data
        #Iterating through each level of dictionary to get required value
        for fields in field_list:
            fields = "_" + fields

            if "[" in fields:
                array_field = fields.split('[')[0]
                array_index = int(fields.split('[')[1].split(']')[0])
                fields = array_field

            #Checking whether we can access more levels of the dictionary or not
            try:
                if type(return_data_copy[fields]) == str or type(return_data_copy[fields]) == int:
                    return return_data_copy[fields]
                elif isinstance(return_data_copy[fields], list):
                    return_data_copy = return_data_copy[fields][array_index]
                else:
                    return_data_copy = return_data_copy[fields].__dict__
            except:
                return getattr(return_data_copy, fields)

    #Converting field name to one that follows Python naming convention
    def modify_name(self, fieldname):
        field = fieldname

        for field_char in field:
            if(field_char.isupper()):
                str1 = field[:field.find(field_char)]
                str2 = field[field.find(field_char) + 1:]
                field = str1 + "_" + field_char.lower() + str2

        return field

    def test_cases(self):
        #Loading data from JSON File
        f = open(os.path.join(os.getcwd(), "test", "executor.json"),'r')
        d_roads = json.load(f)
        f.close()

        dict_roads = d_roads['Execution Order']
        i = 0
        field_map = {}

        #Iterating for every 'road'
        for d in dict_roads:
            flag = 0
            i += 1
            sample_name = d['uniqueName']
            
            print("UNIQUE NAME : " + sample_name)

            response_field_list = d['storedResponseFields']

            #Clearing all response fields for current sample
            for response_field in response_field_list:
                field_map[sample_name+response_field] = None

            dependent_name = d['prerequisiteRoad']
            dependent_field_list = d['dependentFieldMapping']
            value_list = []

            #Fetching the dependent fields from the global map
            for dependent_field in dependent_field_list:
                if field_map[dependent_name + '' + dependent_field] is not None:
                    value_list.append(field_map[dependent_name + '' + dependent_field])
                else:
                    with self.subTest():
                        assert False,'Missing field from dependent sample code: ' + dependent_name + ' fails the sample code: ' + sample_name
                    flag = 1
                    break

            if flag == 1:
                continue

            class_set = d['sampleClassNames']
            #Obtaining path of module
            module_path = class_set['python']
            packages = module_path.split('.')
            
            if ("retrieve_transaction" in module_path or "delete_instrument_identifier" in module_path or "retrieve_available_reports" in module_path or "retrieve_all_payment_instruments" in module_path):
                time.sleep(20)

            #Importing the required sample code module
            try:                
                print("\n##### RUNNING SAMPLE FOR " + module_path + " #####\n")
                temp_path = '.'
                for segment in packages:
                    temp_path = os.path.join(temp_path, segment)

                temp_path = temp_path + '.py'

                module = SourceFileLoader(packages[-1], temp_path).load_module()

                if "get_report_definition" in module_path:
                    value_list.insert(0, "TransactionRequestClass")
                elif "Token_Management" in module_path:
                    value_list.insert(0, "93B32398-AD51-4CC2-A682-EA3E93614EB1")

                return_data = getattr(module, packages[-1])(*value_list)

                print("\n##### ENDING SAMPLE FOR " + module_path + " #####\n")

            except:
                with self.subTest():
                    assert False, 'Failed Sample Code: ' + sample_name
                continue

            #Converting PtsV2PaymentsPost201Response object to Dictionary object
            try:
                return_data_dict = return_data.__dict__
            except:
                continue

            #Storing the required fields for future dependencies in the global map
            try:
                for response_field in response_field_list:
                    field_map[sample_name + response_field] = self.recurse(return_data_dict, self.modify_name(response_field))
            except:
                continue

            #Checking for required fields
            for req in response_field_list:
                with self.subTest(req = req):
                     self.assertIsNotNone(self.recurse(return_data_dict,req),"\n~~~Test Case " + str(i) + "(" + packages[-1] + "): " + req + " is null")

if __name__ == '__main__':
    unittest.main()