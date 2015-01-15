from bottle import run, template, static_file, view, Bottle, request
from sys import argv
import json
import pe
import fit
import codecs

app = Bottle()

@app.route('/export')
@view('export')
def export():
	return { 'get_url':  app.get_url } 

@app.route('/import')
@view('import')
def export():
	return { 'get_url':  app.get_url } 

@app.route('/')
@app.route('/attributes')
@view('attributes')
def attributs():
	return { 'get_url':  app.get_url } 

@app.route('/questions')
@view('questions')
def questions():
	return { 'get_url':  app.get_url } 

@app.route('/ajax', method="POST")
def ajax():
	reader = codecs.getreader("utf-8")
	query = json.load(reader(request.body))

	if query['type'] == "question":
		if query['method']=='PE':
			return pe.PE(float(query['min_interval']),float(query['max_interval']),float(query['proba']), int(query['choice']))
		else:	
			return query['method']
	elif query['type'] == "calc_util":
		return fit.regressions(query['points'])


@app.route('/static/:path#.+#', name='static')
def static(path):
	return static_file(path, root='static')

#run(app, host='localhost', port=8080, debug=True)
app.run(host='0.0.0.0', port=argv[1])
