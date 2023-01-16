const parse = require('csv-parse/lib/sync');
const fs = require('fs');

// buffer형식을 string 형식의 2차원 배열로 변경
const csv = fs.readFileSync('csv/data.csv');
const records = parse(csv.toString('utf-8'));
records.forEach((r, i) => {
    console.log(i, r);
});
