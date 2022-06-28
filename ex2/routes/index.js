var express = require('express');
var router = express.Router();
var axios = require('axios');

router.get('/', function(req, res, next) {
  res.render('index');
});

router.get('/movimentos', function(req, res, next) {
  axios.get("http://localhost:3000/api/movimentos")
  .then( resp => {
    res.render('movs', {data: resp.data});
  })
  .catch(function(erro){
    res.render('error', { error: erro })
  })
});

router.get('/pagamentos', function(req, res, next) {
  axios.get("http://localhost:3000/api/pagamentos")
  .then( resp => {
    res.render('pags', {data: resp.data});
  })
  .catch(function(erro){
    res.render('error', { error: erro })
  })
});


module.exports = router;
