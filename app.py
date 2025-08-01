from flask import Flask, render_template
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data/superstore.csv", encoding='utf-8')

def get_kpis():
    total_sales = round(df["Sales"].sum(), 2)
    total_profit = round(df["Profit"].sum(), 2)
    total_orders = df["Order.ID"].nunique()
    total_states = df["State"].nunique()
    return total_sales, total_profit, total_orders, total_states

@app.route("/")
def dashboard():
    sales, profit, orders, states = get_kpis()
    return render_template("dashboard.html", sales=sales, profit=profit, orders=orders, states=states)

if __name__ == "__main__":
    app.run(debug=True)

