# 지도 새로 띄우기
import folium, re
import requests, json
from folium import plugins
from folium.features import DivIcon

color_list = [
    'beige',
    'black',
    'blue',
    'blueviolet',
    'brown',
    'burlywood',
    'cadetblue',
    'chocolate',
    'coral',
    'cornflowerblue',
    'darkblue',
    'darkcyan',
    'darkgoldenrod',
    'darkgreen',
    'darkmagenta',
    'darkolivegreen',
    'darkorange',
    'darkorchid',
    'darkred',
    'darksalmon',
    'darkseagreen',
    'darkslateblue',
    'darkslategray',
    'darkslategrey',
    'darkturquoise',
    'darkviolet',
    'deeppink',
    'deepskyblue',
    'dimgray',
    'dimgrey',
    'dodgerblue',
    'firebrick',
    'floralwhite',
    'forestgreen',
    'fuchsia',
    'gainsboro',
    'ghostwhite',
    'gold',
    'goldenrod',
    'gray',
    'green',
    'greenyellow',
    'grey',
    'honeydew',
    'hotpink',
    'indianred',
    'indigo',
    'ivory',
    'khaki',
    'lavender',
    'lavenderblush',
    'lawngreen',
    'lemonchiffon',
    'lime',
    'limegreen',
    'linen',
    'magenta',
    'maroon',
    'mediumaquamarine',
    'mediumblue',
    'mediumorchid',
    'mediumpurple',
    'mediumseagreen',
    'mediumslateblue',
    'mediumspringgreen',
    'mediumturquoise',
    'mediumvioletred',
    'midnightblue',
    'mintcream',
    'mistyrose',
    'moccasin',
    'navajowhite',
    'navy',
    'oldlace',
    'olive',
    'olivedrab',
    'orange',
    'orangered',
    'orchid',
    'palegoldenrod',
    'palegreen',
    'paleturquoise',
    'palevioletred',
    'papayawhip',
    'peachpuff',
    'peru',
    'pink',
    'plum',
    'powderblue',
    'purple',
    'rebeccapurple',
    'red',
    'rosybrown',
    'royalblue',
    'saddlebrown',
    'salmon',
    'sandybrown',
    'seagreen',
    'seashell',
    'sienna',
    'silver',
    'skyblue',
    'slateblue',
    'slategray',
    'slategrey',
    'snow',
    'springgreen',
    'steelblue',
    'tan',
    'teal',
    'thistle',
    'tomato',
    'turquoise',
    'violet',
    'wheat',
    'white',
    'whitesmoke',
    'yellow',
    'yellowgreen'
]


