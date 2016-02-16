import time

@app.route('/')
def profile():
    """Render website's home page."""
    return render_template('profile.html')
 
@app.route('/time/')   
now = time.stfrtime("%c")
def timeinfo():
    print "Today is: " + time.strftime("%x")