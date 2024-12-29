from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def render_home():
    return render_template('home.html')

def ftoc(ftemp: float) -> float:
   return (ftemp - 32.0) * (5.0 / 9.0)

def ctof(ctemp: float) -> float:
    return (ctemp * 9. / 5. ) + 32

@app.route("/ctof")
def render_ctof():
    return render_template("ctof.html")


@app.route('/ctof_result')
def render_ctof_result():
    try:
        ctemp_result = float(request.args['ctemp'])
        ftemp_result = ctof(ctemp_result)
        return render_template('ctof_result.html', 
                               ctemp=ctemp_result, 
                               ftemp=ftemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route("/ftoc")
def render_ftoc():
    return render_template("ftoc.html")

def sort_strings(a,b,c):
  list_of_strings = [a,b,c]
  list_of_strings.sort()
  return list_of_strings

@app.route("/sort")
def render_sort():
    return render_template("sort.html")

@app.route('/sort_result')
def render_sort_result():
      a = request.args['a']
      b = request.args['b']
      c = request.args['c']
      result_as_list = sort_strings(a,b,c)
      return render_template('sort_result.html',
                              result = str(result_as_list))

@app.route('/ftoc_result')
def render_ftoc_result():
    try:
        ftemp_result = float(request.args['ftemp'])
        ctemp_result = ftoc(ftemp_result)
        return render_template('ftoc_result.html', 
                               ftemp=ftemp_result, 
                               ctemp=ctemp_result)
    except ValueError:
        return "Sorry: something went wrong."

@app.route('/ctof/<ctemp_str>')
def convert_ctof(ctemp_str):
    ctemp = 0.0
    try:
        ctemp = float(ctemp_str)
        ftemp = ctof(ctemp)
        return "In Celsius: " + ctemp_str + " In Fahrenheit " + str(ftemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ctemp_str + " to a number"


@app.route('/ftoc/<ftemp_str>')
def convert_ftoc(ftemp_str):
    ftemp = 0.0
    try:
        ftemp = float(ftemp_str)
        ctemp = ftoc(ftemp)
        return "In Fahrenheit: " + ftemp_str + " In Celsius " + str(ctemp) 
    except ValueError:
        return "Sorry.  Could not convert " + ftemp_str + " to a number"
    
@app.route("/some-route/<a>/<b>/<c>")    
def handle_some_route(a: str, b: str, c: str) -> str:
    return f"{a=} {b=} {c=}"

if __name__ == "__main__":
    app.run(host='0.0.0.0')