class MapFolium:
    
    def __init__(self):
        self.folium_icons = { 
            "icon" : ["gift", "home", "cloud", "bell", "camera", "comment",
                   "check", "heart", "user", "trash", "tags", "edit", "book", "bell"
                   "lock", 'leaf', 'heart', 'globe', 'flag', 'film', 'file'],
            "color" : ['red', 'purple', 'lightred', 'gray', 'black', 
                   'lightgray', 'green', 'pink', 'white', 'darkblue', 
                   'blue', 'darkgreen', 'lightblue', 'darkpurple', 
                   'darkred', 'beige', 'lightgreen', 'orange', 'cadetblue']}

    def plot(self, table, text='title', number='cluster', color='color',opacity=0.3, zoom=14):
        """rCircle Rounded Map Marker"""
        table = table[table['display']==True].reset_index(drop=True)
        map_data = folium.Map([table['lat'].mean(), table['lon'].mean()], zoom_start=zoom)
        color_map = ['blue','purple','darkred','green','black','darkgreen','darkpurple'] * 30  # ,

        # master_text, table = {"1":"A", "2":"B","3":"C"}, table.reset_index(drop=True)
        # color_master_map = {"1":"darkblue","2":"orange","3":"darkred"}
        # table["master"] = [str(_)  for _ in table["master"]]
        for no, _ in enumerate(range(len(table))): # 개별 데이터 Spot 찍기
            _table = table.iloc[_, :]        # Table Instance
            title = _table[text]             # 1. Title
            color_text = _table[color]       # 2. Marker Boarder Text Color
            number_text = str(_table[number])# 3. Marker Number
            popup_text = title               # 4. Title Popup
            
            # color_text = color_map[no]
            # color_text = color_map[_table['artist_no']]
            # title = f"{_table['artist_no']}-{_table['store']}"
            # popup_text = f"""{title}<br/>
            #     {_table['title']} ({_table['type']}) , {_table['name']} : {_table['phone']}<br/>
            #     {_table['address']} | {_table['addressraw']}"""
            # Text Div ICON 내용 정의하기
            marker_sytle = DivIcon(
                icon_size = (150,50),
                icon_anchor = (7,20),
                html = f'''<div style="font-size:15px;color:{color_text};
                font-weight:bold;margin-top:20px;margin-left:15px">{title}</div>'''
            )
            # Marker Icon Style 정의하기
            icon_style = plugins.BeautifyIcon(
                opacity = opacity,
                number = number_text,
                # number = master_text[_table['master']], # + "-" + title, # , 
                icon_shape   = "circle", 
                inner_icon_style = 'font-size:13px',
                border_color = color_text,
                # border_color = color_master_map[_table["master"]], 
                text_color = color_text, 
                border_width = 2)

            # Icon Marker 에 추가하기
            folium.Marker(
                [ _table['lat'], _table['lon']],
                # tooltip = popup_text, # 지도위 Text
                icon = icon_style).add_to(map_data)
            # 
            map_data.add_child(folium.Marker(
                [_table['lat'], _table['lon']],
                tooltip = popup_text,
                icon =marker_sytle,
            ))
        return map_data

            
    def plot_circle(self, table, title='atrist', zoom=14):
        
        """rCircle Rounded Map Marker"""
        map_data = folium.Map([table['lat'].mean(), table['lon'].mean()], zoom_start=zoom)
        master_text, table = {"0":"N", "1":"A", '2':"B",'3':"C"}, table.reset_index(drop=True)
        color_master_map = {'0':"black", '1':"darkblue",'2':"orange",'3':"darkred"}
        color_map = ['black','blue','purple','darkred','green'] * 30  # 'darkgreen','darkpurple',
        
        table["group"] = [str(_)  for _ in table["group"]]
        for _ in range(len(table)): # 개별 데이터 Spot 찍기
            _table = table.iloc[_, :]
            color_text = color_map[_table['cluster']]
            title  = f"{_table['cluster']}-{_table['store']}"
            manager = f"{master_text[_table['group']]}"
            popup_text = f"""{title}<br/>
                {_table['title']} ({_table['part']}) , {_table['name']} : {_table['telephone']}<br/>
                {_table['address']} | {_table['order']}"""
            # Text Div ICON 내용 정의하기
            marker_sytle = DivIcon(
                icon_size = (150,50),
                icon_anchor = (7,20),
                html = f'''<div style="font-size:15px;color:{color_text};
                font-weight:bold;margin-top:15px;margin-left:15px">{title}</div>'''
            )
            # Marker Icon Style 정의하기
            icon_style = plugins.BeautifyIcon(
                number = master_text[_table['group']], # + "-" + title, # , 
                icon_shape   = "circle", 
                inner_icon_style = 'font-size:13px',
                border_color = color_master_map[_table["group"]], 
                text_color = color_text, 
                border_width = 2)

            folium.Marker(
                [ _table['lat'], _table['lon']],
                tooltip = popup_text,
                icon = icon_style).add_to(map_data)
            map_data.add_child(folium.Marker(
                [_table['lat'], _table['lon']],
                tooltip = popup_text,
                icon =marker_sytle,
            ))
        return map_data



import matplotlib
import string
from collections import Counter
from sklearn.cluster import KMeans
from matplotlib import rcParams
from matplotlib import pyplot as plt
from matplotlib import colors as mcolors

class KMeansFunctions:
    
    def kmeans(self, table, clusters, display=True):
        r"""table 에 Cluster 구분 갯수에 따라 label 및 color 추가"""
        kmeans = KMeans(n_clusters = clusters, init ='k-means++') # 33명 구분 결과값 특정
        kmeans.fit(table.loc[:, ['lon', 'lat']])           # K means 학습모델 완성
        table['cluster'] = kmeans.fit_predict(table.loc[:, ['lon', 'lat']])
        table['cluster'] = list(map(lambda x : x+1 , table['cluster'])) # 0 을 지우고 1개씩 더하기
        # color_names = list(mcolors.cnames.keys())
        # color_names = ['blue','purple','darkred','green','black'] * 30 # ,'darkgreen','darkpurple']
        color_names = color_list
        table['color'] = [color_names[_]  for _ in table["cluster"]]
        if display:
            print(Counter(table['cluster']))
        return table

    def ploting_table(
        self, table, title='title', color='color',
        fig_size = (13,13),
        text_title='Kmeans Map', text_x ='위도', text_y='경도'):
        r""" """
        matplotlib.rc('font', family='NanumGothic')
        plt.rcParams['axes.unicode_minus'] = False
        fig, ax = plt.subplots(figsize=fig_size)
        table.plot(
            kind = 'scatter',
            x = 'lon', 
            y = 'lat', 
            s = 50, # marker size
            c = table[color],
            ax = ax
        ) # marker color by group
        for _ in table.index:
            ax.annotate(
                table.loc[_]['title'], 
                (table.loc[_]['lon'], table.loc[_]['lat']), 
                fontsize=10
            )
        plt.title(text_title, fontsize=20)
        plt.xlabel(text_x, fontsize=14)
        plt.ylabel(text_y, fontsize=14)
        plt.show()

        

