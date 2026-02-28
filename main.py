from __future__ import annotations

import argparse
import json
from pathlib import Path

from src.analyzer import (
    compute_kpis,
    revenue_by_month,
    revenue_by_region,
    salesperson_performance,
    top_products,
)
from src.data_loader import load_sales_data
from src.visualizer import save_monthly_revenue_chart, save_region_revenue_chart


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sales data analysis project")
    parser.add_argument(
        "--input",
        default="data/sales_sample.csv",
        help="Input CSV path (default: data/sales_sample.csv)",
    )
    parser.add_argument(
        "--output",
        default="output",
        help="Output directory for reports and charts (default: output)",
    )
    parser.add_argument(
        "--top-n",
        type=int,
        default=5,
        help="Number of top products to include (default: 5)",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    output_dir = Path(args.output)
    output_dir.mkdir(parents=True, exist_ok=True)

    df = load_sales_data(args.input)

    kpis = compute_kpis(df)
    monthly = revenue_by_month(df)
    regions = revenue_by_region(df)
    products = top_products(df, args.top_n)
    salespeople = salesperson_performance(df)

    monthly.to_csv(output_dir / "monthly_revenue.csv", index=False)
    regions.to_csv(output_dir / "region_revenue.csv", index=False)
    products.to_csv(output_dir / "top_products.csv", index=False)
    salespeople.to_csv(output_dir / "salesperson_performance.csv", index=False)

    with open(output_dir / "kpis.json", "w", encoding="utf-8") as f:
        json.dump(kpis, f, ensure_ascii=False, indent=2)

    chart1 = save_monthly_revenue_chart(monthly, output_dir)
    chart2 = save_region_revenue_chart(regions, output_dir)

    print("=== Sales Analysis Completed ===")
    print(f"Input data: {args.input}")
    print(f"Output folder: {output_dir.resolve()}")
    print(f"Total Revenue: {kpis['total_revenue']:.2f}")
    print(f"Total Orders: {kpis['total_orders']}")
    print(f"Average Order Value: {kpis['avg_order_value']:.2f}")
    print(f"Total Units Sold: {kpis['total_units']:.0f}")
    print(f"Saved charts: {chart1.name}, {chart2.name}")


if __name__ == "__main__":
    main()
