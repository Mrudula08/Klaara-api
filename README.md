1. Hosting url - https://klaara-app.herokuapp.com/
2. Link to git repository - https://github.com/Mrudula08/Klaara-api
3. Curl commands to call the api's
    ```
    curl --location --request GET "https://klaara-app.herokuapp.com/api/branches/autocomplete?q=RTGS&limit=3&offset=0" --header "Content-Type: application/json"
    ```
      
    Sample Output :   
    
    ```
   {
    "branches": [
        {
            "ifsc": "ABHY0065001",
            "bank_id": 60,
            "branch": "RTGS-HO",
            "address": "ABHYUDAYA BANK BLDG., B.NO.71, NEHRU NAGAR, KURLA (E), MUMBAI-400024",
            "city": "MUMBAI",
            "district": "GREATER MUMBAI",
            "state": "MAHARASHTRA"
        },
        {
            "ifsc": "ABNA0000001",
            "bank_id": 110,
            "branch": "RTGS-HO",
            "address": "414 EMPIRE COMPLEX, SENAPATI BAPAT MARG LOWER PAREL WEST MUMBAI 400013",
            "city": "MUMBAI",
            "district": "GREATER BOMBAY",
            "state": "MAHARASHTRA"
        },
        {
            "ifsc": "ADCB0000001",
            "bank_id": 143,
            "branch": "RTGS-HO",
            "address": "75, REHMAT MANZIL, V. N. ROAD, CURCHGATE, MUMBAI - 400020",
            "city": "MUMBAI",
            "district": "MUMBAI CITY",
            "state": "MAHARASHTRA"
        }
    ]}
    ```
        
    ```
    curl --location --request GET "https://klaara-app.herokuapp.com/api/branches?q=Bangalore&limit=4&offset=0" --header "Content-Type: application/json"
    ```
   
   Sample Output : 
   ```
   {
    "branches": [
        {
            "ifsc": "ABNA0100318",
            "bank_id": 110,
            "branch": "BANGALORE",
            "address": "PRESTIGE TOWERS', GROUND FLOOR, 99 & 100, RESIDENCY ROAD, BANGALORE 560 025.",
            "city": "BANGALORE",
            "district": "BANGALORE URBAN",
            "state": "KARNATAKA"
        },
        {
            "ifsc": "ADCB0000002",
            "bank_id": 143,
            "branch": "BANGALORE",
            "address": "CITI CENTRE, 28, CHURCH STREET, OFF M. G. ROAD BANGALORE 560001",
            "city": "BANGALORE",
            "district": "BANGALORE URBAN",
            "state": "KARNATAKA"
        },
        {
            "ifsc": "ALLA0210217",
            "bank_id": 11,
            "branch": "K. G. ROAD",
            "address": "NO. 2, FKCCI BUILDING , K G ROAD , BANGALORE",
            "city": "BANGALORE",
            "district": "BANGALORE URBAN",
            "state": "KARNATAKA"
        },
        {
            "ifsc": "ALLA0210326",
            "bank_id": 11,
            "branch": "BANGALORE BASAVANGUDI",
            "address": "121, RM COMPLEX, DR.D.V.GUNDAPPA ROAD, BASAVANGUDI, BANGALORE - 560004",
            "city": "BANGALORE",
            "district": "BANGALORE URBAN",
            "state": "KARNATAKA"
        }
    ]}
    ```