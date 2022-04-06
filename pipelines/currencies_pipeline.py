from dagster import pipeline

from solids.requests_solids import (
    fetch_xml,
    xml_to_df,
    clean_df,
    filter_for_dollars,
    df_to_csv,
)


@pipeline
def currency_pipeline():
    currencies_xml = fetch_xml()
    currencies_pd = xml_to_df(currencies_xml)
    currencies_pd_clean = clean_df(currencies_pd)
    currencies_dollars_pd = filter_for_dollars(currencies_pd_clean)
    df_to_csv(currencies_dollars_pd)
