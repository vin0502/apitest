#__author__ = 'pan'
# -*- coding:utf-8 -*-

import nose
from parameterized import parameterized
import requests
from utils.log import Log
from utils.readyaml import ReadYaml


class createWayBill(unittest.TestCase):
    '''新增运单'''
    def setUp(self):
        self.logger = Log()
        self.logger.info('############################### START ###############################')
        config = ReadYaml( './config/httpconfig.yaml').getValue()
        self.url = "http://{0}:{1}/tms/api/tms/wayBill/createWayBill".format(config['host'],config['port'])
        self.token = 'eyJlbmNyeXB0ZWREYXRhIjoicFBveUZESkVKR0FWOWpOanVqNGlDRG1uSHNrOWhyVDJRZ2NiTU1LWnBZSXRsZzdFQkVFMFJoR2FzNHMzMXd3SndXb1NVSjJ2Nm1uYjNNdGJ3S1BZcE14UDN5VnNwekh5K05vYzdzd0xTNnhnWEVtWXJUaHlEcGhNY3BMZWFYNjVGa0hsVkFFak80WFk3M1hhbmNkRnF2aVptSWVyOTlKazhucXNjMkZKTkhTTlo2b0RDdTh2VFRyaGxOQzdpUEFlZ1pOK25ZTTZtQkRHUkVJM3dEUEtwWVE5a1RmUXBiczJlbkwvTHZqQWR1Zz0iLCJ3cmFwcGVkS2V5Ijoib1hVN05xNWxsbnVLWUduZEtoc1dtVHpOeSs2RmdhaTFnY0pLeE82NnJ3dTJPMXVhL3dpVzVqTEx2d1NlUEk3N2s2RVFsZ1l0NFVlN2Q2QTVyK0NuTHc9PSJ9'
        self.headers = {
            'Content - Type': 'multipart/form-data',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36',
            'token': self.token}

    def tearDown(self):
        self.logger.info('################################ END ################################')

    @parameterized.expand([
        ("34252919880328581x",'13077327043','京A19901'),
        ("34252919880328581x", '13077327043', '京A19901'),
        ("34252919880328581x", '13077327043', '京A19901'),
    ])
    def test_createWayBill_success(self,idNo,mobile,carNo):
        '''成功新增运单'''
        payload = {"idNo":'34252919880328581x',
                 "mobile":'13077327043',
                 "carNo":'京A19901',
                 "applyDate":'2017-08-05',
                 "partnerNo":'ShiDeTang',
                 "sendCity":'北京',
                 "sendProvince":'北京',
                 "arriveProvince":'天津',
                 "arriveCity":'天津',
                 "realName":'王锡聪',
                 "carType":'2',
                 "income":'0.1',
                 "supplierName":'',
                 "supplierId":'',
                 "totalAmt":'0.1',
                 "preAmt":'0.01',
                 "oilAmt":'0.02',
                 "destAmt":'0.03',
                 "lastAmt":'0.04',
                 "projects":'快递20170804002',
                 "hasReceipt":'1',
                 "content":'',
                 "source":'TMS'}
        request = requests.post(self.url,payload,headers= self.headers)
        response = request.json()
        print(response)
        self.assertEqual(response['code'],1)
        # self.assertEqual(response['msg'], '无效token ')
        #数据库结果校验


if __name__ == '__main__':
    unittest.main()