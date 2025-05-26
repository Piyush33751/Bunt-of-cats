countries = {
    "Singapore": [{"city": "Singapore", "population": 5450000}],
    "Japan": [{"city": "Tokyo", "population": 13960000}, {"city": "Osaka", "population": 2690000}],
    "Indonesia": [{"city": "Jakarta", "population": 10560000}, {"city": "Surabaya", "population": 2800000}]
}


def Avg_population_cities():
    My_list=[]
    
    total =0
    for i in countries:
       for key in countries[i]:
           x=key["population"]
           My_list.append(x)
           total =total +1
           
    y=sum(My_list)    
    avg=y/total
    print(avg)
    return(avg)
          
Avg_population_cities()

def Max_min_pop_cities():
     Ty_list=[]
     for i in countries:
       for key in countries[i]:
           x=key["city"]
           Ty_list.append(x)
     z=max(Ty_list)
     y=min(Ty_list)
     print(z)
     print(y)     

Max_min_pop_cities()       

   