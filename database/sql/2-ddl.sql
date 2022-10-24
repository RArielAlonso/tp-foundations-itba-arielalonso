
drop table if exists schema_pizza.orders CASCADE;

create table schema_pizza.orders (
    order_id INT NOT NULL ,
    date DATE,
    time TEXT,
    year INT,
    month INT,
    day_of_week INT,
    hour INT,
    PRIMARY KEY (order_id)
);

drop table if exists schema_pizza.pizza_types CASCADE;

create table schema_pizza.pizza_types (
    pizza_type_id VARCHAR(20) NOT NULL,
    name VARCHAR(50),
    category VARCHAR(20),
    ingredients VARCHAR(100),
    PRIMARY KEY (pizza_type_id)
);

drop table if exists schema_pizza.pizzas CASCADE;

create table schema_pizza.pizzas (
    pizza_id VARCHAR(20) NOT NULL,
    pizza_type_id VARCHAR(20),
    size VARCHAR(20),
    price NUMERIC,
    PRIMARY KEY (pizza_id),
    CONSTRAINT fk_pizzas
    FOREIGN KEY (pizza_type_id) REFERENCES schema_pizza.pizza_types(pizza_type_id)
    ON DELETE CASCADE
);

drop table if exists schema_pizza.order_details CASCADE;

create table schema_pizza.order_details(
    order_details_id INT NOT NULL,
    order_id INT,
    pizza_id varchar(20),
    quantity INT,
    PRIMARY KEY (order_details_id),
    CONSTRAINT fk_order
    FOREIGN KEY (pizza_id) REFERENCES schema_pizza.pizzas(pizza_id) ON DELETE CASCADE,
    FOREIGN KEY (order_id) REFERENCES schema_pizza.orders(order_id) ON DELETE CASCADE
);




