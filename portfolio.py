from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Nécessaire pour les messages flash

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Simuler une action, ex: envoyer un email
        flash('Merci pour votre message, nous reviendrons vers vous bientôt.', 'success')
        return redirect(url_for('home'))

    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

