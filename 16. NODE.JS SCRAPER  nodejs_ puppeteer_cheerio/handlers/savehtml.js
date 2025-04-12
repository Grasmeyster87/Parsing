import fs from 'fs';
import path from 'path';

export async function saveToHTML(data, fileName) {
    const htmlContent = data

    const filePath = path.join(process.cwd(), fileName);

    await fs.writeFileSync(filePath, htmlContent, 'utf8');

    // console.log(`Данные сохранены в ${filePath}`);
}

// Преобразование массива в строки CSV

export async function saveToCSV(mass){
const csvData = mass.map(item => 
    `"${item.title}","${item.url}","${item.code}"`
  ).join('\n');
  
  // Заголовки столбцов
  const headers = 'title,url,code\n';
  
  // Запись в файл
  fs.writeFile('./saveData/cars.csv', headers + csvData, (err) => {
    if (err) {
      console.error('Ошибка при записи файла:', err);
    } else {
      console.log('Файл cars.csv успешно создан!');
    }
  });
}

export async function saveToJson(mass){   
// Преобразование массива в строку JSON
const jsonData = JSON.stringify(mass, null, 2); // Используем null и 2 для форматирования (включая отступы)

// Запись JSON-данных в файл
fs.writeFile('./saveData/cars.json', jsonData, (err) => {
  if (err) {
    console.error('Ошибка при записи файла:', err);
  } else {
    console.log('Файл cars.json успешно создан!');
  }
});
}