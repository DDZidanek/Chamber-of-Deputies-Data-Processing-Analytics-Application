from .models.models_PaO import *
from .models.models_hl import *
import json
import pandas as pd
from sklearn.cluster import KMeans
from collections import Counter
from .functions import getPoslanecVsechny
import plotly.figure_factory as ff
import pandas as pd
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram, linkage, fcluster
import plotly.express as px
import plotly.graph_objs as go
from plotly.offline import plot
from scipy.spatial.distance import pdist, squareform

def GraphPoslanciVeStrane(poslanci_data):

    strany_counter = Counter([poslanec["strana"] for poslanec in poslanci_data])

    serazene_strany_data = strany_counter.most_common()

    graf_data = {
        "labels": [strana for strana, pocet in serazene_strany_data],
        "data": [pocet for strana, pocet in serazene_strany_data],
    }

    json_graph_data = json.dumps(graf_data)

    return json_graph_data

def genderGraph(poslanci):
    
    pocet_muzu = 0
    pocet_zen = 0

    for poslanec in poslanci:
        if poslanec["pohlavi"] == "Muž":
            pocet_muzu += 1
        elif poslanec["pohlavi"] == "Žena":
            pocet_zen += 1

    data_grafu = {
        "labels": ["Muži", "Ženy"],
        "values" : [pocet_muzu,pocet_zen]
    }

    return json.dumps(data_grafu)

def vek_poslancu_json(poslanci):
    
    veky = [poslanec["vek"] for poslanec in poslanci]

    return json.dumps(veky)

def vypocet_vysledku_hlasovani(poslanci):
    vysledky = {}
    
    for poslanec in poslanci:
        strana = poslanec["strana"]
        
        if strana not in vysledky:
            vysledky[strana] = {"Ano": 0, "Ne": 0, "Zdržel": 0, "Nepřihlášen": 0}
        
        vysledky[strana]["Ano"] += poslanec.get("hlasovani_ano", 0)
        vysledky[strana]["Ne"] += poslanec.get("hlasovani_ne", 0)
        vysledky[strana]["Zdržel"] += poslanec.get("hlasovani_zdrzel", 0)
        vysledky[strana]["Nepřihlášen"] += poslanec.get("hlasovani_neprihlasen", 0)
    
    return json.dumps(vysledky, ensure_ascii=False, indent=4)

def GraphStranyKraje(poslanci,):

    kraje_strany_pocty = {}

    for poslanec in poslanci:
        kraj = poslanec["kraj"]
        strana = poslanec["strana"]

        if kraj not in kraje_strany_pocty:
            kraje_strany_pocty[kraj] = {}

        if strana not in kraje_strany_pocty[kraj]:
            kraje_strany_pocty[kraj][strana] = 0

        kraje_strany_pocty[kraj][strana] += 1

    return json.dumps(kraje_strany_pocty)

def vypocet_json_funkci(poslanci):
    funkceJson = {}
    legenda = {}

    for poslanec in poslanci:
        raw_vybory = poslanec.get("vybory", "")
        raw_vybory_kratky = poslanec.get("vybory_kratky", "")

        if not raw_vybory.strip() or not raw_vybory_kratky.strip():
            continue

        funkceNazvyZkratky = [f.strip() for f in raw_vybory.split(";")]
        funkceNazvy = [z.strip() for z in raw_vybory_kratky.split(";")]
        
        for funkce, zkratka in zip(funkceNazvy, funkceNazvyZkratky):
            if funkce not in funkceJson:
                funkceJson[funkce] = 0    
            funkceJson[funkce] += 1
            legenda[zkratka] = funkce

    return json.dumps(funkceJson, ensure_ascii=False, indent=4), json.dumps({v: k for k, v in legenda.items()}, ensure_ascii=False, indent=4)


def vytvor_histogram_vyboru(poslanci):
    
    pocet_poslancu_podle_vyboru = {}

    for poslanec in poslanci:
        pocet_vyboru = poslanec.get("pocet_vyboru", 0)
        if pocet_vyboru in pocet_poslancu_podle_vyboru:
            pocet_poslancu_podle_vyboru[pocet_vyboru] += 1
        else:
            pocet_poslancu_podle_vyboru[pocet_vyboru] = 1

    data_pro_histogram = {
        "osa_x": list(pocet_poslancu_podle_vyboru.keys()),
        "osa_y": list(pocet_poslancu_podle_vyboru.values())
    }

    return json.dumps(data_pro_histogram, ensure_ascii=False)

