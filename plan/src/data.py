# -*- coding: utf-8 -*-
"""Single source of truth for the plan: profile, foods, menu, workout, shopping."""

PROFILE = dict(weight=58.3, height=165, age=21, sex="m", activity=1.4,
               surplus=300, gym_kcal=250, protein_gkg=2.0, fat_pct=0.25)

def targets(p=PROFILE):
    bmr = 10 * p["weight"] + 6.25 * p["height"] - 5 * p["age"] + (5 if p["sex"] == "m" else -161)
    base = bmr * p["activity"]
    rest = round((base + p["surplus"]) / 10) * 10
    gym = round((base + p["surplus"] + p["gym_kcal"]) / 10) * 10
    prot = round(p["protein_gkg"] * p["weight"])
    def mac(k):
        fat = round(k * p["fat_pct"] / 9)
        carb = round((k - prot * 4 - fat * 9) / 4)
        return dict(kcal=k, p=prot, f=fat, c=carb)
    return dict(bmr=round(bmr), base=round(base), rest=mac(rest), gym=mac(gym),
                tennis_single=round(7 * p["weight"]), tennis_double=round(5 * p["weight"]))

# id, ad (az), italyanca, kateqoriya, kcal, P, K(arb), Y(ağ) per 100 g, porsiya ipucu
FOODS = [
 ("yulaf","Yulaf yarması","fiocchi d'avena","Taxıl",372,13.5,58.7,7.0,"1 xörək qaşığı ≈ 10 q"),
 ("sud15","Süd 1,5%","latte parzialmente scremato","Süd",46,3.3,4.9,1.6,"1 stəkan ≈ 250 q"),
 ("sud35","Süd 3,5%","latte intero","Süd",64,3.3,4.8,3.6,"1 stəkan ≈ 250 q"),
 ("kefir","Kefir","kefir","Süd",60,3.5,4.5,3.0,"1 stəkan ≈ 250 q"),
 ("yoq0","Yunan yoqurtu 0%","yogurt greco 0%","Süd",57,10.0,4.0,0.0,"1 qutu ≈ 170 q"),
 ("yoq2","Yunan yoqurtu 2%","yogurt greco 2%","Süd",73,10.0,3.0,2.0,"1 qutu ≈ 170 q"),
 ("skyr","Skyr","skyr","Süd",63,11.0,4.0,0.2,"1 qutu ≈ 150 q"),
 ("fiocchi","Dənəli kəsmik","fiocchi di latte","Süd",100,12.0,3.0,4.5,"1 qutu ≈ 150 q"),
 ("ricotta","Rikotta","ricotta vaccina","Süd",146,8.8,3.5,10.9,"1 qutu ≈ 250 q"),
 ("mozz","Motsarella","mozzarella","Süd",253,18.7,0.7,19.5,"1 top ≈ 125 q"),
 ("parm","Parmezan","Parmigiano Reggiano","Süd",392,33.0,0.0,28.0,"1 xörək qaşığı rəndələnmiş ≈ 8 q"),
 ("yumurta","Yumurta","uova","Protein",140,12.5,0.7,9.5,"1 ədəd (L) ≈ 55 q"),
 ("albume","Yumurta ağı","albume","Protein",52,10.9,0.7,0.2,"1 yumurtanın ağı ≈ 33 q"),
 ("toyuq","Toyuq döşü (çiy)","petto di pollo","Protein",105,23.0,0.0,1.2,"bişəndə ~25% yüngülləşir"),
 ("hindi","Hind toyuğu döşü (çiy)","fesa di tacchino","Protein",107,24.0,0.0,1.2,""),
 ("qiyme","Mal qiyməsi 5% (çiy)","macinato magro di manzo","Protein",137,21.0,0.0,5.5,""),
 ("mal","Mal əti, yağsız (çiy)","fesa di manzo","Protein",125,22.0,0.0,4.0,""),
 ("bresaola","Bresaola","bresaola","Protein",151,32.0,0.0,2.6,"1 dilim ≈ 10 q"),
 ("cotto","Bişmiş vetçina","prosciutto cotto","Protein",130,19.5,1.0,5.0,"1 dilim ≈ 20 q"),
 ("crudo","Qurudulmuş vetçina","prosciutto crudo","Protein",268,26.0,0.0,18.0,"1 dilim ≈ 15 q"),
 ("mortadella","Mortadella (Bolonya)","mortadella","Protein",288,15.0,0.0,25.0,"1 dilim ≈ 15 q"),
 ("tonno","Tuna, öz suyunda","tonno al naturale","Protein",103,24.0,0.0,0.8,"1 kiçik qutu süzülmüş ≈ 56–80 q"),
 ("tonnoolio","Tuna, yağda (süzülmüş)","tonno sott'olio","Protein",192,25.2,0.0,10.1,""),
 ("salmone","Qızılbalıq (çiy)","salmone","Protein",200,20.0,0.0,13.0,""),
 ("merluzzo","Treska (çiy)","merluzzo","Protein",82,17.8,0.0,0.7,""),
 ("gamberi","Krevet (çiy)","gamberi","Protein",85,18.0,0.0,1.0,""),
 ("whey","Protein tozu (whey)","proteine whey","Protein",380,78.0,6.0,5.0,"1 ölçü qaşığı ≈ 30 q"),
 ("pasta","Makaron (çiy)","pasta di semola","Karbohidrat",357,13.0,71.0,1.5,"çiy çəki ilə yaz"),
 ("pastaint","Tam taxıl makaron (çiy)","pasta integrale","Karbohidrat",340,13.5,64.0,2.5,"çiy çəki ilə yaz"),
 ("pastacotta","Makaron (bişmiş)","pasta cotta","Karbohidrat",158,5.8,31.0,0.9,""),
 ("riso","Düyü (çiy)","riso","Karbohidrat",355,7.0,79.0,0.6,"çiy çəki ilə yaz"),
 ("risocotto","Düyü (bişmiş)","riso cotto","Karbohidrat",130,2.7,28.0,0.3,""),
 ("kartof","Kartof","patate","Karbohidrat",80,2.0,17.5,0.1,"1 orta ≈ 170 q"),
 ("batat","Batat","patata dolce","Karbohidrat",86,1.6,20.0,0.1,""),
 ("corek","Ağ çörək","pane comune","Karbohidrat",270,8.5,55.0,1.5,"1 dilim ≈ 30 q"),
 ("corekint","Tam taxıl çörək","pane integrale","Karbohidrat",240,9.0,46.0,2.5,"1 dilim ≈ 30 q"),
 ("piadina","Piadina","piadina romagnola","Karbohidrat",310,8.0,50.0,9.0,"1 ədəd ≈ 110 q"),
 ("gallette","Düyü qalletası","gallette di riso","Karbohidrat",380,8.0,81.0,2.8,"1 ədəd ≈ 8 q"),
 ("cornetto","Kruasan (bar)","cornetto / brioche","Karbohidrat",410,7.0,48.0,21.0,"1 ədəd ≈ 60 q"),
 ("lenticchie","Mərcimək (quru)","lenticchie secche","Paxlalı",340,24.0,55.0,1.5,"quru çəki ilə yaz"),
 ("ceci","Noxud (konserv, süzülmüş)","ceci lessati","Paxlalı",120,7.0,16.0,2.5,"1 qutu süzülmüş ≈ 240 q"),
 ("fagioli","Lobya (konserv, süzülmüş)","fagioli borlotti","Paxlalı",100,7.0,14.0,0.5,""),
 ("banan","Banan","banana","Meyvə",89,1.1,23.0,0.3,"1 orta (qabıqsız) ≈ 120 q"),
 ("alma","Alma","mela","Meyvə",52,0.3,14.0,0.2,"1 orta ≈ 180 q"),
 ("uzum","Üzüm","uva","Meyvə",69,0.7,18.0,0.2,""),
 ("xurma","Xurma","cachi","Meyvə",70,0.6,18.6,0.2,"1 ədəd ≈ 200 q"),
 ("portagal","Portağal","arancia","Meyvə",47,0.9,12.0,0.1,"1 orta ≈ 150 q"),
 ("kivi","Kivi","kiwi","Meyvə",61,1.1,15.0,0.5,"1 ədəd ≈ 75 q"),
 ("brokoli","Brokoli","broccoli","Tərəvəz",34,2.8,7.0,0.4,""),
 ("ispanaq","İspanaq","spinaci","Tərəvəz",23,2.9,3.6,0.4,""),
 ("pomidor","Pomidor","pomodori","Tərəvəz",18,0.9,3.9,0.2,"1 orta ≈ 120 q"),
 ("salat","Yaşıl salat","insalata","Tərəvəz",15,1.4,2.9,0.2,""),
 ("yerkoku","Yerkökü","carote","Tərəvəz",41,0.9,10.0,0.2,""),
 ("zucchine","Sukkini (balqabaq)","zucchine","Tərəvəz",17,1.2,3.1,0.3,""),
 ("xiyar","Xiyar","cetrioli","Tərəvəz",15,0.7,3.6,0.1,""),
 ("passata","Pomidor sousu","passata di pomodoro","Tərəvəz",30,1.3,5.0,0.2,""),
 ("olive","Zeytun yağı","olio extravergine","Yağ/qoz",899,0.0,0.0,99.9,"1 xörək qaşığı ≈ 10 q"),
 ("burro","Kərə yağı","burro","Yağ/qoz",717,0.9,0.1,81.0,""),
 ("arachidi","Fıstıq pastası","burro d'arachidi","Yağ/qoz",588,25.0,20.0,50.0,"1 xörək qaşığı ≈ 15 q"),
 ("badam","Badam","mandorle","Yağ/qoz",600,22.0,5.0,53.0,"1 ovuc ≈ 25 q"),
 ("qoz","Qoz","noci","Yağ/qoz",680,15.0,5.0,66.0,"1 ovuc ≈ 25 q"),
 ("sokolad","Qara şokolad 85%","cioccolato fondente 85%","Şirin",580,12.5,19.0,46.0,"1 kvadrat ≈ 10 q"),
 ("bal","Bal","miele","Şirin",304,0.3,82.0,0.0,"1 çay qaşığı ≈ 7 q"),
 ("seker","Şəkər","zucchero","Şirin",392,0.0,100.0,0.0,"1 çay qaşığı ≈ 5 q"),
 ("gelato","Dondurma","gelato","Şirin",200,4.0,25.0,9.0,"1 kiçik fincan ≈ 100 q"),
 ("cappuccino","Kapuçino","cappuccino","İçki",45,2.4,3.6,2.4,"1 fincan ≈ 150 q"),
 ("tagliatelle","Tagliatelle al ragù (hazır)","tagliatelle al ragù","Bolonya yeməyi",180,8.0,22.0,6.5,"restoran porsiyası ≈ 280 q"),
 ("tortellini","Tortellini (təzə, çiy)","tortellini freschi","Bolonya yeməyi",310,12.0,45.0,9.0,"porsiya ≈ 100 q"),
 ("tortbrodo","Tortellini in brodo (hazır)","tortellini in brodo","Bolonya yeməyi",100,4.5,13.0,3.5,"restoran porsiyası ≈ 300 q"),
 ("lasagne","Lazanya alla bolognese","lasagne alla bolognese","Bolonya yeməyi",160,8.0,13.0,8.5,"porsiya ≈ 300 q"),
 ("tigelle","Tigelle / crescentine","tigelle","Bolonya yeməyi",330,8.5,52.0,9.5,"1 ədəd ≈ 30 q"),
 ("pizza","Pizza margherita","pizza margherita","Bolonya yeməyi",250,10.0,33.0,8.5,"1 pizza ≈ 300 q"),
]
FOOD = {f[0]: f for f in FOODS}

