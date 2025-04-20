from flask import Flask, request

app = Flask(__name__)

place=['Japan', 'Korea', 'America', 'France' ,'Australia']
images={'Japan':'https://i.pinimg.com/564x/30/1c/fb/301cfb8885cd18b723c2b40da14824da.jpg', 'Korea':'https://i.pinimg.com/736x/28/ee/f1/28eef14b802392be220142041d69ce90.jpg', 'America':'https://i.pinimg.com/564x/8a/74/7a/8a747af5a7109e6e5120c21b9943dcbe.jpg', 'France':'https://i.pinimg.com/564x/a6/da/73/a6da735b32f6b3a89f3c06584b63dcb9.jpg','Australia':'https://i.pinimg.com/564x/37/cb/c7/37cbc7967422fb4e27f26c38de11ce06.jpg'}

@app.route('/')
def index():
  html='''
  <h1> Choose A Country to Travel </h1>'''
  html+='<p> You got a long vacation and wanted to visit another country. Which country would you like to go to the most? </p>'
  
  
  html+='''
  <ol>
  <li>{}</li><img src={} height=200>
  <li>{}</li><img src={} height=200>
  <li>{}</li><img src={} height=200>
  <li>{}</li><img src={} height=200>
  <li>{}</li><img src={} height=200>
  </ol>
  '''.format(place[0], images[place[0]], place[1], images[place[1]], place[2], images[place[2]], place[3], images[place[3]], place[4], images[place[4]])
  html+='''
  <p> Well Considered?</p>
  <a href="/form"> Click Here! </a>'''
  return html

@app.route('/form')
def form():
  html = '''<form action='/result', methods=['GET']>
  Your Name:<input type='text' name='name' required='required'><br><br>
  '''
  html+='''
  <label for="place" >You want to go to:</label>
  <select id="place" name='place'>
    <option value="Japan"> Japan </option>
    <option value="Korea"> Korea </option>
    <option value="America"> America </option>
    <option value="France"> France </option>
    <option value="Australia"> Australia </option>
  </select><br>'''

  html+='''
  <br>
  <h3> A few more questions! </h3>
  <ol>
  <li> What makes you choose this country? </li>
  <label for="a"><input type="checkbox" name="check" id="a" value="That I've never been there.">That I've never been there.</label><br>
  <label for="b"><input type="checkbox" name="check" id="b" value="The beautiful scenery.">The beautiful scenery.</label><br>
  <label for="c"><input type="checkbox" name="check" id="c" value="The local food.">The local food.</label><br>
  <label for="d"><input type="checkbox" name="check" id="d" value="The weather.">The weather.</label><br>
  <label for="e"><input type="checkbox" name="check" id="e" value="Some specific attractions.">Some specific attractions.</label><br>
  <label for="f"><input type="checkbox" name="check" id="f" value="My family members who live there.">My family members who live there.</label><br>
  
  <li> Which part of the country are you heading to? </li>
  <label for="capital">
  <input type="radio" name='part' id="capital" value="Capital"> The capital </label><br>
  <label for="metropolition">
  <input type="radio" name='part' id="metropolition" value="metropolitan"> Metropolitan areas outside the capital </label><br>
  <label for="country">
  <input type="radio" name='part' id="country" value="Country"> The country </label><br>

  <li> How many people will you travel with? </li>
  <label for="anypartners">I will travel with </label>
  <input type="number" name="number" id="anypartners" min="0" max="20"> people.<br>
  </ol>
  <br>
  <p>Ready?</p>'''

  html+='''<input type='submit'></form>'''
  
  return html

@app.route('/result', methods=['GET'])
def result():
  n = request.values.get('name')
  p = request.values.get('place')
  num = request.values.get('number')
  a = request.values.get('part')
  r = request.values.getlist('check')
  html = '''
  <h2> Details About Your Trip </h2>
  <p>Traveling with: {} people</p>'''.format(num)
  html+='<p> Area: {}</p>'.format(a)
  html += 'The reasons:<br>'
  for i in r:
    html +='<li>{}</li>'.format(i)
  
  html += '''
  <p> Wish you a nice vacation in {}, {}!</p><br>'''.format(p, n)
  for i in range(5):
    if(p == place[i]):
      html +='''<img src={} height="400" align="center">'''.format(images[place[i]])
    
  return html

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)