def vytvor_histogram_zarazeni(poslanci,typ):
    
    pocet_poslancu_podle_vyboru = {}

    for poslanec in poslanci:
        pocet_vyboru = poslanec.get(typ, 0)
        if pocet_vyboru in pocet_poslancu_podle_vyboru:
            pocet_poslancu_podle_vyboru[pocet_vyboru] += 1
        else:
            pocet_poslancu_podle_vyboru[pocet_vyboru] = 1

    data_pro_histogram = {
        "osa_x": list(pocet_poslancu_podle_vyboru.keys()),
        "osa_y": list(pocet_poslancu_podle_vyboru.values())
    }

    return json.dumps(data_pro_histogram, ensure_ascii=False)


def histPoslanciVsechnyVO():

    poslanci = getPoslanecVsechny()

    poslancemDict = {}

    for poslanec in poslanci:

        poslancem = poslanec["pocetObsazeni"]

        if poslancem in poslancemDict:

            poslancemDict[poslancem] += 1
        else:
            poslancemDict[poslancem] = 1

    dataPoslancemDict = {
        "x" : list(poslancemDict.keys()),
        "y" : list(poslancemDict.values()),
    }

    print(dataPoslancemDict)

    return json.dumps(dataPoslancemDict)

def getHlasovaniPoslancu(poslanci_list):

    voting_data = []

    for poslanec in poslanci_list:
        foto = poslanec.get("foto")
        poslanec_id = poslanec.get("id_poslanec")
        strana = poslanec.get("strana")
        hlasovani_ano = poslanec.get("hlasovani_ano", 0) 
        hlasovani_ne = poslanec.get("hlasovani_ne", 0)    
        hlasovani_zdrzel = poslanec.get("hlasovani_zdrzel", 0)
        
        voting_data.append({
            "foto": foto,
            "poslanec_id" : poslanec_id,
            "strana": strana,
            "hlasovani_ano": hlasovani_ano,
            "hlasovani_ne": hlasovani_ne,
            "hlasovani_zdrzel": hlasovani_zdrzel
        })

    return voting_data



def plot_elbow_method(data_df):
    cluster_range = range(2, 11)
    inertias = []

    for n_clusters in cluster_range:
        kmeans = KMeans(n_clusters=n_clusters, random_state=10)
        kmeans.fit(data_df[['hlasovani_ano', 'hlasovani_ne', 'hlasovani_zdrzel']])
        inertias.append(kmeans.inertia_)

    fig = go.Figure(data=go.Scatter(x=list(cluster_range), y=inertias, mode='lines+markers'))
    fig.update_layout(
                      xaxis_title='Počet clusterů',
                      yaxis_title='SSE')
    
    graph_html = plot(fig, output_type='div', include_plotlyjs=True)

    return graph_html

def apply_kmeans(data_df, n_clusters):
    kmeans = KMeans(n_clusters=n_clusters, random_state=10)
    kmeans.fit(data_df[['hlasovani_ano', 'hlasovani_ne', 'hlasovani_zdrzel']])
    data_df['cluster'] = kmeans.labels_ + 1
    return data_df


def plot_dendrogram_with_plotly(data_df):
    data = data_df[['hlasovani_ano', 'hlasovani_ne', 'hlasovani_zdrzel']].values
    
    fig = ff.create_dendrogram(data, orientation='bottom', labels=data_df['strana'].tolist())
    fig.update_layout(title='Hiearchické clusterování',autosize=True,height = 600)
    
    graph_html = plot(fig, output_type='div', include_plotlyjs=True)
    
    return graph_html

def plot_sse_for_hierarchical_clustering(data_df):
    data = data_df[['hlasovani_ano', 'hlasovani_ne', 'hlasovani_zdrzel']].values
    
    Z = linkage(data, method='ward')
    distances = squareform(pdist(data, metric='euclidean'))
    
    cluster_counts = range(1, 11) 
    sse = []
    for k in cluster_counts:
        clusters = fcluster(Z, t=k, criterion='maxclust')
        sse_k = sum([(distances[row, :] ** 2).sum() for row in range(len(data)) if clusters[row] == k])
        sse.append(sse_k)

    fig = go.Figure(data=go.Scatter(x=list(cluster_counts), y=sse, mode='lines+markers'))
    fig.update_layout(title='SSE graf pro hierarchické shlukování',
                      xaxis_title='Počet shluků',
                      yaxis_title='SSE',
                      autosize=True)
    
    graph_html = fig.to_html(full_html=False, include_plotlyjs='cdn')
    return graph_html


def apply_hierarchical_clustering(data_df, n_clusters):
    data = data_df[['hlasovani_ano', 'hlasovani_ne', 'hlasovani_zdrzel']].values
    
    Z = linkage(data, method='ward')
    
    clusters = fcluster(Z, t=n_clusters, criterion='maxclust')
    
    data_df['cluster'] = clusters
    return data_df