## Getting Started

1. Clone
1. Activate virtualenv
1. Install dependencies
1. Run - `gunicorn __init__:app -b localhost:8000`
1. Navigate to [http://localhost:8000/](http://localhost:8000/) in your browser

## Structure

```sh
├── __init__.py
├── flask_flow_project
│   ├── __init__.py
│   └── views.py
└── requirements.txt
```

## What's happening?

When ran, you should see the following in your terminal:

```sh
outer __init__.py
inner __init__.py
route loaded!
```

1. When the server is ran, the outer *\_\_init\_\_.py* file is loaded, which imports the application instance from */flask_flow_project/\_\_init\_\_.py*.
1. From there the views are imported and when the end user requests the main route, `/`, a GET request is sent. This is handled by the router handler - `@app.route('/')` - and a response is sent.