
cityList = {'北京': 'bj', '广州': 'gz', '上海': 'sh', '天津': 'tj', '深圳': 'sz', '重庆': 'cq', '南京': 'nj', '武汉': 'wh', '成都': 'cd', '西安': 'xa', '郑州': 'zz', '大连': 'dl', '苏州': 'su', '济南': 'jn', '青岛': 'qd', '哈尔滨': 'hrb', '杭州': 'hz', '宁波': 'nb', '厦门': 'xm', '沈阳': 'sy', '东莞': 'dg', '长春': 'cc', '长沙': 'cs', '海口': 'hn', '太原': 'ty', '三亚': 'sanya', '南宁': 'nn', '石家庄': 'sjz', '阿坝': 'aba', '阿克苏': 'akesu', '阿拉尔': 'alaer', '阿拉善': 'alashan', '阿勒泰': 'aletai', '阿里': 'ali', '安康': 'ankang', '安庆': 'anqing', '鞍山': 'anshan', '安顺': 'anshun', '安阳': 'anyang', '澳门': 'aomen', '白城': 'baicheng', '百色': 'baise', '白山': 'baishan', '白银': 'baiyin', '保定': 'baoding', '宝鸡': 'baoji', '保山': 'baoshan', '包头': 'baotou', '巴彦淖尔': 'bayannaoer', '巴音郭楞': 'bayinguoleng', '巴中': 'bazhong', '北海': 'beihai', '蚌埠': 'bengbu', '本溪': 'benxi', '毕节': 'bijie', '滨州': 'binzhou', '博尔塔拉': 'boertala', '亳州': 'bozhou', '沧州': 'cangzhou', '常德': 'changde', '昌都': 'changdu', '昌吉': 'changji', '常熟': 'changshu', '长治': 'changzhi', '常州': 'changzhou', '巢湖': 'chaohu', '朝阳市': 'chaoyang', '潮州': 'chaozhou', '承德': 'chengde', '郴州': 'chenzhou', '赤峰': 'chifeng', '池州': 'chizhou', '崇左': 'chongzuo', '楚雄': 'chuxiong', '滁州': 'chuzhou', '慈溪': 'cixi', '大理': 'dali', '丹东': 'dandong', '儋州': 'danzhou', '大庆': 'daqing', '大同': 'datong', '大兴安岭': 'daxinganling', '达州': 'dazhou', '德宏': 'dehong', '德阳': 'deyang', '德州': 'dezhou', '定西': 'dingxi', '迪庆': 'diqing', '东营': 'dongying', '鄂尔多斯': 'eerduosi', '恩施': 'enshi', '鄂州': 'ezhou', '防城港': 'fangchenggang', '佛山': 'foshan', '抚顺': 'fushun', '阜新': 'fuxin', '阜阳': 'fuyang', '福州': 'fz', '抚州': 'jxfuzhou', '莆田': 'putian', '甘南': 'gannan', '赣州': 'ganzhou', '甘孜': 'ganzi', '广安': 'guangan', '广元': 'guangyuan', '贵港': 'guigang', '桂林': 'gl', '贵阳': 'gy', '果洛': 'guoluo', '固原': 'guyuan', '海北': 'haibei', '海东': 'haidong', '海南州': 'hainanzhou', '海西': 'haixi', '哈密': 'hami', '邯郸': 'handan', '汉中': 'hanzhong', '鹤壁': 'hebi', '河池': 'hechi', '合肥': 'hf', '鹤岗': 'hegang', '黑河': 'heihe', '衡水': 'hengshui', '衡阳': 'hengyang', '和田': 'hetian', '河源': 'heyuan', '菏泽': 'heze', '贺州': 'hezhou', '红河': 'honghe', '淮安': 'huaian', '淮北': 'huaibei', '怀化': 'huaihua', '淮南': 'huainan', '黄冈': 'huanggang', '黄南': 'huangnan', '黄山': 'huangshan', '黄石': 'huangshi', '呼和浩特': 'nmg', '惠州': 'huizhou', '葫芦岛': 'huludao', '呼伦贝尔': 'hulunbeier', '湖州': 'huzhou', '佳木斯': 'jiamusi', '吉安': 'jian', '江门': 'jiangmen', '胶州': 'jiaozhou', '焦作': 'jiaozuo', '嘉兴': 'jiaxing', '嘉峪关': 'jiayuguan', '揭阳': 'jieyang', '吉林': 'jilin', '即墨': 'jimo', '金昌': 'jinchang', '晋城': 'jincheng', '景德镇': 'jingdezhen', '荆门': 'jingmen', '荆州': 'jingzhou', '金华': 'jinhua', '济宁': 'jining', '晋中': 'jinzhong', '锦州': 'jinzhou', '九江': 'jiujiang', '酒泉': 'jiuquan', '鸡西': 'jixi', '济源': 'jiyuan', '开封': 'kaifeng', '喀什': 'kashi', '克拉玛依': 'kelamayi', '克孜勒苏': 'kezilesu', '库尔勒': 'kuerle', '昆明': 'km', '昆山': 'kunshan', '来宾': 'laibin', '莱芜': 'laiwu', '廊坊': 'langfang', '兰州': 'lz', '拉萨': 'xz', '乐山': 'leshan', '凉山': 'liangshan', '连云港': 'lianyungang', '聊城': 'liaocheng', '辽阳': 'liaoyang', '辽源': 'liaoyuan', '丽江': 'lijiang', '临沧': 'lincang', '临汾': 'linfen', '临夏': 'linxia', '临沂': 'linyi', '林芝': 'linzhi', '丽水': 'lishui', '六盘水': 'liupanshui', '柳州': 'liuzhou', '陇南': 'longnan', '龙岩': 'longyan', '娄底': 'loudi', '六安': 'luan', '漯河': 'luohe', '洛阳': 'luoyang', '泸州': 'luzhou', '吕梁': 'lvliang', '马鞍山': 'maanshan', '茂名': 'maoming', '眉山': 'meishan', '梅州': 'meizhou', '绵阳': 'mianyang', '牡丹江': 'mudanjiang', '南昌': 'nc', '南充': 'nanchong', '南平': 'nanping', '南通': 'nantong', '南阳': 'nanyang', '那曲': 'naqu', '内江': 'neijiang', '宁德': 'ningde', '怒江': 'nujiang', '盘锦': 'panjin', '攀枝花': 'panzhihua', '平顶山': 'pingdingshan', '平凉': 'pingliang', '萍乡': 'pingxiang', '郫县': 'pixian', '普洱': 'puer', '濮阳': 'puyang', '黔东南': 'qiandongnan', '潜江': 'qianjiang', '黔南': 'qiannan', '黔西南': 'qianxinan', '庆阳': 'qingyang', '清远': 'qingyuan', '秦皇岛': 'qinhuangdao', '钦州': 'qinzhou', '琼海': 'qh', '齐齐哈尔': 'qiqihaer', '七台河': 'qitaihe', '泉州': 'quanzhou', '曲靖': 'qujing', '衢州': 'quzhou', '日喀则': 'rikaze', '日照': 'rizhao', '三门峡': 'sanmenxia', '三明': 'sanming', '商洛': 'shangluo', '商丘': 'shangqiu', '上饶': 'shangrao', '山南': 'shannan', '汕头': 'shantou', '汕尾': 'shanwei', '韶关': 'shaoguan', '绍兴': 'shaoxing', '邵阳': 'shaoyang', '神农架': 'shennongjia', '石河子': 'shihezi', '十堰': 'shiyan', '石嘴山': 'shizuishan', '双流': 'shuangliu', '双鸭山': 'shuangyashan', '朔州': 'shuozhou', '四平': 'siping', '松原': 'songyuan', '绥化': 'suihua', '遂宁': 'suining', '随州': 'suizhou', '宿迁': 'suqian', '宿州': 'ahsuzhou', '泰州': 'jstaizhou', '塔城': 'tacheng', '泰安': 'taian', '唐山': 'tangshan', '天门': 'tianmen', '天水': 'tianshui', '铁岭': 'tieling', '铜川': 'tongchuan', '通化': 'tonghua', '通辽': 'tongliao', '铜陵': 'tongling', '铜仁': 'tongren', '吐鲁番': 'tulufan', '图木舒克': 'tumushuke', '台州': 'zjtaizhou', '潍坊': 'weifang', '威海': 'wei', '渭南': 'weinan', '文山': 'wenshan', '温州': 'wenzhou', '乌海': 'wuhai', '芜湖': 'wuhu', '五家渠': 'wujiaqu', '乌兰察布': 'wulanchabu', '乌鲁木齐': 'xj', '武威': 'wuwei', '无锡': 'wx', '五指山': 'wuzhishan', '吴忠': 'wuzhong', '梧州': 'wuzhou', '香港': 'xianggang', '湘潭': 'xiangtan', '湘西': 'xiangxi', '襄阳': 'xiangyang', '咸宁': 'xianning', '仙桃': 'xiantao', '咸阳': 'xianyang', '孝感': 'xiaogan', '锡林郭勒': 'xilinguole', '兴安': 'xingan', '邢台': 'xingtai', '西宁': 'xn', '新乡': 'xinxiang', '信阳': 'xinyang', '新余': 'xinyu', '忻州': 'xinzhou', '西双版纳': 'xishuangbanna', '宣城': 'xuancheng', '许昌': 'xuchang', '徐州': 'xuzhou', '伊春': 'hljyichun', '宜春': 'jxyichun', '榆林': 'sxyulin', '雅安': 'yaan', '延安': 'yanan', '延边': 'yanbian', '盐城': 'yancheng', '阳江': 'yangjiang', '阳泉': 'yangquan', '扬州': 'yangzhou', '烟台': 'yantai', '宜宾': 'yibin', '宜昌': 'yichang', '伊犁': 'yili', '银川': 'yc', '营口': 'yingkou', '鹰潭': 'yingtan', '义乌': 'yiwu', '益阳': 'yiyang', '永州': 'yongzhou', '岳阳': 'yueyang', '玉林': 'gxyulin', '运城': 'yuncheng', '云浮': 'yunfu', '玉树': 'yushu', '玉溪': 'yuxi', '枣庄': 'zaozhuang', '张家界': 'zhangjiajie', '张家口': 'zhangjiakou', '张掖': 'zhangye', '漳州': 'zhangzhou', '湛江': 'zhanjiang', '肇庆': 'zhaoqing', '昭通': 'zhaotong', '镇江': 'zhenjiang', '中山': 'zhongshan', '中卫': 'zhongwei', '周口': 'zhoukou', '舟山': 'zhoushan', '珠海': 'zhuhai', '驻马店': 'zhumadian', '株洲': 'zhuzhou', '淄博': 'zibo', '自贡': 'zigong', '资阳': 'ziyang', '遵义': 'zunyi'}