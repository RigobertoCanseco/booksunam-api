# API for find books of the National Autonomous University of Mexico (UNAM)
*Api not official, site web of [libraries of UNAM](http://bibliotecas.unam.mx/)* 

[URL] http://bapi-rgcn.rhcloud.com/api/{version api}/  
[VERSION API] v1
## API
Start a local webserver by running:

```bash
python flaskapp.py
```

## API Documentation

Add Token-Client header in all request
* Token-Client : 

**Accounts**
----
  Operations for accounts

**Books**
----
  Operations for books
  * Barrow books
  * Favorites books
  * New books
  * Available books

**Clients**
----
  Operations for clients

**Devices**
----
  Operations for devices

**Libraries**
----
  Operations for libraries
  
**Notifications**
----
  Operations for notifications

**Professions**
----
  Operations for professions

**Schools**
----
  Operations for schools

**Search**
----
  Operations for search
  
**Users**
----
  Operations for users 
  
**Example**
----
  Example
    
***Find user by Id***

* **URL**

  /users/:id

* **Method:**

  `GET`
  
*  **URL Params**

   **Required:**
 
   `id=[integer]`

* **Data Params**

  None

* **Body**<br/>
```
{
  "school_id": "2398aa6a722d171da04ca3806e6b2d4d",
  "name": "Rigoberto",
  "lastname": "Canseco",
  "mail": "cansecorigoberto@gmail.com",
  "password": "12345678",
  "account_number": "413113054",
  "genre": "male"
}
```

* **Success Response:**

  * **Code:** 200  
    **Content:** <br/>
    ```
    {
      "status": 1,
      "update_time": "2017-07-17T20:20:35+00:00",
      "name": "RIGOBERTO",
      "lastname": "CANSECO",
      "creation_time": "2017-07-17T20:20:35+00:00",
      "school": {
        "website": null,
        "status": 1,
        "update_time": "2017-06-11T00:38:26+00:00",
        "name": "FES Aragón",
        "creation_time": "2017-06-11T00:38:26+00:00",
        "telephone": null,
        "longitude": null,
        "latitude": null,
        "address": null,
        "active": true,
        "mail": null,
        "type": 1,
        "id": "2398aa6a722d171da04ca3806e6b2d4d"
      },
      "id": "285f07693099f6808cc4d9058d307ae9",
      "phone": null,
      "accounts": [],
      "account_number": "413113054",
      "active": true,
      "mail": "cansecorigoberto@gmail.com",
      "genre": "MALE",
      "password": "ef797c8118f02dfb649607dd5d3f8c7623048c9c063d532cc95c5ed7a898a64f",
      "type": 1,
      "school_id": "2398aa6a722d171da04ca3806e6b2d4d"
    }
    ```
 
* **Error Response:**

  * **Code:** 404 NOT FOUND <br />
    **Content:** `{ error : "User doesn't exist" }`

  * **Code:** 401 UNAUTHORIZED <br />
    **Content:** `{ error : "You are unauthorized to make this request." }`

* **Sample Call:**

  ```
  javascript
    $.ajax({
      url: "/users/1",
      dataType: "json",
      type : "GET",
      success : function(r) {
        console.log(r);
      }
  });
  ```
  
  
  
## License
This code uses the MIT License (https://opensource.org/licenses/MIT)

