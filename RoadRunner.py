import json
import unittest
class Test(unittest.TestCase):
    def recurse(self, return_data, fieldpath):
        field_list = fieldpath.split('.')
        #Creating a copy of the dictionary passed as param
        return_data_copy = return_data
        #Iterating through each level of dictionary to get required value
        for fields in field_list:
            fields = "_"+fields
            #Checking whether we can access more levels of the dictionary or not
            if type(return_data_copy[fields]) == str or type(return_data_copy[fields]) == int:
                return return_data_copy[fields]
            else:
                return_data_copy = return_data_copy[fields].__dict__
    #Converting field name to one that follows Python naming convention
    def modify_name(self, fieldname):
        field = fieldname
        for field_char in field:
            if(field_char.isupper()):
                str1 = field[:field.find(field_char)]
                str2 = field[field.find(field_char)+1:]
                field = str1+"_"+field_char.lower()+str2
        return field
    def test_cases(self):
        #Loading data from JSON File
        f=open('executor.json','r')
        d_roads = json.load(f)
        f.close()
        dict_roads = d_roads['Execution Order']
        i=0
        field_map = {}
        #Iterating for every 'road'
        for d in dict_roads:
            flag=0
            i+=1
            sample_name = d['uniqueName']
            response_field_list = d['storedResponseFields']
            #Clearing all response fields for current sample
            for response_field in response_field_list:
                field_map[sample_name+response_field] = None
            dependent_name = d['prerequisiteRoad']
            dependent_field_list = d['dependentFieldMapping']
            value_list = []
            #Fetching the dependent fields from the global map
            for dependent_field in dependent_field_list:
                if field_map[dependent_name+''+dependent_field] is not None:
                    value_list.append(field_map[dependent_name+''+dependent_field])
                else:
                    with self.subTest():
                        assert False,'Missing field from dependent sample code: '+dependent_name+ ' fails the sample code: '+sample_name
                    flag=1
                    break
            if flag == 1:
                continue
            class_set = d['sampleClassNames']
            #Obtaining path of module
            module_path = class_set['python']
            packages = module_path.split('.')
            #Importing the required sample code module
            try:
                return_data = getattr(__import__(module_path,globals(), locals(), [packages[-1]],0),packages[-1])(*value_list)
            except:
                with self.subTest():
                    assert False, 'Failed Sample Code: '+sample_name
                continue
            #Converting PtsV2PaymentsPost201Response object to Dictionary object
            try:
                return_data_dict = return_data.__dict__
            except:
                continue
            #Storing the required fields for future dependencies in the global map
            for response_field in response_field_list:
                field_map[sample_name+response_field] = self.recurse(return_data_dict, self.modify_name(response_field))
            assertions = d['Assertions']
            if('httpStatus' in assertions):
                responseCode = assertions['httpStatus']
                expectedValues = assertions['expectedValues']
                requiredFields = assertions['requiredFields']
                for expectedValue in expectedValues:
                    expectedValue['field'] = self.modify_name(expectedValue['field'])
                    value = expectedValue['value']
                for index,requiredField in enumerate(requiredFields):
                    requiredFields[index]= self.modify_name(requiredField)
                #Checking for all expected values
                for expectedVal in expectedValues:
                    with self.subTest(expectedVal=expectedVal):
                        self.assertEqual(self.recurse(return_data_dict,expectedVal['field']),expectedVal['value'],"\n~~~Test Case "+str(i)+"("+packages[-1]+"): "+expectedVal['field'])
                #Checking for required fields
                for req in requiredFields:
                    with self.subTest(req=req):
                        self.assertIsNotNone(self.recurse(return_data_dict,req),"\n~~~Test Case "+str(i)+"("+packages[-1]+"): "+req+" is null")
if __name__ == '__main__':
    unittest.main()
        
    



   
    
