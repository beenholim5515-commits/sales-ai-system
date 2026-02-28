# Python 销售数据分析项目（sales-ai-system）

这是一个完整的可运行 Python 销售数据分析示例项目，包含：

- `data/`：销售示例数据 CSV
- `src/`：数据加载、分析、可视化模块
- `main.py`：项目入口脚本
- `requirements.txt`：依赖清单
- `output/`：运行后生成的报表和图表

## 1. 项目结构

```text
sales-ai-system/
├── data/
│   └── sales_sample.csv
├── src/
│   ├── __init__.py
│   ├── analyzer.py
│   ├── data_loader.py
│   └── visualizer.py
├── output/                     # 运行 main.py 后自动生成结果
├── main.py
├── requirements.txt
└── README.md
```

## 2. 环境安装

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

## 3. 快速运行

使用默认示例数据：

```bash
python main.py
```

指定输入和输出路径：

```bash
python main.py --input data/sales_sample.csv --output output --top-n 5
```

## 4. 输出内容

运行完成后，`output/` 目录会包含：

- `kpis.json`：核心指标（总收入、订单数、客单价、销量）
- `monthly_revenue.csv`：月度营收
- `region_revenue.csv`：区域营收
- `top_products.csv`：Top N 产品
- `salesperson_performance.csv`：销售人员绩效
- `monthly_revenue.png`：月度营收趋势图
- `region_revenue.png`：区域营收柱状图

## 5. 数据字段说明

`data/sales_sample.csv` 字段：

- `order_id`：订单编号
- `date`：订单日期
- `region`：销售区域
- `salesperson`：销售人员
- `product`：产品名称
- `category`：产品类别
- `quantity`：销售数量
- `unit_price`：产品单价

程序会自动计算：

- `sales_amount = quantity * unit_price`

## 6. 可扩展方向

- 增加客户维度分析（新客/老客、复购率）
- 增加时间序列预测（Prophet / ARIMA）
- 接入数据库（MySQL / PostgreSQL）替代 CSV
- 增加 Streamlit 可视化仪表盘
