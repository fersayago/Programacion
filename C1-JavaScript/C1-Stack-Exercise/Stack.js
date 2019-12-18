/*
 * Developed by 10Pines SRL
 * License:
 * This work is licensed under the
 * Creative Commons Attribution-NonCommercial-ShareAlike 3.0 Unported License.
 * To view a copy of this license, visit http://creativecommons.org/licenses/by-nc-sa/3.0/
 * or send a letter to Creative Commons, 444 Castro Street, Suite 900, Mountain View,
 * California, 94041, USA.
 *
 */

"use strict";
Object.prototype.shouldImplement = function () {
    throw new Error ("Should implement!");
};

function Stack () {
    this.elements = []
};

Stack.prototype.STACK_EMPTY_DESCRIPTION = "Stack is Empty";

Stack.prototype.push = function (anObject) {
    //ARREGLADO PushAddElementsToTheStack
    return this.elements[this.elements.length] = anObject;
};

Stack.prototype.pop = function () {
    //ARREGLAR CanNotPopWhenThereAreNoObjectsInTheStack
    if (Stack.isEmpty){
        throw new STACK_EMPTY_DESCRIPTION
    } else {
        /*ARREGLADO
        PopRemovesElementsFromTheStack
        PopReturnsLastPushedObject
        StackBehavesLIFO
        */
       //RESPUESTA CON SPLICE 
       return this.elements.splice(-1)[0];       
    };
};
Stack.prototype.top = function (){
    //ARREGLAR CanNotPopWhenThereAreNoObjectsInTheStack
    if (Stack.isEmpty){
        throw new STACK_EMPTY_DESCRIPTION
    } else {
        //ARREGLADO TopReturnsLastPushedObject
        return this.elements[this.elements.length - 1];
    }
};
Stack.prototype.isEmpty = function() {
    //ARREGLADO StackShouldBeEmptyWhenCreated
    return this.elements.length == 0;
};
Stack.prototype.size = function() {
    this.shouldImplement();
};

var assert = require('assert');
assert.isTrue = function (aBoolean) {
    return assert.ok(aBoolean);
};

assert.isFalse = function (aBoolean) {
    return assert.isTrue (!aBoolean);
};

suite('StackTest',function() {

    test('StackShouldBeEmptyWhenCreated', function(){
        var stack = new Stack();

        assert.isTrue(stack.isEmpty());
    });

    test('PushAddElementsToTheStack', function(){
        var stack = new Stack();
        stack.push("Something");

        assert.isFalse(stack.isEmpty());
    });

    test('PopRemovesElementsFromTheStack', function(){
        var stack = new Stack();
        stack.push("Something");
        stack.pop();

        assert.isTrue(stack.isEmpty());
    });

    test('PopReturnsLastPushedObject', function(){
        var stack = new Stack();
        var pushedObject = "Something";
        stack.push(pushedObject);
        assert.deepEqual(pushedObject, stack.pop());
    });

    test('StackBehavesLIFO', function (){
        var firstPushed = "First";
        var secondPushed = "Second";
        var stack = new Stack();
        stack.push(firstPushed);
        stack.push(secondPushed);

        assert.deepEqual(secondPushed,stack.pop());
        assert.deepEqual(firstPushed,stack.pop());
        assert.isTrue(stack.isEmpty());
    });

    test('TopReturnsLastPushedObject', function (){
        var stack = new Stack();
        var pushedObject = "Something";

        stack.push(pushedObject);

        assert.deepEqual(pushedObject, stack.top());
    });

    test('TopDoesNotRemoveObjectFromStack', function(){
        var stack = new Stack();
        var pushedObject = "Something";

        stack.push(pushedObject);

        assert.deepEqual(1,stack.size());
        stack.top();
        assert.deepEqual(1,stack.size());
    });

    test('CanNotPopWhenThereAreNoObjectsInTheStack', function(){
        var stack = new Stack();

        try {
            stack.pop();
            fail();
        } catch (error){
            assert.deepEqual(Stack.prototype.STACK_EMPTY_DESCRIPTION,error.message);
        }
    });

    test('CanNotTopWhenThereAreNoObjectsInTheStack', function(){
        var stack = new Stack();

        try {
            stack.top();
            fail();
        } catch (error){
            assert.deepEqual(Stack.prototype.STACK_EMPTY_DESCRIPTION,error.message);
        }
    });
});
