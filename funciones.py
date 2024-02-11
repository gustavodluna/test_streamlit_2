import plotly.express as px
import plotly.graph_objs as go



paper_color= 'rgba(0,0,0,0)'
plot_color= 'rgba(0,0,0,0)'
paper_color_test= 'rgba(1,1,1,0.5)' 
plot_color_test= 'rgba(0,0,0,0)'



def saludar():
    print("saludar")
    print("saludar")
    print("saludar")
    print("saludar")
    print("saludar")
    print("saludar")
    print("saludar")
    print("saludar")
    return "saludo"


def indicadores(df):
    
    cant=len(df)

    


    casos_confirmados = go.Figure(go.Indicator(
                                    mode = "number",
                                    value = cant,
                                    title = {"text": "<span style='font-size:1.6em;color:gray'>Confirmados<br>",'font_size': 20},
                                    number = {'prefix': "",'font': {'size': 50}}, 
                                    domain = {'x': [0, 1], 'y': [0, 1]}
                                            )                          
                             )

    
    casos_confirmados.update_layout(title_font=dict(size=20, family="Times New Roman"),
                                   height=200,
                                  width=200,
                                  paper_bgcolor=paper_color,
                                    plot_bgcolor=plot_color
                                   )
    casos_confirmados.update_traces(number=dict(valueformat="f"))

    
    decesos=len(df[df['fallecido']==1])


    total_muertes = go.Figure(go.Indicator(
                            mode = "number",
                            value = decesos,
                             title = {"text": "<span style='font-size:1.6em;color:gray'>Fallecidos<br>",'font_size': 20},
                            number = {'prefix': "",'font': {'size': 50}}, 
                             domain = {'x': [0, 1], 'y': [0, 1]}
                                            )

                                  )
    total_muertes.update_traces(number=dict(valueformat="f"))

    total_muertes.update_layout(title_font=dict(size=35, family="Times New Roman"),
                                   height=200,
                                  width=200,
                                paper_bgcolor=paper_color,
                                    plot_bgcolor=plot_color
                               )


    let = go.Figure(go.Indicator(
    mode = "number",
    value = decesos/cant*100,
    title = {"text": "<span style='font-size:1.6em;color:gray'>Letalidad<br>",'font_size': 20}, # Aquí se especifica el tamaño del título
    number = {'prefix': "", 'suffix': "%", 'valueformat': ".2f",'font': {'size': 50}},
    domain = {'x': [0, 1], 'y': [0, 1]})
                        )

    
    let.update_layout(title_font=dict(size=10, family="Times New Roman"),
                               height=200,
                              width=200,
                            paper_bgcolor=paper_color,
                                    plot_bgcolor=plot_color
                           )

    
    
    return casos_confirmados,total_muertes,let