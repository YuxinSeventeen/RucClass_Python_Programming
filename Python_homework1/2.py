# (a) 创建一个字典 info，用于存储以上商家信息。
info = {
    "瑞幸咖啡": {
        "评分": 4.9,
        "配送费": 3,
        "热销饮品": {}
    },
    "CoCo都可": {
        "评分": 4.8,
        "配送费": 0,
        "热销饮品": {}
    },
    "快乐柠檬": {
        "评分": 4.9,
        "配送费": 0,
        "热销饮品": {}
    }
}

# (b) 将热销饮品信息添加到 info 中。
info["瑞幸咖啡"]["热销饮品"] = {
    "生椰拿铁": 289,
    "厚乳拿铁": 173,
    "拿铁": 126
}
info["CoCo都可"]["热销饮品"] = {
    "鲜百香双响炮": 616,
    "红豆奶茶": 493
}
info["快乐柠檬"]["热销饮品"] = {
    "柠檬菠萝饮": 194
}

# (c) 将“瑞幸咖啡”的配送费改为 6 元。
info["瑞幸咖啡"]["配送费"] = 6

# (d) 删除“快乐柠檬”的信息。
del info["快乐柠檬"]

# (e) 对“瑞信咖啡”热销饮品按月销由低到高排序。
sorted_sales = sorted(info["瑞幸咖啡"]["热销饮品"].items(), key=lambda x: x[1])


print(info)
print(sorted_sales)












