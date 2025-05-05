import pandas as pd
import streamlit as st 


def top_locations(violations_df: pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locs = (
        violations_df
        .groupby("location")["amount"]  
        .sum()
        .reset_index()
        .rename(columns={"amount": "amount"})  
    )
    top_locs = top_locs[top_locs["amount"] >= threshold]
    return top_locs



def top_locations_mappable(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locs = top_locations(violations_df, threshold)

    lat_lon_df = (
        violations_df[["location", "lat", "lon"]]
        .drop_duplicates(subset="location")
    )

    merged_df = pd.merge(top_locs, lat_lon_df, on="location", how="left")

    return merged_df[["location", "lat", "lon", "amount"]]


def tickets_in_top_locations(violations_df : pd.DataFrame, threshold=1000) -> pd.DataFrame:
    top_locs = top_locations(violations_df, threshold)
    top_loc_names = top_locs["location"]
    filtered_df = violations_df[violations_df["location"].isin(top_loc_names)]
    return filtered_df


if __name__ == '__main__':
    '''
    Main ETL job. 
    '''
    violations_df = pd.read_csv('./cache/final_cuse_parking_violations.csv')

    top_locs_df = top_locations(violations_df)
    top_locs_map_df = top_locations_mappable(violations_df)
    tickets_df = tickets_in_top_locations(violations_df)

    top_locs_df.to_csv('./cache/top_locations.csv', index=False)
    top_locs_map_df.to_csv('./cache/top_locations_mappable.csv', index=False)
    tickets_df.to_csv('./cache/tickets_in_top_locations.csv', index=False)
