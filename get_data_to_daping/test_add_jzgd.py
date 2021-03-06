# 新增建筑工地数据
import pytest
from common.common_method import *
import requests

data1 = {
    "buildInfo": {
        "address": "浦东新区书院镇 东至用地边界，南至东大公路，西至用地边界，北至X8路",
        "constructionCompany": {
            "address": "中国（上海）自由贸易试验区临港新片区白玉兰大道288号",
            "name": "上海临港书院经济发展有限公司",
            "person": "顾正国",
            "phone": "18916169593"
        },
        "engineerMud": {
            "emissionEndDate": "2020-12-23 00:00:00",
            "emissionStartDate": "2020-11-27 00:00:00",
            "name": "上海雨良土石方工程有限公司",
            "person": "张华栋",
            "phone": "18221365233",
            "planAmount": 30000
        },
        "masterCompany": {
            "address": "上海市浦东新区大同路1355号1幢112室",
            "name": "上海市浦东新区建设（集团）有限公司",
            "person": "吴毅飞",
            "phone": "15618189629"
        },
        "monitorCompany": {
            "address": "上海市杨浦区赤峰路73号",
            "name": "上海同济工程项目管理咨询有限公司",
            "person": "杨云成",
            "phone": "13585756469"
        },
        "name": "书院社区Y5路（东大公路-X8路）及市政配套工程（一标段）",
        "number": "D1PD20201204002*01",
        "serial": "PD20201204002",
        "startTime": "2020-11-27 00:00:00",
        "status": 1
    },
    "company": "上海雨良土石方工程有限公司",
    "forbiddenTime": "22:00-次日7:00",
    "outputBeginTime": "2020-11-27 00:00:00",
    "outputEndTime": "2020-12-23 00:00:00",
    "outputQuantity": "30000",
    "personName": "庄海峰",
    "phone": "13916712146",
    "refillDetailResponse": {
        "address": "S2两港大道门户地块西北侧",
        "companyName": "上海雨良土石方工程有限公司",
        "endTime": "2020-12-23 00:00:00",
        "name": "S2两港大道门户地块",
        "person": "张华栋",
        "phone": "18221365233",
        "serial": "816E4249-2475-4683-BF40-44224135670A",
        "startTime": "2020-11-27 00:00:00",
        "total": 30000
    },
    "reportPerson": "庄海峰",
    "routing": "东大公路,两港大道,卸点",
    "vehicleNum": "沪DR4298",
    "startDate": "2020-11-27 00:00:00",
    "endDate": "2020-12-23 00:00:00",
    "creation_date": "2021-04-16T14:40:05.448Z"
}
data2 = {
    "buildInfo": {
        "address": "浦东新区泥城镇东至G07-09绿地边界，南至G07-08地块边界，西至G07-09绿地边界，北至琼阁路（D51路）",
        "constructionCompany": {
            "address": "上海市浦东新区云端路1566弄7号210室",
            "name": "上海临港检验检测科技产业园有限公司",
            "person": "龚尚书",
            "phone": "13564478721"
        },
        "engineerMud": {
            "emissionEndDate": "2021-05-31 00:00:00",
            "emissionStartDate": "2021-04-01 00:00:00",
            "name": "上海雨良土石方工程有限公司",
            "person": "田君",
            "phone": "15921679896",
            "planAmount": 90000
        },
        "masterCompany": {
            "address": "上海市杨浦区兰州路1100弄1号210室",
            "name": "上海通兴建设集团有限公司",
            "person": "夏红良",
            "phone": "13585555622"
        },
        "monitorCompany": {
            "address": "上海市崇明区高岛路1333弄11号",
            "name": "上海高科工程咨询监理有限公司",
            "person": "周园君",
            "phone": "13918407210"
        },
        "name": "上海临港检验检测科技产业园（G07-07地块）",
        "number": "D1PD20210402001*01",
        "serial": "PD20210402001",
        "startTime": "2021-04-01 00:00:00",
        "status": 1
    },
    "company": "上海雨良土石方工程有限公司",
    "forbiddenTime": "22:00-次日9:00",
    "outputBeginTime": "2021-04-01 00:00:00",
    "outputEndTime": "2021-05-31 00:00:00",
    "outputQuantity": "90000",
    "personName": "庄海峰",
    "phone": "13916712146",
    "refillDetailResponse": {
        "address": "东至L01-08地块，北至规划地块，西至规划地块，南至申能电厂一期",
        "companyName": "上海雨良土石方工程有限公司",
        "endTime": "2021-05-31 00:00:00",
        "name": "LO1-07地块",
        "person": "田君",
        "phone": "15921679896",
        "serial": "CD1BC3AF-C77D-4DA0-AC55-3287A9116EF2",
        "startTime": "2021-04-01 00:00:00",
        "total": 90000
    },
    "reportPerson": "庄海峰",
    "routing": "工地,新元南路,两港大道,妙香路,卸点",
    "vehicleNum": "沪DR4298",
    "startDate": "2021-04-01 00:00:00",
    "endDate": "2021-05-31 00:00:00",
    "creation_date": "2021-04-16T14:40:07.398Z"
}
data3 = {
    "buildInfo": {
        "address": "东至茉莉路绿线、南至方竹路红线WSW-C2-19号地块边界、西至秋涟河河道蓝线、北至申港大道绿线",
        "constructionCompany": {
            "address": "浦东新区临港新城环湖西一路819号",
            "name": "上海海港新城房地产有限公司",
            "person": "姜伟",
            "phone": "18321102571"
        },
        "engineerMud": {
            "emissionEndDate": "2021-05-31 00:00:00",
            "emissionStartDate": "2020-11-25 00:00:00",
            "name": "上海雨良土石方工程有限公司",
            "person": "陶正叶",
            "phone": "13817384640",
            "planAmount": 300000
        },
        "masterCompany": {
            "address": "中国（上海）自由贸易区福山路33号5楼D座",
            "name": "上海建工二建集团有限公司",
            "person": "王振艺",
            "phone": "13816749697"
        },
        "monitorCompany": {
            "address": "上海市静安区广延路359-367号623室",
            "name": "上海智通建设发展股份有限公司",
            "person": "刘强松",
            "phone": "13916191653"
        },
        "name": "临港新城主城区馨尚锦苑商品房项目",
        "number": "D1PD20210125003*01",
        "serial": "PD20210125003",
        "startTime": "2020-11-25 00:00:00",
        "status": 1
    },
    "company": "上海雨良土石方工程有限公司",
    "forbiddenTime": "22:00-次日9:00",
    "outputBeginTime": "2020-11-25 00:00:00",
    "outputEndTime": "2021-05-31 00:00:00",
    "outputQuantity": "300000",
    "personName": "庄海峰",
    "phone": "13916712146",
    "refillDetailResponse": {
        "address": "茉莉路与橄榄路交叉口",
        "companyName": "上海雨良土石方工程有限公司",
        "endTime": "2021-05-31 00:00:00",
        "name": "黄日港临时消纳点",
        "person": "陶正叶",
        "phone": "13817384640",
        "serial": "D7B3039A-E557-44FC-A3F7-0F1C5347C1A8",
        "startTime": "2020-11-25 00:00:00",
        "total": 300000
    },
    "reportPerson": "庄海峰",
    "routing": "工地,方竹路,沪城环路,橄榄路,茉莉路,卸点",
    "vehicleNum": "沪DR4298",
    "startDate": "2020-11-25 00:00:00",
    "endDate": "2021-05-31 00:00:00",
    "creation_date": ISODate("2021-04-16T14:40:07.769Z")
}
data4 = {
    "buildInfo": {
        "address": "南汇新城镇东至云鹃路，西至环湖西二路，南至瑞木路，北至楠木路",
        "constructionCompany": {
            "address": "上海市浦东新区环湖西一路819号",
            "name": "上海港城开发（集团）有限公司",
            "person": "王舒婷",
            "phone": "13621661657"
        },
        "engineerMud": {
            "emissionEndDate": "2021-04-30 00:00:00",
            "emissionStartDate": "2021-02-20 00:00:00",
            "name": "上海雨良土石方工程有限公司",
            "person": "李开元",
            "phone": "18321793563",
            "planAmount": 90000
        },
        "masterCompany": {
            "address": "上海市虹口区东大名路666号",
            "name": "上海建工集团股份有限公司",
            "person": "施灵灵",
            "phone": "18621725620"
        },
        "monitorCompany": {
            "address": "上海市杨浦区宁国路41号",
            "name": "上海浦桥工程建设管理有限公司",
            "person": "王从清",
            "phone": "13370043591"
        },
        "name": "临港南汇新城WNW-A1-9-1地块新建工程（主体部分）",
        "number": "D1PD20210316012*01",
        "serial": "PD20210316012",
        "startTime": "2021-02-20 00:00:00",
        "status": 1
    },
    "company": "上海雨良土石方工程有限公司",
    "forbiddenTime": "22：00-次日9:00",
    "outputBeginTime": "2021-02-20 00:00:00",
    "outputEndTime": "2021-04-30 00:00:00",
    "outputQuantity": "90000",
    "personName": "庄海峰",
    "phone": "13916712146",
    "refillDetailResponse": {
        "address": "浦东新区南汇新城镇DSH-H1-12地块临港北路北侧地块",
        "companyName": "上海雨良土石方工程有限公司",
        "endTime": "2021-04-30 00:00:00",
        "name": "临港新城主城区滴水湖一号码头公共绿地工程",
        "person": "李开元",
        "phone": "18321793563",
        "serial": "36D4F583-2D4D-4366-BCC5-3D2EE7F6484B",
        "startTime": "2021-02-20 00:00:00",
        "total": 90000
    },
    "reportPerson": "庄海峰",
    "routing": "工地,云鹃路,瑞木路,环湖西二路,临港大道,环湖西一路,卸点",
    "vehicleNum": "沪DR4298",
    "startDate": "2021-02-20 00:00:00",
    "endDate": "2021-04-30 00:00:00",
    "creation_date": ISODate("2021-04-16T14:40:10.590Z")
}
data5 = {
    "buildInfo": {
        "address": "南汇新城镇NHC105社区03单元01-05地块",
        "constructionCompany": {
            "address": "浦东新区临港新城环湖西一路819号",
            "name": "上海市临港地区建设项目管理服务中心",
            "person": "陶伟",
            "phone": "18001668838"
        },
        "engineerMud": {
            "emissionEndDate": "2020-10-31 00:00:00",
            "emissionStartDate": "2020-08-28 00:00:00",
            "name": "上海雨良土石方工程有限公司",
            "person": "陶正叶",
            "phone": "13817384640",
            "planAmount": 300600
        },
        "masterCompany": {
            "address": "上海（中国）自由贸易试验区世纪大道1568号27层",
            "name": "中国建筑第八工程局有限公司",
            "person": "闵凡文",
            "phone": "18263369452"
        },
        "monitorCompany": {
            "address": "上海市徐汇区斜土路1223号",
            "name": "上海富达工程管理咨询有限公司",
            "person": "杨丽娟",
            "phone": "13816354819"
        },
        "name": "南汇新城星空之境海绵公园DBO项目（四阶段）",
        "number": "D1PD20200901001*01",
        "serial": "PD20200901001",
        "startTime": "2020-08-28 00:00:00",
        "status": 1
    },
    "company": "上海雨良土石方工程有限公司",
    "outputBeginTime": "2020-08-28 00:00:00",
    "outputEndTime": "2020-10-31 00:00:00",
    "outputQuantity": "300600",
    "personName": "庄海峰",
    "phone": "13916712146",
    "refillDetailResponse": {
        "address": "春涟临时消纳点",
        "companyName": "上海雨良土石方工程有限公司",
        "endTime": "2020-10-31 00:00:00",
        "name": "春涟临时消纳点",
        "person": "陶正叶",
        "phone": "13817384640",
        "serial": "003B6B9F-A4D9-4C0E-BCA0-E6077966F4B5",
        "startTime": "2020-08-28 00:00:00",
        "total": 300600
    },
    "reportPerson": "庄海峰",
    "routing": "环湖北三路,环湖东三路,春涟河临时消纳点",
    "vehicleNum": "沪DR4298",
    "startDate": "2020-08-28 00:00:00",
    "endDate": "2020-10-31 00:00:00",
    "creation_date": ISODate("2021-04-16T14:40:11.929Z")
}
data6 = {
    "buildInfo": {
        "address": "泥城镇东至G07-09绿地边界，南至G07-08绿地边界，西至G07-09绿地边界，北至琼阁路（D51路）",
        "constructionCompany": {
            "address": "上海市浦东新区云端路1566弄7号210室",
            "name": "上海临港检验检测科技产业园有限公司",
            "person": "龚尚书",
            "phone": "13564478721"
        },
        "engineerMud": {
            "emissionEndDate": "2021-04-08 00:00:00",
            "emissionStartDate": "2021-03-08 00:00:00",
            "name": "上海雨良土石方工程有限公司",
            "person": "田君",
            "phone": "15921679896",
            "planAmount": 20000
        },
        "masterCompany": {
            "address": "上海市杨浦区兰州路1100弄1号210室",
            "name": "上海通兴建设集团有限公司",
            "person": "夏红良",
            "phone": "13585555622"
        },
        "monitorCompany": {
            "address": "上海市崇明区高岛路1333弄11号",
            "name": "上海高科工程咨询监理有限公司",
            "person": "周园君",
            "phone": "13918407210"
        },
        "name": "上海临港检验检测科技产业园（G07-07地块）分一期",
        "number": "D1PD20210322001*01",
        "serial": "PD20210322001",
        "startTime": "2021-03-08 00:00:00",
        "status": 1
    },
    "company": "上海雨良土石方工程有限公司",
    "forbiddenTime": "22:00-次日9:00",
    "outputBeginTime": "2021-03-08 00:00:00",
    "outputEndTime": "2021-04-08 00:00:00",
    "outputQuantity": "20000",
    "personName": "庄海峰",
    "phone": "13916712146",
    "refillDetailResponse": {
        "address": "层林路新元南路",
        "companyName": "上海雨良土石方工程有限公司",
        "endTime": "2021-04-08 00:00:00",
        "name": "两港大道南侧绿化带回填点",
        "person": "田君",
        "phone": "15921679896",
        "serial": "D6C5E1F9-10A0-4FD7-A8C7-384639A631A8",
        "startTime": "2021-03-08 00:00:00",
        "total": 20000
    },
    "reportPerson": "庄海峰",
    "routing": "工地,新元南路,两港大道,卸点",
    "vehicleNum": "沪DR4298",
    "startDate": "2021-03-08 00:00:00",
    "endDate": "2021-04-08 00:00:00",
    "creation_date": ISODate("2021-04-16T14:40:13.522Z")
}

data_list = [data1, data2, data3, data4, data5, data6]


def add_jzgd_data():
    '''
    添加建筑工地数据
    API: http://10.242.212.163:10620/gms/report/create/report?admin=true&userId=1
    ???
    :return:
    '''
