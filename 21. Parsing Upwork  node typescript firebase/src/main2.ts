
import axios from 'axios';
const jsdom = require("jsdom");
const { JSDOM } = jsdom;

import puppeteer from 'puppeteer';

import { initializeApp } from "firebase/app";

var Email = 'azal11@meta.ua';
var Password = '[Azal11_#12345]';
var UID = 'neCFzzBhvlebYaqpbSozB4i5iRH2';

let headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Referer': 'https://www.upwork.com/',
    'Origin': 'https://www.upwork.com',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
  }

let url = 'https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&sort=recency&t=1';

// (async () => {
    
//     let html: string;

//     try {

//         const resp = await axios.get(url, {headers});
//         html = resp.data;

//     } catch (error) {
//         if(axios.isAxiosError(error)){
//            console.log(error);
//         } else {
//            console.log(error)
//         }        
//     }

//     const dom = new JSDOM(html);
//     const document = dom.window.document;
//     const items = document.querySelectorAll('article.job-tile.cursor-pointer.px-md-4.air3-card.air3-card-list.px-4x')
    
    
//     //---------------------------------------------------------------------------------------------------------------------------------------------------
//     let mas = [];

//     for (let node of items) {
//         let id = node.querySelector('article.job-tile.cursor-pointer.px-md-4.air3-card.air3-card-list.px-4x.visited').getAttribute('data-ev-job-uid');
//         let url = node.querySelector('a.air3-link').getAttribute('href');
//         let price = Number(node.querySelector('.job-tile-info-list [data-test="is-fixed-price"] strong:last-child').textContent.trim());
//         let title = node.querySelector('a.air3-link').textContent.trim(); // Исправлено на textContent для корректного доступа
    
//         // Добавляем объект в массив
//         mas.push({ id, url, price, title });
//     }
    
//     console.log(mas);
    

//     process.exit(1);
   
// })()

(async () => {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();
    await page.goto('https://www.upwork.com/nx/search/jobs/?category2_uid=531770282580668418&sort=recency&t=1');
  
    const content = await page.content();
  
    // Тут можно использовать JSDOM или Cheerio для парсинга
    
    const dom = new JSDOM(content);
    const document = dom.window.document;
    const items = document.querySelectorAll('article.job-tile.cursor-pointer.px-md-4.air3-card.air3-card-list.px-4x')
    console.log(content);
    await new Promise(_func=> setTimeout(_func, 5000));
    await browser.close();
  })();