import chalk from 'chalk';
import * as cheerio from 'cheerio';
import puppeteer from 'puppeteer';
import { slugify } from 'transliteration';

import { saveToJson, saveToCSV, saveToHTML } from './handlers/savehtml.js';
import listItemsHandler from './handlers/listItemsHandler.js';
import { arrayFromLength } from './helpers/common.js';
import { getPageContent } from './helpers/puppeteer.js';
const startTime = new Date();

const pages = 1;
let num = 1;

export const taskQueue = queue(async (task, done) => {
    try {
      await task();
      console.log(chalk.bold.magenta('Task completed, tasks left: ' + taskQueue.length() + '\n'));
      done();
    } catch (err) {
      throw err;
    }
}, concurrency);
  
taskQueue.drain(function() {
    const endTime = new Date();
    console.log(chalk.green.bold(`🎉  All items completed [${(endTime - startTime) / 1000}s]\n`));
    p.closeBrowser();
    process.exit();
});


(async function main() {
    try {
        for (let page = 1; page <= pages; page++) {
            let site = `https://auto.ria.com/uk/search/?lang_id=4&page=${page}&countpage=100&category_id=1&custom=1&abroad=2`;
            const pageContent = await getPageContent(site);
            const $ = cheerio.load(pageContent);
            const carsItems = [];

            $('.address').each((i, header) => {
                const url = $(header).attr('href');
                const title = $(header).attr('title');

                carsItems.push({
                    title,
                    url,
                    code: slugify(title)
                });
            });
            
            // for (let i=0; i < carsItems.length; i++) {
            //         console.log(`${num}. ${carsItems[i].title} - ${carsItems[i].url}`);
            //         num++
            // }
            
            //console.log(`page - ${page} - ${site}`);
            // console.log(pageContent)
            //await saveToHTML(pageContent, `./savehtml/page - ${page}.html`);
            //listItemsHandler(carsItems) 
            saveToCSV(carsItems)  
            saveToJson(carsItems)          
            console.log(carsItems)            
            if (page == pages) { break; }
        }
    } catch (err) {
        console.log(chalk.red('An error has occured \n'));
        console.log(err);
    }
}());