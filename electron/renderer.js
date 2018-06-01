//jshint esversion:6 

const zerorpc = require("zerorpc");
let client = new zerorpc.Client();

client.connect("tcp://127.0.0.1:4242");

client.invoke("echo", "hello world", (error, res) => {
  if(error || res !== 'hello world') {
    console.error(error);
  } else {
    console.log(res);
  }
});