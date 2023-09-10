
var MyQueue = function() {
    this.queue = [];
    this.index = 0;
};

/** 
 * @param {number} x
 * @return {void}
 */
MyQueue.prototype.push = function(x) {
    this.queue.push(x);

};

/**
 * @return {number}
 */
MyQueue.prototype.pop = function() {
    this.index ++;
    return this.queue[this.index-1];
};

/**
 * @return {number}
 */
MyQueue.prototype.peek = function() {
    return this.queue[this.index];
};

/**
 * @return {boolean}
 */
MyQueue.prototype.empty = function() {
    if (this.index == this.queue.length){
        return true;
    }
    else{
        return false;
    }
};

