# docker run --rm -v $PWD/ETL/csv_files:/csv_files test-tp

#libraries
import pandas as pd
import os

#path of files
path_etl=os.getcwd()
print(path_etl)

# csv_dict
csv_dict={"order_details":"order_details.xlsx",
"orders":"orders.xlsx",
"pizza_types":"pizzas_types.xlsx",
"pizzas":"pizzas.xlsx"
}

# looping through the csv_dict
for k,v in csv_dict.items():
    print(k)
    print(v)

print(pd.read_excel('csv_files/order_details.xlsx'))



print('NOOOOOOOOOOOOOOOoooo')
