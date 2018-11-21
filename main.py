import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

url = 'https://api.smartcountry-hacks.de/itdz/stats/service/'
first_freeday_url = 'https://api.smartcountry-hacks.de/itdz/stats/firstfreeday/'
location_details_url = 'https://api.smartcountry-hacks.de/itdz/subjects'

location_customer_detail_url = 'https://api.smartcountry-hacks.de/itdz/stats/customer/'
location_service_detail_url = 'https://api.smartcountry-hacks.de/itdz/stats/service/'

response = requests.get(location_details_url)

df = pd.read_json(response.content)

standort_ids = df['StandortID'].unique()

dataResults = pd
dataResultsDF = pd.DataFrame()
data = []


def main():
    # get_user_usage_data()
    # get_service_data()
    print("in main")
    plotting()
    return

def get_user_usage_data():
    #####
    # saving customer data to csv
    #####

    # for i in range(1,3):
    #     for year in range(2013, 2014):
    #         for month in range(01, 13):
    #             if(month < 10):
    #                 month = "0"+str(month)
    #             print(location_customer_detail_url + str(standort_ids[i])+"/"+str(year)+"-"+str(month))
    #             response2 = requests.get(location_customer_detail_url + str(standort_ids[i])+"/"+str(year)+"-"+str(month))
    #             try:
    #
    #                 dataf = pd.read_json(response2.content)
    #                 dataResultsDF = dataResults.concat([dataf,dataResultsDF],ignore_index=True)
    #
    #             except ValueError, e:
    #                 print("value not found")
    #
    # print(dataResultsDF)
    #
    # dataResultsDF.to_csv('collection_data.csv', sep=',')

    # data = pd.read_csv('service_date.csv')
    #
    #
    # d = data[pd.to_datetime(data['date']).dt.month == 6]
    # data_by_month = d[['clientscount','subjectid','date']]
    #
    #
    #
    #
    # print(data_by_month)
    #
    # # objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    # ids = np.arange(len(standort_ids))
    # print(ids)
    # clients = d['clientscount'].values#[10, 8, 6, 4, 2, 1]
    # print(np.array(clients))
    #
    # plt.bar(np.array(ids), np.array(clients), align='center', alpha=0.5)
    #
    # plt.xticks(y_pos, objects)
    # plt.ylabel('Usage')
    # plt.title('Programming language usage')
    #
    # plt.show()
    return



def get_service_data():
    ####
    #Service
    #
    # response = requests.get(location_service_detail_url)
    #
    dataServiceResults = pd
    dataServiceResultsDF = pd.DataFrame()


    # for i in range(1, 3):
    for i in range(len(standort_ids)):
        for year in range(2013, 2018):
            for month in range(1, 13):
                if(month < 10):
                    month = "0"+str(month)
                print(location_service_detail_url + str(standort_ids[i])+"/"+str(year)+"-"+str(month))
                response2 = requests.get(location_service_detail_url + str(standort_ids[i])+"/"+str(year)+"-"+str(month))
                try:

                    dataf = pd.read_json(response2.content)
                    dataServiceResultsDF = dataServiceResults.concat([dataf,dataServiceResultsDF],ignore_index=True)

                except ValueError:
                    print("value not found")

    # for i in range(1,3):
    #     for year in range(2013, 2014):
    #         for month in range(01, 13):
    #             if(month < 10):
    #                 month = "0"+str(month)
    #             print(location_customer_detail_url + str(standort_ids[i])+"/"+str(year)+"-"+str(month))
    #             response2 = requests.get(location_customer_detail_url + str(standort_ids[i])+"/"+str(year)+"-"+str(month))
    #             try:
    #
    #                 dataf = pd.read_json(response2.content)
    #                 dataResultsDF = dataResults.concat([dataf,dataResultsDF],ignore_index=True)
    #
    #             except ValueError, e:
    #                 print("value not found")
    #

    # print(dataResultsDF)
    # #
    dataServiceResultsDF.to_csv('service_data.csv', sep=',')
    return

def plotting():
    data = pd.read_csv('collection_data.csv')


    d = data[pd.to_datetime(data['date']).dt.month == 6]
    data_by_month = d[['clientscount','subjectid','date']]
    #
    #
    #
    #
    # print(data_by_month)
    #
    # objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
    ids = np.arange(len(standort_ids))
    ids = np.asarray(ids)
    print(ids)
    print(type(ids))

    clients = d['clientscount'].values#[10, 8, 6, 4, 2, 1]
    print(np.array(clients))

    plt.bar(np.array(ids), np.array(clients), align='center', alpha=0.5)

    plt.xticks(y_pos, objects)
    plt.ylabel('Usage')
    plt.title('Programming language usage')

    plt.show()

    # N = 50
    # x = np.random.rand(N)
    # y = np.random.rand(N)
    # colors = np.random.rand(N)
    # area = (30 * np.random.rand(N)) ** 2  # 0 to 15 point radii
    #
    # plt.scatter(x, y, s=area, c=colors, alpha=0.5)
    # plt.show()

    return

main()
