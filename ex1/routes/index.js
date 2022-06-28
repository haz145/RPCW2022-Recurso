var express = require('express');
var router = express.Router();

var Controller = require('../controllers/controller')

router.get('/api/movimentos', function(req, res, next) {
  if(req.query.groupBy=='entidade') {
    Controller.movsbyent()
      .then(data => {res.jsonp(data)})
      .catch(error => {res.status(500).jsonp({error: error})})
  }
  else if(req.query.groupBy) {
    Controller.movsbytype(req.query.groupBy)
      .then(data => {res.jsonp(data)})
      .catch(error => {res.status(500).jsonp({error: error})})
  }
  else {
    Controller.listmovs()
      .then(data => {res.jsonp(data)})
      .catch(error => {res.status(500).jsonp({error: error})})
  }
});

router.get('/api/pagamentos', function(req, res, next) {
  if(req.query.status) {
    Controller.findpagsby(req.query.status)
      .then(data => {res.jsonp(data)})
      .catch(error => {res.status(500).jsonp({error: error})})
  }
  else {
    Controller.listpags()
      .then(data => {res.jsonp(data)})
      .catch(error => {res.status(500).jsonp({error: error})})
  }
});

router.get('/api/pagamentos/:id', function(req, res, next) {
  Controller.findpagbyid(req.params.id)
    .then(data => {res.jsonp(data)})
    .catch(error => {res.status(500).jsonp({error: error})})
});

router.post('/api/movimentos', function(req, res, next) {
  Controller.addmov(req.body)
    .then(data => {res.jsonp(data)})
    .catch(error => {res.status(500).jsonp({error: error})})
});

router.post('/api/pagamentos', function(req, res, next) {
  Controller.addpag(req.body)
    .then(data => {res.jsonp(data)})
    .catch(error => {res.status(500).jsonp({error: error})})
});

module.exports = router;
