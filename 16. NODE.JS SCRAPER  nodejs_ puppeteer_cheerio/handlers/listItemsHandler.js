import * as cheerio from 'cheerio';
import chalk from 'chalk';

import { saveToHTML } from './savehtml.js';
import { taskQueue, p } from '../index.js';


const task = async initialData => {

    try {
        
        for (let i = 0; i < data.length; i++) {
            //console.log(data[i].url)
            const detailContent = await p.getPageContent(data[i].url);
            //console.log(detailContent)
            //console.log(` ${chalk.green(data[i].title)} - ${chalk.green.bold(data[i].url)}`);                    
            //console.log(chalk.green('Getting data from: ') + chalk.green.bold(initialDataurl));
            //await saveToHTML(detailContent, `./savehtml/onepage/page - ${i}.html`);
            const $ = cheerio.load(detailContent);

            // Получаем текст заголовка
            const carModel = $('h1.head').text();

            // Получаем цену
            const carPrice = $('div.price_value strong').text();

            console.log(`${carModel} - ${carPrice}  - ${chalk.green.bold(data[i].url)}`);
        }
        
    } catch (err) {
        throw err;
    }
};


export default function listItemsHandler(data) {
    data.forEach(initialData => {
        taskQueue.push(
            () => task(initialData),
            err => {
                if (err) {
                    console.log(err);
                    throw new Error('Error getting data from url[ ' + initialData.url + ' ]');
                }
                console.log(chalk.green.bold(`Success getting data from: \n${initialData.url}\n`));
            }
        );
    });
}