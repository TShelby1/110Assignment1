
from flask import Flask, request
import json
from mock_data import mock_catalog
from config import db 

from bson import ObjectId

app = Flask('Server')

# endpoints


@app.route("/")
def root():
    return "Welcome to our Server"

########################
########### API Catalog ###############
# defaults to get route unless specified


@app.route("/api/about", methods=["POST"])
def about():
    me = {
        "first": "Albert",
        "last": "Lara"

    }
    return json.dumps(me)  # parse into json then return


@app.route("/api/catalog")
def get_catalog():
    cursor = db.products.find({}) #get all, cursor
    all_products = []

    for prod in cursor:
        prod["_id"] = str(prod["_id"])
        all_products.append(prod)

    return json.dumps(all_products)

@app.route("/api/catalog", methods=["POST"]) #receive post, and use data to create product
def save_product():
    product = request.get_json()
    db.products.insert_one(product)

    print("product saved")
    print(product)

    product["_id"] = str(product["_id"])
    return json.dumps(product)  #this will crash the




#/api/catalog/cheapest
# returns the cheapest product in the catalog

@app.route("/api/catalog/cheapest")
def get_cheapest():
    cursor = db.products.find({})
    solution = cursor[0]
    for prod in cursor:
        if prod["price"] < solution["price"]:
            solution = prod
    solution["_id"] = str(solution["_id"])
    return json.dumps(solution)

@app.route("/api/catalog/total")
def get_sum():
    cursor = db.products.find({})
    total = 0
    for prod in cursor:
        total += prod["price"]

    
    return json.dumps(total)
    

#find a product based off the unique ID, the id tag at the end will catch any ID 
@app.route("/api/products/<id>")
def find_product(id):
    prod = db.products.find_one({"_id": ObjectId (id) })
    prod["_id"] = str(prod["_id"])

    return json.dumps(prod)
    

@app.route("/api/products/categories")
def get_categories():
    categories = []
    cursor = db.products.find({})

    for prod in cursor:
        cat = prod["category"]
        if cat not in categories:
            categories.append(cat)
    return json.dumps(categories)
    

@app.route("/api/products/category/<cat_name>")
def get_by_category(cat_name):
    results = []
    cursor = db.products.find({"category": cat_name}) #getting products from cursor, fix id

    for prod in cursor:
        prod["_id"] = str(prod["_id"])   #to make the search case in-sensitive
        results.append(prod)



    return json.dumps(results)


@app.route("/api/products/search/<text>")
def search_by_text(text):
    results = []

    for prod in mock_catalog:
        title = prod["title"].lower()
        if text.lower() in title:
            results.append(prod)        

    return json.dumps(results)

#######################################
#########   Coupon Codes   ############
#######################################

@app.route("/api/couponCodes")
def coupon_codes():
    cursor = db.couponCodes.find({}) #get all, cursor
    results = []

    for coupon in cursor:
        coupon["_id"] = str(coupon["_id"])
        coupon_codes.append(coupon)

    return json.dumps(results)

@app.route("/api/couponCodes", methods=["POST"]) #receive post, and use data to create product
def save_coupon():
    coupon = request.get_json()
    db.coupons.insert_one(coupon)

    print("coupon saved")
    print(coupon)

    coupon["_id"] = str(coupon["_id"])
    return json.dumps(coupon)  #this will crash the






app.run(debug=True)


# exercise createa a new script file 
# 1 call a function named, numbers
# numbers fn will print 1-20 except 11/13