MEALS = ["Səhər yeməyi", "Qəlyanaltı 1", "Nahar", "Qəlyanaltı 2", "Şam yeməyi"]

# 7-day menu: (day name, type, [(meal, title, [(food, grams), ...]), ...])
MENU = [
 ("Bazar ertəsi", "gym", [
   ("Səhər yeməyi", "Yulaf sıyığı, banan, fıstıq pastası", [("yulaf",90),("sud15",300),("banan",120),("arachidi",15),("bal",10)]),
   ("Qəlyanaltı 1", "Yunan yoqurtu, bal, qoz", [("yoq0",170),("bal",10),("qoz",15)]),
   ("Nahar", "Toyuq, düyü, brokoli", [("toyuq",140),("riso",120),("brokoli",150),("olive",10)]),
   ("Qəlyanaltı 2", "Bresaola ilə panino, alma", [("corekint",80),("bresaola",40),("alma",180)]),
   ("Şam yeməyi", "Tuna və pomidor sousu ilə makaron, salat", [("pasta",110),("tonno",80),("passata",150),("olive",10),("salat",80),("parm",10)]),
 ]),
 ("Çərşənbə axşamı", "rest", [
   ("Səhər yeməyi", "Omlet (3 yumurta), çörək, pomidor", [("yumurta",165),("corekint",80),("pomidor",120),("olive",5)]),
   ("Qəlyanaltı 1", "Skyr və üzüm", [("skyr",150),("uzum",200)]),
   ("Nahar", "Mərcimək şorbası, çörək, yumurta", [("lenticchie",80),("yerkoku",80),("passata",100),("olive",5),("corek",90),("yumurta",55)]),
   ("Qəlyanaltı 2", "Kefir, banan, badam", [("kefir",250),("banan",120),("badam",20)]),
   ("Şam yeməyi", "Qızılbalıq, kartof, sukkini", [("salmone",130),("kartof",300),("zucchine",200),("olive",5)]),
 ]),
 ("Çərşənbə", "gym", [
   ("Səhər yeməyi", "Kəsmik, yulaf, kivi", [("fiocchi",150),("yulaf",80),("sud15",200),("kivi",150)]),
   ("Qəlyanaltı 1", "Piadina + bişmiş vetçina", [("piadina",110),("cotto",60)]),
   ("Nahar", "Mal qiyməsi, düyü, salat", [("qiyme",150),("riso",120),("salat",100),("olive",10)]),
   ("Qəlyanaltı 2", "Yunan yoqurtu, banan, bal", [("yoq0",170),("banan",120),("bal",10),("gallette",16)]),
   ("Şam yeməyi", "Hind toyuğu, batat, ispanaq", [("hindi",150),("batat",350),("ispanaq",150),("olive",10)]),
 ]),
 ("Cümə axşamı", "rest", [
   ("Səhər yeməyi", "Yulaf, süd, alma, qoz", [("yulaf",80),("sud15",250),("alma",180),("qoz",15)]),
   ("Qəlyanaltı 1", "Rikotta, bal, çörək", [("ricotta",100),("corekint",60),("bal",10)]),
   ("Nahar", "Noxud və tuna salatı, çörək", [("ceci",240),("tonno",80),("pomidor",150),("xiyar",100),("olive",10),("corek",80)]),
   ("Qəlyanaltı 2", "Skyr, xurma", [("skyr",150),("xurma",200)]),
   ("Şam yeməyi", "Toyuq, kartof, yerkökü", [("toyuq",140),("kartof",300),("yerkoku",150),("olive",10)]),
 ]),
 ("Cümə", "gym", [
   ("Səhər yeməyi", "Yumurta, çörək, portağal", [("yumurta",110),("albume",100),("corekint",100),("portagal",150),("olive",5)]),
   ("Qəlyanaltı 1", "Yunan yoqurtu, yulaf, banan", [("yoq0",170),("yulaf",60),("banan",120)]),
   ("Nahar", "Tagliatelle al ragù (restoran / mensa)", [("tagliatelle",280),("salat",100),("olive",5)]),
   ("Qəlyanaltı 2", "Qalleta + bresaola, alma", [("gallette",50),("bresaola",60),("alma",180)]),
   ("Şam yeməyi", "Treska, düyü, brokoli", [("merluzzo",200),("riso",120),("brokoli",200),("olive",10)]),
 ]),
 ("Şənbə", "rest", [
   ("Səhər yeməyi", "Bar: kapuçino + kruasan, sonra skyr", [("cappuccino",150),("cornetto",60),("skyr",150)]),
   ("Qəlyanaltı 1", "Banan, badam", [("banan",120),("badam",25)]),
   ("Nahar", "Tortellini in brodo + toyuq salatı", [("tortbrodo",300),("toyuq",120),("salat",100),("olive",5),("corek",60)]),
   ("Qəlyanaltı 2", "Kəsmik, üzüm", [("fiocchi",150),("uzum",200),("bal",10)]),
   ("Şam yeməyi", "Pizza margherita (bayır), salat", [("pizza",300),("salat",80)]),
 ]),
 ("Bazar", "rest", [
   ("Səhər yeməyi", "Yulaf pancake (yulaf + yumurta + banan)", [("yulaf",70),("yumurta",110),("banan",120),("yoq0",100),("bal",10)]),
   ("Qəlyanaltı 1", "Kefir, qoz", [("kefir",250),("qoz",10)]),
   ("Nahar", "Mal əti, kartof, salat", [("mal",150),("kartof",350),("salat",100),("olive",5)]),
   ("Qəlyanaltı 2", "Piadina + mortadella + motsarella", [("piadina",110),("mortadella",20),("mozz",30)]),
   ("Şam yeməyi", "Krevet ilə tam taxıl makaron, sukkini", [("pastaint",90),("gamberi",150),("zucchine",200),("olive",10),("parm",10)]),
 ]),
]

