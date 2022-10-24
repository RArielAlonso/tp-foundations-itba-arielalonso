#docker run -it --rm --network nt-pizza -v $PWD/Reports/graphs:/graphs reports-test

#libraries
import pandas as pd
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt
from queries import *

# create string for connection
POSTGRES_USER='aalonso'
POSTGRES_PASS='ITBA'
POSTGRES_HOST="postgres-db"
POSTGRES_DB='database_pizza'
POSTGRES_PORT='5432'
POSTGRES_SCHEMA='schema_pizza'

str_conection=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

#create engine for conections
print(f'Connecting to {POSTGRES_DB}')
engine=create_engine(str_conection,
                    connect_args={'options': f'-csearch_path={POSTGRES_SCHEMA}'})
conn = engine.connect()

#create dataframes from queries
print('Creating dataframes')
df_year_month=pd.read_sql(query_1,conn)
df_pizza_revenue=pd.read_sql(query_2_amount,conn)
df_pizza_sales=pd.read_sql(query_2_sales,conn)
df_category_revenue=pd.read_sql(query_3_revenue,conn)
df_category_sales=pd.read_sql(query_3_sales,conn)
df_sales_day_of_week=pd.read_sql(query_4_day_of_week,conn)
df_sales_hour=pd.read_sql(query_4_hour,conn)

# close connection
print(f'Closing Connection to {POSTGRES_DB}')
conn.close()
print(f'Connection closed to {POSTGRES_DB}')

#print reports before generating the plots
print("\n-----------------------------------------------------------------------------------------------------------\n")
print("While the graphs are generated, we will show some brief data")
#highest month
print("\n-----------------------------------------------------------------------------------------------------------\n")
print("The month with the highest revenue was:",
    '\tYear:',
    df_year_month.loc[df_year_month['total_order_amount']==df_year_month['total_order_amount'].max(),:]['year'].values[0],
    "\tMonth:",
    df_year_month.loc[df_year_month['total_order_amount']==df_year_month['total_order_amount'].max(),:]['month'].values[0],
    "\tRevenue:",
    df_year_month.loc[df_year_month['total_order_amount']==df_year_month['total_order_amount'].max(),:]['total_order_amount'].values[0]
    )
#pizza with the highest revenue
print("\n-----------------------------------------------------------------------------------------------------------\n")
print("The pizza with the highest revenue is:",
    df_pizza_revenue.loc[df_pizza_revenue['total_order_amount']==df_pizza_revenue['total_order_amount'].max(),:]['name'].values[0],
    "\tRevenue:",
    df_pizza_revenue.loc[df_pizza_revenue['total_order_amount']==df_pizza_revenue['total_order_amount'].max(),:]['total_order_amount'].values[0]
)
#pizza with the most sales
print("\n-----------------------------------------------------------------------------------------------------------\n")
print("The pizza with the most sales is:",
    df_pizza_sales.loc[df_pizza_sales['total_orders']==df_pizza_sales['total_orders'].max(),:]['name'].values[0],
    "\tOrders:",
    df_pizza_sales.loc[df_pizza_sales['total_orders']==df_pizza_sales['total_orders'].max(),:]['total_orders'].values[0]
)
#category with the highest revenue
print("\n-----------------------------------------------------------------------------------------------------------\n")
print("The category with the highest revenue is:",
    df_category_revenue.loc[df_category_revenue['total_order_amount']==df_category_revenue['total_order_amount'].max(),:]['category'].values[0],
    "\tRevenue:",
    df_category_revenue.loc[df_category_revenue['total_order_amount']==df_category_revenue['total_order_amount'].max(),:]['total_order_amount'].values[0]
)
#category with the most sales
print("\n-----------------------------------------------------------------------------------------------------------\n")
print("The category with the most sales is:",
    df_category_sales.loc[df_category_sales['total_orders']==df_category_sales['total_orders'].max(),:]['category'].values[0],
    "\t Orders:",
    df_category_sales.loc[df_category_sales['total_orders']==df_category_sales['total_orders'].max(),:]['total_orders'].values[0]
)
#day with most sales
print("\n-----------------------------------------------------------------------------------------------------------\n")
print("The day of week with the most sales is:",
    df_sales_day_of_week.loc[df_sales_day_of_week['total_orders']==df_sales_day_of_week['total_orders'].max(),:]['day_name'].values[0],
    "\t Orders:",
    df_sales_day_of_week.loc[df_sales_day_of_week['total_orders']==df_sales_day_of_week['total_orders'].max(),:]['total_orders'].values[0]
)
print("\n-----------------------------------------------------------------------------------------------------------\n")
print("The hour with the most sales is:",
    df_sales_hour.loc[df_sales_hour['total_orders']==df_sales_hour['total_orders'].max(),:]['hour'].values[0],
    "\t Orders:",
    df_sales_hour.loc[df_sales_hour['total_orders']==df_sales_hour['total_orders'].max(),:]['total_orders'].values[0]
)
print("\n-----------------------------------------------------------------------------------------------------------\n")

