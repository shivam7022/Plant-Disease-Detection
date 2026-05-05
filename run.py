from app import create_app
from app.models import db

app = create_app()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()          # create tables if they don't exist
        print("Database tables ready.")
    print("Plant Disease Detection Server starting...")
    app.run(debug=False, host='0.0.0.0', port=5000, use_reloader=False)
