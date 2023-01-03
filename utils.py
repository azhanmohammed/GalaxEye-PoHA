def popupTable(dataframe, row):
    chlorophyll = '%.6f'%dataframe["Chlorophyll"][row]
    dissolvedo2 = str('%.6f'%dataframe["DissolvedOxygen"][row])+" mg/l"
    ph = '%.6f'%dataframe["pH"][row]
    salinity = str('%.6f'%dataframe["Salinity"][row])+" ppt"
    turbidity = str('%.6f'%dataframe["Turbidity"][row])+" NTU"
    centroidCoordinates = ['%.6f'%dataframe["geometry"][row].centroid.x, '%.6f'%dataframe["geometry"][row].centroid.y] 
    
    html = """<!DOCTYPE html>
    <html>
    <head>
    <h4 style="margin-bottom:5"; width="300px">{}</h4>""".format("Pond Details") + """
    </head>
        <table style="height: 150px; width: 300px;">
    <tbody>
    <tr>
    <td style="padding-left: 5px;width:100px;background-color: """+ "#6573c3" +""";"><span style="color: #ffffff;">Coordinates</span></td>
    <td style="width: 150px;background-color: """+ "#6573c3" +""";"><span style="color: #ffffff;">{}</td>""".format(centroidCoordinates) + """
    </tr>
    <tr>
    <td style="padding-left: 5px;width:100px;background-color: """+ "#3f51b5" +""";"><span style="color: #ffffff;">Chlorophyll</span></td>
    <td style="width: 150px;background-color: """+ "#3f51b5" +""";"><span style="color: #ffffff;">{}</td>""".format(chlorophyll) + """
    </tr>
    <tr>
    <td style="padding-left: 5px;width:100px;background-color: """+ "#6573c3" +""";"><span style="color: #ffffff;">Dissolved Oxygen</span></td>
    <td style="width: 150px;background-color: """+ "#6573c3" +""";"><span style="color: #ffffff;">{}</td>""".format(dissolvedo2) + """
    </tr>
    <tr>
    <td style="padding-left: 5px;width:100px;background-color: """+ "#3f51b5" +""";"><span style="color: #ffffff;">pH</span></td>
    <td style="width: 150px;background-color: """+ "#3f51b5" +""";"><span style="color: #ffffff;">{}</td>""".format(ph) + """
    </tr>
    <tr>
    <td style="padding-left: 5px;width:100px;background-color: """+ "#6573c3" +""";"><span style="color: #ffffff;">Salinity</span></td>
    <td style="width: 150px;background-color: """+ "#6573c3" +""";"><span style="color: #ffffff;">{}</td>""".format(salinity) + """
    </tr>
     <tr>
    <td style="padding-left: 5px;width:100px;background-color: """+ "#3f51b5" +""";"><span style="color: #ffffff;">Turbidity</span></td>
    <td style="width: 150px;background-color: """+ "#3f51b5" +""";"><span style="color: #ffffff;">{}</td>""".format(turbidity) + """
    </tr>
    </tbody>
    </table>
    </html>
    """
    return html