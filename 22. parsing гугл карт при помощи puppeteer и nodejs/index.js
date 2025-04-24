const puppeteer = require('puppeteer');

(async () => {
    // Launch the browser and open a new blank page
    const browser = await puppeteer.launch({
        headless: false,
        args: ['--no-sandbox', '--disable-setuid-sandbox']
    });

    const page = await browser.newPage();

    await page.goto('https://www.google.com/maps/search/%D0%BF%D0%B8%D0%B2%D0%BE+%D0%B3%D0%BE%D1%80%D0%B8%D1%88%D0%BD%D0%B8+%D0%BF%D0%BB%D0%B0%D0%B2%D0%BD%D0%B8/@49.0112963,33.6137973,14z/data=!3m1!4b1?entry=ttu&g_ep=EgoyMDI1MDQyMC4wIKXMDSoASAFQAw%3D%3D', { waitUntil: 'domcontentloaded' });
    // await page.waitFor(300);
    // Set screen size.
    await page.setViewport({width: 1080, height: 1024});

    await page.evaluate(async () => {
        const scrollStep = window.innerHeight; // Шаг прокрутки
        const scrollInterval = 100; // Интервал в миллисекундах
    
        while (document.documentElement.scrollHeight - window.scrollY > window.innerHeight) {
            window.scrollBy(0, scrollStep);
            await new Promise(resolve => setTimeout(resolve, scrollInterval)); // Пауза перед следующей прокруткой
        }
    });
    // Выполняем клик по элементу
    await page.click('[aria-label="Hop Hey"]');

    const carts = await page.evaluate(() => {
        return Array.from(document.querySelectorAll('a.hfpxzc')).map(el => el.getAttribute('aria-label'));
    });
    console.log(carts);
    

    // let k = 1;
    // while (k <= 10) {
    //     console.log(k + ' ряд');
    //     let i = 1;
    //     while (i <= 20) {
    //         console.log(i + ' колонка');
    //         // await page.waitFor(5000);
    //         try {
    //             // Ждем, пока нужный элемент загрузится
    //             await page.waitForSelector('[aria-label="Hop Hey"]', { timeout: 5000 });

    //             // Выполняем клик по элементу
    //             await page.click('[aria-label="Hop Hey"]');
    //         } catch (error) {
    //             console.log(error);
    //         }
    //         i++;
    //     }
    //     k++;
    // }
    // console.log('The title of this blog post is "%s".', page);
    await new Promise(r => setTimeout(r, 5000));
    await browser.close();
})();