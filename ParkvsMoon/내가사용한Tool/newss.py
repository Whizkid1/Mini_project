import pandas as pd 

#원본 데이터 호출 
df = pd.read_csv('Election2.csv') 



#키워드 총 셋 만들기 
key_set = set()
for i in range(31630):
    temp_temp_key = df['Keyword'][i].split(',')
    for a in temp_temp_key:
        key_set.add(a)

#키워드 리스트 변형 
key_list = list(key_set)

#월별 데이터 호출 
#6월 키워드 데이터 작업 
df_month = pd.read_csv('7.csv')
df_month 

#키 리스트 카운팅 작업 
key_count_list = [ ]
mun_park = 0 
mun = 0
park = 0

for x in range(88593):
    for y in range(1858):  #월별 데이터량 만큼 필요 
        if '문재인, 박근혜' == df_month['Person'][y]:
            if key_list[x] in df_month['Keyword'][y]:
                mun_park +=1
        elif '문재인' == df_month['Person'][y]:
            if key_list[x] in df_month['Keyword'][y]:
                mun +=1 
        elif '박근혜' == df_month['Person'][y]:
            if key_list[x] in df_month['Keyword'][y]:
                park +=1
        if y == 1:
            print('ing')
    if mun != 0:
        key_count_list.append(['7월','문재인',key_list[x],mun])
    if park != 0:
        key_count_list.append(['7월','박근혜',key_list[x],park])
    if mun_park != 0:
        key_count_list.append(['7월','문재인,박근혜',key_list[x],mun_park])

    mun_park = 0 
    mun = 0
    park = 0 
    
print('finish')

print(key_count_list)

df_7result = pd.DataFrame(key_count_list)

df_7result.to_csv('7result.csv')