# Bring your own vectors - Python complete sample
import weaviate
import json

client = weaviate.Client(
    url = "https://some-endpoint.weaviate.network",  # Replace with your endpoint
    auth_client_secret=weaviate.AuthApiKey(api_key="YOUR-WEAVIATE-API-KEY"),  # Replace w/ your Weaviate instance API key
)

# ===== Create schema =====
# Class definition object. Weaviate's autoschema feature will infer properties when importing.
class_obj = {
    "class": "Question",
    "vectorizer": "none",
}

# Add the class to the schema
client.schema.create_class(class_obj)

# ===== Import data =====
import requests
url = 'https://raw.githubusercontent.com/weaviate-tutorials/quickstart/main/data/jeopardy_tiny+vectors.json'
resp = requests.get(url)
data = json.loads(resp.text)

# Configure a batch process
client.batch.configure(batch_size=100)  # Configure batch
with client.batch as batch:
    # Batch import all Questions
    for i, d in enumerate(data):
        print(f"importing question: {i+1}")

        properties = {
            "answer": d["Answer"],
            "question": d["Question"],
            "category": d["Category"],
        }

        batch.add_data_object(properties, "Question", vector=d["Vector"])

# ===== Test import =====
schema = client.schema.get()
obj_count = client.query.aggregate("Question").with_meta_count().do()

assert "Question" in [c["class"] for c in schema["classes"]]
assert obj_count["data"]["Aggregate"]["Question"][0]["meta"]["count"] == 10

