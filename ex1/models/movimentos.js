const mongoose = require('mongoose')

const MovimentoSchema = new mongoose.Schema({
    _id: String,
    tipo: String,
    data: String,
    valor: Number,
    entidade: String,
    descricao: String
})

module.exports = mongoose.model("movimento", MovimentoSchema)