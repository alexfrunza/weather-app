# Weather application
### Description
Basic python console application that fetch weather data about a city from OpenWeatherMap API.
### How to use it
#### 1. You need to insert your API_KEY from OpenWeatherMap API in `development.env`
#### 2. Create a new python environment
```
python3 -m venv venv
```
#### 3. Activate the environment
```
source venv/bin/activate
```
#### 4. Install requirements
```
pip install -r requirements.txt
```
#### 5. Get environment variables
```
source development.env
```
#### 6.a. Run sync version of application
```
python sync_version.py
```
#### 6.b. Run async version of application
```
python async_version.py
```