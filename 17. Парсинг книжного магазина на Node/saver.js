export default async function SaveBooksData(value) {
    fs.writeFile('books_data.csv', value, (err)=>{
        if(err){
            console.log("Возникла ошибка", err);
        } else {
            console.log('Файл успешно books_data.csv упешно сохранен')
        }
    })
    
}