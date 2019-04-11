import requests
from lxml import etree as et
import multiprocessing
import google.cloud.bigquery as bq
import os
import traceback


def position(arg):
    l = arg
    if l == 0:
        pos = 1
        return (pos)
    else:
        return (l + 1)


def foc_cum_call(url):
    try:
        return_list = [1]
        response = requests.get(url)
        tree = et.fromstring(response.content)
        cum_srh = tree.xpath('//srh/text()')
        cum_power_id = tree.xpath('//cumulativePower/@id')
        if len(cum_power_id) > 0:
            cum_href = tree.xpath('//href/text()')
            cum_srh = tree.xpath('//srh/text()')
            cum_start_date = tree.xpath('//interval/startDate/text()')
            cum_end_date = tree.xpath('//interval/endDate/text()')
            cum_total_power = tree.xpath('//totalPower/text()')
            meter_list = tree.xpath('//meter/@id')
            meter_list_len = len(meter_list)
            rang = range(meter_list_len)
            if meter_list_len > 0:
                for l, i in zip(rang, meter_list):
                    interim_list = []
                    pos = position(l)
                    meter_id = tree.xpath("//meter[position()='%s'][@id='%s']/@id" % (pos, i))
                    meter_active = tree.xpath("//meter[position()='%s'][@id='%s']/@active" % (pos, i))
                    meter_serialnum = tree.xpath("//meter[position()='%s'][@id='%s']/serialNumber/text()" % (pos, i))
                    meter_provider = tree.xpath("//meter[position()='%s'][@id='%s']/provider/text()" % (pos, i))
                    meter_power = tree.xpath("//meter[position()='%s'][@id='%s']/meterPower/text()" % (pos, i))
                    meter_start_dt = tree.xpath(
                        "//meter[position()='%s'][@id='%s']/interval/startDate/text()" % (pos, i))
                    meter_end_dt = tree.xpath("//meter[position()='%s'][@id='%s']/interval/endDate/text()" % (pos, i))
                    if meter_power == ['0.0']:
                        meter_start_read = ['']
                        meter_end_read = ['']
                        meter_first_read_dt = ['']
                        meter_last_read_dt = ['']
                    else:
                        meter_start_read = tree.xpath(
                            "//meter[position()='%s'][@id='%s']/readings/reading[position()='1']/text()" % (pos, i))
                        meter_end_read = tree.xpath(
                            "//meter[position()='%s'][@id='%s']/readings/reading[position()='2']/text()" % (pos, i))
                        meter_first_read_dt = tree.xpath(
                            "//meter[position()='%s'][@id='%s']/readings/reading[position()='1']/@time" % (pos, i))
                        meter_last_read_dt = tree.xpath(
                            "//meter[position()='%s'][@id='%s']/readings/reading[position()='2']/@time" % (pos, i))
                    interim_list = [cum_srh, cum_power_id, cum_start_date[0], cum_end_date[0], cum_total_power,
                                    meter_id, meter_active, meter_serialnum, meter_provider, meter_start_dt,
                                    meter_end_dt, meter_start_read, meter_end_read, meter_first_read_dt,
                                    meter_last_read_dt]
                    l = []
                    for item in interim_list:
                        l.append(''.join(item))
                    return_list.append(l)
    except Exception as errmsg:
        print(errmsg)
        return_list = [1]
    return return_list


if __name__ == '__main__':
    p = 20
    pool = multiprocessing.Pool(p)
    try:
        failed_list = []
        success_list = []
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "noc_service_account_sr-dev-datahub.json"
        project_id = 'sr-dev-datahub'
        bigquery_client = bq.Client(project=project_id)
        select_sql = """SELECT Agreement_Number__c,PTO__c FROM `sr-dev-datahub.Datahub.ORN_SERVICE_CONTRACT_V` order by 1 LIMIT 1"""
        select_job = bigquery_client.query(select_sql)
        select_results = select_job.result()
        print("...............................", select_results)
        for row in select_results:
            srh = row[0]
            endDate = row[1].strftime('%Y-%m-%d')
            # url = 'https://foc.sunrun.com/foc/rest/v1/power?srh={}&endDate={}'.format(srh, endDate)
            url = 'https://foc.sunrun.com/foc/rest/v1/power?srh={}&endDate={}'.format('03', '2018-11-01')
            if len(srh) > 0 and len(endDate) > 0:
                return_list = foc_cum_call(url)
                print(return_list)
                if return_list[0] == 1:
                    failed_list.append(url)
                else:
                    success_list.append(url)
            else:
                failed_list.append(url)

        print("failed list is : {}".format(failed_list))
        print("success list is: {}".format(success_list))
    except Exception as e:
        print(traceback.format_exc())
