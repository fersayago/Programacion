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

//Correr con: mocha -u tdd Numero.js
"use strict";

function Numero(){
};

Numero.prototype.DESCRIPCION_DE_ERROR_NO_SE_PUEDE_DIVIDIR_POR_CERO = "No se puede dividir por 0";
Numero.prototype.shouldImplement = function () {
    throw new Error ("Should implement!");
};
Numero.prototype.esCero = function () {shouldImplement();};
Numero.prototype.esUno = function () {shouldImplement();};
Numero.prototype.mas = function (sumando) { shouldImplement(); };
Numero.prototype.por = function (multiplicador) { shouldImplement(); };
Numero.prototype.dividido = function (divisor) { shouldImplement(); };

function Entero(value) {
    Numero.call(this);
    this.value = value;
};
Entero.prototype = Object.create(Numero.prototype);

Entero.prototype.esCero = function () {
    return this.value === 0;
};

Entero.prototype.esUno = function () {
    return this.value === 1;
};

Entero.prototype.mas = function (sumando) {
    if(sumando instanceof Entero) {
        return new Entero(this.value + sumando.value);
    } else {
        let divisor = sumando.denominador;
        let dividendo = this.por(divisor).mas(sumando.numerador);
        return dividendo.dividido(divisor);
    }
};

Entero.prototype.por = function (multiplicador) {
    if (multiplicador instanceof Entero) {
        return new Entero (this.value*multiplicador.value);
    } else {
        let divisor = multiplicador.denominador;
        let dividendo = this.por(multiplicador.numerador);
        return dividendo.dividido(divisor);
    };
};

Entero.prototype.dividido = function(divisor) {
    if (divisor instanceof Entero) {
        return Fraccion.dividir(this, divisor);
    } else {
        //ARREGLAR DivisionDeEnteroPorFraccion
    }
};

Entero.prototype.maximoComunDivisorCon = function (otroEntero) {
    if (otroEntero.esCero())
        return this;
    else
        return otroEntero.maximoComunDivisorCon(this.restoCon(otroEntero));
};

Entero.prototype.restoCon = function (divisor) {
    return new Entero (this.value%divisor.value);
};

Entero.prototype.divisionEntera = function (divisor){
    return new Entero (this.value/divisor.value);
};

function Fraccion(numerador, denominador) {
    if(denominador.esUno()) throw new Error(this.INVALID_DENOMINADOR);

    Numero.call(this);
    this.numerador = numerador;
    this.denominador = denominador;
};
Fraccion.prototype = Object.create(Numero.prototype);
Fraccion.prototype.INVALID_DENOMINADOR = "Denominador no puede ser 1";

Fraccion.dividir = function(dividendo, divisor ) {

    if(divisor.esCero()) throw new Error (
        Numero.prototype.DESCRIPCION_DE_ERROR_NO_SE_PUEDE_DIVIDIR_POR_CERO);
    if(dividendo.esCero()) return dividendo;

    var maximoComunDivisor = dividendo.maximoComunDivisorCon(divisor);
    var numerador = dividendo.divisionEntera(maximoComunDivisor);
    var denominador = divisor.divisionEntera(maximoComunDivisor);

    if (denominador.esUno()) return numerador;

    return new Fraccion(numerador,denominador);
};

Fraccion.prototype.esCero = function () {
    return false;
};

Fraccion.prototype.esUno = function () {
    return false;
};

Fraccion.prototype.mas = function (sumando) {
    if (sumando instanceof Fraccion) {

        var nuevoDenominador = this.denominador.por(sumando.denominador);
        var nuevoNumerador1 = this.numerador.por(sumando.denominador);
        var nuevoNumerador2 = this.denominador.por(sumando.numerador);
        var nuevoNumerador = nuevoNumerador1.mas(nuevoNumerador2);
    
        return nuevoNumerador.dividido(nuevoDenominador);
    } else {
        //ARREGLAR SumaDeFraccionYEntero
        return null
    }
};