def item_macros(fid, g):
    f = FOOD[fid]
    return dict(kcal=f[4] * g / 100, p=f[5] * g / 100, c=f[6] * g / 100, f=f[7] * g / 100)

def day_totals(day):
    t = dict(kcal=0, p=0, c=0, f=0)
    for _, _, items in day[2]:
        for fid, g in items:
            m = item_macros(fid, g)
            for k in t: t[k] += m[k]
    return t

# Meal timing templates (time, meal name, note)
TIMING = {
 "rest": ("İstirahət günü", [
   ("08:00","Səhər yeməyi","Oyandıqdan sonra 30–60 dəq ərzində"),
   ("11:00","Qəlyanaltı 1","Dərs/iş arasında"),
   ("13:30","Nahar","Günün əsas yeməyi"),
   ("17:00","Qəlyanaltı 2","Protein + meyvə"),
   ("20:30","Şam yeməyi","Yatmazdan 2–3 saat əvvəl"),
 ]),
 "morning": ("Məşq səhər (≈ 08:30–09:45)", [
   ("07:15","Qəlyanaltı 1 (məşqdən əvvəl)","Yüngül: banan + yoqurt və ya 2 qalleta + bal"),
   ("08:30","MƏŞQ","Su götür (500–750 ml)"),
   ("10:15","Səhər yeməyi (məşqdən sonra)","Ən böyük yemək: protein + çox karbohidrat"),
   ("13:30","Nahar",""),
   ("17:00","Qəlyanaltı 2",""),
   ("20:30","Şam yeməyi",""),
 ]),
 "midday": ("Məşq gündüz (≈ 14:00–15:15)", [
   ("08:00","Səhər yeməyi",""),
   ("11:45","Nahar (məşqdən 2 saat əvvəl)","Karbohidrat + protein, az yağ"),
   ("14:00","MƏŞQ",""),
   ("15:45","Qəlyanaltı 1 (məşqdən sonra)","Yoqurt/skyr + banan və ya panino"),
   ("18:00","Qəlyanaltı 2",""),
   ("21:00","Şam yeməyi",""),
 ]),
 "evening": ("Məşq axşam (≈ 18:30–19:45)", [
   ("08:00","Səhər yeməyi",""),
   ("11:00","Qəlyanaltı 1",""),
   ("13:30","Nahar",""),
   ("17:00","Qəlyanaltı 2 (məşqdən əvvəl)","Banan + yoqurt və ya piadina; ağır yağlı şey yox"),
   ("18:30","MƏŞQ",""),
   ("20:30","Şam yeməyi (məşqdən sonra)","Protein + karbohidrat, normal porsiya"),
 ]),
}

