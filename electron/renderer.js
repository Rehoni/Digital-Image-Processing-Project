//jshint esversion:6 

const zerorpc = require("zerorpc");
let client = new zerorpc.Client();

client.connect("tcp://127.0.0.1:4242");

// client.invoke("echo", "hello world", (error, res) => {
//   if (error || res !== 'hello world') {
//     console.error(error);
//   } else {
//     console.log(res);
//   }
// });

const selectImage = document.getElementById('selected-image');


if (selectImage.src == null) {
  document.getElementById('shape').innerHTML = 'shape:';
  document.getElementById('size').innerHTML = 'size:';
  document.getElementById('mean').innerHTML = 'mean:';
} else {
  client.invoke("open", selectImage.src, (error, res) => {
    console.log(selectImage.src);
  });
  client.invoke("shape", (error, res) => {
    console.log(res);
  });
  client.invoke("size", (error, res) => {
    if (res == undefined) {

    } else {
      document.getElementById('size').innerHTML = 'size:' + res;
    }
  });
  client.invoke("mean", (error, res) => {
    if (res == undefined) {

    } else {
      document.getElementById('mean').innerHTML = 'mean:' + res;
    }
  });
}