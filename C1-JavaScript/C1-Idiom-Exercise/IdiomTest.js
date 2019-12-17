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

//Correr con: mocha -u tdd IdiomTest.js

function CustomerBook() {
    this.customerNames = [];
}

function IllegalArgumentException(message) {
    this.message = message;
}

CustomerBook.prototype.CUSTOMER_NAME_EMPTY = "Customer name can not be empty";
CustomerBook.prototype.CUSTOMER_ALREADY_EXISTS = "Customer already exists";
CustomerBook.prototype.INVALID_CUSTOMER_NAME = "Invalid customer name";

CustomerBook.prototype.addCustomerNamed = function (name) {

    if (name.length===0) throw new Error(CustomerBook.prototype.CUSTOMER_NAME_EMPTY);
    if (this.containsCustomerNamed(name)) throw new Error(CustomerBook.prototype.CUSTOMER_ALREADY_EXISTS);

    this.customerNames.push(name);
};

CustomerBook.prototype.isEmpty = function () {
    return this.customerNames.length === 0;
};

CustomerBook.prototype.numberOfCustomers = function () {
    return this.customerNames.length;
};

CustomerBook.prototype.containsCustomerNamed = function (name) {
    return this.customerNames.indexOf(name)!=-1;
};

CustomerBook.prototype.removeCustomerNamed = function (name) {
    if (!this.containsCustomerNamed(name))
        throw new IllegalArgumentException(CustomerBook.prototype.INVALID_CUSTOMER_NAME);

    var nameIndex = this.customerNames.indexOf(name);
    this.customerNames.splice(nameIndex,1);
};

var assert = require('assert');

suite('IdiomTest',function() {
    var customerBook;

    setup(function () {
        customerBook = new CustomerBook();
    });

    test('AddingCustomerShouldNotTakeMoreThan50Milliseconds', function () {
        var millisecondsBeforeRunning = new Date().getTime();
        customerBook.addCustomerNamed("John Lennon");
        var millisecondsAfterRunning = new Date().getTime();

        assert((millisecondsAfterRunning - millisecondsBeforeRunning) < 50);
    });

    test('RemovingCustomerShouldNotTakeMoreThan100Milliseconds', function () {
        var paulMcCartney = "Paul McCartney";

        customerBook.addCustomerNamed(paulMcCartney);

        var millisecondsBeforeRunning = new Date().getTime();
        customerBook.removeCustomerNamed(paulMcCartney);
        var millisecondsAfterRunning = new Date().getTime();

        assert((millisecondsAfterRunning - millisecondsBeforeRunning) < 100);
    });

    test('CanNotAddACustomerWithEmptyName', function () {
        try {
            customerBook.addCustomerNamed("");
            fail();
        } catch (e) {
            if (e instanceof Error) {
                assert.equal(e.message, CustomerBook.prototype.CUSTOMER_NAME_EMPTY);
                assert(customerBook.isEmpty());
            }
            else
                throw e;
        }
    });

    test('CanNotRemoveNotAddedCustomers', function () {
        try {
            customerBook.removeCustomerNamed("John Lennon");
            fail();
        } catch (e) {
            if (e instanceof IllegalArgumentException) {
                assert.equal(e.message, CustomerBook.prototype.INVALID_CUSTOMER_NAME);
                assert.equal(0, customerBook.numberOfCustomers());
            }
            else
                throw e;
        }
    });
});