Fraccion.prototype.por = function (multiplicador) {
    return this.numerador.por(multiplicador.numerador).
    dividido(this.denominador.por(multiplicador.denominador));
};

Fraccion.prototype.dividido = function (divisor) {
    return this.numerador.por(divisor.denominador).
        dividido(this.denominador.por(divisor.numerador));
};

/*




*/

var assert = require('assert');
assert.isTrue = function (aBoolean) {
    return assert.ok(aBoolean);
};

assert.isFalse = function (aBoolean) {
    return assert.isTrue (!aBoolean);
};

suite('IdiomTest',function() {
    var cero;
    var uno;
    var dos;
    var tres;
    var cuatro;
    var cinco;
    var seis;

    var unQuinto;
    var dosQuintos;
    var tresQuintos;
    var dosVeinticincoavos;
    var unMedio;
    var cincoMedios;
    var seisQuintos;
    var cuatroMedios;
    var dosCuartos;

    setup(function () {
        cero = new Entero(0);
        uno = new Entero(1);
        dos = new Entero(2);
        tres = new Entero(3);
        cuatro = new Entero(4);
        cinco = new Entero(5);
        seis = new Entero(6);

        unQuinto = uno.dividido(cinco);
        dosQuintos = dos.dividido(cinco);
        tresQuintos = tres.dividido(cinco);
        dosVeinticincoavos = dos.dividido(new Entero(25));
        unMedio = uno.dividido(dos);
        cincoMedios = cinco.dividido(dos);
        seisQuintos = seis.dividido(cinco);
        cuatroMedios = cuatro.dividido(dos);
        dosCuartos = dos.dividido(cuatro);
    });

    test("EsCeroDevuelveTrueSoloParaElCero", function () {
        assert.isTrue(cero.esCero());
        assert.isFalse(uno.esCero());
    });

    test("EsUnoDevuelveTrueSoloParaElUno", function () {
        assert.isTrue(uno.esUno());
        assert.isFalse(cero.esUno());
    });

    test("FraccionNoPuedeTenerUnoComoDenominador", function () {
        assert.throws(()=>new Fraccion(uno,uno),Error,Fraccion.prototype.INVALID_DENOMINADOR);
    });

    test("SumaDeEnteros", function () {
        assert.deepEqual(dos, uno.mas(uno));
    });

    test("MultiplicacionDeEnteros", function () {
        assert.deepEqual(cuatro, dos.por(dos));
    });

    test("DivisionDeEnteros", function () {
        assert.deepEqual(uno, dos.dividido(dos));
    });

    test("SumaDeFracciones", function () {
        var sieteDecimos = new Entero(7).dividido(new Entero(10));
        assert.deepEqual(sieteDecimos, unQuinto.mas(unMedio));
        /*
         * La suma de fracciones es:
         *
         * a/b + c/d = (a.d + c.b) / (b.d)
         *
         * SI ESTAN PENSANDO EN LA REDUCCION DE FRACCIONES NO SE PREOCUPEN!
         * TODAVIA NO SE ESTA TESTEANDO ESE CASO
         */
    });

    test("MultiplicacionDeFracciones", function () {
        assert.deepEqual(dosVeinticincoavos, unQuinto.por(dosQuintos));
        /*
         * La multiplicación de fracciones es:
         *
         * (a/b) * (c/d) = (a.c) / (b.d)
         *
         * SI ESTAN PENSANDO EN LA REDUCCION DE FRACCIONES NO SE PREOCUPEN!
         * TODAVIA NO SE ESTA TESTEANDO ESE CASO
         */
    });

    test("DivisionDeFracciones", function () {
        assert.deepEqual(cincoMedios, unMedio.dividido(unQuinto));
        /*
         * La división de fracciones es:
         *
         * (a/b) / (c/d) = (a.d) / (b.c)
         *
         * SI ESTAN PENSANDO EN LA REDUCCION DE FRACCIONES NO SE PREOCUPEN!
         * TODAVIA NO SE ESTA TESTEANDO ESE CASO
         */
    });

    /*
     * Ahora empieza lo lindo! - Primero hacemos que se puedan sumar enteros con fracciones
     * y fracciones con enteros
     */
    test("SumaDeEnteroYFraccion", function () {
        assert.deepEqual(seisQuintos, uno.mas(unQuinto));
    });

    test("SumaDeFraccionYEntero", function () {
        assert.deepEqual(seisQuintos, unQuinto.mas(uno));
    });

    /*
     * Hacemos lo mismo para la multipliación
     */
    test("MultiplicacionDeEnteroPorFraccion", function () {
        assert.deepEqual(dosQuintos, dos.por(unQuinto));
    });

    test("MultiplicacionDeFraccionPorEntero", function () {
        assert.deepEqual(dosQuintos, unQuinto.por(dos));
    });

    /*
     * Hacemos lo mismo para la division
     */
    test("DivisionDeEnteroPorFraccion", function () {
        assert.deepEqual(cincoMedios, uno.dividido(dosQuintos));
    });

    test("DivisionDeFraccionPorEntero", function () {
        assert.deepEqual(dosVeinticincoavos, dosQuintos.dividido(cinco));
    });

    /*
     * Ahora si empezamos con problemas de reducción de fracciones
     */
    test("UnaFraccionPuedeSerIgualAUnEntero", function () {
        assert.deepEqual(dos, cuatroMedios);
    });

    test("LasFraccionesAparentesSonIguales", function () {
        assert.deepEqual(unMedio, dosCuartos);
        /*
         * Las fracciones se reducen utilizando el maximo comun divisor (mcd)
         * Por lo tanto, para a/b, sea c = mcd (a,b) => a/b reducida es:
         * (a/c) / (b/c).
         *
         * Por ejemplo: a/b = 2/4 entonces c = 2. Por lo tanto 2/4 reducida es:
         * (2/2) / (4/2) = 1/2
         *
         * Para obtener el mcd pueden usar el algoritmo de Euclides que es:
         *
         * mcd (a,b) =
         * 		si b = 0 --> a
         * 		si b != 0 -->mcd(b, restoDeDividir(a,b))
         *
         * Ejemplo:
         * mcd(2,4) ->
         * mcd(4,restoDeDividir(2,4)) ->
         * mcd(4,2) ->
         * mcd(2,restoDeDividir(4,2)) ->
         * mcd(2,0) ->
         * 2
         */
    });

    test("LaSumaDeFraccionesPuedeDarEntero", function () {
        assert.deepEqual(uno, unMedio.mas(unMedio));
    });

    test("LaMultiplicacionDeFraccionesPuedeDarEntero", function () {
        assert.deepEqual(dos, cuatro.por(unMedio));
    });

    test("LaDivisionDeEnterosPuedeDarFraccion", function () {
        assert.deepEqual(unMedio, dos.dividido(cuatro));
    });

    test("LaDivisionDeFraccionesPuedeDarEntero", function () {
        assert.deepEqual(uno, unMedio.dividido(unMedio));
    });

    test("NoSePuedeDividirEnteroPorCero", function () {
        try {
            uno.dividido(cero);
            fail();
        }
        catch (e) {
            assert.deepEqual(
                Numero.prototype.DESCRIPCION_DE_ERROR_NO_SE_PUEDE_DIVIDIR_POR_CERO, e.message);
        }
    });

    test("NoSePuedeDividirFraccionPorCero", function () {
        try {
            unQuinto.dividido(cero);
            fail();
        }
        catch (e) {
            assert.deepEqual(
                Numero.prototype.DESCRIPCION_DE_ERROR_NO_SE_PUEDE_DIVIDIR_POR_CERO, e.message);
        }
    });
});

