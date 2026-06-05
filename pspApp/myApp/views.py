from django.shortcuts import render
from .functions import *
from .graphs import *
from scipy.cluster.hierarchy import linkage, dendrogram


def baseView(request):
    return render(request, "index.html")

def tableView(request):

    poslanci = []

    volebni_obdobi = getNazvyVolebnichObdobi()

    selected_obdobi = getVolebniObdobi(request)

    data = dataPoslanci(selected_obdobi)

    for poslanec in data.all():

        poslanci.append(createPoslanciDict(poslanec))

    return render(
        request,
        "tables.html",
        {
            "poslanci": poslanci,
            "volebni_obdobi": volebni_obdobi,
            "selected_obdobi": selected_obdobi,
            "graf_data": GraphPoslanciVeStrane(poslanci),
        },
    )


def chartView(request):

    poslanci = []

    volebni_obdobi = getNazvyVolebnichObdobi()

    selected_obdobi = getVolebniObdobi(request)

    data = dataPoslanci(selected_obdobi)

    for poslanec in data.all():

        poslanci.append(createPoslanciDict(poslanec))


    data_json, legenda_json = vypocet_json_funkci(poslanci)

    return render(
        request,
        "charts.html",
        {
            "poslanci": poslanci,
            "volebni_obdobi": volebni_obdobi,
            "selected_obdobi": selected_obdobi,
            "genderPieJson" : genderGraph(poslanci),
            "vekPoslancuJson": vek_poslancu_json(poslanci),
            "hlasovaniStranyJson" : vypocet_vysledku_hlasovani(poslanci),
            "vyboryJson": data_json,
            "legendaJson": legenda_json,
            "histogramVybory" : vytvor_histogram_zarazeni(poslanci,"pocet_vyboru"),
            "histogramPodvybory" : vytvor_histogram_zarazeni(poslanci,"pocet_podvyboru"),
            "histogramFunkce" : vytvor_histogram_zarazeni(poslanci,"pocet_funkci"),
            "kolikratPoslancem" : histPoslanciVsechnyVO(),
            "krajeGrafJson": GraphStranyKraje(poslanci),
        },
    )

def clusteringView(request):
    poslanci = []
    volebni_obdobi = getNazvyVolebnichObdobi()

    if request.method == 'POST':
        selected_obdobi = request.POST.get('id_obdobi')
    else:
        selected_obdobi = getVolebniObdobi(request)

    data = dataPoslanci(selected_obdobi)
    for poslanec in data.all():
        poslanci.append(createPoslanciDict(poslanec))

    hlasovani_poslanci_data = getHlasovaniPoslancu(poslanci)
    data_df = pd.DataFrame(hlasovani_poslanci_data)

    sc_graph_html = plot_elbow_method(data_df) if data_df.size > 0 else ""
    sse_hi_html = plot_sse_for_hierarchical_clustering(data_df)

    if request.method == 'POST' and 'num_clusters' in request.POST:
        n_clusters = int(request.POST.get('num_clusters', 3))
        clustering_method = request.POST.get('clustering_method', 'kmeans')
        if clustering_method == 'kmeans':
            modified_data_df = apply_kmeans(data_df, n_clusters)
            dendogram_html = None
        elif clustering_method == 'hierarchical':
            modified_data_df = apply_hierarchical_clustering(data_df, n_clusters)
            dendogram_html = plot_dendrogram_with_plotly(data_df)
            print(modified_data_df)
        poslaneci_cl = modified_data_df.to_dict('records')
    else:
        poslaneci_cl = None
        dendogram_html = None

    return render(
        request,
        "clustering.html",
        {
            "poslanci": poslanci,
            "volebni_obdobi": volebni_obdobi,
            "selected_obdobi": selected_obdobi,
            "sc_graph_html": sc_graph_html,
            "sse_hi_html": sse_hi_html,
            "poslaneci_cl": poslaneci_cl,
            "dendogram_html" : dendogram_html,
        },
    )


def testView(request):
    return render(request, "test.html")
