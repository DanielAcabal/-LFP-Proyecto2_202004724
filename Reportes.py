import webbrowser
class Reporte:
    def __init__(self) -> None:
        print("")
    def printTableToken(self,report,lis):
        report.write("""<div class="container"><table class="table">
                                <thead class="letra">
                                    <tr>
                                    <th scope="col">Token</th>
                                    <th scope="col">Lexema</th>
                                    <th scope="col">Fila</th>
                                    <th scope="col">Columna</th>
                                    </tr>
                                </thead>
                                <tbody class="letra">
                                """)
        for tok in lis:
            if tok.getTipo() != "Final":
                report.write("<tr><td>"+tok.getTipo()+"</td><td>"+str(tok.getLexema())+"</td><td>"+str(tok.getFila())+"</td><td>"+str(tok.getColumna())+"</td></tr>")
        report.write(""" </center></tbody>
                                </table></div>""")
    def printTableError(self,report,lis):
        report.write("""<div class="container"><table class="table">
                                <thead class="letra">
                                    <tr>
                                    <th scope="col">Carácter Desconocido</th>
                                    <th scope="col">Fila</th>
                                    <th scope="col">Columna</th>
                                    </tr>
                                </thead>
                                <tbody class="letra">
                                """)
        for tok in lis:
             report.write("<tr><td>"+str(tok.getLexema())+"</td><td>"+str(tok.getFila())+"</td><td>"+str(tok.getColumna())+"</td></tr>")
        report.write(""" </center></tbody>
                                </table></div>""")
    def reporteTokens(self,titulo,tokens):
        report = open("Reporte"+titulo+".html","w")
        report.write("<html><head><title>Reporte "+titulo+" </title>"+
        """<style>
        body{
        background: #b92b27;  /* fallback for old browsers */
        background: -webkit-linear-gradient(to top, #1565C0, #b92b27);  /* Chrome 10-25, Safari 5.1-6 */
        background: linear-gradient(to top, #1565C0, #b92b27); /* W3C, IE 10+/ Edge, Firefox 16+, Chrome 26+, Opera 12+, Safari 7+ */
        }
        .letra{
            color: White;
        }
        h1{
            color: White;
        }
        </style>
        <link href=\"https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css\" rel=\"stylesheet\" integrity=\"sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC\" crossorigin=\"anonymous\"><link rel=\"stylesheet\" href=\"style.css\"></link></head>""")
        report.write("<body><center><h1>Reporte de "+titulo+" </h1><br>")
        report.write("<br>")
        self.printTableToken(report,tokens)
        report.write("</body></html>")
        report.close()
        webbrowser.open("Reporte"+titulo+".html")