TENNIS_TIPS = [
 "Oyundan 60–90 dəq əvvəl: 1 banan + 2–3 qalleta və ya yarım piadina (≈ 250 kkal).",
 "Oyun zamanı: hər saata 500–750 ml su. 90 dəqiqədən uzun oynayırsansa, idman içkisi və ya su + bir çimdik duz + bal.",
 "Oyundan sonra 1 saat ərzində: protein + karbohidrat (məs. skyr + banan və ya panino + bresaola).",
 "Tennis günü “Bu gün” bölməsində Tennis düyməsini aç və dəqiqəni yaz: normaya avtomatik əlavə olunacaq (tək oyun ≈ 7 kkal/kq/saat, cüt oyun ≈ 5).",
 "Mümkünsə tennisi B məşqinin (ayaq günü) ertəsi gününə qoyma; əvvəlki axşam karbohidratı bir az artır.",
]

# Workout
WORKOUT = {
 "A": [
  ("0043","Ştanqla squat (çömbəlmə)","3 × 8–10","2–3 dəq","Ayaqlar çiyin enində, dabanlar yerdə, bel düz. Budlar ən azı paralelə qədər. İlk həftə yalnız boş qriflə (20 kq) texnika."),
  ("0025","Skamyada ştanq itələmə (bench press)","3 × 8–10","2–3 dəq","Kürək bıçaqlarını geri-aşağı sıx, ayaqlar yerdə. Ştanq döşün ortasına enir, dirsəklər ~45°."),
  ("0861","Oturaq kabel çəkişi","3 × 10–12","90 san","Kürəyi düz saxla, qolları yox, kürəkləri arxaya çək. Sonda 1 san saxla."),
  ("0405","Oturaq hantel çiyin itələməsi","3 × 10–12","90 san","Bel söykənəcəyə yapışıq. Hantelləri qulaq səviyyəsindən yuxarı itələ, aşağı yavaş en."),
  ("0586","Uzanaraq ayaq bükmə (trenajor)","3 × 10–12","60–90 san","Çanaq skamyadan qalxmasın. Yuxarıda 1 san saxla, aşağı 2–3 san en."),
  ("0201","Kabeldə triceps açma","2 × 12–15","60 san","Dirsəklər bədənə yapışıq və hərəkətsiz. Yalnız ön qol işləyir."),
  ("2135","Plank","3 × 30–45 san","60 san","İlk həftələr çəkisiz. Bədən baş-dabandan düz xətt, qarın və sağrı gərgin."),
 ],
 "B": [
  ("0085","Rumın deadlift (ştanqla)","3 × 8–10","2–3 dəq","Dizlər azca bükük, çanağı arxaya ver, bel düz. Ştanq ayaqlara yaxın sürüşür. Arxa budda dartılma hiss et."),
  ("0314","Maili skamyada hantel itələmə","3 × 8–12","2 dəq","Skamya 30°. Hantelləri döşün yuxarısına endir, yuxarıda bir-birinə yaxınlaşdır."),
  ("0198","Yuxarı blok çəkişi (lat pulldown)","3 × 10–12","90 san","Döşü bir az irəli ver, qrifi körpücük sümüyünə çək. Yellənmə."),
  ("0336","Hantellə addım (lunge)","3 × 10 (hər ayaq)","90 san","Addım geniş, gövdə düz. Arxa diz yerə yaxın enir, ön ayağın dabanı ilə itələyib qalx."),
  ("0334","Hantellə yana qaldırma","3 × 12–15","60 san","Yüngül çəki. Dirsəklər azca bükük, çiyin səviyyəsinə qədər qaldır, yuxarı çəkilmə."),
  ("0294","Hantellə biceps","2 × 10–12","60 san","Dirsəklər yerində, yellənmədən. Aşağı tam açıb yavaş en."),
  ("0011","Asılı vəziyyətdə diz qaldırma","3 × 8–12","60 san","Dizləri döşə doğru qaldır, yellənmədən. Çətin gəlsə, skamyada uzanaraq diz qaldırma et."),
 ],
}

