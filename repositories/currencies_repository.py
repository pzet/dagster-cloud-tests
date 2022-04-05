from dagster import repository

from pipelines.currencies_pipeline import currency_pipeline


@repository
def currencies_repo():
    return {
        "pipelines": {
            "currency_pipeline": lambda: currency_pipeline
        }
    }