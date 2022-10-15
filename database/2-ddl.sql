
drop table if exists schema_pizza.orders;

create table schema_pizza.orders (
    order_id INT NOT NULL ,
    date DATE,
    time TIMESTAMP,
    year INT,
    month INT,
    day_of_week INT,
    hour INT,
    PRIMARY KEY (order_id)
);

drop table if exists schema_pizza.pizza_types;

create table schema_pizza.pizza_types (
    pizza_type_id VARCHAR(20) NOT NULL,
    name VARCHAR(20),
    category VARCHAR(20),
    ingredients VARCHAR(30),
    PRIMARY KEY (pizza_type_id)
);

drop table if exists schema_pizza.pizzas;

create table schema_pizza.pizzas (
    pizza_id VARCHAR(20) NOT NULL,
    pizza_type_id VARCHAR(20),
    size VARCHAR(20),
    price FLOAT,
    PRIMARY KEY (pizza_id),
    CONSTRAINT fk_pizzas
    FOREIGN KEY (pizza_type_id) REFERENCES schema_pizza.pizza_types(pizza_type_id)
);

drop table if exists schema_pizza.order_details;

create table schema_pizza.order_details(
    order_details_id INT NOT NULL,
    order_id INT,
    pizza_id varchar(20),
    quantiy INT,
    PRIMARY KEY (order_details_id),
    CONSTRAINT fk_order
    FOREIGN KEY (pizza_id) REFERENCES schema_pizza.pizzas(pizza_id),
    FOREIGN KEY (order_id) REFERENCES schema_pizza.orders(order_id)
);




