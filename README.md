# Python-stores-API

 This is an API returns and creates new stores, then appends to a master Stores list.
* **URL**

  <localhost:5000/store>

* **Methods:**
  
  `GET` | `POST`
  
*  **URL Params**


   **Required:**
 
   `/store`
   
   **Optional**
   `/store/<name>` or `/store/<name>/item`
   
* **Data Params**

  Note that I used Postman to supply POST data to the API. 
  If accessing the API from a browser then only the `GET` section applies.
  Using Postman, specify the *complete url and select the `POST` option. 
  Select `Content-Type` then `application-json`. Go to the body and input data using {}.
  Create a POST view for both `/store/<name>` or `/store/<name>/item`.

* **Success Response:**

  * **Code:** 200 <br />
    **Content:** `{
  "stores": [
    {
      "items": [
        {
          "name": "My Item", 
          "price": 15.99
        }
      ], 
      "name": "My Wonderful Store"
    }`
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{'message': 'store not found'}`

## Acknowledgements
This project was created for Udemy's Rest API's in Python course. Additionally, I did use iros' API README template and example to better guide my own efforts. Due credit goes to those sources.

## License
This repository is provided under the MIT License. If you would like to read what that entails, please refer to the [license](https://github.com/nortorious-flame89/Python-stores-API/blob/master/LICENSE) page in this repository.
