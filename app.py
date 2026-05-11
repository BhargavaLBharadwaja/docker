from flask import Flask
app=Flask(__name__)
@app.route('/')
def home():
    return """
    <p>hello ! deocker executed successfully<p>
    <button onclick='windows.location.href='/page2'">
    go to second page
    </button>
    """
@app.route('/page2')
def page2():
      return """
    <p>another page<p>
    <button onclick='windows.location.href='/'">
    go to home
    </button>
    """
  
if __name__=="__main__":
    app.run(host='0.0.0.0',port=5003)
