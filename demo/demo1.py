import jsonpath

data = {
    "code": 0,
    "msg": "请求成功",
    "data": {
        "total": 2,
        "union_code": "0000106698140",
        "details": [
            {
                "isPoint": 1.0,
                "tradeNo": "test_tradeNo_0000",
                "remain_points": 1000,
                "sourceCodeRemark": "天猫: 消费积分",
                "orderId": "test_tradeNo_0000",
                "pointTypeName": "消费积分",
                "pointType": "CBP",
                "points": 1000,
                "sourceCode": "天猫",
                "createdDate": "20200909",
                "ID": "f0384d18577b467980041ff41864991d",
                "expirationDate": "20211231",
                "createDateTime": "2020-09-09 18:51:55",
                "remark": "null"
            },
            {
                "isPoint": 1.0,
                "remain_points": 1000,
                "sourceCodeRemark": "积分商城兑换-虚拟物品: 手工调整增积分",
                "orderId": "000000000",
                "pointTypeName": "手工调整增积分",
                "remark": "积分变更接口",
                "pointType": "ABP",
                "points": 1000,
                "sourceCode": "积分商城兑换-虚拟物品",
                "createdDate": "20200909",
                "ID": "04692f1b44f0440baef884e21fee97bd",
                "expirationDate": "20211231",
                "createDateTime": "2020-09-09 22:13:06"
            }
        ]
    }
}
print(data['code'])
token=jsonpath.jsonpath(data, '$..createDateTime')[0]
print(token)