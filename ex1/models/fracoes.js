const mongoose = require('mongoose')

const FracaoSchema = new mongoose.Schema({
    _id: String,
    permilagem: Number,
    mensalidade: Number
})

module.exports = mongoose.model("fracao", FracaoSchema, "fracoes")