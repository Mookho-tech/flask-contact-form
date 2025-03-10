from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Route to display the contact form
@app.route("/", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        # Get form data
        name = request.form["name"]
        email = request.form["email"]
        message = request.form["message"]
        
        # Call the function to send email
        send_email(name, email, message)

        # Redirect to the thank you page after submitting
        return redirect(url_for('thank_you'))
    return render_template("contact.html")

# Thank you page after form submission
@app.route("/thank_you")
def thank_you():
    return "Thank you for reaching out! We will get back to you soon."

# Function to send email
def send_email(name, email, message):
    sender_email = "boitumelomercy@gmail.com"  
    receiver_email = "boitumelomercy@gmail.com"
    password = "5MomR#pE"

    # Create the email message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "New Contact Form Submission"

    # Body of the email
    body = f"Name: {name}\nEmail: {email}\nMessage: {message}"
    msg.attach(MIMEText(body, 'plain'))

    # Send email via SMTP (For Gmail)
    try:
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
    except Exception as e:
        print(f"Error sending email: {e}")

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
