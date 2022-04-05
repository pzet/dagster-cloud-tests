import requests

import pandas as pd
from dagster import solid


@solid
def fetch_xml() -> str:
    res = requests.get("https://www.nbp.pl/kursy/xml/a064z220401.xml")
    res.encoding = "UTF-8"
    if res.status_code == 200:
        print("Data fetched correctly.")
        return res.text
    else:
        print(res.status_code)


@solid
def xml_to_df(xml_data: str) -> pd.DataFrame:
    return pd.read_xml(xml_data)


@solid
def clean_df(df: pd.DataFrame) -> pd.DataFrame:
    return df.iloc[2:]


@solid
def filter_for_dollars(df: pd.DataFrame) -> pd.DataFrame:
    return df[df["nazwa_waluty"].str.contains("dolar")]


currencies_xml = fetch_xml()
currencies_pd = xml_to_df(currencies_xml)
currencies_pd_clean = clean_df(currencies_pd)
currencies_dollars_pd = filter_for_dollars(currencies_pd_clean)
