'use strict';
const fs = require('fs-extra');
const path = require('path');

let pathToRead = '/home/abolanos/airwaveJcampAdmin/';
let listData = fs.readFileSync('/home/abolanos/data.txt', 'utf8');
let allData = fs.readdirSync(pathToRead)
listData = listData.split('\n');
listData = listData.filter(e => e.match('Airwave-'))
let toMove = [];
for (let a of allData) {
  if (!listData.includes(a)) copyFile(path.join(pathToRead, a), a, '/home/abolanos','toMove')
}

async function copyFile(filePath, fileName, base, dest) {
  const destination = path.join(base, dest, fileName);
  await tryCopy(filePath, destination);
}

async function tryCopy(from, to, suffix = 0) {
  try {
    await fs.copy(from, to);
  } catch (e) {
    throw new Error(`Could not rename ${from} to ${newTo}: ${e}`);
  }
}
