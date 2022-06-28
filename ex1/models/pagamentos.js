const mongoose = require('mongoose')

const PagamentoSchema = new mongoose.Schema({
    _id: String,
    meses_pagos: [String]
})

module.exports = mongoose.model("pagamento", PagamentoSchema)