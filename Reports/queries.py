query_1="""select o2.year,o2.month, round(sum(o.quantity*p.price)) as total_order_amount 
from schema_pizza.order_details o
inner join schema_pizza.orders o2 on o.order_id=o2.order_id
left join schema_pizza.pizzas p on p.pizza_id=o.pizza_id
group by o2.year,o2.month
order by o2.year,o2.month;
"""

query_2_amount="""select  pt.name,sum(o.quantity) as total_oders,round(sum(o.quantity*p.price),2) as total_order_amount
from schema_pizza.order_details o
inner join schema_pizza.orders o2 on o.order_id=o2.order_id
left join schema_pizza.pizzas p on p.pizza_id=o.pizza_id
left join schema_pizza.pizza_types pt on pt.pizza_type_id=p.pizza_type_id 
group by pt.name
order by total_order_amount DESC;"""

query_2_sales="""select  pt.name,sum(o.quantity) as total_orders,round(sum(o.quantity*p.price),2) as total_order_amount
from schema_pizza.order_details o
inner join schema_pizza.orders o2 on o.order_id=o2.order_id
left join schema_pizza.pizzas p on p.pizza_id=o.pizza_id
left join schema_pizza.pizza_types pt on pt.pizza_type_id=p.pizza_type_id 
group by pt.name
order by total_orders DESC;"""

query_3_revenue="""select pt.category ,sum(o.quantity) as total_orders,round(sum(o.quantity*p.price),2) as total_order_amount 
from schema_pizza.order_details o
inner join schema_pizza.orders o2 on o.order_id=o2.order_id
left join schema_pizza.pizzas p on p.pizza_id=o.pizza_id
left join schema_pizza.pizza_types pt on pt.pizza_type_id=p.pizza_type_id 
group by pt.category
order by total_order_amount DESC"""

query_3_sales="""select pt.category ,sum(o.quantity) as total_orders,round(sum(o.quantity*p.price),2) as total_order_amount 
from schema_pizza.order_details o
inner join schema_pizza.orders o2 on o.order_id=o2.order_id
left join schema_pizza.pizzas p on p.pizza_id=o.pizza_id
left join schema_pizza.pizza_types pt on pt.pizza_type_id=p.pizza_type_id 
group by pt.category
order by total_orders DESC"""

query_4_day_of_week="""select  case when day_of_week=1 then 'Sunday'
		when day_of_week=2 then 'Monday' 
		when day_of_week=3 then 'Tuesday' 
		when day_of_week=4 then 'Wednesday'
		when day_of_week=5 then 'Thursday'
		when day_of_week=6 then 'Friday'
		when day_of_week=7 then 'Saturday'
		end as day_name,
		day_of_week,
		sum(o.quantity) as total_orders,
		round(sum(o.quantity*p.price),2) as total_order_amount,
		round(avg(o.quantity*p.price),2) as mean_order_amount
from schema_pizza.order_details o
inner join schema_pizza.orders o2 on o.order_id=o2.order_id
left join schema_pizza.pizzas p on p.pizza_id=o.pizza_id
left join schema_pizza.pizza_types t on p.pizza_type_id=t.pizza_type_id
group by day_of_week
order by total_orders DESC ;"""

query_4_hour="""select  hour,sum(o.quantity) as total_orders,
round(sum(o.quantity*p.price),2) as total_order_amount,
round(avg(o.quantity*p.price),2) as mean_order_amount
from schema_pizza.order_details o
inner join schema_pizza.orders o2 on o.order_id=o2.order_id
left join schema_pizza.pizzas p on p.pizza_id=o.pizza_id
left join schema_pizza.pizza_types t on p.pizza_type_id=t.pizza_type_id
group by hour
order by total_orders DESC ;"""