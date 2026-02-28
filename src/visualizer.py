from pathlib import Path

import matplotlib.pyplot as plt
import seaborn as sns


sns.set_theme(style="whitegrid")


def save_monthly_revenue_chart(monthly_df, output_dir: str | Path) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    chart_path = output_dir / "monthly_revenue.png"
    plt.figure(figsize=(10, 5))
    sns.lineplot(data=monthly_df, x="month", y="sales_amount", marker="o")
    plt.title("Monthly Revenue Trend")
    plt.xlabel("Month")
    plt.ylabel("Revenue")
    plt.xticks(rotation=30)
    plt.tight_layout()
    plt.savefig(chart_path, dpi=150)
    plt.close()
    return chart_path


def save_region_revenue_chart(region_df, output_dir: str | Path) -> Path:
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)

    chart_path = output_dir / "region_revenue.png"
    plt.figure(figsize=(8, 5))
    sns.barplot(data=region_df, x="region", y="revenue", palette="Blues_d")
    plt.title("Revenue by Region")
    plt.xlabel("Region")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig(chart_path, dpi=150)
    plt.close()
    return chart_path
