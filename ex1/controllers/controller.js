const Fracao = require('../models/fracoes')
const Movimento = require('../models/movimentos')
const Pagamento = require('../models/pagamentos')

module.exports.listmovs = () => {
    return Movimento.find({}).exec()
}

module.exports.movsbyent = () => { //todo
    //return Movimento.find({}, '-_id entidade valor').exec()
    return Movimento.aggregate([{
        $lookup: {
            _id: '$_id',
            valor_gasto: { $cond: { 
                if: { $match: [ "$tipo", "Despesa" ] }, 
                then: "$valor", 
                else: 0
            },
            valor_recebido: { $cond: { 
                if: { $match: [ "$tipo", "Receita" ] }, 
                then: "$valor", 
                else: 0}
            }
            }
        }
    }]).exec()
}

module.exports.movsbytype = (t) => {
    return Movimento.find({tipo:t}).exec()
}

module.exports.listpags = () => {
    return Pagamento.find({}).exec()
}

//devolve a lista de devedores e o respetivo montante até ao mês indicado
module.exports.findpagsby = (mes) => {
    dict = {'jan':1, 'fev':2, 'mar':3, 'abr':4, 'mai':5, 'jun':6, 'jul':7, 'ago':8, 'set':9, 'out':10, 'nov':11, 'dez':12}
    nm = dict[mes]
    return Pagamento.aggregate([{
        $match : { meses_pagos : { "$nin": [mes] } }
    }, {
        $lookup: {
            'from': Fracao.collection.name,
            'localField': "_id",
            "foreignField": "_id",
            "as": "fracao"
        }
    }, {
        $unwind: {
            path: '$fracao',
            preserveNullAndEmptyArrays: true
        }
    }, {
        $project: {
            _id: '$_id',
            divida: {$multiply: [ "$fracao.mensalidade", {$subtract: [ nm, {$size: '$meses_pagos'}] } ]}
        }   
    }]).exec()
}

module.exports.findpagbyid = (id) => {
    return Pagamento.aggregate([{
        $match: {_id: id}
    }, {
        $lookup: {
            'from': Fracao.collection.name,
            'localField': "_id",
            "foreignField": "_id",
            "as": "fracao"
        }
    }, {
        $unwind: {
            path: '$fracao',
            preserveNullAndEmptyArrays: true
        }
    }, {
        $project: {
            _id: '$_id',
            meses_pagos : '$meses_pagos',
            total_pago : { $multiply: [ "$fracao.mensalidade", {$size: '$meses_pagos'} ] },
            total_divida : { $multiply: [ "$fracao.mensalidade", { $subtract: [ 12, {$size: '$meses_pagos'} ] }] }
        }   
    }]).exec()
}

module.exports.addpag = function(p){
    var newP = new Pagamento(p)
    return newP.save()
}

module.exports.addmov = function(m){
    var newM = new Movimento(m)
    return newM.save()
}