# -*- coding: utf-8 -*-
"""
无人机与飞行系统高精宣传画册 - 50P完整编目数据 (23专题 精准匹配46张截图)
每个专题严格对应 2 张真实图片 (1张正面大图 + 1张背面副图)，无任何占位图
"""

ALBUM_META = {
    "title_zh": "未来飞行 · 航空航天无人系统工程画册",
    "title_en": "AEROSPACE DYNAMICS // ADVANCED UAV & PROPULSION SYSTEMS",
    "subtitle": "工业级飞行平台 · 战术飞行器 · 复合翼系统 · 核心航电动力工程解构",
    "edition": "2026-2027 GLOBAL EDITION // FLIGHT SPECIFICATION BLUEPRINT",
    "confidential_code": "DOC.ID: AGY-AERO-2026-V50",
    "total_pages": 50
}

PRODUCTS = [
    {
        "id": "UNIT-01",
        "category_zh": "战略察打系列",
        "category_en": "MALE ARMED STRIKE UAV",
        "name_zh": "AERO-REAPER 3000 // 中空长航时察打一体无人机",
        "name_en": "MALE Armed Reconnaissance & Strike UAV",
        "code": "SYS.ID: ULS-3000R",
        "tagline": "远距超视距巡逻 · 昼夜全天候精确制导打击 · 卫星中继全自主作战",
        "desc": "AERO-REAPER 3000采用经典高升阻比上单翼与V形尾翼气动布局，机身大面积采用高模量碳纤维预浸料整体热压成型。集成大口径多光谱光电/红外转塔与合成孔径雷达（SAR），机翼下方配备4个标准化重载通用外挂点，支持挂载空地微型制导导弹及精确制导滑翔炸弹。搭载重油涡轮增压发动机与低噪声后推螺旋桨，具备长达36小时的超长滞空巡航时间与卫星视距外中继自主控制能力。",
        "highlights": [
            {"title": "超长滞空耐力", "detail": "大展弦比机翼配合燃油经济性动力链，支持单次起降36小时不间断高空巡逻。"},
            {"title": "多载荷智能融合", "detail": "标配红外热成像、激光测距指示器及毫米波SAR雷达，支持复杂气象下超视距侦搜。"},
            {"title": "标准化武器挂架", "detail": "4个标准航空挂载导轨，最大外挂载荷达450kg，兼具精确侦察与定点压制能力。"},
            {"title": "全自主卫星通信", "detail": "三轴自稳Ku/Ka波段卫星通信天线，支持2000公里超视距低延迟数据传输。"}
        ],
        "specs": [
            {"label": "机身翼展", "value": "18.5 m"},
            {"label": "机身全长", "value": "9.2 m"},
            {"label": "最大起飞重量", "value": "1850 kg"},
            {"label": "有效载荷能力", "value": "480 kg"},
            {"label": "最大巡航速度", "value": "260 km/h"},
            {"label": "实用升限", "value": "9500 m"},
            {"label": "最大续航时间", "value": "36 hrs"},
            {"label": "通信数据链路", "value": "Ku/Ka SATCOM + 双冗余视距微波"}
        ],
        "front_image": "ScreenShot_2026-10-18_011033_050.png",
        "front_caption": "AERO-REAPER 3000 侧后45°外挂精确打击弹药全貌渲染",
        "back_sub_image": "ScreenShot_2026-10-18_015952_347.png",
        "back_sub_caption": "正视气动流线截面与微波卫星天线机头工程图"
    },
    {
        "id": "UNIT-02",
        "category_zh": "特种突击系列",
        "category_en": "FUTURE VTOL ASSAULT",
        "name_zh": "VALKYRIE // 未来重型垂直起降隐身武装突击旋翼机",
        "name_en": "Heavy Tactical Stealth VTOL Gunship",
        "code": "SYS.ID: VTOL-G90",
        "tagline": "多重升力复合推进 · 低雷达散射外形 · 强火力全域低空突防",
        "desc": "VALKYRIE融合了多重共轴多旋翼高推力升力系统与机身推进短翼，机头搭载机腹隐藏式多管重型加特林航空机炮及前向光电瞄准具。整机采用菱形折面隐身气动外形与雷达吸波涂层，有效压缩雷达与红外特征。机体内部集成分布式飞控计算机与自适应气动倾角控制律，能够在狭窄峡谷与复杂城市战场环境中实现极速悬停与横向超机动突袭。",
        "highlights": [
            {"title": "低可探测隐身修形", "detail": "倾斜多面体机身与雷达散射内倾座舱罩设计，全向RCS截面优于传统武装直升机70%。"},
            {"title": "重型共轴旋翼矩阵", "detail": "多叶高刚性碳复合材料主旋翼，结合翼下增压涵道，实现超大起飞推重比与抗过载性。"},
            {"title": "机腹收纳式航炮系统", "detail": "配备30mm多管旋转机关炮，支持全自动雷达伺服火控跟踪与瞬时大倾角平飞射击。"},
            {"title": "城市复杂空域突防", "detail": "三维激光雷达全向地形测绘与主动避障雷达，支持在复杂建筑群内全自主低空穿透。"}
        ],
        "specs": [
            {"label": "旋翼主直径", "value": "12.8 m"},
            {"label": "机身全长", "value": "14.2 m"},
            {"label": "最大起飞重量", "value": "5600 kg"},
            {"label": "巡航平飞时速", "value": "380 km/h"},
            {"label": "最大突防速度", "value": "440 km/h"},
            {"label": "作战作战半径", "value": "650 km"},
            {"label": "内置载荷仓容积", "value": "3.8 m³"},
            {"label": "动力推进架构", "value": "双轴混动涡轮发动机 + 电驱动矢量旋翼"}
        ],
        "front_image": "ScreenShot_2026-10-18_004138_699.png",
        "front_caption": "VALKYRIE 重型突击旋翼机三维光影工程模型展示",
        "back_sub_image": "ScreenShot_2026-10-18_021235_318.png",
        "back_sub_caption": "特种双向动力旋翼构型与矢量倾转短舱应力透视"
    },
    {
        "id": "UNIT-03",
        "category_zh": "复合翼巡检系列",
        "category_en": "HYBRID VTOL PLATFORM",
        "name_zh": "AERO-VTOL HORIZON-X // 双尾撑垂直起降长航时无人机",
        "name_en": "Twin-Boom Long-Endurance Hybrid VTOL UAV",
        "code": "SYS.ID: VTOL-HX4",
        "tagline": "四旋翼垂直起落 · 固定翼高效平飞 · 零跑道依赖全自主巡检",
        "desc": "AERO-VTOL HORIZON-X采用成熟高效的“四旋翼起降+后推巡航”混合动力架构与高刚度碳纤维双尾撑气动布局。无需任何跑道或弹射架，即可在山地、森林、舰船等狭小非平整场地垂直起飞并迅速切换至高速巡航模式。机翼采用大展弦比微下反设计，机身前部预留大容量快拆载荷舱，可搭载五镜头正射倾斜航测相机、机载激光雷达（LiDAR）或气体检测传感器。",
        "highlights": [
            {"title": "零跑道全自主起降", "detail": "四旋翼垂直平稳起降，固定翼极速平飞巡检，完美解决复杂地形受限痛点。"},
            {"title": "双尾撑稳定结构", "detail": "一体化碳纤维复合材料双尾撑，带来卓越的风洞抗扭强度与抗风颤性能。"},
            {"title": "模块化快拆机翼", "detail": "免工具滑轨快锁卡扣结构，5分钟内完成从装箱到组装部署，单人即可轻松操作。"},
            {"title": "多传感器扩展舱", "detail": "标准化供电与数据总线接口，兼容激光雷达、倾斜摄影、红外吊舱等多样化任务。"}
        ],
        "specs": [
            {"label": "机身翼展", "value": "3200 mm"},
            {"label": "机身机长", "value": "1800 mm"},
            {"label": "空机重量", "value": "12.5 kg"},
            {"label": "最大起飞全重", "value": "26.0 kg"},
            {"label": "任务载荷", "value": "5.5 kg"},
            {"label": "经济巡航速度", "value": "90 ~ 110 km/h"},
            {"label": "纯电巡航续航", "value": "180 min"},
            {"label": "抗风能力", "value": "起降 6 级 / 巡航 7 级"}
        ],
        "front_image": "ScreenShot_2026-10-18_021019_041.png",
        "front_caption": "HORIZON-X 复合翼双尾撑整机轻量化曲面造型",
        "back_sub_image": "ScreenShot_2026-10-18_002321_755.png",
        "back_sub_caption": "复合翼机翼俯视气动构型与垂直起降撑杆布局"
    },
    {
        "id": "UNIT-04",
        "category_zh": "复合翼重载系列",
        "category_en": "HYBRID CARGO VTOL",
        "name_zh": "HYBRID-CARGO VTOL-350 // 双尾撑大载荷复合翼货运物流机",
        "name_en": "Twin-Boom Heavy Hybrid VTOL Cargo Aircraft",
        "code": "SYS.ID: HCAR-350",
        "tagline": "宽体腹部快卸货仓 · 4+1油电动力混合 · 偏远海岛支线急送",
        "desc": "HYBRID-CARGO VTOL-350专为高价值冷链药品、海岛快件及山区偏远站点点对点低空货运而打造。机身拥有规整宽大的腹部中央货舱，支持标准物流箱模块化快速装卸。机翼四点垂直起降电机负责平稳离地与精准定点着陆，机尾由大马力高推力发动机驱动高效推力桨进行平飞巡航。采用双尾撑结构与下垂端板小翼，在大载重起飞条件下仍保持优良的纵向稳定性。",
        "highlights": [
            {"title": "宽体快拆标准化货仓", "detail": "50L方形规整货舱空间，配备电控防盗货舱门与温湿度实时传感器，全程数字追溯。"},
            {"title": "4+1动力全闭环切换", "detail": "自主飞控无缝管理垂直升力转平飞推力，过渡阶段平稳无掉高，保障易碎物资安全。"},
            {"title": "全自动航线无人值守", "detail": "配合智能自动起降机场机巢，实现全自动换电、货物自动投放、全自动返航。"},
            {"title": "全天候防冰与防雨", "detail": "关键皮托管电加热防冻，机翼前缘防雨蚀涂层，保障海上与高寒多雾天气安全运作。"}
        ],
        "specs": [
            {"label": "主翼翼展", "value": "3500 mm"},
            {"label": "整机长度", "value": "2100 mm"},
            {"label": "空机重量", "value": "16.0 kg"},
            {"label": "最大起飞全重", "value": "35.0 kg"},
            {"label": "有效商业载荷", "value": "8.0 ~ 10.0 kg"},
            {"label": "巡航速度", "value": "100 ~ 125 km/h"},
            {"label": "配送作业半径", "value": "100 km (单程直达)"},
            {"label": "动力组合", "value": "4轴垂直电驱动 + 1轴巡航混动推进"}
        ],
        "front_image": "ScreenShot_2026-10-18_021053_273.png",
        "front_caption": "HYBRID-CARGO VTOL-350 复合翼重载机身三维模型",
        "back_sub_image": "ScreenShot_2026-10-18_005239_831.png",
        "back_sub_caption": "复合翼机翼短舱四旋翼起降动力撑杆装配特写"
    },
    {
        "id": "UNIT-05",
        "category_zh": "农业重载系列",
        "category_en": "SMART AGRICULTURE",
        "name_zh": "AGRI-TITAN HEX-60 // 智能六旋翼精准农业植保喷雾机",
        "name_en": "Precision Hexacopter Agricultural Spraying System",
        "code": "SYS.ID: AGRI-60H",
        "tagline": "60升超大容量药箱 · 双离心雾化智能喷盘 · 毫米波全向仿地雷达",
        "desc": "AGRI-TITAN HEX-60专为大规模现代化农林植保作业设计。整机采用六轴对称大轴距桁架布局与折叠碳纤机臂，展开工作状态稳固坚实，折叠后运输体积压缩65%。标配60升快拆大容量药箱与双高压隔膜水泵，配备前后双喷杆阵列及高速离心雾化喷头，支持药液微米级粒径调节与风场强效压下。搭载前后双向避障雷达与下视仿地雷达，在梯田、坡地及果园等复杂地形中实现厘米级精准贴地仿地自主飞行。",
        "highlights": [
            {"title": "60L快拆防晃药箱", "detail": "大容量水平低重心药箱，内置多级防波隔板，有效抑制大幅度飞行中的药液晃动。"},
            {"title": "强风场离心喷雾", "detail": "六旋翼强劲下洗气流精准将50-300微米细雾压送至作物根部，药效利用率提升50%。"},
            {"title": "全地形厘米级仿地", "detail": "高频毫米波雷达实时测量相对作物冠层高度，自适应保持恒定喷洒距离与航迹。"},
            {"title": "IP67级全机水洗", "detail": "全密封三防航电与动力仓，作业完毕后可直接用高压水枪全机冲洗，耐农药腐蚀。"}
        ],
        "specs": [
            {"label": "轴距尺寸", "value": "2180 mm"},
            {"label": "药箱满载容积", "value": "60 L"},
            {"label": "空载作业重量", "value": "38.5 kg"},
            {"label": "最大作业全重", "value": "108 kg"},
            {"label": "有效作业喷幅", "value": "9.0 ~ 12.0 m"},
            {"label": "单小时喷洒效率", "value": "280 ~ 350 亩/小时"},
            {"label": "雷达感知系统", "value": "全向有源相控阵雷达 + 双目视觉"},
            {"label": "防护等级", "value": "全机 IP67 工业防水防尘"}
        ],
        "front_image": "ScreenShot_2026-10-18_010159_380.png",
        "front_caption": "AGRI-TITAN HEX-60 植保整机三维仿真带药箱视角",
        "back_sub_image": "ScreenShot_2026-10-18_010219_917.png",
        "back_sub_caption": "六旋翼展开机臂几何轴线与喷幅管路分布俯视图"
    },
    {
        "id": "UNIT-06",
        "category_zh": "重载运输系列",
        "category_en": "HEAVY UTILITY CARRIER",
        "name_zh": "TITAN-CARRIER H6 // 工业级模块化重载六旋翼运输平台",
        "name_en": "Modular Heavy-Duty Hexacopter Utility Platform",
        "code": "SYS.ID: HCAR-600",
        "tagline": "航空碳板矩阵中心舱 · 动力冗余单桨停转保全 · 重型物资精准投送",
        "desc": "TITAN-CARRIER H6是一款针对极限物流、山地物资运输、应急消防灭火及野外重型设备吊装设计的工业旗舰六旋翼平台。机身中心板采用多层3K高模量碳纤维板配合航空7075铝合金数控锁扣，具备极其优异的承重刚度与抗扭疲劳强度。六轴动力单元拥有单电机故障紧急容错算法，即使任意一个电机或螺旋桨在空中受损失效，剩余五个动力轴依然能够平稳控制姿态并安全迫降返航。",
        "highlights": [
            {"title": "单桨失效容错控制", "detail": "先进的六轴非对称动力重构算法，空中突发单轴停转时毫秒级平稳接管姿态。"},
            {"title": "模块化箱体挂载", "detail": "机腹导轨兼容医疗急救箱、消防灭火弹发射箱、物流标准箱及多波段通信中继舱。"},
            {"title": "高载荷结构拓扑优化", "detail": "经有限元FEA应力拓扑优化的中心板与一体折叠机臂接头，承重安全系数达3.5倍。"},
            {"title": "智能航线自主抛投", "detail": "集成激光测距与电控投掷钩，达到预定目标经纬度与高度后全自动精准无损脱钩。"}
        ],
        "specs": [
            {"label": "对角线轴距", "value": "1650 mm"},
            {"label": "最大起飞全重", "value": "45.0 kg"},
            {"label": "最大纯有效载重", "value": "20.0 kg"},
            {"label": "满载作业续航", "value": "28 min"},
            {"label": "半载巡航续航", "value": "42 min"},
            {"label": "动力电池系统", "value": "14S 30000mAh 半固态高能锂电池"},
            {"label": "最大上升/下降速度", "value": "6 m/s / 5 m/s"},
            {"label": "结构材质", "value": "东丽 T700 碳纤维 + 7075-T6 航空铝合金"}
        ],
        "front_image": "ScreenShot_2026-10-18_020505_942.png",
        "front_caption": "TITAN-CARRIER H6 重载运输作业飞行器整机渲染",
        "back_sub_image": "ScreenShot_2026-10-18_015402_876.png",
        "back_sub_caption": "六旋翼高强度模块化机身中心板与折叠臂CNC连接件细节"
    },
    {
        "id": "UNIT-07",
        "category_zh": "工业巡检系列",
        "category_en": "INDUSTRIAL INSPECTION",
        "name_zh": "HEXA-PATROL 650 // 工业六旋翼多功能空中巡检作业平台",
        "name_en": "Industrial Hexacopter Multi-Task Inspection Platform",
        "code": "SYS.ID: HPAT-650",
        "tagline": "集成化防雨航电舱 · 多孔载荷扩展挂钩 · 复杂工业场景稳定作业",
        "desc": "HEXA-PATROL 650专为城市公共安全、风电光伏巡检、环保水质采样及大型桥梁缺陷扫描量身设计。整机配备低风阻全天候中央防水电控仓与双侧快拆电池托盘，下部设有大承载载荷固定支架，可快速安装多光谱相机、气体采样器或喊话探照一体机。六旋翼充沛的推重比提供了极高的横风抵抗冗余，即便在桥下或高耸风机附近遭遇强剪切风，依然能够保持毫米级稳定悬停。",
        "highlights": [
            {"title": "全密封中央任务舱", "detail": "防护等级达到IP55，有效防范突发阵雨、工业粉尘及盐雾侵蚀，保障核心航电无忧。"},
            {"title": "风机光伏专用航线", "detail": "飞控内置三维环绕与贴面扫描航线规划，实现沿风力叶片全自动近距离高清巡检。"},
            {"title": "多载荷快换电控总线", "detail": "标配标准PWM、CAN与高压供电接口，5秒内完成倾斜相机与喊话探照灯快速轮换。"},
            {"title": "低噪声折叠动力组", "detail": "匹配特殊降噪折叠碳纤维螺旋桨，城区夜间巡检时声学噪音控制在65分贝以下。"}
        ],
        "specs": [
            {"label": "对角轴距", "value": "1150 mm"},
            {"label": "空机重量", "value": "5.6 kg"},
            {"label": "最大起飞全重", "value": "15.0 kg"},
            {"label": "额定任务载荷", "value": "4.0 kg"},
            {"label": "最大抗风等级", "value": "6 级 (13.8 m/s)"},
            {"label": "悬停作业时间", "value": "45 min (2kg负载)"},
            {"label": "巡检经济航速", "value": "40 km/h"},
            {"label": "遥测遥控距离", "value": "10 km 高清低延迟数字图传"}
        ],
        "front_image": "ScreenShot_2026-10-18_004446_698.png",
        "front_caption": "HEXA-PATROL 650 六旋翼工业巡检作业平台带机载任务箱",
        "back_sub_image": "ScreenShot_2026-10-18_002442_401.png",
        "back_sub_caption": "全包围环形防撞保护环四旋翼高安全性机架"
    },
    {
        "id": "UNIT-08",
        "category_zh": "高精测绘系列",
        "category_en": "PRECISION SURVEYING",
        "name_zh": "SKY-SURVEYOR 400 // 工业级四旋翼高精度测绘巡检无人机",
        "name_en": "Industrial Survey & Mapping Quadcopter",
        "code": "SYS.ID: SS-400X",
        "tagline": "RTK厘米级定位 · 三轴增稳双光吊舱 · 工业级全天候高防护机身",
        "desc": "SKY-SURVEYOR 400是一款专为电力巡检、地理测绘、城市规划与安防应急量身定制的高可靠性四旋翼作业平台。机身核心骨架采用高抗扭碳纤维方管与航空铝数控加工连接件，具备卓越的结构刚性。顶部标配双天线RTK差分导航模块，具备极强的抗电磁干扰性能，支持在高压输电线与变电站强磁环境下稳定定高定点。下部搭载标准快拆接口，支持无缝更换30倍变焦热成像双光云台或机载激光雷达。",
        "highlights": [
            {"title": "双天线抗磁干扰RTK", "detail": "双天线差分定角技术，在强电磁辐射电网及金属塔架旁依然能够精准锁定航线。"},
            {"title": "全温区智能加热电池", "detail": "自加热智能双电池备份系统，支持在-20℃极寒至50℃酷暑环境下稳定安全放电。"},
            {"title": "AI目标识别跟踪", "detail": "机载神经网络加速芯片，实时识别电力绝缘子破损、电缆引流线发热等典型缺陷。"},
            {"title": "轻量便携一体折叠", "detail": "旋翼机臂采用双向反折机构，收纳后单人可单手提行或直接装入SUV后备箱。"}
        ],
        "specs": [
            {"label": "对角线轴距", "value": "890 mm"},
            {"label": "整机整备质量", "value": "4.8 kg"},
            {"label": "最大有效负载", "value": "2.5 kg"},
            {"label": "无载续航时间", "value": "55 min"},
            {"label": "满载作业续航", "value": "38 min"},
            {"label": "定位精度", "value": "水平 1cm+1ppm / 垂直 1.5cm+1ppm"},
            {"label": "图传测控距离", "value": "15 km (FCC认证高清图传)"},
            {"label": "工作温度范围", "value": "-20℃ ~ +55℃"}
        ],
        "front_image": "ScreenShot_2026-10-18_004254_919.png",
        "front_caption": "SKY-SURVEYOR 400 工业巡检四旋翼三维模型",
        "back_sub_image": "ScreenShot_2026-10-18_020732_614.png",
        "back_sub_caption": "特种远程双天线四旋翼通信巡航构型工程图"
    },
    {
        "id": "UNIT-09",
        "category_zh": "飞翼测绘系列",
        "category_en": "STEALTH FLYING WING",
        "name_zh": "PHANTOM WING-800 // 飞翼布局长航时高空遥感无人机",
        "name_en": "Flying-Wing Long-Endurance Remote Sensing UAV",
        "code": "SYS.ID: FW-800P",
        "tagline": "纯飞翼无尾气动布局 · 极致超低空气阻力 · 广域大面积正射航测",
        "desc": "PHANTOM WING-800基于纯飞翼空气动力学流线设计，彻底消除传统机身与尾翼带来的寄生阻力与诱导阻力，全机身均作为升力面提供卓越的气动效率。采用超高强度凯夫拉与碳纤维复合三明治机翼，机头集成超低风阻防护光学视窗，机尾搭载静音低震动后推动力总成。在同等电池容量下，飞翼布局相比传统构型航程提升超过40%，是超长距离石油管道巡视与边防巡逻的理想平台。",
        "highlights": [
            {"title": "极致气动升阻比", "detail": "翼身融合设计使全机升阻比高达18.5，显著降低高速巡航功耗，航程大幅延伸。"},
            {"title": "低雷达/红外特征", "detail": "连续平滑机身曲线与嵌入式发动机进排气设计，大幅降低声学与雷达被探测概率。"},
            {"title": "高精度惯导直驱", "detail": "差分GNSS+高精度MEMS惯性导航单元，确保超长距离巡航中的毫米级姿态控制。"},
            {"title": "大开间中段机舱", "detail": "机翼中心段宽阔内舱，提供充沛的电池配重空间与隔振精密航电安装位。"}
        ],
        "specs": [
            {"label": "机翼翼展", "value": "2400 mm"},
            {"label": "机翼面积", "value": "0.78 m²"},
            {"label": "最大起飞重量", "value": "7.8 kg"},
            {"label": "任务载荷", "value": "1.8 kg"},
            {"label": "巡航速度", "value": "75 ~ 95 km/h"},
            {"label": "失速速度", "value": "38 km/h"},
            {"label": "最大航程", "value": "240 km"},
            {"label": "回收方式", "value": "深失速伞降 / 机腹滑擦着陆"}
        ],
        "front_image": "ScreenShot_2026-10-18_004351_191.png",
        "front_caption": "PHANTOM WING-800 纯飞翼气动曲面 CAD 渲染视角",
        "back_sub_image": "ScreenShot_2026-10-18_003115_044.png",
        "back_sub_caption": "大展弦比轻质巡航滑翔机身与高效后推推进构型"
    },
    {
        "id": "UNIT-10",
        "category_zh": "串列双翼系列",
        "category_en": "TANDEM-WING VTOL",
        "name_zh": "AERO-TANDEM VTOL-II // 串列双机翼垂直起降巡查无人机",
        "name_en": "Tandem-Wing Hybrid VTOL UAV System",
        "code": "SYS.ID: TDM-200V",
        "tagline": "前后串列双翼抗紊流布局 · 紧凑机身大升力 · 高原与海上强风适航",
        "desc": "AERO-TANDEM VTOL-II采用了航空动力学中独特的串列双机翼构型，前后翼面协同产生升力，有效分散主梁应力集中，并在较小的总翼展下获得了极佳的有效升力面积。串列翼的气动耦合特性使得该机在遭遇阵风或高空紊流时具有天然的高阻尼恢复力矩，抗风与抗颠簸能力显著优于传统单机翼飞机。前后翼端配置4点垂直起降电机，机尾设置高效推进电机，完美兼顾山区林区复杂气候巡护。",
        "highlights": [
            {"title": "串列双翼气动增益", "detail": "前后翼气流耦合效应产生下洗流自适应调谐，升力系数提高25%，巡航姿态极其稳定。"},
            {"title": "机身结构紧凑高刚", "detail": "在相同起飞重量下较常规机型翼展缩短30%，极大提升野外机动性与收纳便捷度。"},
            {"title": "高原强紊流适应性", "detail": "独特的气动下洗自阻尼特性，在海拔4500米以上高原及高落差峡谷强风中表现优异。"},
            {"title": "油电双混动可选", "detail": "支持纯电版或油电混合动力包选装，混动版本最大留空巡检时间可达6.5小时。"}
        ],
        "specs": [
            {"label": "前翼/后翼翼展", "value": "2600 mm / 2800 mm"},
            {"label": "机身全长", "value": "1650 mm"},
            {"label": "最大起飞重量", "value": "18.0 kg"},
            {"label": "载荷仓承载力", "value": "4.0 kg"},
            {"label": "巡航速度", "value": "85 ~ 115 km/h"},
            {"label": "最大抗风等级", "value": "7 级 (16 m/s)"},
            {"label": "最大起飞海拔", "value": "5000 m"},
            {"label": "航程覆盖", "value": "350 km (纯电配置)"}
        ],
        "front_image": "ScreenShot_2026-10-18_015727_076.png",
        "front_caption": "AERO-TANDEM VTOL-II 串列双翼气动模型展示",
        "back_sub_image": "ScreenShot_2026-10-18_005747_692.png",
        "back_sub_caption": "经典T尾高稳定性固定翼机身下反角布局细节"
    },
    {
        "id": "UNIT-11",
        "category_zh": "战术侦察系列",
        "category_en": "TACTICAL RECON",
        "name_zh": "V-TAIL SCOUT-5 // 倒V尾长航时中程战术侦察无人机",
        "name_en": "Tactical Inverted V-Tail Reconnaissance UAV",
        "code": "SYS.ID: VTS-500",
        "tagline": "倒V尾阻力自消减 · 静音后推推进 · 战术侦察与激光照射引导",
        "desc": "V-TAIL SCOUT-5专为前线中程战术战情侦察、边境巡逻与定点目标跟踪而研发。创新的倒V形双垂尾结构兼具水平安定面与垂直安定面的双重功能，同时将发动机尾流与螺旋桨噪声向上反射遮蔽，极大降低地面声音被截获率。机腹前方设有低风阻收放式光电侦察球舱，支持白天高倍光学变焦与夜间长波红外热成像无缝切换，为地面指挥中枢提供连续稳定的战术全景视频流。",
        "highlights": [
            {"title": "倒V尾气动声学抑制", "detail": "倒V尾结构形成天然的声学屏障，显著衰减下向螺旋桨脉动声波，实现隐蔽侦查。"},
            {"title": "抗侧滑气动增稳", "detail": "复合舵面解耦控制律在横侧向提供更平顺的转弯侧倾响应，摄像画面无多余抖动。"},
            {"title": "微型双光吊舱集成", "detail": "集成30倍光学变焦相机与非制冷红外热成像传感器，5公里外清晰识别车辆牌号。"},
            {"title": "跑道起落/气动弹射", "detail": "支持传统硬化地面滑跑起降，亦可配置紧凑型车载弹射架进行野外无跑道发射。"}
        ],
        "specs": [
            {"label": "翼展全宽", "value": "3600 mm"},
            {"label": "机身长度", "value": "2100 mm"},
            {"label": "最大起飞重量", "value": "32.0 kg"},
            {"label": "有效设备载荷", "value": "6.0 kg"},
            {"label": "巡航速度", "value": "110 ~ 130 km/h"},
            {"label": "最大航速", "value": "165 km/h"},
            {"label": "巡航续航时间", "value": "8.5 hrs (汽油机) / 3.0 hrs (锂电)"},
            {"label": "作业半径", "value": "120 km (视距数字链路)"}
        ],
        "front_image": "ScreenShot_2026-10-18_020320_907.png",
        "front_caption": "V-TAIL SCOUT-5 战术侦察无人机三维外形透视图",
        "back_sub_image": "ScreenShot_2026-10-18_005830_638.png",
        "back_sub_caption": "倒V尾纯白测试机身与后推双叶桨流线侧视工程图"
    },
    {
        "id": "UNIT-12",
        "category_zh": "无人直升机系列",
        "category_en": "TACTICAL HELICOPTER",
        "name_zh": "CYBER-COPTER 700 // 工业级重载单旋翼无人直升机",
        "name_en": "Heavy-Payload Industrial Drone Helicopter",
        "code": "SYS.ID: CCOP-700",
        "tagline": "主副旋翼变距机构 · 机械效率巅峰 · 超强抗风与大重量吊挂作业",
        "desc": "CYBER-COPTER 700代表了传统单旋翼机械直升机在无人化领域的巅峰工艺。搭载高强度合金主旋翼十字盘与精密无刷变距伺服舵机，动力由高性能无刷马达或微型涡轴发动机直驱。相较于多旋翼飞行器，单主旋翼具有无可比拟的气动盘载效率与超大风阻抗性，能够在8级强阵风及暴雨等极端恶劣海况下完成悬停作业。下机身设置一体式加固滑橇式起落架，支持应急投送、吊载运输与海上搜救。",
        "highlights": [
            {"title": "高精度变距控制", "detail": "金属全CNC加工主旋翼头与数控斜盘系统，实现毫秒级螺距响应与极速自旋着陆保护。"},
            {"title": "8级超强抗阵风", "detail": "高惯量碳纤旋翼与高盘载比优势，在海上钻井平台、强风峡谷作业时依旧坚如磐石。"},
            {"title": "多任务重心自适应", "detail": "飞控系统内置载荷质量与动态质心在线辨识算法，吊挂物体摆动时自动补偿平抑。"},
            {"title": "自旋降落安全冗余", "detail": "发生主动力故障时，飞控自动进入自旋下滑减速模式，最大程度保护高价值设备。"}
        ],
        "specs": [
            {"label": "主旋翼直径", "value": "1780 mm"},
            {"label": "机身机长", "value": "1580 mm"},
            {"label": "空机全重", "value": "8.5 kg"},
            {"label": "最大起飞全重", "value": "22.0 kg"},
            {"label": "最大外吊负荷", "value": "10.0 kg"},
            {"label": "最大平飞速度", "value": "140 km/h"},
            {"label": "悬停留空时间", "value": "45 min (电推) / 120 min (油动)"},
            {"label": "抗风极限", "value": "8 级 (20.7 m/s)"}
        ],
        "front_image": "ScreenShot_2026-10-18_020202_110.png",
        "front_caption": "CYBER-COPTER 700 战术红色涂装单旋翼直升机渲染",
        "back_sub_image": "ScreenShot_2026-10-18_010331_515.png",
        "back_sub_caption": "高位加固碳纤起落架与科研传感器测试机架"
    },
    {
        "id": "UNIT-13",
        "category_zh": "工程设计系列",
        "category_en": "CAD DIMENSIONAL BLUEPRINT",
        "name_zh": "TILT-ROTOR QUAD-PLANE // 倾转多旋翼精密三维工程标注机",
        "name_en": "CAD Dimensioned Tilt-Rotor Quadplane System",
        "code": "SYS.ID: CAD-TR237",
        "tagline": "机械工程基准标注 · 动态重心严苛平衡 · 倾转机构空间几何剖析",
        "desc": "TILT-ROTOR QUAD-PLANE展现了航空器从三维CAD概念设计向精密数控加工转化的工程原貌。模型完整保留了三维坐标系基准（171.40mm x 237mm工程界限尺寸）、重心标记点（Center of Gravity）与旋翼扫掠干涉圆。该机型采用革命性的倾转旋翼架构，前向电机兼顾垂直起飞与水平推进。碳纤维蜂窝夹层中心板上紧凑布局动力电调、动力电池与RTK航向天线，展现了极致的机械空间集成艺术。",
        "highlights": [
            {"title": "毫厘级精准工程标注", "detail": "严格基于三维CAD拓扑数据设计，精确标定电机轴间距、重心垂线与空间干涉界限。"},
            {"title": "动态CG重心匹配", "detail": "电池滑动配重导轨与旋翼倾转力矩精准重合，确保模式转换过渡瞬间零俯仰漂移。"},
            {"title": "碳纤编织蜂窝主板", "detail": "高刚度斜纹碳纤维板与CNC轻量化铝合金垫柱，承受超大扭矩而不发生结构形变。"},
            {"title": "多轴动力冗余布局", "detail": "前后旋翼异径差速匹配，在提供充沛垂直推力的同时，显著改善平飞巡航推重比。"}
        ],
        "specs": [
            {"label": "前后轴距基准", "value": "171.40 mm"},
            {"label": "左右轮廓宽度", "value": "237.00 mm"},
            {"label": "结构重量", "value": "680 g (含全套舵机机构)"},
            {"label": "旋翼倾转角度", "value": "0°(平飞) ~ 90°(悬停) 连续可调"},
            {"label": "倾转伺服精度", "value": "0.08° 数码无刷高压伺服"},
            {"label": "主板材料规范", "value": "3K 斜纹哑光纯碳纤维 (厚度 2.5mm)"},
            {"label": "最大设计推重比", "value": "2.8 : 1"},
            {"label": "适配动力系统", "value": "2207 ~ 2306 级别无刷电机"}
        ],
        "front_image": "VIEW3.jpg",
        "front_caption": "TILT-ROTOR 倾转旋翼 CAD 轴向尺寸与重心工程标注图",
        "back_sub_image": "ScreenShot_2026-10-18_010348_311.png",
        "back_sub_caption": "X4四旋翼教学实验机型动力布局与碳板桁架架构"
    },
    {
        "id": "UNIT-14",
        "category_zh": "智能航拍系列",
        "category_en": "AERIAL CINEMATOGRAPHY",
        "name_zh": "AERO-STREAM 7 // 消费级流线型智能航拍无人机",
        "name_en": "Sleek Aerodynamic Smart Aerial Drone",
        "code": "SYS.ID: STR-700A",
        "tagline": "仿生流线一体成型机壳 · 4K三轴无刷增稳云台 · 视觉全向智能避障",
        "desc": "AERO-STREAM 7将航天流体力学外形与工业设计美学融为一体。流线型深海蓝涂装外壳宛如飞鸟掠空，有效降低飞行中的涡流风阻与气动风噪。机身腹部搭载三轴微型无刷增稳机械云台与1英寸大底4K 60帧高清影像传感器。整机周身密布双目立体视觉相机阵列，支持实时构建周围三维环境深度点云，在茂密树林、复杂岩石间穿行时能够智能规避障碍并全自动跟焦拍摄运动主体。",
        "highlights": [
            {"title": "仿生水滴流线壳体", "detail": "通过风洞阻力优化的高光注塑一体化外壳，显著降低迎风阻力并提供全机防泼溅。"},
            {"title": "1英寸大底航拍镜头", "detail": "2000万像素专业摄影镜头，支持10-bit D-Log M色彩模式，捕捉电影级丰富暗部细节。"},
            {"title": "APAS 5.0智能避障", "detail": "全向双目视觉融合前向毫米波雷达，复杂树丛障碍物中全自动规划顺畅绕行路径。"},
            {"title": "高能量密度电池", "detail": "定制高电压高密度智能动力电池，单块电池支持长达46分钟的从容航拍创作。"}
        ],
        "specs": [
            {"label": "机身对角尺寸", "value": "350 mm"},
            {"label": "整机起飞重量", "value": "920 g"},
            {"label": "相机传感器", "value": "1 英寸 CMOS / 2000万有效像素"},
            {"label": "视频录制规格", "value": "4K @ 60fps / 1080P @ 120fps"},
            {"label": "最大抗风速度", "value": "12 m/s (6 级风)"},
            {"label": "最长悬停时间", "value": "40 min"},
            {"label": "最长航拍续航", "value": "46 min"},
            {"label": "数字图传距离", "value": "12 km (1080P/60fps 低延迟)"}
        ],
        "front_image": "7.jpg",
        "front_caption": "AERO-STREAM 7 流线型机壳与红橙色螺旋桨整机渲染",
        "back_sub_image": "ScreenShot_2026-10-18_020802_359.png",
        "back_sub_caption": "高韧性全包围防撞涵道圈微型航拍穿越机"
    },
    {
        "id": "UNIT-15",
        "category_zh": "室内安防系列",
        "category_en": "INDOOR CINEWHOOP",
        "name_zh": "CINE-SHIELD 20 // 室内微型安全反推涵道穿越机",
        "name_en": "Micro Inverted-Thrust CineWhoop FPV Drone",
        "code": "SYS.ID: CS-20IN",
        "tagline": "倒置反推动力拓扑 · 多叶微型高压螺旋桨 · 狭窄密闭空间丝滑运镜",
        "desc": "CINE-SHIELD 20专为室内狭小密闭空间安全拍摄、管道探伤与一镜到底运镜设计。采用颠覆性的倒置反推电机布局，将电机安装在机架底部向下喷气，使上方吸气气流彻底避开机身横梁阻挡，低速悬停工况推力能效跃升15%。配置8叶高密度高升力微型青色螺旋桨，在极低转速下即可产生平顺细腻的悬停升力，将高频尖锐气动噪声抑制到极致，即便掠过人耳亦无刺耳轰鸣。",
        "highlights": [
            {"title": "倒置反推流场优化", "detail": "电机倒装避开机臂迎风下洗干扰，低速微距悬停稳定性提高30%，运镜如履平地。"},
            {"title": "8叶高密度静音微桨", "detail": "多叶气动小桨提供超大圆盘载荷与细密升力阶跃，完全消解低频抖动与共振。"},
            {"title": "微型轻量化碳纤底盘", "detail": "采用厚度1.5mm超轻全碳纤镂空底盘，兼顾电子元器件安装与结构轻量化极致。"},
            {"title": "微型高清图传快拆", "detail": "预留微型高清数字图传排线位与高强度减震球，适配各主流超轻4K高清拇指相机。"}
        ],
        "specs": [
            {"label": "轴距规格", "value": "85 mm"},
            {"label": "空机重量", "value": "68 g (不含电池)"},
            {"label": "起飞全重", "value": "115 g (含2S高倍率电池)"},
            {"label": "螺旋桨叶数", "value": "8 叶超静音专用多叶微桨"},
            {"label": "动力驱动", "value": "1103 ~ 1104 级超微型外转子无刷电机"},
            {"label": "飞控电调架构", "value": "一体化AIO 12A 四合一飞控板"},
            {"label": "室内续航时长", "value": "5.5 ~ 7.0 min"},
            {"label": "防护安全特性", "value": "低动能撞击自停，零人身刮伤隐患"}
        ],
        "front_image": "ScreenShot_2026-10-18_003853_629.png",
        "front_caption": "CINE-SHIELD 20 反推式动力与8叶青色微型螺旋桨装配全景",
        "back_sub_image": "ScreenShot_2026-10-18_020641_847.png",
        "back_sub_caption": "轻量化极简四旋翼纯碳纤维装配底盘与中心孔位"
    },
    {
        "id": "UNIT-16",
        "category_zh": "远距机架系列",
        "category_en": "LONG-RANGE RACER",
        "name_zh": "SPECTER LR-7 // 远距离长航时碳纤维穿越机架",
        "name_en": "Long-Range Carbon Fiber FPV Racing Frame",
        "code": "SYS.ID: SPC-LR7",
        "tagline": "T700高刚度纯碳板材 · 几何拉长轴距抗抖 · 超视距山峰巡航基石",
        "desc": "SPECTER LR-7是专为穿越机远距离探索（Long Range FPV）与高山风口巡航打造的高强度机架底盘。机臂采用厚达6mm的一体式碳纤维板切割，搭配双侧碳纤加强拉杆，彻底消除了大油门爬升时机臂产生的微小共振与弯曲变形。拉长的前后轴距使螺旋桨完全退出FPV高清摄像机的第一视角画面，让飞手尽享纯净无遮挡的辽阔天际视野。尾部集成高刚性TPU打印天线座与GPS罗盘防护罩。",
        "highlights": [
            {"title": "6mm极厚碳纤机臂", "detail": "采用日本东丽T700高纯度碳纤维板，超强抗扭曲疲劳刚度，抗摔毁强度提升200%。"},
            {"title": "无桨叶遮挡宽广视野", "detail": "机头加长前后拉伸结构，使高清图传画面与录制相机彻底摆脱旋转黑边的视觉遮挡。"},
            {"title": "双机臂加强拉杆", "detail": "对角线高强度合金支撑拉杆设计，有效平抑低频机械共振，大幅降低飞控陀螺仪噪声。"},
            {"title": "大容量电池双绑带位", "detail": "长达160mm的顶部防滑碳板空间，支持平放长条形4S/6S 21700超长续航锂电包。"}
        ],
        "specs": [
            {"label": "对角线轴距", "value": "320 mm (支持7寸桨叶)"},
            {"label": "机臂板厚度", "value": "6.0 mm 倒角打磨碳板"},
            {"label": "顶板/底板厚度", "value": "2.5 mm / 3.0 mm"},
            {"label": "机架净重", "value": "182 g (含金属螺丝及打印件)"},
            {"label": "飞控安装孔位", "value": "20x20mm / 30.5x30.5mm 双规格兼容"},
            {"label": "图传安装位", "value": "兼容 DJI O3 Air Unit / 蜗牛高清图传"},
            {"label": "相机侧板间距", "value": "19mm / 20mm 微型摄像头"},
            {"label": "推荐动力搭配", "value": "2806.5 / 2807 电机 + 7040 螺旋桨"}
        ],
        "front_image": "ScreenShot_2026-10-18_002253_983.png",
        "front_caption": "SPECTER LR-7 纯碳纤长轴距机架及前后天线座展示",
        "back_sub_image": "ScreenShot_2026-10-18_002722_183.png",
        "back_sub_caption": "宽X型竞速机架底部加强筋与前后对角拉杆抗扭结构"
    },
    {
        "id": "UNIT-17",
        "category_zh": "自由花飞系列",
        "category_en": "FREESTYLE FPV",
        "name_zh": "APEX FREESTYLE 5 // 5寸专业特技花飞与竞速穿梭机",
        "name_en": "5-Inch Freestyle Acrobatics Racing FPV Drone",
        "code": "SYS.ID: APX-5F",
        "tagline": "几何重心高度集中 · 瞬时加速度爆发力 · 丝滑翻滚极速穿桥",
        "desc": "APEX FREESTYLE 5专为高难度三维极限特技飞行动作而生。全机结构以“质量重心高度集中化”为核心设计原则，将电池、飞控与四合一电调全部紧凑布置在旋转几何中心，赋予飞行器难以置信的角加速度响应与翻滚敏捷度。坚韧的碳纤维机臂在机身中部交错锁止，配合超轻航空铝侧板，经得起激进动作中的高难度碰撞。无论是急速俯冲、极速贴地漂移还是空中悬停自旋，皆能游刃有余。",
        "highlights": [
            {"title": "质心向心化设计", "detail": "三轴转动惯量极小化布局，使得翻滚（Roll）与俯仰（Pitch）转速最高可突破1800°/s。"},
            {"title": "模块化独立可拆机臂", "detail": "每根机臂仅需拆卸两颗螺丝即可单独更换，野外炸机后2分钟内迅速复飞。"},
            {"title": "CNC航空铝护头侧板", "detail": "7075定制铝合金机头相机防护侧板，给予高单价FPV高清摄像头坚固的铠甲级保护。"},
            {"title": "优化电容与走线通道", "detail": "机身内部预设防震高频低阻电容卡槽与接收机天线出线孔，走线工整清爽无杂乱。"}
        ],
        "specs": [
            {"label": "标准轴距尺寸", "value": "225 mm (经典正X / 宽X)"},
            {"label": "空机裸重", "value": "125 g"},
            {"label": "整机起飞全重", "value": "680 g (含6S电池与高清录制机)"},
            {"label": "最大推重比", "value": "高达 12.5 : 1"},
            {"label": "0-100km/h加速", "value": "仅需 1.1 秒"},
            {"label": "极限最高平飞时速", "value": "210 km/h"},
            {"label": "推荐无刷马达", "value": "2207 1950KV (6S) / 2550KV (4S)"},
            {"label": "极限特技续航", "value": "4.5 ~ 6.0 min (全油门激进操控)"}
        ],
        "front_image": "ScreenShot_2026-10-18_003525_079.png",
        "front_caption": "APEX FREESTYLE 5 整机组装就绪三维紧凑视角",
        "back_sub_image": "ScreenShot_2026-10-18_002602_215.png",
        "back_sub_caption": "经典高刚性X型碳纤维底板数控精雕几何形态"
    },
    {
        "id": "UNIT-18",
        "category_zh": "特种突防系列",
        "category_en": "TACTICAL PAYLOAD FPV",
        "name_zh": "TACTICAL STRIKE FPV // 特种任务挂载穿越机系统",
        "name_en": "Tactical Modular Payload FPV Strike Platform",
        "code": "SYS.ID: TAC-STK8",
        "tagline": "腹部电控脱钩挂载 · 抗电子压制跳频天线 · 极速突防定点投送",
        "desc": "TACTICAL STRIKE FPV是一款针对特种安全防范、特种破拆引导及应急物资超低空投掷开发的任务级穿越飞行平台。针对复杂电磁对抗环境设计，配备双频高增益圆极化全向天线与跳频抗干扰微波链路，具备在强GPS信号屏蔽干扰下的纯手动惯导与FPV视觉强行突入能力。腹部配备电磁触发快卸吊舱支架，可在高速平飞掠过目标上空的瞬间，以毫秒级响应精准释放特种救援器材或破拆工具。",
        "highlights": [
            {"title": "抗电子干扰跳频链路", "detail": "采用868/915MHz与2.4GHz双频自适应跳频技术，有效抵御宽带电子压制。"},
            {"title": "高速掠地突防突击", "detail": "平飞极速超160km/h，利用低空雷达盲区与地表障碍物掩护快速逼近指定坐标。"},
            {"title": "电控毫秒级投掷释放", "detail": "专用舵机/电磁锁扣联动机构，地面遥控一键触发，确保载荷平稳脱离不缠绕。"},
            {"title": "重型碳板加强梁", "detail": "全机采用双层加厚碳纤维板强化承重底盘，承受高达1.5kg腹部集中载荷而不变形。"}
        ],
        "specs": [
            {"label": "工作轴距", "value": "350 mm"},
            {"label": "机体全重 (不含载荷)", "value": "780 g"},
            {"label": "最大腹部挂载能力", "value": "1800 g"},
            {"label": "高速突防航速", "value": "140 ~ 175 km/h"},
            {"label": "最大作业作战半径", "value": "10 km (低空超视距)"},
            {"label": "挂架释放响应延迟", "value": "＜ 50 ms"},
            {"label": "动力电调规格", "value": "60A 四合一金属屏蔽大功率电调"},
            {"label": "遥测控制频率", "value": "ELRS 915MHz / 2.4GHz True Diversity"}
        ],
        "front_image": "ScreenShot_2026-10-18_020533_865.png",
        "front_caption": "TACTICAL STRIKE 腹部挂载特种吊舱外形渲染",
        "back_sub_image": "ScreenShot_2026-10-18_004010_510.png",
        "back_sub_caption": "高承载加强型碳纤骨架与模块化支柱排布工程图"
    },
    {
        "id": "UNIT-19",
        "category_zh": "科研开发系列",
        "category_en": "AUTONOMOUS RESEARCH",
        "name_zh": "AUTONOMOUS LAB-X // 多传感器自主飞行科研四旋翼平台",
        "name_en": "Multi-Sensor Autonomous Research Quadcopter Platform",
        "code": "SYS.ID: LAB-X4",
        "tagline": "机载边缘AI算力核心 · 激光雷达SLAM建图 · ROS2机器人开源生态",
        "desc": "AUTONOMOUS LAB-X专为高校航空航天学院、机器人研究所及前沿智能无人机算法团队打造。机身上层宽阔甲板预留标准螺孔矩阵，原生适配NVIDIA Jetson Orin机载深度学习计算模块、全向固态激光雷达、双目深度相机及超宽带UWB室内定位基站。支持在彻底失去全球卫星导航（GNSS-Denied）的地下矿道、核电站内部及建筑室内环境中，依靠纯机载视觉与激光SLAM算法实现全自主探索导航与避障。",
        "highlights": [
            {"title": "机载百TOPS算力加持", "detail": "直接搭载Jetson边缘AI终端，支持机载实时运行YOLO目标检测与三维点云配准。"},
            {"title": "原生支持ROS2/PX4", "detail": "完全打通ROS2 Humble与PX4 Autopilot微服务架构，提供丰富的开放API与仿真环境。"},
            {"title": "无GPS自主探索SLAM", "detail": "融合下视光流、单线/多线激光雷达与IMU数据，在无卫星室内环境厘米级悬停。"},
            {"title": "模块化高位起落架", "detail": "高离地间隙碳纤起落架，为机腹全向激光雷达和倾斜相机提供充裕的视野净空。"}
        ],
        "specs": [
            {"label": "对角轴距", "value": "450 mm"},
            {"label": "整机净重 (含航电)", "value": "1950 g"},
            {"label": "机载AI算力", "value": "最高支持 275 TOPS (Jetson Orin)"},
            {"label": "激光雷达规格", "value": "Livox Mid-360 / 3D全向固态激光雷达"},
            {"label": "室内悬停精度", "value": "水平 ± 2 cm / 垂直 ± 1.5 cm"},
            {"label": "二次开发接口", "value": "CAN / UART / USB 3.2 / 千兆以太网"},
            {"label": "供电输出扩展", "value": "双路 5V/3A, 12V/5A 独立DC-DC稳压"},
            {"label": "标准测试续航", "value": "24 min (全算力与雷达满载状态)"}
        ],
        "front_image": "ScreenShot_2026-10-18_020706_152.png",
        "front_caption": "AUTONOMOUS LAB-X 多传感器天线科研平台模型",
        "back_sub_image": "ScreenShot_2026-10-18_003609_866.png",
        "back_sub_caption": "异构折叠机身中框拓扑受力结构与高刚度减震塔柱"
    },
    {
        "id": "UNIT-20",
        "category_zh": "结构工艺系列",
        "category_en": "CARBON MONOCOQUE",
        "name_zh": "CARBON-MONOCOQUE // 一体成型高模量碳纤维极简骨架",
        "name_en": "Monocoque Ultra-Rigid Carbon Airframe Architecture",
        "code": "SYS.ID: CFA-MONO",
        "tagline": "连续纤维无缝热压 · 航空级应力拓扑精雕 · 极致轻量化与高模量",
        "desc": "CARBON-MONOCOQUE机身展示了现代碳纤维复材工艺在无人机结构减重上的终极追求。突破传统碳板拼接用螺丝连接的工艺瓶颈，采用3D连续预浸布在特制金属模具内经过130℃高温高压一体共固化成型。彻底消除了应力集中孔位与金属紧固件死重，使机体抗弯抗扭刚度跃升300%，而整体重量比传统金属架构减轻55%。机体预埋碳化硅耐磨螺套与气动倒角边缘，将空气阻力与机械震动降至理论极限。",
        "highlights": [
            {"title": "一体无缝热压共固化", "detail": "无螺栓拼接死角，连续纤维沿主受力路径无断裂排布，彻底杜绝空中疲劳分层。"},
            {"title": "三维拓扑镂空减重", "detail": "基于有限元算法精准剔除非承力多余材质，在保证绝对刚度的前提下达到羽量级。"},
            {"title": "航空级CNC高精倒角", "detail": "全机边缘采用0.5mm微弧倒角CNC精铣打磨，不仅手感细腻丝滑，更能杜绝划伤导线。"},
            {"title": "共振频率大幅提高", "detail": "机体天然固有频率高达180Hz以上，远超电机震动主频带，无需复杂陷波滤波。"}
        ],
        "specs": [
            {"label": "成型工艺", "value": "高压真空热压罐一体共固化成型"},
            {"label": "纤维材质", "value": "日本东丽 T800 / M40J 级碳纤维预浸布"},
            {"label": "杨氏弹性模量", "value": "294 GPa (超高弹性模量)"},
            {"label": "抗拉极限强度", "value": "4900 MPa"},
            {"label": "结构重量削减", "value": "对比铝合金机身减轻 58%"},
            {"label": "抗冲击韧性", "value": "特种环氧树脂增韧体系，抗落锤冲击"},
            {"label": "工作耐温界限", "value": "-55℃ ~ +125℃ 无形变"},
            {"label": "适用机型范围", "value": "高竞速无人机 / 军规微型侦察机"}
        ],
        "front_image": "ScreenShot_2026-10-18_021304_646.png",
        "front_caption": "CARBON-MONOCOQUE 一体成型纯碳纤骨架透视",
        "back_sub_image": "ScreenShot_2026-10-18_003718_911.png",
        "back_sub_caption": "伸展X型长距离低风阻竞速机臂几何形态与电机座"
    },
    {
        "id": "UNIT-21",
        "category_zh": "动力总成系列",
        "category_en": "INTEGRATED PROPULSION",
        "name_zh": "AERO-PROPULSION // 航空级无刷电机与折叠碳桨动力总成",
        "name_en": "Aviation-Grade Brushless Motor & Folding Carbon Prop System",
        "code": "SYS.ID: AP-SYS8",
        "tagline": "N45SH耐高温稀土钕铁硼磁钢 · 动平衡G1.0高精校准 · 离心自锁折叠桨",
        "desc": "AERO-PROPULSION动力系统是无人机强劲心跳的来源。电机定子采用0.2mm超薄高硅川崎无取向硅钢片，搭配220℃军工级耐高温无氧铜漆包线手工精密绕组，铁损降低35%，电机工作效率突破91%。高刚性折叠碳纤维螺旋桨叶片经风洞精密调校，在电机启动瞬间依靠离心力瞬间平稳展开并自锁，折叠后紧贴机臂收纳，便于野外运输且极大减小抗风风阻，是工业长航时无人机的首选动力动力链。",
        "highlights": [
            {"title": "0.2mm超薄低铁损定子", "detail": "极细晶粒硅钢冲片大幅降低高速交变磁场下的涡流发热，长时间高负荷运转温升极低。"},
            {"title": "进口NSK/EZO超静音轴承", "detail": "精密双大尺寸航空滚珠轴承，有效抵御剧烈机动中的强向径向轴向交变冲击载荷。"},
            {"title": "动平衡等级G1.0极致调谐", "detail": "每台转子均经过双平面动态高速去重调平，振动加速度＜0.08G，从源头消灭果冻抖动。"},
            {"title": "自锁折叠碳纤维螺旋桨", "detail": "采用航空级连续碳纤模压成型，桨根部加厚防疲劳设计，提供澎湃充沛的瞬时推力。"}
        ],
        "specs": [
            {"label": "电机规格尺寸", "value": "8318 / 10015 级别无刷马达"},
            {"label": "定子极槽配置", "value": "36N42P (多极高扭矩平稳输出)"},
            {"label": "单轴最大推力", "value": "16.5 kg / 轴 (12S高压驱动)"},
            {"label": "推荐单轴载荷", "value": "5.0 ~ 7.5 kg / 轴 (最高能效工作区间)"},
            {"label": "最大工作能效", "value": "11.8 g/W @ 4.0kg 恒定悬停推力"},
            {"label": "防护等级规范", "value": "IP56 工业防尘防水，全封闭防沙"},
            {"label": "折叠螺旋桨尺寸", "value": "30 英寸 (30x10.5 复合折叠桨)"},
            {"label": "配套FOC矢量电调", "value": "CAN总线实时回传转速、温度、母线电流"}
        ],
        "front_image": "ScreenShot_2026-10-18_010933_442.png",
        "front_caption": "无刷电机与高强度折叠碳纤维螺旋桨一体化动力总成",
        "back_sub_image": "ScreenShot_2026-10-18_010846_708.png",
        "back_sub_caption": "双叶碳纤维折叠螺旋桨气动翼型剖面细节与离心锁止结构"
    },
    {
        "id": "UNIT-22",
        "category_zh": "核心电机系列",
        "category_en": "BRUSHLESS MOTORS",
        "name_zh": "AERO-BRUSHLESS // 高性能航空级外转子无刷马达",
        "name_en": "High-Efficiency Brushless Outrunner Aircraft Motor",
        "code": "SYS.ID: MOT-8318X",
        "tagline": "开放式离心多孔风冷结构 · 0.15mm精密气隙 · 航空级超轻外转子",
        "desc": "AERO-BRUSHLESS外转子无刷电机专为对推重比与热稳定性要求极为严苛的多旋翼与垂直起降机型研发。外转子外壳采用高强度7075-T6航空级数控精雕铝壳，并在顶部集成自抽风式离心风扇结构，运转过程中自动形成强劲负压气流抽吸冷却定子铁芯。内部转子磁钢采用弧形贴片工艺，与定子形成均匀且极其狭窄的0.15mm微气隙，实现磁通量密度的极大化与转矩脉动率的微小化。",
        "highlights": [
            {"title": "自抽风离心冷却转子", "detail": "电机高速旋转时叶片形成强制风冷循环，连续满载工作下定子温升比常规电机低18℃。"},
            {"title": "弧形高性能瓦形磁钢", "detail": "N45SH级稀土钕铁硼磁钢精密磨制弧形表面，提升气隙磁密并显著降低齿槽转矩。"},
            {"title": "多孔轻量化端盖设计", "detail": "基于受力分析的多孔蜂窝端盖，在保障抗拉抗剪切强度的同时将转动惯量削减22%。"},
            {"title": "军工级三防绝缘浸漆", "detail": "线圈经过真空压力浸漆（VPI）处理，耐高湿度、耐农药酸碱与盐雾绝缘击穿。"}
        ],
        "specs": [
            {"label": "电机外径尺寸", "value": "Φ 92.0 mm"},
            {"label": "电机机身高度", "value": "40.5 mm"},
            {"label": "电机重量", "value": "620 g (含长硅胶出线)"},
            {"label": "KV转速常数", "value": "100 KV / 120 KV 可选"},
            {"label": "最大持续电流", "value": "75 A (180 秒持续测试)"},
            {"label": "最大持续功率", "value": "3600 W (瞬时爆发超4500W)"},
            {"label": "空载电流 (Io)", "value": "1.2 A @ 20V"},
            {"label": "相间内阻 (Rm)", "value": "24 mΩ"}
        ],
        "front_image": "ScreenShot_2026-10-18_004941_704.png",
        "front_caption": "航空级高效外转子无刷电机定转子透视与多孔散热结构",
        "back_sub_image": "ScreenShot_2026-10-18_014944_782.png",
        "back_sub_caption": "航空级高动平衡双叶纯碳纤维螺旋桨翼尖流线特写"
    },
    {
        "id": "UNIT-23",
        "category_zh": "航电配件系列",
        "category_en": "AVIONICS & AERO-PROPS",
        "name_zh": "AVIONICS & PROPS // 气动螺旋桨矩阵与智能电源管理分电系统",
        "name_en": "Aero-Props Matrix & Intelligent Power Distribution Architecture",
        "code": "SYS.ID: PDB-PROP9",
        "tagline": "三叶低噪宽弦静音桨 · 高动平衡碳桨 · 大电流智能分电与多路平衡充",
        "desc": "本单元汇集了飞行系统核心的外围关键动力与航电配套矩阵。涵盖专为城市安防低噪巡航设计的三叶宽弦大曲率静音螺旋桨、用于高速竞速的高动平衡双叶纯碳桨，以及用于地面保障与机载配电的智能大电流分电与多通道平衡充电插座模块。分电系统采用厚达4oz沉金铜箔与一体压铸铝散热外壳，支持高达200A瞬时峰值大电流安全通过，集成过流保护、短路阻断与独立霍尔电流采样，保障整机用电坚不可摧。",
        "highlights": [
            {"title": "三叶降噪气动翼尖", "detail": "三叶低雷诺数特殊翼型，在较低转速下提供充沛推力，人耳感知声学噪声削减4.5dB。"},
            {"title": "高动平衡双叶纯碳桨", "detail": "大倾角微下反翼梢设计，抑制桨尖气流分离，极速工况下推力传递无迟滞。"},
            {"title": "4oz加厚沉金分电核心", "detail": "超低内阻发热，支持12S~14S高电压大电流持续放电，为大载重多旋翼提供纯净电源。"},
            {"title": "全功能地面维护生态", "detail": "多路智能平衡充电插座与快速诊断接口，满足野外高频次作业时的快速补能需求。"}
        ],
        "specs": [
            {"label": "三叶静音桨规格", "value": "3-Blade 8.5x4.2 / 10x4.5 (高韧复材)"},
            {"label": "双叶碳纤桨规格", "value": "2-Blade 15x5.5 / 18x6.2 (100%全碳模压)"},
            {"label": "分电板持续电流", "value": "160 A (环境温度 25℃ 持续工作)"},
            {"label": "瞬时峰值耐受电流", "value": "240 A (持续 10 秒)"},
            {"label": "输入供电电压范围", "value": "6S ~ 14S LiPo (22.2V ~ 58.8V)"},
            {"label": "独立BEC降压输出", "value": "5V/4A, 12V/4A 双路超低纹波滤波"},
            {"label": "平衡充接口协议", "value": "支持 JST-XH 2S~8S 全通道插针标准"},
            {"label": "外壳屏蔽材质", "value": "CNC阳极氧化防电磁辐射铝合金防护外壳"}
        ],
        "front_image": "ScreenShot_2026-10-18_005038_903.png",
        "front_caption": "三叶低噪高推力螺旋桨气动造型大图",
        "back_sub_image": "ScreenShot_2026-10-18_002945_219.png",
        "back_sub_caption": "智能分电管理与多通道平衡充电插座模块接口总成"
    }
]
