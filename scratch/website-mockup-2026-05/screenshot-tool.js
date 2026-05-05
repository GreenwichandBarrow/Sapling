const puppeteer = require('puppeteer-core');

const URL = process.argv[2] || 'http://localhost:8765/';
const OUT = process.argv[3] || '/tmp/out.png';
const WIDTH = parseInt(process.argv[4] || '1440', 10);
const HEIGHT = parseInt(process.argv[5] || '900', 10);
const MODE = process.argv[6] || 'fullpage'; // fullpage | viewport

(async () => {
  const browser = await puppeteer.launch({
    executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
    headless: 'new',
    args: ['--no-sandbox', '--disable-gpu'],
  });
  const page = await browser.newPage();
  await page.setViewport({ width: WIDTH, height: HEIGHT, deviceScaleFactor: 1 });
  await page.goto(URL, { waitUntil: 'networkidle0', timeout: 20000 });
  // Wait extra for fonts
  await new Promise(r => setTimeout(r, 800));
  await page.screenshot({
    path: OUT,
    fullPage: MODE === 'fullpage',
  });
  await browser.close();
  console.log(`OK ${OUT} (${WIDTH}x${HEIGHT}, ${MODE})`);
})().catch(e => { console.error(e); process.exit(1); });
