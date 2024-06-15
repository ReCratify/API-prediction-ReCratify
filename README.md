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
