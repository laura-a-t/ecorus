# ecorus

### Endpoints with examples
##### GET Office example
```bash
curl --request GET http://localhost:8080/office/7
```
##### Output
```json
{"message":"Office with id 7","office":{"id":7,"name":"HR","people_working":[]}}
```
---
##### DELETE Office example
```bash
curl --request DELETE http://localhost:8080/office/10
```
##### Output
```json
{"message":"Office with id 10 does not exist"}
```
---
##### POST Office example
```bash
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"name":"IT"}' \
  http://localhost:8080/office/
```
##### Output
```json
{"message":"Created office with id 8","office":{"id":8,"name":"IT","people_working":[]}}
```
---
#### GET Person example
```bash
curl --request GET http://localhost:8080/person/5
```
##### Output
```json
{"message":"Success","person":{"age":34,"id":5,"name":"Ana","office":"IT","office_id":8}}
```
---
#### POST Person example
```bash
curl --header "Content-Type: application/json"   --request POST   --data '{"name":"Laura", "age": 32, "office_id": 80}'   http://localhost:8080/person/
```
##### Output
```json
{"message":"Created person with id 6","person":{"age":32,"id":6,"name":"Laura"}}
```
---
#### PUT Person example
```bash
curl --header "Content-Type: application/json"   --request PUT   --data '{"name": "Ana", "age": true}'   http://localhost:8080/person/5
```
##### Output
```json
{"message":"Success","person":{"age":34,"id":5,"name":"Ana","office":"IT","office_id":8}}
```
---
#### DELETE Person example
```bash
curl --request DELETE http://localhost:8080/person/3 
```
##### Output
```json
{"message":"Person with id 3 was deleted","person":{"age":32,"id":3,"name":"Laura","office":null,"office_id":null}}
```