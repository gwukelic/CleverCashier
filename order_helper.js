'use strict';
module.change_code = 1;

function OrderHelper (obj) {
  this.order_list = [{menuItem: null, size: null, count: 0}];
  this.doneOrdering = false;
  
  // Assign each field to values stored in given obj
  this.order_list[0].menuItem = obj.menuItem;
  this.order_list[0].size = obj.size;
  this.order_list[0].count = obj.count;
  
  this.justStarted = this.hasStarted();
}

OrderHelper.prototype.getAttributes = function() {
  return this.order_list[0];
};

OrderHelper.prototype.addQuantity = function(count) {
  // this.hasStarted();
  this.justStarted = false;
  this.order_list[0].count = count;
};

OrderHelper.prototype.addSize = function(size) {
  // this.hasStarted();
  this.justStarted = false;
  this.order_list[0].size = size;

};

OrderHelper.prototype.addMenuItem = function(menuItem) {
  // this.hasStarted();
  this.justStarted = false;
  this.order_list[0].menuItem = menuItem;
};

OrderHelper.prototype.completed = function() {
  if (this.order_list[0].menuItem != null && this.order_list[0].size != null 
      && this.order_list[0].count > 0) {
    this.doneOrdering = true;
  }
  return this.doneOrdering;
};

OrderHelper.prototype.hasStarted = function() {
  this.justStarted = false;
  if (this.order_list[0].menuItem == null && this.order_list[0].size == null 
      && this.order_list[0].count <= 0) {
    this.justStarted = true;
  }
  return this.justStarted;
};

OrderHelper.prototype.getOrder = function() {
  return this.order_list[0].count + " " 
          + this.order_list[0].size + " " 
          + this.order_list[0].menuItem;
};

OrderHelper.prototype.getPrompt = function() {
  if (this.justStarted) {
    return "What would you like to order?";
  }
  if (this.order_list[0].menuItem == null) {
    return "Which menu item would you like to order?";
  }
  if (this.order_list[0].size == null) {
    return "What " + this.order_list[0].menuItem + " size would you like?";
  }
  if (this.order_list[0].count == null || this.order_list[0].count == 0) {
    return "How many " + this.order_list[0].menuItem + " would you like?";
  }
  return;
};

module.exports = OrderHelper;

