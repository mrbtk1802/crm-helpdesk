from flask import Flask, render_template, request, redirect, url_for
from models import db, Ticket
import utils

app = Flask(__name__)
app.config.from_pyfile('config.py')
db.init_app(app)


with app.app_context():
    db.create_all()

@app.route('/')
def index():
    tickets = Ticket.query.all()
    return render_template('index.html', tickets=tickets)

@app.route('/ticket/new', methods=['GET', 'POST'])
def new_ticket():
    if request.method == 'POST':
        title = request.form['title']
        category = request.form['category']
        priority = request.form['priority']
        ticket = Ticket(title=title, category=category, priority=priority)

        db.session.add(ticket)
        db.session.commit()

        utils.send_notification(ticket)  # Simulated Apex-like trigger logic
        return redirect(url_for('index'))

    return render_template('new_ticket.html')

if __name__ == '__main__':
    app.run(debug=True)
