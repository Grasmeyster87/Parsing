// npm i axios jsdom

const jsdom = require("jsdom");
const { JSDOM } = jsdom;
const axios = require('axios');

url = "https://www.ebay.com/itm/264714553889?_skw=nodebook&itmmeta=01JSC5JQ5JPJD7ANQ1RZPQ5EXD&hash=item3da2378a21:g:zZQAAOSwX41n7zAA&itmprp=enc%3AAQAKAAAA4FkggFvd1GGDu0w3yXCmi1fTcCpsnF0NmVYy01romaqsEFkaY6yg%2BmL3MP6VAK7LIUh%2BQTQetGxGTodmKQd25dZEAM8adTnrprT8dr%2BsXeuEhWh4setTfljUUqwZdcBt%2BucIM3kNGnJOc4SIHMX9XL9Ujhf6XzBnnLfiMWKEUiId%2FUjlP3Ld%2FGXO6HMK9MsmedfLdWW4jCxqHYiDUZi22zPJnaoq8QXeIuNxN6Cy4kP5AH8279RiA14HpvrXYfX1ABuwUK4lMk331blyAeZJaOk3PvsMlgEAxAYx5OEoiULJ%7Ctkp%3ABFBMzvTKhctl";
axios.get(url).then(response => {
    const doc = new JSDOM(response.data); // Use 'doc' instead of 'dom.window.document'
    const dom = doc.window.document;

    const product = {};

    product.title = dom.querySelector("span.ux-textspans.ux-textspans--BOLD")
        .textContent.trim(); // Use optional chaining in case the element is not found
    product.price = dom.querySelector("div.x-price-primary span.ux-textspans").textContent.trim(); // Same here for safety
    product.description = dom.querySelector("div.x-item-condition-desc span.ux-textspans.ux-textspans--ITALIC").textContent.trim();


    console.log(product);
});