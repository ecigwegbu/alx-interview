#!/usr/bin/node
// Print the Characters of a Star Wars Movie

const print = (...x) => console.log(...x); // and your own print() function!
const request = require('request');
// const argv = require 'process.argv';

function printCharacters (x) {
  // Print the Characters of a Star Wars Movie"""
  // Get a list of the characters URIs using the films URI
  // and the characters attribute
  request(`https://swapi-api.alx-tools.com/api/films/${x}/`,
    function (error, code, response) {
      // console.error('error:', error); // Print the error if one occurred
      // print('statusCode:', response && response.statusCode,'\n\n');
      if (error) {
        return print(error);
      }
      const charUrls = JSON.parse(response).characters; // Print the films.
      if (!charUrls) {
        return;
      }

      // Custom function that returns a promise; will wrap the callback
      const getChars = (url) => {
        return new Promise((resolve, reject) => {
          request(url, (err, code, res) => {
            if (err) {
              reject(err);
            } else {
              const name = JSON.parse(res).name;
              resolve(name);
            }
          });
        });
      };

      // Array of promises respects insertion order
      const charPromises = charUrls.map(getChars);

      // resolve all at work but respect the insertion order when thening
      Promise.all(charPromises)
        .then(names => names.forEach(name => print(name)))
        .catch(err => print(err));
    });
}

if ((process.argv.length >= 3) &&
        (Number.isInteger(parseFloat(process.argv[2]))) &&
         parseInt(process.argv[2]) !== 0) {
  printCharacters(parseInt(process.argv[2]));
} else {
  print(`Usage: node ${process.argv[1]} <movie-id>`);
}
