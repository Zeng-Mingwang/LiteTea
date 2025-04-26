from app import create_app, db
from app.models.models import User, Product
from werkzeug.security import generate_password_hash
import os

def init_db():
    app = create_app()
    with app.app_context():
        # 清空现有数据
        db.drop_all()
        db.create_all()
        
        # 创建管理员账户
        admin = User(
            username='admin',
            password=generate_password_hash('admin123', method='pbkdf2:sha256'),
            is_admin=True
        )
        db.session.add(admin)
        
        # 创建测试用户
        test_user = User(
            username='test',
            password=generate_password_hash('test123', method='pbkdf2:sha256'),
            is_admin=False
        )
        db.session.add(test_user)
        
        # 创建测试商品
        products = [
            # 21. 黄芪玫瑰饮
            {
                "name": "黄芪玫瑰饮",
                "description": "甘肃黄芪搭配山东玫瑰，3:1调气养颜配比，现煮现萃，香气温和，滋补不燥。",
                "price": 28.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/黄芪玫瑰饮.png",
                "product_features": "甘肃黄芪搭配山东玫瑰，3:1调气养颜配比，现煮现萃，香气温和，滋补不燥。",
                "objective_analysis": "黄芪≥3g/杯，黄芪多糖含量≥0.2g；玫瑰花瓣≥1.5g，挥发油保留率≥85%；总溶出物浓度约1.1%。",
                "drinking_suggestions": "饭后一小时饮用最佳；建议一周饮用3次作为日常调理；经期与孕期女性建议遵医指导饮用。",
                "ingredients": "纯净水、黄芪、玫瑰花",
                "origin": "黄芪（甘肃定西）\n玫瑰（山东平阴）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "气虚体弱、肤色晦暗、作息紊乱者"
            },
            # 22. 红豆薏米水
            {
                "name": "红豆薏米水",
                "description": "东北红豆与江西薏米，1:1.2祛湿健脾黄金配比，谷香浓郁，适合久坐少动者。",
                "price": 26.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/红豆薏米水.png",
                "product_features": "东北红豆与江西薏米，1:1.2祛湿健脾黄金配比，谷香浓郁，适合久坐少动者。",
                "objective_analysis": "红豆≥8g、薏米≥10g；总膳食纤维≥0.6g/杯；无添加糖，热量＜50kcal。",
                "drinking_suggestions": "建议早餐或午后饮用；每周饮用3~5次，适合湿气重调理；孕妇、低血糖人群请酌情饮用。",
                "ingredients": "纯净水、红小豆、薏米",
                "origin": "红小豆（黑龙江海伦）\n薏米（江西广昌）\n纯净水（湖北武汉）",
                "specifications": "净含量：350ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "湿气重、水肿、脾胃虚弱者"
            },
            # 23. 黑米决明子茶
            {
                "name": "黑米决明子茶",
                "description": "云南紫黑米与安徽决明子搭配，谷香醇厚，滋补护眼，适合日常用眼频繁人群。",
                "price": 25.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/黑米决明子茶.png",
                "product_features": "云南紫黑米与安徽决明子搭配，谷香醇厚，滋补护眼，适合日常用眼频繁人群。",
                "objective_analysis": "黑米≥10g，富含花青素≥15mg；决明子≥10g，大黄酚≥0.05g；总多酚约0.3g/杯。",
                "drinking_suggestions": "午后饮用缓解眼部疲劳；不建议睡前饮用，以免轻度通便影响休息。",
                "ingredients": "纯净水、黑米、炒决明子",
                "origin": "黑米（云南元江）\n决明子（安徽亳州）\n纯净水（湖北武汉）",
                "specifications": "净含量：330ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "视疲劳、眼干涩、作息不规律者"
            },
            # 24. 玉米须茶
            {
                "name": "玉米须茶",
                "description": "精选吉林黄金玉米须，自然晒干后提取利水成分，清香淡雅，适合易水肿人群日常饮用。",
                "price": 22.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/玉米须茶.png",
                "product_features": "精选吉林黄金玉米须，自然晒干后提取利水成分，清香淡雅，适合易水肿人群日常饮用。",
                "objective_analysis": "玉米须≥6g，黄酮类物质≥0.25g/杯；钾离子含量约55mg/杯；总溶出物含量约1%。",
                "drinking_suggestions": "建议午后饮用，帮助代谢多余水分；不建议空腹或睡前饮用。",
                "ingredients": "纯净水、玉米须",
                "origin": "玉米须（吉林农安）\n纯净水（湖北武汉）",
                "specifications": "净含量：320ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "易浮肿、饮食重口、高盐摄入者"
            },
            # 25. 草本金银花茶
            {
                "name": "草本金银花茶",
                "description": "河北巨鹿金银花轻焙处理后现场萃取，茶汤金黄透亮，入口甘凉，适合上火人群。",
                "price": 24.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/草本金银花茶.png",
                "product_features": "河北巨鹿金银花轻焙处理后现场萃取，茶汤金黄透亮，入口甘凉，适合上火人群。",
                "objective_analysis": "金银花≥2g，绿原酸≥0.25g/杯；清热抗氧指标（DPPH自由基清除率）≥65%；咖啡因含量：0mg。",
                "drinking_suggestions": "适合口干、咽痛、上火期饮用；每日1次，建议不空腹饮用；脾胃虚寒或孕期女性慎用。",
                "ingredients": "纯净水、金银花",
                "origin": "金银花（河北巨鹿）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "咽干舌燥、上火、油腻饮食人群"
            },
            # 26. 桂圆水
            {
                "name": "桂圆水",
                "description": "福建莆田桂圆肉现熬浓煮，香甜软糯，滋补养血。茶汤色深味浓，适合体寒乏力人群。",
                "price": 26.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/桂圆水.png",
                "product_features": "福建莆田桂圆肉现熬浓煮，香甜软糯，滋补养血。茶汤色深味浓，适合体寒乏力人群。",
                "objective_analysis": "桂圆干≥12g/杯；天然果糖含量≥2.8g/杯（无额外添加糖）；总糖溶出物≥3.5g/杯。",
                "drinking_suggestions": "推荐在上午或饭后饮用；不建议热性体质或上火期间饮用；糖尿病人群慎饮。",
                "ingredients": "纯净水、桂圆干",
                "origin": "桂圆（福建莆田）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "气血不足、经常熬夜、手脚冰凉者"
            },
            # 27. 陈皮水
            {
                "name": "陈皮水",
                "description": "采用新会三年以上老陈皮，低温慢煮，清香醇厚，理气健脾，口感微甘略涩。",
                "price": 25.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/陈皮水.png",
                "product_features": "采用新会三年以上老陈皮，低温慢煮，清香醇厚，理气健脾，口感微甘略涩。",
                "objective_analysis": "陈皮≥3g/杯；橙皮苷含量≥0.08g/杯；挥发油溶出率≥75%。",
                "drinking_suggestions": "饭后饮用最佳，有助于消食理气；慢性胃炎人群应温饮；空腹不宜饮用。",
                "ingredients": "纯净水、老陈皮",
                "origin": "陈皮（广东新会）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "脾胃虚弱、消化不良、饭后胀气人群"
            },
            # 28. 枸杞水
            {
                "name": "枸杞水",
                "description": "精选宁夏中宁中粒枸杞，现泡提取，微甜润口，补肝养肾，日常代茶优选。",
                "price": 24.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/枸杞水.png",
                "product_features": "精选宁夏中宁中粒枸杞，现泡提取，微甜润口，补肝养肾，日常代茶优选。",
                "objective_analysis": "枸杞干果≥6g/杯；β-胡萝卜素≥0.3mg/杯；枸杞多糖≥0.25g/杯。",
                "drinking_suggestions": "推荐每日1次，适合上班族长期饮用；有热性症状（口干咽痛）时应暂缓饮用。",
                "ingredients": "纯净水、枸杞",
                "origin": "枸杞（宁夏中宁）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "视力疲劳、作息不规律、肝肾虚弱者"
            },
            # 29. 五红水
            {
                "name": "五红水",
                "description": "红豆、红枣、红皮花生、枸杞、红糖五味合煮，温补养血，滋润不上火，甜香适中。",
                "price": 28.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/五红水.png",
                "product_features": "红豆、红枣、红皮花生、枸杞、红糖五味合煮，温补养血，滋润不上火，甜香适中。",
                "objective_analysis": "总投料量≥20g/杯；铁含量（天然食材提取）约1.1mg/杯；天然糖分（含红糖）≤4g/杯。",
                "drinking_suggestions": "建议月经期或产后调理时饮用；体热者少量饮用为宜；每周2~3次饮用为佳。",
                "ingredients": "纯净水、红豆、红枣、红皮花生、枸杞、红糖",
                "origin": "红豆（黑龙江海伦）\n红枣（新疆若羌）\n花生（河南南阳）\n枸杞（宁夏中宁）\n红糖（云南保山）\n纯净水（湖北武汉）",
                "specifications": "净含量：330ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "气血亏虚、面色苍白、体寒女性"
            },
            # 30. 五白水
            {
                "name": "五白水",
                "description": "白茯苓、白莲子、白扁豆、山药、银耳五种白色药食同源食材组合，健脾补气，口感浓润顺滑。",
                "price": 29.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/五白水.png",
                "product_features": "白茯苓、白莲子、白扁豆、山药、银耳五种白色药食同源食材组合，健脾补气，口感浓润顺滑。",
                "objective_analysis": "总干料≥18g/杯；可溶性多糖≥0.6g/杯（主要来自银耳与茯苓）；蛋白质含量约0.5g/杯。",
                "drinking_suggestions": "适合脾虚食少、肠胃不适者日常调理饮用；冬季热饮效果更佳。",
                "ingredients": "纯净水、白茯苓、白莲子、白扁豆、山药、银耳",
                "origin": "白茯苓（云南文山）\n白莲子（江西广昌）\n白扁豆（湖南邵阳）\n山药（河南焦作）\n银耳（四川通江）\n纯净水（湖北武汉）",
                "specifications": "净含量：330ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "脾胃虚弱、气短乏力、食欲不振人群"
            },
            # 31. 五指毛桃茯苓水
            {
                "name": "五指毛桃茯苓水",
                "description": "精选广东五指毛桃与云南茯苓，遵循1:1草本健脾祛湿黄金配比，融合五指毛桃的椰香与茯苓的甘淡，口感醇厚回甘。",
                "price": 27.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/五指毛桃茯苓水.png",
                "product_features": "精选广东五指毛桃与云南茯苓，遵循1:1草本健脾祛湿黄金配比，融合五指毛桃的椰香与茯苓的甘淡，口感醇厚回甘。",
                "objective_analysis": "五指毛桃≥6g/杯；茯苓≥6g/杯；总膳食纤维≥0.5g/杯；无添加糖，热量＜35kcal（天然植物低卡）。",
                "drinking_suggestions": "晨起空腹或餐后30分钟温饮，助力全天代谢；特殊提醒：孕妇、阴虚火旺者建议咨询医师后饮用。",
                "ingredients": "纯净水、五指毛桃、茯苓",
                "origin": "五指毛桃（广东韶关）\n茯苓（云南楚雄）\n纯净水（湖北武汉）",
                "specifications": "净含量：350ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：开封后常温2小时，冷藏保存≤24小时（建议即饮）",
                "suitable_crowd": "湿气重、脾虚乏力、易水肿者，及长期空调环境工作者"
            },
            # 32. 百合雪梨水
            {
                "name": "百合雪梨水",
                "description": "河北百合搭配砀山雪梨，现煮润肺止咳，汤色微黄，入口柔滑，甜度天然适中。",
                "price": 26.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/百合雪梨水.png",
                "product_features": "河北百合搭配砀山雪梨，现煮润肺止咳，汤色微黄，入口柔滑，甜度天然适中。",
                "objective_analysis": "百合≥6g/杯，雪梨果肉≥40g/杯；水溶性纤维≥0.3g/杯；总糖（天然果糖）≤5g/杯。",
                "drinking_suggestions": "推荐秋冬季节热饮；适用于干咳、咽干口燥；咳嗽带痰或寒湿体质者慎用。",
                "ingredients": "纯净水、百合干、鲜雪梨块",
                "origin": "百合（河北安国）\n雪梨（安徽砀山）\n纯净水（湖北武汉）",
                "specifications": "净含量：320ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "阴虚咳嗽、咽喉干痒、秋冬易上火者"
            },
            # 33. 乌梅山楂水
            {
                "name": "乌梅山楂水",
                "description": "乌梅酸爽，山楂开胃，辅以少量甘草调和，生津解腻，特别适合油腻饮食后饮用。",
                "price": 24.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/乌梅山楂水.png",
                "product_features": "乌梅酸爽，山楂开胃，辅以少量甘草调和，生津解腻，特别适合油腻饮食后饮用。",
                "objective_analysis": "乌梅干≥5g，山楂干≥6g；总有机酸含量≥0.45g/杯；清除口腔油腻感比率＞80%（主观测试）。",
                "drinking_suggestions": "推荐午餐或晚餐后饮用；脾胃虚寒者不宜频繁饮用；酸性较强，不宜空腹饮用。",
                "ingredients": "纯净水、乌梅、山楂、甘草",
                "origin": "乌梅（浙江临安）\n山楂（山东泰安）\n甘草（甘肃陇西）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "油腻饮食后、食欲不振、口干无味者"
            },
            # 34. 大麦茶
            {
                "name": "大麦茶",
                "description": "安徽黄大麦炒香现煮，麦香浓郁，清热利湿，生津止渴。无咖啡因，适合全年龄段饮用。",
                "price": 22.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/大麦茶.png",
                "product_features": "安徽黄大麦炒香现煮，麦香浓郁，清热利湿，生津止渴。无咖啡因，适合全年龄段饮用。",
                "objective_analysis": "大麦≥12g/杯；焙炒挥发物浓度≥0.35g/杯；饮后口腔清新率主观评分＞85%。",
                "drinking_suggestions": "建议常温或温饮，适合三餐搭配；口干、口气重、喜饮浓茶人群可替代绿茶使用。",
                "ingredients": "纯净水、炒大麦",
                "origin": "大麦（安徽宿州）\n纯净水（湖北武汉）",
                "specifications": "净含量：330ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "口干口苦、喜饮冷饮、肠胃湿热者"
            },
            # 35. 茉莉花茶
            {
                "name": "茉莉花茶",
                "description": "广西横县茉莉花与绿茶清香融合，花香沁人，入口清新不苦涩，提神醒脑，气质典雅型养生茶。",
                "price": 25.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/茉莉花茶.png",
                "product_features": "广西横县茉莉花与绿茶清香融合，花香沁人，入口清新不苦涩，提神醒脑，气质典雅型养生茶。",
                "objective_analysis": "茉莉花干≥2g/杯；绿茶≥4g，茶多酚≥0.3g/杯；挥发香气成分含量＞90%保持率。",
                "drinking_suggestions": "建议上午饮用，利于提神清心；不建议空腹饮用；肠胃敏感者请选温饮。",
                "ingredients": "纯净水、绿茶、茉莉花",
                "origin": "茉莉花（广西横县）\n绿茶（福建福鼎）\n纯净水（湖北武汉）",
                "specifications": "净含量：320ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "思绪繁杂、精神疲乏、工作压力大者"
            },
            # 36. 青柑普洱
            {
                "name": "青柑普洱",
                "description": "新会青柑搭配云南普洱，陈香柑韵融合，汤色红褐透亮，口感顺滑，润喉暖胃，适合日常养护脾胃。",
                "price": 28.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/青柑普洱.png",
                "product_features": "新会青柑搭配云南普洱，陈香柑韵融合，汤色红褐透亮，口感顺滑，润喉暖胃，适合日常养护脾胃。",
                "objective_analysis": "青柑皮≥3g/杯，挥发油保留率≥80%；普洱≥5g，茶褐素含量≥0.2g/杯；总多酚含量≥0.3g/杯。",
                "drinking_suggestions": "建议饭后饮用，助消食暖胃；体寒人群热饮更佳；不建议睡前饮用。",
                "ingredients": "纯净水、青柑皮、熟普洱茶叶",
                "origin": "青柑（广东新会）\n普洱茶（云南西双版纳）\n纯净水（湖北武汉）",
                "specifications": "净含量：330ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "脾胃虚寒、油腻饮食、长期应酬者"
            },
            # 37. 乌龙茶
            {
                "name": "乌龙茶",
                "description": "精选安溪铁观音，半发酵焙香，汤色金黄透亮，口感醇厚回甘，茶气十足。",
                "price": 24.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/乌龙茶.png",
                "product_features": "精选安溪铁观音，半发酵焙香，汤色金黄透亮，口感醇厚回甘，茶气十足。",
                "objective_analysis": "乌龙茶干叶≥5g/杯；茶多酚含量≥0.4g/杯；咖啡因约35mg/杯。",
                "drinking_suggestions": "午后或晚餐后一小时饮用，助消化；不建议空腹或睡前饮用；肠胃敏感人群适量饮用。",
                "ingredients": "纯净水、乌龙茶叶",
                "origin": "乌龙茶（福建安溪）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "消化不良、口腔异味、饭后疲乏者"
            },
            # 38. 绿茶
            {
                "name": "绿茶",
                "description": "明前龙井低温冲泡，色绿清澈，味道清鲜回甘，保留更多天然抗氧成分。",
                "price": 23.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/绿茶.png",
                "product_features": "明前龙井低温冲泡，色绿清澈，味道清鲜回甘，保留更多天然抗氧成分。",
                "objective_analysis": "绿茶≥4g/杯；茶多酚≥0.5g/杯；抗氧化能力评分（主观测试）＞90%。",
                "drinking_suggestions": "适合上午饮用，提神解腻；空腹饮用可能引起胃部不适；夏季冷饮尤佳，冬季建议温饮。",
                "ingredients": "纯净水、绿茶叶",
                "origin": "绿茶（浙江杭州）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "口干口苦、压力大、体内偏热人群"
            },
            # 39. 红茶
            {
                "name": "红茶",
                "description": "武夷正山小种，浓香型红茶，低温萃取带有天然松烟香气，暖胃不燥，适合体寒调理。",
                "price": 25.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/红茶.png",
                "product_features": "武夷正山小种，浓香型红茶，低温萃取带有天然松烟香气，暖胃不燥，适合体寒调理。",
                "objective_analysis": "红茶≥5g/杯；茶黄素含量≥0.25g/杯；咖啡因约30mg/杯。",
                "drinking_suggestions": "推荐早餐后或下午饮用；女性经期可作为温补饮品；不建议睡前饮用。",
                "ingredients": "纯净水、红茶叶",
                "origin": "红茶（福建武夷山）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "体寒怕冷、消化缓慢、情绪低落者"
            },
            # 40. 黑乌龙
            {
                "name": "黑乌龙",
                "description": "台湾冻顶乌龙经重焙发酵，油切清爽，带焦糖香气，色深味浓，适合搭配重口餐食。",
                "price": 26.00,
                "category": "养生茶",
                "image_url": "/static/images/products/清茶坊/黑乌龙.png",
                "product_features": "台湾冻顶乌龙经重焙发酵，油切清爽，带焦糖香气，色深味浓，适合搭配重口餐食。",
                "objective_analysis": "黑乌龙≥5g/杯；茶多酚含量≥0.45g/杯；油脂乳化指数（模拟实验）提升约25%。",
                "drinking_suggestions": "建议饭后饮用，帮助分解油脂；不宜空腹饮用，易刺激胃酸；日饮不超2杯。",
                "ingredients": "纯净水、黑乌龙茶叶",
                "origin": "黑乌龙（台湾南投）\n纯净水（湖北武汉）",
                "specifications": "净含量：300ml\n包装方式：食品级透明塑料杯（PP材质）＋封膜密封盖\n保质期：常温2小时内，冷藏不超过24小时",
                "suitable_crowd": "油腻饮食频繁者、减脂期间、爱喝浓茶者"
            }
        ]
        
        for product_data in products:
            product = Product(**product_data)
            db.session.add(product)
        
        db.session.commit()
        print('数据库初始化完成！')
        print(f'已创建 {len(products)} 个测试商品')
        print('管理员账户：admin / admin123')
        print('测试用户账户：test / test123')

if __name__ == '__main__':
    init_db() 