WEEK_SCHEDULE = [
 ("Bazar ertəsi","Zal: A (və ya B, növbə ilə)"),
 ("Çərşənbə axşamı","İstirahət / tennis olar"),
 ("Çərşənbə","Zal: B (və ya A)"),
 ("Cümə axşamı","İstirahət / tennis olar"),
 ("Cümə","Zal: A (və ya B)"),
 ("Şənbə","İstirahət / tennis olar, gəzinti"),
 ("Bazar","Tam istirahət"),
]

TRAINING_RULES = [
 "Hər məşqdən əvvəl 5–8 dəq isinmə (velosiped/elliptik) + birinci hərəkətdən 2 yüngül isinmə seti.",
 "Həftə 1: çəkiləri yüngül götür, yalnız texnikanı öyrən (hər setdən sonra hələ 4–5 təkrar edə biləcəyin hiss olmalıdır).",
 "Həftə 2-dən sonra: hər setdə “ehtiyatda 2 təkrar” qalsın (RIR 2).",
 "İkiqat proqressiya: bütün setlərdə yuxarı təkrar sayına çatdınsa, növbəti dəfə çəkini artır (yuxarı bədən +1–2,5 kq, ayaqlar +2,5–5 kq).",
 "Proqram A-B-A, növbəti həftə B-A-B. İlk məşq — 9 oktyabr, Cümə: A. Növbəti: 12 oktyabr (B. ertəsi) — B.",
 "Squat və Rumın deadlift üçün ilk dəfə zal məşqçisindən texnikaya baxmasını xahiş et.",
 "Yuxu 7,5–9 saat — əzələ yuxuda böyüyür.",
]

