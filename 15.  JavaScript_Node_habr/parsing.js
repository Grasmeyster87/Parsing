//npm i unirest

/*
Unirest - это легковесная библиотека HTTP-запросов, доступная на нескольких языках, созданная и обслуживаемая Kong. Она поддерживает различные HTTP-методы, такие как GET, POST, DELETE, HEAD и т.д., которые могут быть легко добавлены в ваши приложения, благодаря чему ее предпочитают применять для несложных юзкейсов.

Unirest - одна из самых популярных библиотек JavaScript, которая может быть использована для извлечения ценных данных, доступных в интернете.
Давайте рассмотрим на примере, как это можно сделать. Прежде чем начать, я полагаю, что вы уже настроили свой проект Node.js с рабочим каталогом.

Во-первых, установите Unirest JS, выполнив следующую команду в терминале проекта
*/
// const unirest = require("unirest");
//     const getData = async() => {
//     try{
//     const response = await unirest.get("https://quotes.toscrape.com/")
//     console.log(response.body); // HTML
//     }
//     catch(e)
//     {
//     console.log(e);
//     }
//     }
//     getData();

//------------------------------------------------------------------------
/*
Axios

Axios - это HTTP клиент на основе промисов как для Node.js, так и для браузеров. Axios широко используется сообществом разработчиков благодаря разнообразию методов, простоте и активному сопровождению. Она также поддерживает различные фичи, такие как отмена запросов, автоматические преобразования для JSON-данных и т.д.

Вы можете установить библиотеку Axios, выполнив приведенную ниже команду в терминале.
*/
//npm i axios

// const axios = require("axios");
//     const getData = async() => {
//     try{
//         const response = await axios.get("https://books.toscrape.com/")
//         console.log(response.data); // HTML
//     }
//     catch(e)
//     {
//         console.log(e);
//     }
//     }
//     getData();   

//------------------------------------------------------------------------

// SuperAgent

// SuperAgent - еще одна легковесная HTTP клиент библиотека как для Node.js, так и для браузера. Она поддерживает множество высокоуровневых фич HTTP клиента. Она имеет тот же API, что и Axios, и поддерживает как синтаксис промиса, так и синтаксис async/await для обработки ответов.

// Вы можете установить SuperAgent, выполнив следующую команду.
//npm i superagent

// const superagent = require("superagent");
//     const getData = async() => {
//     try{
//         const response = await superagent.get("https://books.toscrape.com/")
//         console.log(response.text); // HTML
//     }
//     catch(e)
//     {
//         console.log(e);
//     }
//     }
//     getData();

//-----------------------------------------------------------------------------------------------

// Cheerio

// Cheerio - это легковесная библиотека для парсинга в интернете, основанная на мощном API jQuery, которая может использоваться для того, чтобы парсить и извлекать данные из HTML и XML документов.

// Cheerio отличается молниеносной скоростью парсинга, манипулирования и рендеринга HTML, поскольку работает с простой последовательной моделью DOM. Это не интернет-браузер, поскольку он не может производить визуальный рендеринг, применять CSS и выполнять JavaScript. Для скрейпинга SPA (Single Page Applications) нам нужны полноценные инструменты автоматизации браузера, такие как Puppeteer, Playwright и т.д., о которых мы поговорим чуть позже.

// const unirest = require("unirest");
// const cheerio = require("cheerio");
// const getData = async() => {
// try{
//     const response = await unirest.get("https://books.toscrape.com/catalogue/sharp-objects_997/index.html")
// const $ = cheerio.load(response.body);
//     console.log("Book Title: " + $("h1").text()); // "Book Title: Sharp Objects"
// }
// catch(e)
// {
//     console.log(e);
// }
// }
// getData(); 

//--------------------------------------------------------------------------
/*
Puppeteer

Puppeteer - это библиотека Node.js, разработанная компанией Google, которая предоставляет высокоуровневый API, позволяющий управлять браузерами Chrome или Chromium.

Особенности, связанные с Puppeteer JS:

    Puppeteer можно использовать для лучшего контроля над Chrome.

    Она может генерировать скриншоты и PDF-файлы веб-страниц.

    Ее можно использовать для скрейпинга веб-страниц, которые используют JavaScript при динамической загрузке содержимого.
*/
/* import puppeteer from "puppeteer";
const browser = await puppeteer.launch({
    headless: false,
    });
    const page = await browser.newPage(); 
    await page.goto("https://books.toscrape.com/index.html" , {
    waitUntil: 'domcontentloaded'
    })  */  

/*
Пошаговое объяснение:

    Сначала мы запустили браузер в headless-режиме, установленном на false, благодаря чему можно видеть, что именно происходит.

    Затем мы создали новую страницу в headless-браузере.

    После этого мы перешли к нашему целевому URL и подождали, пока HTML полностью загрузится.

Теперь мы выполним парсинг HTML.
*/
/* let data = await page.evaluate(() => {
    return Array.from(document.querySelectorAll("article h3")).map((el) => {
    return {
    title: el.querySelector("a").getAttribute("title"),
    link: el.querySelector("a").getAttribute("href"),
    };
  });
}); */

