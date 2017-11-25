import folium
import pandas as pd
import branca.colormap as bcm
import numpy as np

def insert_code(df, tmp, topo_data):
    tmp = df.copy()
    tmp['code'] = ''
    for d in topo_data['objects']['countries1']['geometries']:
        if d['properties']['name'] == 'Bosnia and Herzegovina':
            tmp.loc['Bosnia-Herzegovina', 'code'] = d['id']
        if d['properties']['name'] == 'Cambodia':
            tmp.loc['Cambodia (Kampuchea)', 'code'] = d['id']
        if d['properties']['name'] == 'Democratic Republic of the Congo':
            tmp.loc['DR Congo (Zaire)', 'code'] = d['id']
        if d['properties']['name'] == 'Republic of the Congo':
            tmp.loc['Congo', 'code'] = d['id']
        if d['properties']['name'] == 'Guinea-Bissau':
            tmp.loc['Guinea', 'code'] = d['id']
        if d['properties']['name'] == 'Macedonia':
            tmp.loc['Macedonia, FYR', 'code'] = d['id']
        if d['properties']['name'] == 'Madagascar':
            tmp.loc['Madagascar (Malagasy)', 'code'] = d['id']
        if d['properties']['name'] == 'Romania':
            tmp.loc['Rumania', 'code'] = d['id']
        if d['properties']['name'] == 'Russia':
            tmp.loc['Russia (Soviet Union)', 'code'] = d['id']
        if d['properties']['name'] == 'Serbia':
            tmp.loc['Serbia (Yugoslavia)', 'code'] = d['id']
        if d['properties']['name'] == 'Myanmar':
            tmp.loc['Myanmar (Burma)', 'code'] = d['id']
        if d['properties']['name'] == 'Yemen':
            tmp.loc['Yemen (North Yemen)', 'code'] = d['id']
        if d['properties']['name'] == 'Zimbabwe':
            tmp.loc['Zimbabwe (Rhodesia)', 'code'] = d['id']
        if d['properties']['name'] == 'Myanmar':
            tmp.loc['Myanmar (Burma)', 'code'] = d['id']
        if d['properties']['name'] == 'Republic of Serbia':
            tmp.loc['Serbia (Yugoslavia)', 'code'] = d['id']
        if d['properties']['name'] == 'United Republic of Tanzania':
            tmp.loc['Tanzania', 'code'] = d['id']
        if d['properties']['name'] in tmp.index:
            tmp.loc[d['properties']['name'], 'code'] = d['id']
    return tmp

def my_color_function(df, feature, field, cm):
    """Maps low values to green and hugh values to red."""
    rate = df.loc[df['code'] == feature['id'], int(field)]
    if len(rate)>0: # check if the country is in the dataframe
        rate = float(df.loc[df['code'] == feature['id'], int(field)].values)
        return cm(rate)
    else:
        return cm(0)
    
def get_color_scale(df):
    l = list(set(pd.qcut(list(set(np.reshape(df.loc[:, df.columns != 'code'].values, (-1,)))), 10)))
    t = [a.left for a in sorted(l)]
    t.append(sorted(l)[-1].right)
    t[0]= 0
    cm = bcm.linear.YlOrRd
    cm = cm.to_step(index=t)
    cm.caption = 'Number of events'
    return cm

def build_map(df, topo_data, year, centro, legend):
    m = folium.Map(location=[50, 10], zoom_start=2, tiles='cartodbpositron')
    cm = get_color_scale(df)
    folium.TopoJson(topo_data, 'objects.countries1', style_function=lambda feature: {
            'fillColor': my_color_function(df, feature, year, cm),
            'fillOpacity':.7,
            'color' : 'black',
            'weight' : .7,
            'dashArray' : '2, 2'
            }).add_to(m)

    m_c = MarkerCluster().add_to(m)

    tmpp = df.loc[:, int(year)].drop_duplicates()
    for i in tmpp.index:
        n = i
        p = tmpp.loc[i]
        if p > 0:
            if n == 'Bosnia-Herzegovina':
                n = 'Bosnia and Herzegovina'
            if n == 'Cambodia (Kampuchea)':
                n = 'Cambodia'
            if n == 'DR Congo (Zaire)':
                n = 'Democratic Republic of the Congo'
            if n == 'Congo':
                n = 'Republic of the Congo'
            if n == 'Ivory Coast':
                n = "Cote d'Ivoire"
            if n == 'Macedonia, FYR':
                n = 'Macedonia'
            if n == 'Madagascar (Malagasy)':
                n = 'Madagascar'
            if n == 'Myanmar (Burma)':
                n = 'Burma'
            if n == 'Rumania':
                n = 'Romania'
            if n == 'Russia (Soviet Union)':
                n = 'Russia'
            if n == 'Serbia (Yugoslavia)':
                n = 'Serbia'
            if n == 'United States of America':
                n = 'United States'
            if n == 'Yemen (North Yemen)':
                n = 'Yemen'
            if n == 'Zimbabwe (Rhodesia)':
                n = 'Zimbabwe'
            long, lat = centro.loc[centro.name == n, 'long'].values[0], centro.loc[centro.name == n, 'lat'].values[0]
            folium.Marker([lat, long], popup='{} : {} {}'.format(n, p, legend) , icon=folium.Icon(color='green')).add_to(m_c)

    return m