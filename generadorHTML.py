def htmlHead():
    return """<!DOCTYPE html>
		<html>
		<head>
			<title>Factura Digital</title>
			<style type="text/css">
				body{
					font-family: courier;
					font-size: 14px;
					line-height: 0.9em;
					background-image: url('plantilla.jpg');
					width: 21.0cm;
					height: 29.7cm;
					background-repeat: no-repeat;
					background-size: 21.0cm, 29.7cm;	
				}

				ul{
					list-style-type: none;
					padding: 0;
					margin: 10px 0;
				}


				/*CAPÇALERA*/

				#infoFactura{
					position: absolute;
					text-align: center;
					top: 4.7cm;
				}
				#numFactura{
					position: absolute;
					left: 0.9cm;
				}
				#data{
					position: absolute;
					left: 3.4cm;
				}
				#numClient{
					position: absolute;
					left:6.6cm;
				}
				#infoClient {
					position: absolute;
					text-align: left;
					width: 9.3cm;
					top: 3.7cm;
					left:10cm;
				}
				#infoClient p{
					margin: 8px 0;
				}

				/*COS*/

				#cos{
					position: absolute;
					width: 19cm;
					height: 15.5cm;
					top: 8.8cm;
					left: 1cm;
				}

				.titolAlbara{
					position: absolute;
					font-weight: bold;"""

def cabezera(numFactura, data, numClient, nomClient, address, codiPostal, ciutat, provincia, nif):
	return """<div id="cabezera">
		<div id="infoFactura">
			<p id="numFactura">{}</p>
			<p id="data">{}</p>
			<p id="numClient">{}</p>
		</div>
		<div id="infoClient">
			<p id="nomClient">{}</p>
			<p id="address">{}</p>
			<p><span id="codiPostal">{}</span> <span id="ciutat">{}</span></p>
			<p id="provincia">{}</p>	
			<p>N.I.F.: <span id="nif">{}</span></p>
		</div>
	</div>""".format(numFactura, data, numClient, nomClient, address, codiPostal, ciutat, provincia, nif)

def article(referencia, descripcio, quantitat, preu, importa):
	return """<li><p><span class="referencia">{}</span>
						<span class="descripcio">{}</span>
						<span class="quantitat">{}</span><span class="preu">{}</span>
						<span class="import">{}</span>
					</p><br></li>""".format(referencia, descripcio, quantitat, preu, importa)

def albara(articles):
	articlesStr = ''

	for art in articles:
		articlesStr += article(art['referencia'], art['descripcio'], art['quantitat'], art['preu'], art['import'])

	return """<ul class="articles">{}
				</ul>""".format(articlesStr)