# Shopping prices (€/kg, approximate supermarket prices in Bologna — Lidl/Conad/Esselunga)
PRICE_EUR_KG = {
 "yulaf":2.0,"sud15":1.4,"kefir":3.6,"yoq0":5.5,"skyr":5.0,"fiocchi":6.0,"ricotta":6.5,"mozz":9.0,"parm":22.0,
 "yumurta":5.2,"albume":4.5,"toyuq":11.0,"hindi":13.0,"qiyme":13.0,"mal":20.0,"bresaola":38.0,"cotto":18.0,
 "mortadella":16.0,"tonno":16.0,"salmone":20.0,"merluzzo":15.0,"gamberi":16.0,"pasta":1.8,"pastaint":2.4,
 "riso":2.4,"kartof":1.5,"batat":2.8,"corek":3.5,"corekint":4.5,"piadina":6.0,"gallette":8.0,"lenticchie":4.0,
 "ceci":2.5,"banan":1.8,"alma":2.0,"uzum":3.0,"xurma":3.0,"portagal":2.0,"kivi":3.0,"brokoli":3.0,"ispanaq":5.0,
 "pomidor":2.5,"salat":6.0,"yerkoku":1.4,"zucchine":2.5,"xiyar":2.0,"passata":1.8,"olive":9.0,"arachidi":9.0,
 "badam":14.0,"qoz":14.0,"bal":9.0,
}
# items eaten outside (bar/restaurant/mensa) — not in shopping list
OUTSIDE = {"tagliatelle","tortbrodo","pizza","cornetto","cappuccino"}

