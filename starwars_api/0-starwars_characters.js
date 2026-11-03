#!/usr/bin/node
const request = require('request');

const filmId = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${filmId}`;

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }
  const characters = JSON.parse(body).characters;
  const promises = characters.map(
    (charUrl) =>
      new Promise((resolve, reject) => {
        request(charUrl, function (charErr, charRes, charBody) {
          if (charErr) {
            reject(charErr);
          } else {
            resolve(JSON.parse(charBody).name);
          }
        });
      })
  );

  Promise.all(promises)
    .then((names) => {
      names.forEach((name) => console.log(name));
    })
    .catch((err) => console.error(err));
});
