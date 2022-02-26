"""Application entry point."""

### local-packages
from project import create_app

app = create_app()

if __name__ == "__main__":
    print("APPLICATION LINK: http://ec2-54-242-77-29.compute-1.amazonaws.com:5000/")
    app.run(host='0.0.0.0', port=5000)
