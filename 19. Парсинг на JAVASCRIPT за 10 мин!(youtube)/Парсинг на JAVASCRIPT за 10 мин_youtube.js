const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch({ headless: false });
    const page = await browser.newPage();
    await page.goto('https://www.youtube.com/@Illya.Landar/videos');
    //await page.screenshot({ path: 'img.png' });

    let arr = await page.evaluate(() => {
        let text = Array.from(document.querySelectorAll('#video-title'), el => el.innerText);
        return text;
    });
    console.log(arr);

    await browser.close();
})();