from workingHoursLogger.app import db, create_app

# Run this file as module eg. python3 -m workingHoursLogger.create_db
app = create_app()
with app.app_context():
    db.create_all()