import pandas as pd
import streamlit as st
from pyecharts import options as opts
from pyecharts.charts import Pie
from streamlit_echarts import st_pyecharts
st.set_page_config(layout="wide")
from functions import *
import streamlit.components.v1 as components

st.markdown(f'''
    <style>
        section[data-testid="stSidebar"] .css-ng1t4o {{width: 14rem;}}
        section[data-testid="stSidebar"] .css-1d391kg {{width: 14rem;}}
    </style>
''',unsafe_allow_html=True)
st.write(
        """
        <style>
        [data-testid="stMetricDelta"] svg {
            display: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

df = pd.read_csv('for_streamlit.csv')

df2 = pd.read_csv('final.csv')
data = df2.groupby(['shop'], as_index=False).agg('sum')
data_pair = list(zip(data['shop'], data['houses_nearby']))
data_pair.sort(key=lambda x: x[1])
shops = pd.read_csv('final.csv')



st.sidebar.markdown("# Управление")


add_selectbox = st.sidebar.radio(
    "Выберите ритейлера",
    ("Общая статистика", "Дикси", "Пятёрочка", "Магнит", "Перекрёсток", "Лента", "Верный", "Вкустер")
)



config = {'displayModeBar': False}
#col1, col2 = st.columns(2)

if add_selectbox == "Общая статистика":

    fig = visualize_scatter(df, 'mapbox://styles/zoneofcomfort/clffhb0sf00ix01mru1o98kf0')

    col1, col2,col3,col4,col5,col6,col7 = st.columns(7)
    with col1:
        st.image('https://play-lh.googleusercontent.com/zWsmHqTC2roqBsZx1n3jLIlkrCPoAb6M0EMW0A6H-GPzCV61J6fTn8P6oSxx2AD9eZPT', width=100)
    with col2:
        st.image('https://abrakadabra.fun/uploads/posts/2021-12/1639269949_5-abrakadabra-fun-p-pyatorochka-logo-6.jpg', width=100)
    with col3:
        st.image('https://invest-brands.cdn-tinkoff.ru/RU000A0JKQU8x640.png', width=100)
    with col4:
        st.image('https://www.news-w.org/uploads/posts/2021-12/1640631734_900.jpg', width=100)
    with col5:
        st.image(
        'https://upload.wikimedia.org/wikipedia/commons/9/94/%D0%9B%D0%95%D0%9D%D0%A2%D0%90_%D0%BB%D0%BE%D0%B3%D0%BE.jpg', width=100)
    with col6:
        st.image('https://www.alladvertising.ru/porridge/83/101/h_7982190ee8f9aaf9165066e08ab27d85', width=100)
    with col7:
         st.image('https://yoplace.ru/media/chain/vkuster.jpg', width=100)




    st.text("")
    st.text("")
    st.text("")
    st.text("")

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('Данные продуктовые сети суммарно имеют:')

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric('Магазинов:', len(shops))
    with col2:
        st.metric('Домов в шаговой доступности:', len(df[df['Магазинов по близости'] != 0]), f"~{int(round(len(df[df['Магазинов по близости'] != 0])/len(df),2)*100)}% от жилищного фонда СПБ")
    with col3:
        st.metric('Квартир в этих домах:',df[df['Магазинов по близости'] != 0]['Квартир'].sum(), f"~{int(round((df[df['Магазинов по близости'] != 0]['Квартир'].sum()) / (df['Квартир'].sum()), 2)*100)}%")

    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")
    st.text("")

    data_pair0 = list(zip(shops.groupby(['shop'], as_index=False).agg('count')['shop'],
                          shops.groupby(['shop'], as_index=False).agg('count')['shop_name']))
    data_pair0.sort(key=lambda x: x[1])
    pie = (
        Pie(init_opts=opts.InitOpts())
        .add(
            series_name="Кол-во магазинов",
            data_pair=data_pair0,
            rosetype="radius",
            radius="80%",
            center=["50%", "50%"],
            label_opts=opts.LabelOpts(is_show=False),
        )
        .set_global_opts(
            title_opts=opts.TitleOpts(
                title="Магазины",
                pos_left="center",
                pos_top="1",
                title_textstyle_opts=opts.TextStyleOpts(color="#FFFFFF"),
            ),
            legend_opts=opts.LegendOpts(is_show=False),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            label_opts=opts.LabelOpts(color="rgba(0,0,0, 1)", font_size=20),
        )
    )
    st_pyecharts(pie, height=800)









    year = [df[df['Дикси'] == True]['Год постройки'].astype(int).median(),
            df[df['Пятёрочка'] == True]['Год постройки'].astype(int).median(),
            df[df['Магнит'] == True]['Год постройки'].astype(int).median(),
            df[df['Перекрёсток'] == True]['Год постройки'].astype(int).median(),
            df[df['Лента'] == True]['Год постройки'].astype(int).median(),
            df[df['Вкустер'] == True]['Год постройки'].astype(int).median(),
            df[df['Верный'] == True]['Год постройки'].astype(int).median()]

    apartment = [df[df['Дикси'] == True]['Квартир'].astype(int).median(),
                 df[df['Пятёрочка'] == True]['Квартир'].astype(int).median(),
                 df[df['Магнит'] == True]['Квартир'].astype(int).median(),
                 df[df['Перекрёсток'] == True]['Квартир'].astype(int).median(),
                 df[df['Лента'] == True]['Квартир'].astype(int).median(),
                 df[df['Вкустер'] == True]['Квартир'].astype(int).median(),
                 df[df['Верный'] == True]['Квартир'].astype(int).median()]

    names = ['Дикси', 'Пятёрочка', 'Магнит', 'Перекрёсток', 'Лента', 'Вкустер', 'Верный']
    from pyecharts import options as opts
    from pyecharts.charts import Bar, Line
    from pyecharts.faker import Faker

    colors = ["#5793f3", "#d14a61", "#675bba"]

    # Combine the names and apartment data into a single list
    data = list(zip(names, apartment))

    # Sort the data in descending order
    sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

    # Separate the sorted names and apartment data back into separate lists
    sorted_names, sorted_apartment = zip(*sorted_data)
    c = (
        Bar()
        .add_xaxis(sorted_names)
        .add_yaxis("Медианное количество квартир", y_axis=sorted_apartment, yaxis_index=0)
        .set_global_opts(
            xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(font_size=20)),
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                is_show=False,
                type_="value",
                min_=1000,
                max_=2021,
                position="right",

                axisline_opts=opts.AxisLineOpts(is_show=False,
                                                linestyle_opts=opts.LineStyleOpts(color='#ffffff', is_show=False)
                                                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} Год", is_show=False),
                splitline_opts=opts.SplitLineOpts(
                    is_show=False, linestyle_opts=opts.LineStyleOpts(opacity=1)
                ),
            ),
        )
        .extend_axis(
            yaxis=opts.AxisOpts(
                type_="value",
                min_=0,
                max_=90,
                position="left",
                axisline_opts=opts.AxisLineOpts(
                    linestyle_opts=opts.LineStyleOpts(color='#ffffff')
                ),
                axislabel_opts=opts.LabelOpts(formatter="{value} кв."),
                splitline_opts=opts.SplitLineOpts(
                    is_show=False, linestyle_opts=opts.LineStyleOpts(opacity=1)
                )
            )
        )
        .set_global_opts(
            yaxis_opts=opts.AxisOpts(is_show=False,
                                     type_="value",
                                     name="Медианный год постройки",
                                     min_=0,
                                     max_=90,
                                     position="right",
                                     axisline_opts=opts.AxisLineOpts(
                                         linestyle_opts=opts.LineStyleOpts(color=colors[0])
                                     )
                                     ),
            tooltip_opts=opts.TooltipOpts(trigger="axis", axis_pointer_type="cross"),
        )
        .set_series_opts(
            tooltip_opts=opts.TooltipOpts(
                trigger="item", formatter="{a} <br/>{b}: {c} ({d}%)"
            ),
            axisline_opts=opts.AxisLineOpts(
                linestyle_opts=opts.LineStyleOpts(color='#ffffff')
            ),
            label_opts=opts.LabelOpts(color="rgba(255,255,255, 1)", font_size=20),
        )
    )

    line = (
        Line()
        .add_xaxis(xaxis_data=sorted_names)  # Use the sorted names for the x-axis
        .add_yaxis(
            series_name="Медианный год постройки",
            y_axis=year,
            yaxis_index=1,
            label_opts=opts.LabelOpts(is_show=True, font_size=20, position="top"),
        )
    )

    z = c.overlap(line)

    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader('Они охватывают дома со следующими характеристиками:')


    chart = st_pyecharts(z, key=122134, width='100%', height=800)




    legend_html = '''
         <div style="position: fixed; 
                     bottom: 50px; left: 50px; width: 150px; height: 90px; 
                     border:2px solid grey; z-index:9999; font-size:55px;
                     background-color:white;
                     ">&nbsp; Legend <br>
                       &nbsp; Trace 1 &nbsp; <i class="fa fa-circle"
                       style="color:white"></i>
          </div>
             '''

    st.markdown("""
    <style>
    .custom-text {
        color: red;
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown("""
    ## Охват жилищного фонда <span class="custom-text">зонами 5-минутной шаговой доступности</span> продуктовых магазинов:
    """, unsafe_allow_html=True)
    # Display the legend in Streamlit

    st.plotly_chart(fig, use_container_width=True, config=config, key=0, height=1000)
if add_selectbox != "Общая статистика":
    st.title('Многоквартирные дома в 5 минутной шаговой доступности')
    if add_selectbox == "Дикси":
        st.image(
            'https://play-lh.googleusercontent.com/zWsmHqTC2roqBsZx1n3jLIlkrCPoAb6M0EMW0A6H-GPzCV61J6fTn8P6oSxx2AD9eZPT',
            width=50)

        fig = visualize_shop(df, 'mapbox://styles/zoneofcomfort/clffgdi8k006k01mxnf6tt5pz', 'Дикси')

        create_metrics('Дикси', df, shops)
        st.plotly_chart(fig, use_container_width=True, config=config, key=3)
    elif add_selectbox == "Пятёрочка":
        st.image('https://abrakadabra.fun/uploads/posts/2021-12/1639269949_5-abrakadabra-fun-p-pyatorochka-logo-6.jpg', width=50)
        fig = visualize_shop(df, 'mapbox://styles/zoneofcomfort/clffgnxgg003101qixz92eukn','Пятёрочка')
        create_metrics('Пятёрочка', df, shops)
        st.plotly_chart(fig, use_container_width=True, config=config, key=4, height=1000)
    elif add_selectbox == "Магнит":
        st.image('https://invest-brands.cdn-tinkoff.ru/RU000A0JKQU8x640.png', width=50)
        fig = visualize_shop(df, 'mapbox://styles/zoneofcomfort/clffgpzz800iv01mraftarvil', 'Магнит')
        create_metrics('Магнит', df, shops)
        st.plotly_chart(fig, use_container_width=True, config=config, key=5)
    elif add_selectbox == "Перекрёсток":
        st.image('https://pharmvestnik.ru/apps/fv/assets/cache/files/content/news/740/74007/front-jpg/front-z-400.jpg?time=1619167484', width=50)
        fig = visualize_shop(df, 'mapbox://styles/zoneofcomfort/clffgs90r00na01mof7t5xrgk', 'Перекрёсток')
        create_metrics('Перекрёсток', df, shops)
        st.plotly_chart(fig, use_container_width=True, config=config, key=6)
    elif add_selectbox == "Лента":
        st.image(
            'https://upload.wikimedia.org/wikipedia/commons/9/94/%D0%9B%D0%95%D0%9D%D0%A2%D0%90_%D0%BB%D0%BE%D0%B3%D0%BE.jpg',
            width=50)
        fig = visualize_shop(df, 'mapbox://styles/zoneofcomfort/clffgu4sm003301qip6ebpx2n', 'Лента')
        create_metrics('Лента', df, shops)
        st.plotly_chart(fig, use_container_width=True, config=config, key=7)
    elif add_selectbox == "Верный":
        st.image('https://www.alladvertising.ru/porridge/83/101/h_7982190ee8f9aaf9165066e08ab27d85', width=50)
        fig = visualize_shop(df, 'mapbox://styles/zoneofcomfort/clffgytjw004701qp2jzxv26a', 'Верный')
        create_metrics('Верный', df, shops)
        st.plotly_chart(fig, use_container_width=True, config=config, key=8)
    elif add_selectbox == "Вкустер":
        st.image('https://yoplace.ru/media/chain/vkuster.jpg', width=50)
        fig = visualize_vkuster(df, 'mapbox://styles/zoneofcomfort/cl80qc0e200no15rynhb4tcvs', 'Вкустер')
        create_metrics('Вкустер', df, shops)
        st.plotly_chart(fig, use_container_width=True, config=config, key=9)

#with col2:
#  st_pyecharts(pie)