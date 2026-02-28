from pathlib import Path

import pandas as pd


REQUIRED_COLUMNS = {
    "order_id",
    "date",
    "region",
    "salesperson",
    "product",
    "category",
    "quantity",
    "unit_price",
}


def load_sales_data(csv_path: str | Path) -> pd.DataFrame:
    """Load and validate sales data from CSV."""
    path = Path(csv_path)
    if not path.exists():
        raise FileNotFoundError(f"CSV file not found: {path}")

    df = pd.read_csv(path)
    missing = REQUIRED_COLUMNS - set(df.columns)
    if missing:
        raise ValueError(f"CSV missing required columns: {sorted(missing)}")

    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    if df["date"].isna().any():
        raise ValueError("Found invalid date values in 'date' column")

    df["quantity"] = pd.to_numeric(df["quantity"], errors="coerce")
    df["unit_price"] = pd.to_numeric(df["unit_price"], errors="coerce")
    if df[["quantity", "unit_price"]].isna().any().any():
        raise ValueError("Found non-numeric values in quantity/unit_price")

    df["sales_amount"] = df["quantity"] * df["unit_price"]
    return df
