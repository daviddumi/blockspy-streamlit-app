import pandas as pd
import datetime
from sqlalchemy import create_engine
import streamlit as st
import psycopg2
import pytz
import keys


def style_24h_change(val):
    color = 'green' if val > 0 else 'red' if val < 0 else 'white'
    return f'color: {color}'

def get_token_data(token):
    # Supabase credentials
    db_username = 'postgres'
    db_password = f'{keys.db_password}'
    db_host = 'db.qvcvedpjrhiirkiuauxs.supabase.co'
    db_port = '5432'
    db_name = 'postgres'

    #postgres connection engine created
    engine = create_engine(f'postgresql://{db_username}:{db_password}@{db_host}:{db_port}/{db_name}')

    #set timezone to avoid errors of servers being in different timezones
    utc = pytz.utc

    #get current datetime, includes hour and minute
    current_datetime = datetime.datetime.now(utc)

    # Subtract one day from the current date if query has not run yet (dune queries run at 12-12:30 UTC and python script runs at 12:45 UTC)
    if current_datetime.hour < 13 or (current_datetime.hour == 13 and current_datetime.minute < 45):
        current_datetime -= datetime.timedelta(days=1)

    # format datetime to only have year month day
    formatted_datetime = current_datetime.strftime("%m-%d-%Y")

    # create dynamic table name that changes whenever you run this shit
    table_name = f"token_flows-{token}-{formatted_datetime}"

    #query for todays table
    query = f'SELECT * FROM "{table_name}"'

    #query supabase and write table to df
    df = pd.read_sql(query, engine)

    #add style to df for up or down
    styled_df = df.style.applymap(style_24h_change, subset=['24h Change'])

    return styled_df