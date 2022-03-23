import requests

Project_Id = 'uaiGmJ-OP06FJSuRSjRjLQ'
Job_ID = 'JAH5Q8lCE02GsJ5wKiPA0g'
url = 'https://api.testproject.io/v2/projects/'+Project_Id+'/jobs/'+Job_ID+'/run'

report = 'https://api.testproject.io/v2/projects/'+Project_Id+'/jobs/'+Job_ID+'/reports/latest'
report_All = 'https://api.testproject.io/v2/projects/'+Project_Id+'/jobs/'+Job_ID+'/reports'
API_Key = 'CkOEXQiyYDtAxYZmQdw0j5AdncmtFlDcRWifMTgdbIo1'
headers = {'Authorization':API_Key}
response = requests.post(url,headers=headers)
Execution_ID = response.json().get('id')
print (Execution_ID)

while True:
    resp = requests.get(report, headers=headers)
    #print(resp.json())
    Report_ID = resp.json().get('id')
    print(Report_ID )
    T = str(Execution_ID)
    D = str(Report_ID)
    print(T)
    print(D)
    
    if( T == D ) :
        print('matched')
        Status = resp.json().get('resultType')
        print(Status)

        Report_URL = resp.json().get('reportUrl')
        print(Report_URL)
        print(resp.json())

        break
    else:
        resp = requests.get(report,headers= headers)

