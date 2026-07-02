from flask import Flask, render_template
import mysql.connector

app = Flask(__name__)
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ravi@123",
    database="shopeasy"
)
cursor = db.cursor()
@app.route("/")
def home():
    return render_template("index.html")
@app.route("/login")
def login():
    return render_template("login.html")
@app.route("/signup")
def signup():
    return render_template("signup.html")
@app.route("/products")
def products():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM products")
    products = cursor.fetchall()
    return render_template("products.html", products=products)

@app.route("/product-details")
def product_detail():
    return render_template("product-detail.html")
@app.route("/cart")
def cart():
    return render_template("cart.html")
@app.route("/checkout")
def checkout():
    return render_template("checkout.html")
@app.route("/order-success")
def order_success():
    return render_template("order-success.html")

@app.route("/admin-login")
def admin_login():
    return render_template("admin-login.html")
@app.route("/admin_dashboard",methods=["GET","POST"])
def admin_dashboard():
    return render_template("admin_dashboard.html")
@app.route("/add-product")
def add_product():
    return render_template("add-product.html")
@app.route("/save-product", methods=["POST"])
def save_product():
    return "Product Saved Successfully!"
@app.route("/edit-product")
def edit_product():
    return render_template("edit-product.html")


@app.route("/update-product", methods=["POST"])
def update_product():
    return "Product Updated Successfully"


@app.route("/delete-product/<int:id>")
def delete_product(id):
    return f"Product {id} Deleted Successfully"
from flask import request


def products():

    search = request.args.get("search")

    cursor = db.cursor(dictionary=True)

    if search:
        cursor.execute(
            "SELECT * FROM products WHERE product_name LIKE %s",
            ("%" + search + "%",)
        )
    else:
        cursor.execute("SELECT * FROM products")

    products = cursor.fetchall()

    return render_template(
        "products.html",
        products=products
    )

from flask import Flask, render_template, request, redirect
@app.route("/contact", methods=["GET", "POST"])
def contact():

    if request.method == "POST":

        full_name = request.form["full_name"]
        email = request.form["email"]
        subject = request.form["subject"]
        message = request.form["message"]

        cursor = db.cursor()

        sql = """
        INSERT INTO contact_messages
        (full_name,email,subject,message)
        VALUES (%s,%s,%s,%s)
        """

        values = (full_name, email, subject, message)

        cursor.execute(sql, values)

        db.commit()

        return redirect("/contact")

    return render_template("contact.html")
@app.route("/orders")
def orders():

    cursor = db.cursor(dictionary=True)

    cursor.execute("SELECT * FROM orders ORDER BY id DESC")

    orders = cursor.fetchall()

    return render_template("orders.html", orders=orders)
@app.route("/delete-order/<int:id>")
def delete_order(id):

    cursor = db.cursor()

    cursor.execute(
        "DELETE FROM orders WHERE id=%s",
        (id,)
    )

    db.commit()

    return redirect("/admin/orders")
@app.route("/order-status/<int:id>/<status>")
def order_status(id, status):

    cursor = db.cursor()

    cursor.execute(
        "UPDATE orders SET status=%s WHERE id=%s",
        (status, id)
    )

    db.commit()

    return redirect("/admin/orders")
@app.route("/admin/orders")
def admin_orders():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM orders ORDER BY id DESC")
    orders = cursor.fetchall()
    return render_template("admin_orders.html", orders=orders)

@app.route("/update-order/<int:id>/<status>")
def update_order(id, status):
    cursor = db.cursor()
    cursor.execute(
        "UPDATE orders SET status=%s WHERE id=%s",
        (status, id)
    )
    db.commit()
    return redirect("/admin/orders")
if __name__ == "__main__":
    app.run(debug=True)
