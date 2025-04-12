import * as cheerio from 'cheerio';
import chalk from 'chalk';

import path from 'path';
import fs from 'fs';

import { saveToHTML } from './savehtml.js';

import {getPageContent} from '../helpers/puppeteer.js';
import { formatPrice, formatPeriod } from '../helpers/common.js';


export default async function listItemsHandler(data) {

    try {        
            console.log('listItemsHandler work')
            for (let i=0; i < data.length; i++) {
                    //console.log(data[i].url)
                    const detailContent = await getPageContent(data[i].url)
                    //console.log(detailContent)
                    //console.log(` ${chalk.green(data[i].title)} - ${chalk.green.bold(data[i].url)}`);                    
                    //console.log(chalk.green('Getting data from: ') + chalk.green.bold(initialDataurl));
                    await saveToHTML(detailContent, `./savehtml/onepage/page - ${i}.html`);
                    const $ = cheerio.load(detailContent);

                    // Получаем текст заголовка
                    const carModel = $('h1.head').text();

                    // Получаем цену
                    const carPrice = $('div.price_value strong').text();                    
                                                                   
                    console.log(`${carModel} - ${carPrice}  - ${chalk.green.bold(data[i].url)}`)                                                
                }
            // }    

    //let priceNew = priceNewStr ? formatPrice(priceNewStr) : null;
    //let priceWithMileage = priceWithMileageStr ? formatPrice(priceWithMileageStr) : null;
        
    } catch (err) {
        throw err
    }
}
// async function saveData(data) {
    
// }