// Функция page.evalueate() выполнит javascript в контексте текущей страницы. Затем, document.querySelectorAll() выберет все элементы, которые идентифицируются с тегами h3 статьи. document.querySelector() - сделает то же самое, но при этом выберет только один HTML-элемент.

// Отлично! Теперь выведем данные и закроем браузер.

/* console.log(data)
    await browser.close();  */    

//------------------------------------------------------------------------------------

/*
Playwright

Playwright - это фреймворк автоматизации тестирования для автоматизации веб-браузеров Chrome, Firefox и Safari с API, аналогичным Puppeteer. Она [библиотека] была разработана той же командой, которая работала над Puppeteer. Как и Puppeteer, Playwright может работать в режимах headless и non-headless, что делает ее подходящим для широкого спектра задач - от автоматизации задач до веб-скрейпинга или веб-краулинга.

Основные различия между Playwright и Puppeteer

    Playwright совместима с браузерами Chrome, Firefox и Safari, в то время как Puppeteer поддерживает только Chrome.

    Playwright предоставляет широкий спектр опций для управления браузером в режиме headless.

    Puppeteer ограничен только Javascript, в то время как Playwright поддерживает различные языки, такие как C#, .NET, Java, Python и т.д.
*/
// npm i playwright
// 
// const browser = await playwright['chromium'].launch({ headless: false,});
//     const context = await browser.newContext();
//     const page = await context.newPage();
//     await page.goto("https://books.toscrape.com/index.html"); 

// // Функция newContext() создаст новый контекст браузера.

// // Теперь мы подготовим наш парсер.

// let articles =  await page.$$("article");

//     let data = [];                 
//     for(let article of articles)
//     {
//         data.push({
//             price: await article.$eval("p.price_color", el => el.textContent),
//             availability: await article.$eval("p.availability", el => el.textContent),
//         });
//     } 

// // Затем закроем браузер.

// await browser.close();

//--------------------------------------------------------------------------------------

/*
Nightmare JS

Nightmare - это высокоуровневая библиотека, спроектированная как средство автоматизации интернет-браузинга, веб-скрейпинга и различных других задач. Она использует фреймворк Electron (похожий на Phantom JS, но в два раза быстрее), который предоставляет ей headless-браузер, делая ее эффективной и простой в эксплуатации. Применяется преимущественно для тестирования пользовательского интерфейса и краулинга.

Может использоваться для имитации действий пользователя, таких как переход на сайт, нажатие кнопки или ссылки, ввод текста и т.д. с помощью API, который обеспечивает плавное выполнение действий для каждого блока сценария.

Установите Nightmare JS, выполнив следующую команду.
*/
//npm i nightmare

//Теперь мы будем искать результаты "Serpdog" на duckduckgo.com.

// const Nightmare = require('nightmare')
//     const nightmare = Nightmare()
//         nightmare
//     .goto('https://duckduckgo.com')
//     .type('#search_form_input_homepage', 'Serpdog')
//     .click('#search_button_homepage')
//     .wait('.nrn-react-div')
//     .evaluate(() =>
//     {
//         return Array.from(document.querySelectorAll('.nrn-react-div')).map((el) => {
//         return {
//         title: el.querySelector("h2").innerText.replace("\n",""),
//         link: el.querySelector("h2 a").href
//         }
//     })
//     })
//         .end()
//         .then((data) => {
//         console.log(data)
//         })
//         .catch((error) => {
//         console.error('Search failed:', error)
//         })                        

//-----------------------------------------------------------------------------------
/*
Node Fetch

Node Fetch - это легковесная библиотека, которая предоставляет Fetch API в Node.js, позволяя эффективно выполнять HTTP-запросы в среде Node.js.

Особенности:

    Позволяет использовать промисы и асинхронные функции.

    Реализует функциональность Fetch API в Node.js.

    Простой API, который регулярно поддерживается, легкий в использовании и понимании.

Вы можете инсталлировать Node Fetch, выполнив следующую команду.
*/

// const fetch = require("node-fetch")
// const getData = async() => {
// const response = await fetch('https://en.wikipedia.org/wiki/JavaScript');
// const body = await response.text();

// console.log(body);
// }
// getData(); 
//---------------------------------------------------------------------
// Osmosis

// Osmosis - это библиотека веб-скрейпинга, используемая для извлечения HTML или XML документов с веб-страницы.

// Особенности:

//     Не имеет больших зависимостей, таких как jQuery и Cheerio.

//     Имеет чистый интерфейс, похожий на промис.

//     Быстрый парсинг и небольшой объем занимаемой памяти.

// Преимущества:

//     Поддерживает ретраи (повторные попытки) и перенаправляет лимиты (ограничения).

//     Поддерживает один и несколько прокси-серверов.

//     Поддерживает отправку форм, сессионные куки и т.д.