#making the graphs

#revenue month year
plt.figure(figsize=(10,5))
sns.barplot(data=df_year_month,x=df_year_month['month'],
            y='total_order_amount',
            #color='blue',
            hue='year',
            )
plt.title('Total revenue per month and year',fontsize=20)
plt.xlabel('Month')
plt.ylabel('Amount')
plt.legend(loc=8, bbox_to_anchor=(1.1, 0.5),title="Año")
plt.tight_layout()
plt.savefig('/graphs/revenue_month_year.jpg',dpi=300)

#revenue pizza
plt.figure(figsize=(22,10))
fig=sns.barplot(data=df_pizza_revenue.head(10),
            x=df_pizza_revenue.head(10)['name'],
            y='total_order_amount',
            #color='blue',
            #hue='year',
            )
plt.title('TOP 10 Pizzas Revenue',fontsize=20)
plt.xlabel('Pizza name')
plt.ylabel('Amount')
plt.tight_layout()
plt.savefig('/graphs/revenue_pizza.jpg',dpi=300)

# sales pizza
plt.figure(figsize=(22,10))
fig=sns.barplot(data=df_pizza_sales.head(10),
            x=df_pizza_sales.head(10)['name'],
            y='total_orders',
            #color='blue',
            #hue='year',
            )
plt.title('TOP 10 Pizzas Sales',fontsize=20)
plt.xlabel('Pizza name')
plt.ylabel('Total Orders')
plt.tight_layout()
plt.savefig('/graphs/sales_pizza.jpg',dpi=300)

#revenue category
plt.figure(figsize=(10,5))
fig=sns.barplot(data=df_category_revenue.head(10),
            x=df_category_revenue.head(10)['category'],
            y='total_order_amount',
            #color='blue',
            #hue='year',
            )
plt.title('Categories Revenue',fontsize=20)
plt.xlabel('Category name')
plt.ylabel('Amount')
plt.tight_layout()
plt.savefig('/graphs/revenue_category.jpg',dpi=300)

#sales category
plt.figure(figsize=(10,5))
fig=sns.barplot(data=df_category_sales.head(10),
            x=df_category_sales.head(10)['category'],
            y='total_orders',
            #color='blue',
            #hue='year',
            )
plt.title('Categories Sales',fontsize=20)
plt.xlabel('Category name')
plt.ylabel('Total Orders')
plt.tight_layout()
plt.savefig('/graphs/sales_category.jpg',dpi=300)

#orders day of week

plt.figure(figsize=(10,5))
fig=sns.barplot(data=df_sales_day_of_week,
            x=df_sales_day_of_week['day_name'],
            y='total_orders',
            #color='blue',
            #hue='year',
            )
plt.title('Orders per day of week',fontsize=20)
plt.xlabel('Day of week')
plt.ylabel('Total Orders')
plt.tight_layout()
plt.savefig('/graphs/sales_day_of_week.jpg',dpi=300)

#orders hour

plt.figure(figsize=(22,10))
fig=sns.barplot(data=df_sales_hour.head(10),
            x=df_sales_hour.head(10)['hour'].astype('str'),
            y='total_orders',
            #color='blue',
            #hue='year',
            )
plt.title('TOP 10 Sales per hour',fontsize=20)
plt.xlabel('Hour')
plt.ylabel('Total Orders')
plt.tight_layout()
plt.savefig('/graphs/sales_hour.jpg',dpi=300)


print("The reports are generated,please check /Reports/graphs")