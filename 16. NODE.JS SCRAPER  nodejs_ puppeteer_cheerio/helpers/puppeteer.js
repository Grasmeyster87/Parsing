import puppeteer from 'puppeteer';
import chalk from 'chalk';


export const LAUNCH_PUPPETEER_OPTS = {
    args: [
        '--no-sandbox',
        '--disable-setuid-sandbox',
        '--disable-dev-shm-usage',
        '--disable-accelerated-2d-canvas',
        '--disable-gpu',
        '--window-size=1920x1080'
    ]
};

export const PAGE_PUPPETEER_OPTS = {
    networkIdle2Timeout: 5000,
    waitUntil: 'networkidle2',
    timeout: 3000000
};

export class PuppeteerHandler {
    constructor() {
        this.browser = null;
    }
    async initBrowser() {
        this.browser = await puppeteer.launch(LAUNCH_PUPPETEER_OPTS);
    }

    // closeBrowser() {
    //   this.browser.close();
    // }

    async closeBrowser() {
        if (this.browser) {
            try {
                await this.browser.close();
                console.log(chalk.green('Browser closed successfully.'));
            } catch (err) {
                console.error(chalk.red('Failed to close browser:'), err);
            }
        }
    }

    async getPageContent(url) {
        if (!this.browser) {
            await this.initBrowser();
        }

        try {
            const page = await this.browser.newPage();
            await page.goto(url, PAGE_PUPPETEER_OPTS);
            const content = await page.content();
            return content;
        } catch (err) {
            throw err;
        }
    }
}