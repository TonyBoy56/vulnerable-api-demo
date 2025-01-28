from app import create_app

# Create the Flask app instance
app = create_app()

if __name__ == "__main__":
    # Run the Flask app
    app.run(
        host = app.config["HOST"],
        port = app.config["PORT"],
        debug = app.config["DEBUG"]
    )