# clustering 함수
def table_clusters(table, clusters, cluster_number):
    color_map = ['blue','purple','darkred','green','black','darkgreen','darkpurple'] * 30 
    # indexs = table[table['cluster'].isin(clusters)].index.to_list()
    indexs = clusters
    table.loc[indexs,'cluster'] = int(cluster_number)
    table.loc[indexs,'color'] = color_map[int(cluster_number)]
    table.loc[indexs,'display'] = False
    return table
        
    
# Index 로 label 추가함수
def table_index(table, index_list, cluster_number):
    table.loc[index_list,'label'] = int(cluster_number)
    table.loc[index_list,'display'] = False
    return table
    
# Naver 주소정보 수집기
def naver_address(address, latlon='127.1052133,37.3595316'):
    r"""Naver Cloud API 를 활용한 주소 상세정보 추출기
    :param address: 은천로 28, 봉일프라자 나-120
    :param latlon : 추출 기준이 되는 위도, 경도값
    :return: list 결과값 출력
    """
    # address  = ""
    url_head = 'https://naveropenapi.apigw.ntruss.com/map-geocode/v2/geocode?query='
    url      = f"{url_head}{address}&coordinate={latlon}"
    headers  = {
        "X-NCP-APIGW-API-KEY-ID" : "wstocuk035",
        "X-NCP-APIGW-API-KEY" : "Na6VgNttRRMbehOv6Uswfw8iYld2INbvZMvGBOHQ",    
    }
    resp = requests.get(url, headers=headers)
    resp = json.loads(resp.text)
    if resp['status'] == 'OK': # 상태값이 유효하고
        if resp['meta']['totalCount'] >= 1: # 결과값이 1개 이상일 떄
            return_keys = ['roadAddress', 'jibunAddress','englishAddress','x', 'y']
            return [resp['addresses'][0][_]  for _ in return_keys]
        else:
            return resp
    else:
        return resp
    

import requests 
import xml.etree.ElementTree as ET
from tqdm import tqdm

# 검색할 사업자번호
def check_tex(index):
    url = "https://teht.hometax.go.kr/wqAction.do?actionId=ATTABZAA001R08&screenId=UTEABAAA13&popupYn=false&realScreenId="
    post = "<map id=\"ATTABZAA001R08\"><pubcUserNo/><mobYn>N</mobYn><inqrTrgtClCd>1</inqrTrgtClCd><txprDscmNo>Biznum</txprDscmNo><dongCode>81</dongCode><psbSearch>Y</psbSearch><map id=\"userReqInfoVO\"/></map><nts<nts>nts>58cKuokaDhrUdtF8gFLDQZU6XMel7xRdgvDvT322quE47" 
    res = requests.post(url, data=post.replace("Biznum",Biznum)) 
    return ET.fromstring(res.text).findtext("trtCntn")


# folium Map 
def folium_map(table, title='label', tooltip="name", opacity=0.3):
    
    color_map = ['red', 'blue', 'purple', 'orange', 'green', 'black'] * 30
    color_map = {_:color_map[no]  for no, _ in enumerate(sorted(set(table[title].to_list())))}
    table = table.reset_index(drop=True)
    instance_map = folium.Map(  # tiles = 'Stamen Watercolor',
        [table['lat'].mean(), table['lon'].mean()], zoom_start = 14)
    
    for _ in range(len(table)):
        color = color_map[table.loc[_,title]]
        title_name = str(_) + "," + str(table.loc[_,title])
        icon_style = plugins.BeautifyIcon(
            number = title_name,
            icon_shape = "marker", inner_icon_style = 'margin-top:0;',
            border_color = color, text_color = color, border_width=2,
        )

        folium.Marker([
            table.loc[_,'lat'], table.loc[_,'lon']], 
            icon = icon_style).add_to(instance_map)
    return instance_map