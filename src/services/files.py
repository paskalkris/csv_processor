from fastapi import Depends
import dask.dataframe as dd
from celery import shared_task

from src import config

from src.exceptions import OutOfRangeColumnsList


@shared_task
def process(filepath: str, delta: int):
    df = _get_dataframe(filepath)
    ds_res = _sum_columns(df, delta)
    return ds_res.to_dict()


def _get_dataframe(filepath: str) -> dd.DataFrame:
    df = dd.read_csv(
        filepath,
        sep='["/?,]+',
        engine="python",
        storage_options=config.get_settings().STORAGE_OPTIONS,
    ).dropna(how="all")
    df.set_index("Unnamed: 0")
    if df.columns[-1].startswith("Unnamed"):
        df.drop(columns=[df.columns[-1]])
    return df


def _sum_columns(df: dd.DataFrame, delta: int) -> dd.Series:
    if len(df.columns) < (delta):
        raise OutOfRangeColumnsList(filepath, delta, len(df.columns))
    return df[df.columns[delta::delta]].sum().compute()
