def json_to_html(input):
     html = '<table class="table table-striped" style="width:100%">'
     html+="<tr>"
     for key in input[0]:
          html+='<th>' + str(key) + "</th>"
     html+="</tr>"
     for row in range(0, len(input)):
          html+="<tr>"
          for key in input[row]:
               html+='<td scope="col">' + str(input[row][key]) + "</td>"
          html+="</tr>"
     html += "</table>"
     return html