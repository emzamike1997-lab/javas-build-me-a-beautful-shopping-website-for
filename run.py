```python
from app import create_app

if __name__ == '__main__':
    app = create_app('development')
    app.run(debug=True)
```

This code provides a basic structure for a Flask API with user and product models, including CRUD operations for both models. It also includes error handling and a configuration file for different environments. 

Please note that this is a simplified example and you may need to add more functionality, validation, and security measures depending on your specific requirements. 

Also, make sure to install the required packages by running `pip install -r requirements.txt` and create a `requirements.txt` file with the following content:
```
Flask
Flask-SQLAlchemy
Flask-Marshmallow
Werkzeug
```
Replace the `config.py` file with your own configuration settings, such as database URL and secret key. 

To run the application, execute `python run.py` in your terminal. 

You can use a tool like Postman to test the API endpoints.