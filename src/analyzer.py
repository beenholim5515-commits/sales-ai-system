from __future__ import annotations

import pandas as pd


def compute_kpis(df: pd.DataFrame) -> dict[str, float]:
    """Compute high-level KPI metrics."""
    total_revenue = float(df["sales_amount"].sum())
    total_orders = int(df["order_id"].nunique())
    avg_order_value = total_revenue / total_orders if total_orders else 0.0
    total_units = float(df["quantity"].sum())

    return {
        "total_revenue": round(total_revenue, 2),
        "total_orders": total_orders,
        "avg_order_value": round(avg_order_value, 2),
        "total_units": round(total_units, 2),
    }


def revenue_by_month(df: pd.DataFrame) -> pd.DataFrame:
    monthly = (
        df.assign(month=df["date"].dt.to_period("M").dt.to_timestamp())
        .groupby("month", as_index=False)["sales_amount"]
        .sum()
        .sort_values("month")
    )
    monthly["sales_amount"] = monthly["sales_amount"].round(2)
    return monthly


def top_products(df: pd.DataFrame, n: int = 5) -> pd.DataFrame:
    product_df = (
        df.groupby("product", as_index=False)
        .agg(
            revenue=("sales_amount", "sum"),
            units=("quantity", "sum"),
            orders=("order_id", "nunique"),
        )
        .sort_values("revenue", ascending=False)
        .head(n)
    )
    return product_df.round({"revenue": 2, "units": 2})


def revenue_by_region(df: pd.DataFrame) -> pd.DataFrame:
    region_df = (
        df.groupby("region", as_index=False)["sales_amount"]
        .sum()
        .sort_values("sales_amount", ascending=False)
    )
    region_df = region_df.rename(columns={"sales_amount": "revenue"})
    return region_df.round(2)


def salesperson_performance(df: pd.DataFrame) -> pd.DataFrame:
    perf = (
        df.groupby("salesperson", as_index=False)
        .agg(
            revenue=("sales_amount", "sum"),
            units=("quantity", "sum"),
            orders=("order_id", "nunique"),
        )
        .sort_values("revenue", ascending=False)
    )
    return perf.round({"revenue": 2, "units": 2})
