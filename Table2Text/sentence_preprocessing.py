# -*- coding: utf-8 -*-
"""Sentence_preprocessing.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1BbzvlBWifsC5SEprWyaQxtD3ihPgqOQV
"""

from google.colab import drive
drive.mount('/content/gdrive')

import pandas as pd

data = pd.read_csv("/content/gdrive/MyDrive/2024_컨퍼런스/bank-direct-marketing-campaigns.csv")
data.head()

data.shape

"""## Job"""

data['job'] = data['job'].apply(lambda x : x.replace(".",""))

data['job'].value_counts()

#admin = 관리자
#blue-collar = 숙련, 미숙련에 상관없이 생산업과 서비스업에 종사하는 노동자
#technician = 기술자
#services = 서비스업 종사자
#management = 관리자(admin과는 다른)
#retired = 은퇴 후 무직
#entrepreneur = 기업가
#self-employed = 자영업자
#housemaid = 가정주부
#unemployed = 무직백수
#student = 학생
#unknown = 알수 없음

"""## Marital"""

data['marital'].value_counts()

"""## Education"""

data['education'] = data['education'].apply(lambda x : x.replace(".","_"))

data['education'].value_counts()

"""## Default"""

data['default'].value_counts()

"""## Housing"""

data['housing'].value_counts()

"""## Loan"""

data['loan'].value_counts()

"""## Contact"""

data['contact'].value_counts()

"""## Month"""

data['month'].value_counts()

"""## Day_of_week"""

data['day_of_week'].value_counts()

"""## Campaign"""

data['campaign'].value_counts()

#이전 캠페인에서 클라이언트가 마지막으로 연락을 받은 후 경과한 일 수 (숫자, 999는 클라이언트가 이전에 연락을 받지 않았음을 의미)
data = data.rename(columns = {'pdays': '마지막연락_경과일수'})
data['마지막연락_경과일수'] = data['마지막연락_경과일수'].fillna(999)

#이 캠페인 이전에 수행된 연락처 수 및 이 클라이언트에 대한 연락처 수(숫자)
data = data.rename(columns = {'previous': '수행된연락처및_연락처수'})

#이전 마케팅 캠페인의 결과(범주: '실패', '존재하지 않음', '성공')
data = data.rename(columns={'poutcome': '이전마케팅캠페인결과'})

## <<여기부터 사회적 및 경제적 맥락 속성>>
#고용 변화율 - 분기별 지표 (숫자)
data = data.rename(columns={'emp.var.rate': '고용변화율_분기별지표'})

#소비자물가지수 - 월별 지표(숫자)
data = data.rename(columns={'cons.price.idx': '소비자물가지수_월별지표'})

#소비자 신뢰 지수 - 월별 지표
data = data.rename(columns={'cons.conf.idx':'소비자신뢰지수_월별지표'})

#유리보 3개월 환율 - 일간 지표(숫자)
data = data.rename(columns={'euribor3m': 'EURIBOR3개월환율_일간지표'})

#직원 수 - 분기별 지표(숫자)
data = data.rename(columns={'nr.employed':'직원수_분기별지표'})

data = data.rename(columns = {'age':'나이', 'job':'직업', 'marital':'결혼여부', 'education':'교육수준', 'default':'신용여부','housing':'주택대출여부', 'loan':'개인대출여부',
                              'contact':'이전상담수단', 'month':'최근상담월', 'day_of_week':'최근상담요일', 'campaign':'이전상담횟수'})
data

# Function to generate multiple descriptions for a customer with shortened and properly formatted strings
def generate_descriptions(row):
    descriptions = [
        f"This customer is {row['나이']} years old, works as a {row['직업']}, and is {row['결혼여부']}. "
        f"They have completed {row['교육수준']} education, have no credit issues, and do not have a housing or personal loan. "
        f"The previous contact was made by {row['이전상담수단']}, with the most recent contact occurring on a {row['최근상담요일']} in {row['최근상담월']}. "
        f"The customer has never been contacted before and did not participate in previous marketing campaigns. "
        f"At that time, the quarterly employment change rate was {row['고용변화율_분기별지표']}%, the consumer price index was {row['소비자물가지수_월별지표']}, "
        f"the consumer confidence index was {row['소비자신뢰지수_월별지표']}, the EURIBOR 3-month rate was {row['EURIBOR3개월환율_일간지표']}, and the employee count was {row['직원수_분기별지표']}."
    ]
    return descriptions

# Apply the function to each row to create a new 'Customer_Description' column
data['Customer_Description'] = data.apply(generate_descriptions, axis=1)

data

df_exploded = data.explode('Customer_Description').reset_index(drop=True)
df_exploded

df_exploded = df_exploded[['Customer_Description','y']]
df_exploded

df_exploded.to_excel("original_data.xlsx", index = False)