# ===== Query =====
nearVector = {
    "vector": [0.0042927247,-0.007413445,0.00034457954,-0.01897398,-0.00251218,0.020693844,-0.027351381,-0.008647864,-0.000042449385,-0.012337249,-0.006678342,0.0072608762,0.0051838635,-0.020555146,0.00017055604,0.028821588,0.047351733,-0.0045319796,0.008959935,-0.012323379,-0.008585449,0.022483058,0.0013869869,-0.01801696,-0.0014806085,0.01269093,0.021539906,-0.03592296,-0.0024116235,-0.012087591,0.014369184,-0.0019261781,-0.03506303,-0.028932547,-0.008162417,-0.026949156,-0.011782453,0.00049628125,0.018044699,0.011213789,0.014452403,0.028072614,-0.010957196,-0.0006033393,-0.008876716,-0.008079199,-0.011789389,-0.007517469,-0.028960286,-0.0059328363,0.006758094,0.021997612,-0.004521577,-0.015506513,-0.010208224,-0.014577232,-0.004726158,0.025714736,-0.0025104464,-0.016421925,-0.025922785,-0.00038467214,-0.021054462,0.019611996,-0.013315074,0.0014346646,-0.0017857456,0.01572843,-0.01003485,-0.008675603,0.02323203,0.0033079637,0.0056970487,-0.0129405875,0.035534605,-0.010769953,-0.023010112,-0.001464138,-0.008932196,0.015700692,0.010166614,-0.022483058,0.00788502,0.0029698857,0.018710453,0.0029768206,-0.014341445,0.008897521,-0.013141701,-0.037115768,0.0148546295,0.004067339,-0.0060680676,0.02529864,-0.027601039,0.021345729,-0.010721409,0.033676043,-0.0191959,-0.06807332,-0.009812932,0.015312335,-0.010825433,-0.018613365,-0.02110994,0.006248376,0.008550774,0.0044556954,0.023134941,-0.026990766,-0.010097264,0.021623125,-0.0070979055,-0.04798975,0.0006449489,-0.0011338618,0.0033894493,-0.011172179,0.0053641717,-0.010430141,0.021484427,-0.012885109,0.010298378,-0.013003002,0.019917132,0.010832367,-0.04235858,-0.010222093,-0.0017658077,0.009466185,0.023564907,0.01998648,0.0036928526,0.01162295,-0.022413708,0.016421925,-0.008842042,0.0043065944,-0.017503774,-0.031262685,0.007739387,0.033787,-0.040583238,-0.00029863563,0.003266354,0.025423469,0.012579971,0.023759086,0.0168935,0.0042996593,0.015437164,-0.0035125443,0.029043505,0.0031709988,-0.0038350187,-0.0030479038,-0.009889216,0.008696408,0.0022053092,0.003027099,-0.009507795,0.0028918677,0.012406598,-0.022344358,0.009695038,0.017462164,0.007059763,0.012316444,-0.0020596755,-0.019487167,-0.0132734645,0.038197618,-0.022385968,0.030153096,0.00017857457,0.019736823,0.010624319,0.0026023341,-0.014715931,0.0079405,-0.024965765,0.026200183,0.018627234,0.0108670425,-0.0010913853,0.009181853,0.01484076,-0.0072192666,0.031207206,-0.020638365,-0.004466098,0.016061308,0.0054855333,0.004379411,-0.6910524,-0.032178096,0.009660364,-0.005471663,0.012371923,0.0264221,0.007586818,-0.0030929807,-0.012434337,0.011678429,0.019320728,-0.0058392147,-0.009098634,-0.015132027,-0.013571667,-0.030014396,0.008328856,-0.03281611,0.008481425,0.002597133,-0.024008743,-0.0026543462,-0.009015415,-0.011983567,0.009154114,0.0044799675,0.018155659,-0.018821413,-0.008890586,-0.007989044,-0.0075729485,0.0119211525,-0.000356499,-0.0021550308,0.019487167,0.0044314233,-0.0039737173,0.028280662,0.021317989,0.043828785,-0.01319718,-0.030097615,0.0011035214,0.012815759,-0.022691106,0.028211314,0.016602233,-0.0020648767,0.023981003,0.015756171,0.012337249,0.0019556514,0.01583939,0.018710453,0.02334299,-0.0115536,0.017531514,-0.008946066,-0.0024619016,-0.0015447567,-0.010069525,0.0008317587,-0.014743671,-0.027295902,-0.02328751,0.027878437,-0.032483235,0.009743583,0.019917132,-0.010215159,0.022330489,0.022815935,-0.014604972,-0.0008096536,-0.0001595035,0.016075179,0.022372099,-0.0052601476,-0.015132027,0.0032004723,0.0068309107,-0.010083395,-0.02106833,-0.0066228625,0.028904807,-0.020915762,-0.007628428,0.010478686,0.0037240598,0.0037136574,0.014299835,0.02868289,0.0009223463,-0.0052428106,-0.014702061,0.009701974,-0.011810194,-0.0084952945,0.00659859,-0.013044612,-0.005218538,0.000095517884,0.021248639,0.010346922,0.011352488,0.0045909267,-0.004670678,0.020763194,0.044022962,-0.021539906,0.0077809966,-0.00095181976,-0.0062934533,0.010714474,-0.00017369844,-0.033592824,0.0066089923,-0.0025104464,0.021997612,-0.01805857,-0.0023474754,0.0060819373,0.006276116,-0.011962762,0.0061720917,0.01590874,-0.018946242,-0.020888023,-0.017670212,0.0003892232,0.017795041,0.013377489,0.011269269,-0.015464904,0.028252924,0.009681169,0.015534253,-0.020541277,0.010679799,-0.007836476,-0.027073985,-0.015561993,0.005603427,-0.0010081661,-0.013342814,-0.006154754,-0.022427578,-0.0022053092,-0.019279119,0.012933653,0.017448295,0.012815759,0.0019105745,0.028849328,0.034674674,-0.023689736,-0.0062449086,-0.0008872382,-0.0068690525,0.013516188,0.010561905,0.01814179,-0.018391447,0.003644308,-0.0026716834,-0.017032199,-0.0070181536,0.015173636,-0.0076006884,-0.04776783,0.01110283,-0.03919625,-0.015451034,0.010242898,0.011123635,0.0003929074,-0.017808912,0.01603357,0.021387339,-0.0055479477,-0.016297096,-0.0038107466,-0.020333229,-0.0032958277,0.018405316,0.0031796675,0.032316796,0.020555146,-0.004365541,0.012933653,0.009951631,0.02227501,0.0012266166,0.0085299695,0.019182028,0.009819867,0.0014468007,0.010020981,-0.0030704422,0.02314881,0.04449454,-0.00095702097,0.01794761,-0.011095895,0.0017319999,-0.042968854,-0.0022139777,-0.038197618,0.021595387,0.015437164,0.0070909704,-0.020236138,0.0027913111,-0.039473645,0.012614646,0.012316444,-0.009743583,0.001855095,-0.019681344,-0.009743583,0.00084866263,-0.017157027,0.00058080076,-0.00075634127,0.0057143862,0.017198637,0.011858738,0.012420468,-0.00026157705,-0.013849064,0.017420555,-0.0037517995,-0.001249155,0.0019539178,0.00023535434,0.02323203,0.013439903,-0.018987851,0.039751045,0.018641103,-0.0019660539,0.009119439,0.01319718,-0.0072678113,0.010464816,-0.008821237,0.016505145,0.008710277,0.0009656896,-0.0037726043,-0.006210234,-0.0020388707,-0.033620562,-0.001653115,0.01678254,-0.021359598,0.016297096,0.022857545,0.012240159,0.026935285,0.009743583,0.005721321,0.004119351,-0.0048717917,0.008821237,0.0018377576,0.00633853,-0.01159521,-0.023398468,0.008412075,-0.03287159,-0.022496928,0.0030635074,-0.01271867,0.009188788,0.021539906,-0.0035749588,0.0062969206,-0.008751887,-0.0121846795,-0.00661246,-0.0108670425,0.00954247,0.017517645,0.0061408845,-0.013509252,-0.012191615,-0.010485621,-0.00028606606,0.009965501,-0.01697672,0.0140640475,0.012538361,0.0042476472,-0.0034223902,-0.010804628,0.007732452,-0.014494013,-0.010423207,-0.0030756434,-0.0034657335,-0.0132387895,0.0005292222,-0.006678342,0.0117269745,0.008800432,-0.0062449086,-0.022427578,-0.018419186,-0.017795041,0.012288704,0.0028329208,-0.0077948663,0.0013878538,-0.0072192666,0.014604972,-0.008328856,-0.005766398,0.026852066,-0.0041505583,-0.019209769,-0.005579155,-0.02644984,-0.013682626,0.074231535,0.022982374,-0.011747779,0.04737947,0.0021376936,-0.023315249,-0.010811563,-0.0041366885,0.00527055,-0.01907107,0.006158222,-0.027060114,0.018280488,0.005957109,-0.011858738,0.0072539416,-0.014452403,-0.02220566,0.015326206,-0.0036928526,-0.017906,-0.024008743,0.0070008165,0.027129464,0.0033287685,0.0022798597,-0.0025416536,0.02231662,-0.006650602,-0.026269533,-0.003377313,0.0046360036,0.008536904,0.012462078,0.0075660134,0.019223638,0.016740931,0.0013055014,0.0001641629,-0.012545297,0.01585326,0.020929633,0.010069525,-0.018779803,0.0101042,-0.021775695,-0.0098476065,0.033481862,-0.00319007,-0.0024237595,0.019501036,0.006761561,-0.0073787705,-0.016879631,0.009403771,0.009112504,0.0047608325,0.015367815,-0.007177657,-0.00002692705,-0.027129464,-0.044217143,0.020444186,0.0017944142,0.0011052552,-0.009653429,-0.038475018,0.0013497117,-0.023592647,0.000589036,0.0035957636,-0.029820219,-0.00023080329,-0.022496928,0.008079199,-0.00632466,0.029293163,-0.011928087,0.0046810806,0.030125355,-0.0018932371,0.0013809188,-0.0026526125,-0.030069876,0.0044418257,0.0068447804,-0.0009275475,-0.0065188385,0.011401032,0.021900523,0.0061339494,0.004902999,0.02653306,0.005773333,-0.0012517556,0.00581841,0.01994487,0.020263879,-0.00839127,-0.012323379,0.0025728608,-0.023065591,-0.00661246,0.010485621,0.008210963,0.0032351469,0.0011980099,0.031290423,-0.014161136,0.007725517,0.028849328,-0.007049361,0.018155659,0.0148685,0.0041332208,0.019528776,0.0056450367,0.01801696,0.005246278,-0.0220947,-0.001432064,-0.028100355,0.013689561,0.017642474,-0.0050139576,-0.016796412,0.00212209,-0.016560623,-0.013849064,0.0007424714,-0.016089048,0.023967134,0.0030739098,-0.032677412,-0.03206714,-0.009986306,-0.019833913,0.021886652,-0.020818673,-0.011498122,0.0005365906,0.005274018,0.021914393,-0.023093332,-0.0018446926,-0.047240775,-0.01058271,-0.0022538537,-0.014923979,0.024674498,-0.013960023,-0.0022746585,-0.007864215,-0.010769953,-0.0071637873,-0.049238034,-0.022011481,-0.019958742,0.043745566,0.018641103,0.019847782,-0.016435795,0.01697672,0.016158398,0.0028953352,0.0068690525,0.004972348,0.013793585,-0.035867482,0.0191959,0.028655149,-0.006137417,0.017725693,-0.008897521,0.0023145343,0.04208118,-0.003514278,-0.020901892,-0.0026006005,-0.0135369925,-0.014098722,0.0072400714,-0.0021966405,0.014979458,-0.009244268,-0.001380052,0.006449489,-0.0015967686,-0.012108396,-0.019931002,0.03292707,-0.024521928,0.031013027,-0.017545383,-0.004667211,-0.009473121,-0.0020683443,-0.008536904,-0.002578062,0.008113873,0.0028294532,0.019736823,0.00086599996,0.0027965123,-0.0048059095,0.0063940096,-0.0034900059,-0.011525861,0.010624319,-0.014618842,0.010506426,-0.0016297096,-0.016200008,-0.03284385,0.0064078793,0.011241529,-0.0075452086,0.01693511,-0.0121846795,-0.010284508,0.038585976,-0.0045077074,0.013966958,-0.012808824,0.030985286,0.037726045,0.0015369549,-0.026796587,-0.008370466,-0.0013289069,-0.0003181401,0.02323203,0.0074689244,0.007621493,-0.027878437,0.0070181536,0.009154114,-0.012559166,-0.03706029,0.021803435,0.016297096,0.0012985665,-0.019778432,0.00033179327,-0.024951894,0.026297271,0.0065708505,-0.003065241,-0.013100091,-0.008516099,0.0007281681,0.009313617,0.0016600499,0.03270515,0.011879543,0.005801073,-0.012635451,-0.0038904983,-0.013044612,0.009459251,-0.0046845484,0.024050353,-0.01572843,0.0044834353,0.005048632,-0.0076769725,0.0003972417,-0.012469012,-0.004670678,0.03481337,-0.018322097,-0.0064182817,-0.011616015,0.02657467,0.019917132,0.010624319,-0.0038731608,-0.017725693,-0.026227923,-0.0062449086,0.022594016,0.023925524,0.0011884744,-0.012087591,-0.0014702061,-0.0063697374,-0.007857281,-0.0042615174,-0.000051063875,-0.015561993,-0.007808736,0.009944696,0.00954247,0.017808912,0.0052948226,-0.015783912,-0.0026543462,0.024660626,-0.02337073,0.027448472,-0.02117929,-0.016213877,-0.025423469,0.0069141295,-0.0012768948,-0.025173813,0.02539573,-0.017059939,-0.023551038,-0.012420468,-0.020901892,0.018211138,0.0026803522,-0.02016679,0.019667475,-0.01114444,0.017323466,-0.033287685,-0.043662347,0.023010112,-0.014396924,0.0055375453,0.0048891287,-0.011026545,0.009805998,0.014285965,0.013183311,-0.006137417,-0.024840936,-0.017184768,-0.026075354,0.020846413,-0.00029235083,-0.022066962,-0.013786649,-0.011511991,-0.012656256,0.012045981,0.0026283402,-0.0051838635,-0.0026664822,-0.008259507,0.023981003,0.011858738,-0.021623125,-0.0034657335,-0.0028936013,-0.010707539,-0.023426209,0.0075244037,-0.00037773722,0.030319534,0.0071707224,-0.0052358755,-0.018322097,0.010138874,-0.024147442,-0.018710453,0.024410969,0.005291355,0.021872783,0.0001582032,0.0069279997,0.0029109388,-0.0015733633,0.015284596,-0.026685627,-0.0052636154,0.0025173812,-0.006130482,0.02231662,-0.009133309,-0.010978001,-0.023981003,0.021581516,-0.007063231,0.0048925965,0.00223825,-0.004847519,0.0050659697,-0.0082664415,0.023634257,0.010430141,0.014244355,0.015367815,-0.019501036,-0.009930826,0.013301204,-0.015340075,-0.024757717,-0.008065329,-0.016338706,-0.008751887,0.036366798,-0.011574405,-0.0129405875,0.022108572,-0.010326117,0.015783912,0.018821413,-0.0024358958,0.0066401996,0.0016513813,-0.007878086,-0.014369184,-0.0057109185,-0.027642649,-0.0047296253,0.014729801,-0.00065751845,0.020763194,-0.01210146,0.0009795595,-0.013349749,-0.0024653692,-0.024258401,-0.0013471111,-0.0051630586,0.015298465,0.021650866,-0.02314881,-0.02427227,0.0000668571,-0.018322097,-0.007933565,-0.011498122,0.010908652,-0.0074758595,0.0090570245,0.005100644,-0.018419186,-0.014383054,-0.0051457216,0.012788019,-0.022843674,-0.010138874,0.17021103,-0.031345904,0.0020614092,0.024091963,-0.004341269,0.005180396,0.019182028,-0.0011312612,0.0013644483,0.016408054,0.0028173171,-0.0062379735,-0.01106122,0.00850223,0.008897521,-0.0047747022,-0.02334299,-0.012801889,-0.0202084,-0.014181941,0.0033305022,-0.0015196175,-0.0083011165,-0.03167878,0.031123986,0.0016505144,-0.01003485,-0.021997612,0.004341269,-0.0058946945,-0.011241529,-0.016477404,-0.00028324872,-0.009785193,-0.019639734,0.0076561677,-0.0029525484,0.0037275273,0.016477404,0.00036668466,0.0036720478,0.010783823,0.029209943,-0.027573299,0.0009691571,0.034646932,-0.0055652848,-0.017906,0.009133309,0.01592261,-0.031651042,0.01803083,-0.0057906704,0.032400016,0.0072955512,-0.0072539416,0.013030742,0.0019747226,0.006775431,0.023564907,-0.027143333,0.01586713,-0.018585624,0.018114049,-0.01059658,0.010360792,-0.011310878,0.010125005,0.0028398556,-0.015312335,-0.015104287,-0.0025936656,-0.022066962,0.010395466,-0.028128095,-0.019889392,0.041581865,0.0356733,0.0190572,0.010055655,0.000041853415,0.0025919317,-0.018918501,-0.022372099,-0.010749148,-0.027198814,0.015284596,0.020263879,-0.014937849,0.01803083,-0.019556515,-0.0023925523,-0.020569015,-0.024008743,0.010201288,0.018086309,-0.006560448,0.030402754,-0.029154465,0.0106381895,-0.028627409,0.016768672,0.03181748,0.0007095305,-0.0006332462,0.0031467266,-0.027184943,0.0055340775,0.0022573213,-0.018710453,0.0006384474,-0.017378947,-0.005128384,-0.008398206,0.0022642561,0.019806173,0.0023682802,-0.016283225,0.0190572,-0.013190245,-0.015007198,-0.010229029,0.0122193545,0.011331683,-0.008516099,-0.007989044,-0.014188876,0.018238878,0.009043154,-0.040444538,-0.011213789,-0.0019383142,0.0014476676,-0.006449489,-0.017254118,-0.0006939269,-0.018835282,-0.013703431,-0.02434162,0.011747779,-0.0025364524,0.0007021621,-0.0036339057,0.007489729,-0.0034848046,-0.014951719,0.03167878,0.012753344,-0.005176929,-0.022732716,-0.016505145,-0.005097177,-0.026255662,-0.008842042,0.010887847,-0.000096547294,-0.00951473,-0.03481337,0.0070146862,0.007975175,-0.022427578,0.0053086923,0.03511851,-0.012302574,0.013335879,-0.018654974,-0.18252748,0.0028346544,0.024577407,-0.029709259,0.027864566,0.025797956,0.002408156,-0.0002698123,0.005759463,0.0030877795,0.012801889,0.0074550547,-0.04152639,-0.0018689649,-0.012857368,-0.0084952945,-0.000054964774,0.011331683,0.0029178737,0.010804628,0.023828436,-0.020693844,0.011498122,-0.022774326,0.007115243,0.018405316,0.0005461261,0.009327487,-0.0040846765,-0.028544191,-0.010686734,-0.018488536,0.017281856,-0.0012309508,-0.0150488075,0.014799151,-0.011872608,-0.027711999,-0.01708768,0.008321921,0.0059120315,0.040860634,0.013446838,-0.0037483322,0.005152656,0.012073721,0.009001545,0.012788019,0.027351381,-0.026366621,0.0042337775,-0.0018013492,0.0030756434,0.005430054,0.033315424,0.0012734274,-0.043939743,0.025950525,-0.02099898,-0.006151287,-0.021012852,-0.028433232,0.020721585,-0.016879631,-0.010520295,-0.0135369925,-0.024258401,0.0103746625,-0.019931002,0.003027099,0.008204027,-0.013176376,0.024716107,-0.012919783,0.0058808243,-0.0012612912,0.0066540698,0.010811563,-0.0015248187,-0.0140640475,-0.02228888,0.025978265,-0.012489817,-0.018807542,0.0085646445,-0.0014832091,-0.0016305764,0.0018308227,-0.007056296,-0.016019698,0.0046186666,-0.024091963,-0.018738193,-0.021470558,0.01482689,0.027947785,-0.007850346,0.012288704,-0.0026976895,-0.014563362,0.014175006,-0.00047027523,-0.0048856614,0.011505056,0.04760139,-0.0046498734,0.019667475,-0.008536904,0.027975526,0.0023006645,-0.009570209,-0.0010359058,0.012018242,0.035867482,-0.0077671264,0.007760192,-0.012510622,-0.01159521,0.0038731608,-0.009951631,0.040943854,-0.0036616453,-0.0190572,0.0127464095,0.0006341131,-0.015353945,-0.10768566,-0.02848871,-0.00011756881,0.02644984,-0.011935023,0.021942133,-0.031207206,0.014674322,0.0074273148,0.031872958,-0.019445557,-0.002134226,-0.01893237,-0.010097264,0.0011399299,0.007933565,-0.0043308665,-0.009882282,-0.0069349343,0.036810633,0.005305225,-0.0076492326,0.006054198,0.014563362,-0.011401032,0.011851803,-0.0024896415,0.03706029,0.008349661,-0.0019209769,0.002571127,-0.019778432,0.007760192,-0.032316796,-0.008356596,0.0006618528,-0.014618842,-0.014341445,0.016047439,-0.0033374373,0.02314881,0.007205397,0.021207029,-0.017739562,0.011435707,-0.013710366,0.0012274834,0.004719223,-0.0022642561,-0.026963025,-0.010360792,0.00084172765,-0.018474666,-0.00082742434,0.0093899015,-0.013107026,-0.0028727967,0.02002809,-0.009632624,-0.0014754073,0.010353858,0.0016383782,-0.0068933247,0.04435584,0.008363531,-0.015742302,-0.02321816,-0.026130833,0.027850697,-0.023509428,0.016019698,0.03256645,-0.025936656,0.011151374,-0.019306857,0.0129405875,-0.016671583,0.010548036,0.02013905,-0.022815935,-0.009126374,-0.019140419,0.016130658,-0.020804804,0.026644018,0.011588275,-0.005128384,-0.006664472,0.008086134,0.002212244,-0.0153816845,0.008294182,0.021415077,-0.009854542,-0.0032299457,-0.0010731812,-0.01482689,-0.027309772,0.00066098594,0.010450946,-0.012316444,-0.007871151,-0.072456196,0.0009197457,0.008204027,-0.005371107,0.017628603,0.0020267346,0.005381509,-0.0079405,0.009896152,0.02965378,-0.015298465,0.018322097,-0.0013601141,-0.02432775,-0.019140419,-0.028294533,0.035534605,0.02016679,0.020041961,0.015312335,0.022663366,-0.0050798394,0.037975702,0.0039355755,-0.023856174,-0.007822606,-0.0023162682,0.010215159,-0.013897609,-0.028031005,0.01055497,-0.011338618,-0.00012883807,0.026865937,0.0074550547,-0.017434426,0.014077917,0.00034067867,-0.00013642316,0.06025071,-0.02525703,-0.03620036,-0.0070909704,-0.009438446,0.01215694,0.01800309,-0.027004635,0.02009744,0.0064529567,-0.01316944,0.0061998316,0.013550862,-0.02119316,-0.034646932,-0.012045981,-0.010409337,0.019681344,0.0080029145,0.011935023,-0.0077879312,0.028155833,0.048433583,0.0026526125,0.00042476473,-0.014168072,-0.00633853,-0.009230398,-0.008162417,0.012371923,-0.030957548,-0.0200697,-0.00948699,0.0026335414,0.005031295,0.019098809,-0.008308051,-0.02319042,0.008959935,-0.0030635074,0.028627409,0.025548298,0.016269356,-0.016574493,0.026741108,0.023634257,0.024993503,-0.01678254,0.009029285,0.012045981,0.0071637873,-0.007961305,0.015756171,0.0061270148,-0.003606166,0.026810456,0.014660452,-0.005825345,-0.014230486,0.005142254,0.0134676425,-0.014660452,-0.007080568,0.0054508587,-0.020555146,-0.0020926164,-0.0039667827,-0.026158573,-0.042663716,-0.009570209,0.013980828,0.019681344,0.004802442,-0.010721409,0.006702614,-0.025492819,0.016089048,-0.006990414,-0.01798922,-0.018169528,0.037753783,0.021359598,0.011775519,0.023634257,0.010936392,0.00850223,0.01214307,0.028877066,-0.0057698656,0.0021671671,0.0044140858,0.012801889,-0.008807367,-0.029293163,-0.010229029,-0.0018134854,-0.023842305,0.0101458095,0.017739562,-0.029431863,0.047934268,0.0026266065,-0.004015327,0.016089048,-0.02205309,0.012337249,0.014244355,0.020360967,-0.04260824,-0.010797693,0.009070895,-0.0006332462,0.0036789828,-0.0140293725,-0.032122616,-0.0036893853,-0.01904333,0.019265248,0.002271191,-0.0055132727,-0.0018464263,-0.0055028703,0.029764738,0.009327487,-0.02868289,-0.0085646445,0.014168072,-0.0011243263,-0.0057109185,-0.024022613,0.028932547,0.0028450568,-0.04629762,-0.011338618,0.0070250886,-0.00013393092,-0.021720216,-0.007961305,0.012801889,0.028072614,-0.0042407126,0.018682713,-0.019722953,-0.022538537,-0.0032507505,0.010645124,-0.021803435,-0.020763194,-0.025992135]
}

result = client.query.get(
        "Question", ["question", "answer", "category"]
    ).with_near_vector(
        nearVector
    ).with_limit(2).with_additional(['certainty']).do()

print(json.dumps(result, indent=4))

# ===== Test query results =====
assert len(result["data"]["Get"]["Question"]) == 2
assert result["data"]["Get"]["Question"][0]["answer"] == "DNA"

client.schema.delete_class("Question")  # Cleanup after
