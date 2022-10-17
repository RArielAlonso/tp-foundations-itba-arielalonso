# docker run --rm -v $PWD/csv_files:/csv_files test-tp
# docker run -it --rm --network nt-pizza -v $PWD/ETL/csv_files:/csv_files test-tp

#libraries
import pandas as pd
import os
from sqlalchemy import create_engine

# set variables to connect
POSTGRES_USER='aalonso'
POSTGRES_PASS='ITBA'
POSTGRES_HOST="postgres-db"
POSTGRES_DB='database_pizza'
POSTGRES_PORT='5432'
POSTGRES_SCHEMA='schema_pizza'

#make string conection to postgres
str_conection=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#make conection
engine=create_engine(str_conection,
                    connect_args={'options': f'-csearch_path={POSTGRES_SCHEMA}'}
                    )
conn = engine.connect()

# csv_dict of 
csv_dict={"pizza_types":"pizza_types.xlsx",
"pizzas":"pizzas.xlsx",
"orders":"orders.xlsx",
"order_details":"order_details.xlsx",
}

# looping through the csv_dict
for k,v in csv_dict.items():
    print(f"Excel file to DataFrame: {k}")
    print('/csv_files/'+f'{v}')
    data=pd.read_excel("/csv_files/"+f"{v}")
    print(f"Dataframe to Postgres: {k}")
    data.to_sql(
    		k,
        	conn,
        	index=False,
        	if_exists='append'
        )
conn.close()
print('Closing connection to Database')
print('LOADED DATA TO DB ENDED')