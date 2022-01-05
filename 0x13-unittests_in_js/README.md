# 0x13. Unittests in JS

## Resources:books:
Read or watch:
* [Mocha documentation](https://mochajs.org/)
* [Chai](https://www.chaijs.com/api/)
* [Sinon](https://sinonjs.org/releases/v7.5.0/)
* [Express](https://expressjs.com/en/guide/routing.html)
* [Request](https://www.npmjs.com/package/request) - request has been deprecated, see https://github.com/request/request/issues/3142

* [How to Test NodeJS Apps using Mocha, Chai and SinonJS](https://www.digitalocean.com/community/tutorials/how-to-test-nodejs-apps-using-mocha-chai-and-sinonjs) - This tutorial is out of date and no longer maintained.


---
## Learning Objectives:bulb:
* How to use Mocha to write a test suite
* How to use different assertion libraries (Node or Chai)
* How to present long test suites
* When and how to use spies
* When and how to use stubs
* What are hooks and when to use them
* Unit testing with Async functions
* How to write integration tests with a small node server
---

### [0. Basic test with Mocha and Node assertion library](./package.json)
* Install Mocha using npm:


### [1. Combining descriptions](./1-calcul.js)
* Create a new file named 1-calcul.js:


### [2. Basic test using Chai assertion library](./2-calcul_chai.js)
* While using Node assert library is completely valid, a lot of developers prefer to have a behavior driven development style. This type being easier to read and therefore to maintain.


### [3. Spies](./utils.js)
* Spies are a useful wrapper that will execute the wrapped function, and log useful information (e.g. was it called, with what arguments). Sinon is a library allowing you to create spies.


### [4. Stubs](./4-payment.js)
* Stubs are similar to spies. Except that you can provide a different implementation of the function you are wrapping. Sinon can be used as well for stubs.


### [5. Hooks](./5-payment.js)
* Hooks are useful functions that can be called before execute one or all tests in a suite


### [6. Async tests with done](./6-payment_token.js)
* Look into how to support async testing, for example when waiting for the answer of an API or from a Promise


### [7. Skip](./7-skip.test.js)
* When you have a long list of tests, and you can’t figure out why a test is breaking, avoid commenting out a test, or removing it. Skip it instead, and file a ticket to come back to it as soon as possible


### [8. Basic Integration testing](./8-api/package.json)
* In a folder 8-api located at the root of the project directory, copy this package.json over.


### [9. Regex integration testing](./9-api/api.js)
* In a folder 9-api, reusing the previous project in 8-api (package.json, api.js and api.test.js)


### [10. Deep equality & Post integration testing](./10-api/api.js)
* In a folder 10-api, reusing the previous project in 9-api (package.json, api.js and api.test.js)

---

## Author
* **Manuel Torres Vesga** - [matcls](https://github.com/matcls)