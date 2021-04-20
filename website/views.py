from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Item
from . import db, market
from steam_community_market import  AppID
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        name = request.form.get('name')
        price = request.form.get('price')

        if len(name) < 1:
            flash("Item is not valid.", category='error')
        else:
            new_item = Item(name=name, price=price, user_id=current_user.id)
            db.session.add(new_item)
            db.session.commit()
            flash("Item added!", category='success')
    
    items = Item.query.filter_by(id=Item.id).all()
    for item in items:
        item.current_price = market.get_lowest_price(item.name, AppID.CSGO)

    return render_template("home.html", user=current_user)

@views.route('/delete-item', methods=['POST'])
def delete_item():
    item = json.loads(request.data)
    itemId = item['itemId']
    item = Item.query.get(itemId)
    if item:
        if item.user_id == current_user.id:
            db.session.delete(item)
            db.session.commit()

    return jsonify({})