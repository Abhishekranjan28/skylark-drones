def merge_deals_work(deals_df, work_df, link_col):

    if link_col not in work_df.columns:
        return None

    merged = work_df.merge(
        deals_df,
        left_on=link_col,
        right_on="item_id",
        how="left",
        suffixes=("_work", "_deal")
    )

    return merged
