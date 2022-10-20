import pandas as pd
import os
from sqlalchemy import create_engine
import seaborn as sns
import matplotlib.pyplot as plt

POSTGRES_USER='aalonso'
POSTGRES_PASS='ITBA'
POSTGRES_HOST="localhost"
POSTGRES_DB='database_pizza'
POSTGRES_PORT='5432'
POSTGRES_SCHEMA='schema_pizza'

str_conection=f"postgresql://{POSTGRES_USER}:{POSTGRES_PASS}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}"

engine=create_engine(str_conection,
connect_args={'options': f'-csearch_path={POSTGRES_SCHEMA}'})

conn = engine.connect()
