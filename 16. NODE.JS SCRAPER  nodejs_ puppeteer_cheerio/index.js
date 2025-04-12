import chalk from 'chalk';
import * as cheerio from 'cheerio';
import { slugify } from 'transliteration';
import queue from 'async/queue.js';

import { saveToJson, saveToCSV, saveToHTML } from './handlers/savehtml.js';
import { arrayFromLength } from './helpers/common.js';
import { PuppeteerHandler } from './helpers/puppeteer.js';

const concurrency = 10;
const startTime = new Date();

const pages = 1;
let page = 1;
let site = `https://auto.ria.com/uk/search/?lang_id=4&page=${page}&countpage=100&category_id=1&custom=1&abroad=2`;

export const p = new PuppeteerHandler();

export const taskQueue = queue(async (task, done) => {
  try {
    await task();
    console.log(chalk.bold.magenta('Task completed, tasks left: ' + taskQueue.length() + '\n'));

  } catch (err) {
    throw err;
  }
}, concurrency);

taskQueue.drain(async function () {
  const endTime = new Date();
  console.log(chalk.green.bold(`🎉  All items completed [${(endTime - startTime) / 1000}s]\n`));
  await p.closeBrowser();
  process.exit();
});


async function listPageHandle(url, page) {
  try {
    const pageContent = await p.getPageContent(url);
    const $ = cheerio.load(pageContent);
    const carsItems = [];

    $('.address').each((i, header) => {
      const url = $(header).attr('href');
      const title = $(header).attr('title');

      carsItems.push({
        title,
        url,
        code: slugify(title),
      });
    });

    saveToCSV(carsItems);
    saveToJson(carsItems);
    // console.log(carsItems);
  } catch (err) {
    console.log(chalk.red('An error has occurred \n'));
    console.log(err);
  }
}

(async function main() {
  arrayFromLength(pages).forEach(page => {
    taskQueue.push(
      () => listPageHandle(site, page),
      err => {
        if (err) {
          console.log(err);
          console.log(chalk.green.bold(`✅ Completed getting data from page#${page}\n`));
        }
        console.log(chalk.green.bold(`Completed getting data from page#${page}\n`));
      }
    );
  });
})();