const puppeteer = require('puppeteer')

(async () => {

})()
// Launch the browser and open a new blank page
const browser = await puppeteer.launch();
const page = await browser.newPage();

// Navigate the page to a URL.
await page.goto('https://www.google.com.ua/maps/@49.0570586,33.428651,13z?entry=ttu&g_ep=EgoyMDI1MDQyMC4wIKXMDSoJLDEwMjExNDUzSAFQAw%3D%3D');

// Set screen size.
await page.setViewport({width: 1080, height: 1024});

// Type into search box.
await page.locator('.devsite-search-field').fill('automate beyond recorder');

// Wait and click on first result.
await page.locator('.devsite-result-item-link').click();