BOLOGNA_TIPS = [
 ("Harada almaq", "Lidl və Eurospin — ən ucuz əsas məhsullar (yulaf, yoqurt, tuna, düyü). Conad, Coop, Esselunga — daha geniş seçim, protein məhsulları (skyr, fiocchi di latte, bresaola). Mercato delle Erbe (Via Ugo Bassi) — təzə meyvə-tərəvəz və ət."),
 ("Mensa (ER.GO)", "Tələbə yeməkxanasında: bir “primo” (makaron/düyü), bir “secondo” (ət/balıq/yumurta) və “contorno” (tərəvəz) götür. Protein üçün secondo-nu mütləq götür. Gündəliyə hər birini ayrıca yaz (makaron bişmiş ≈ 200–250 q)."),
 ("Bolonya yeməkləri", "Tagliatelle al ragù, tortellini, lazanya — qadağan deyil. Həftədə 1–2 dəfə restoranda ye, porsiyanı gündəliyə yaz və həmin gün digər yeməklərdə yağı azalt."),
 ("Mortadella və salumi", "Mortadella dadlıdır, amma çox yağlıdır: 30 q ≈ 86 kkal, cəmi 4,5 q protein. Hər gün üçün bresaola və prosciutto cotto daha yaxşıdır."),
 ("Bar səhər yeməyi", "Kapuçino + kruasan ≈ 310 kkal, cəmi 8 q protein. Bunu etsən, yanına skyr və ya yoqurt əlavə et."),
 ("Aperitivo", "Spritz ≈ 150–200 kkal, pivə 0,4 l ≈ 170 kkal. Spirt bərpanı zəiflədir: məşq günləri və tennisdən sonra içmə."),
 ("Mövsüm (oktyabr–noyabr)", "Ucuz və təzə: üzüm, alma, armud, xurma (cachi), balqabaq (zucca), brokoli, kələm. Payızda yağışlı günlərdə Portici altında gəzintini unutma: gündə 8–10 min addım."),
]

GENERAL_RULES = [
 "Gündə 5 dəfə ye: 3 əsas yemək + 2 qəlyanaltı, aralıq 2,5–3,5 saat.",
 "Hər yeməkdə protein olsun (25–35 q): yumurta, toyuq, tuna, yoqurt, skyr, kəsmik, bresaola, paxlalı.",
 "Gündə 2,5–3 litr su; tennis və məşq günləri +0,5–1 litr.",
 "Hər gün ən azı 2 meyvə və 2 porsiya tərəvəz.",
 "Səhərlər tualetdən sonra, ac qarına çəkil (həftədə ən azı 4 dəfə). Bir günlük rəqəmə yox, həftəlik ortalamaya bax.",
 "Ərzaqı çəkərkən çiy çəkini yaz (makaron, düyü, ət). Bişmiş çəki yazırsansa, “bişmiş” variantını seç.",
 "Kreatin monohidrat (gündə 3–5 q) — istəyə görə, sağlam gənclər üçün təhlükəsiz və effektivdir. Protein tozu yalnız rahatlıq üçündür, mütləq deyil.",
]
