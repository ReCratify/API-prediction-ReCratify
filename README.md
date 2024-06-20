# ReCratify Machine Learning API

This is the documentation of The ReCratify Machine Learning API. It is a part of the Capstone Project "ReCratify" by C241-PS077 Bangkit Academy 2024 Batch 1.

```markdown
# Tech We Use in Capstone Project

- Tensorflow (Machine Learning Library)
- Flask (Python API Framework)
- numpy (Scientific Computing Library)
- Pillow (Image Processing Library)
- Compute Engine (API Deployment)
```

## Getting Started

To run this API on your local computer, follow these steps:

1. Clone this repository
   ```bash
    git clone https://github.com/ReCratify/API-prediction-ReCratify.git
    ```
2. Install the required depedencies
   ```bash
    pip install -r requirements.txt
    ```
3. Start the server
   ```bash
    python app.py
    ```
4. The API will be running on http://127.0.0.1:5000 
5. You can test the API using Postman or any other API testing tool.

## Endpoints

- **Predict**
  <pre>POST /predict</pre>
  <pre>Content-Type: multipart/form-data</pre>

  Request Body:

  ```json
  {
    "file": "waste-image.jpg"
  }
  ```

  Response Body:

  ```json
  {
    "response": {
      "code": 200,
      "data": {
        "confidence": 0.9954487681388855,
        "label": "Organic-Waste"
      },
      "error": false,
      "message": "Waste successfully predicted!"
    }
  }
  ```
