# About My Project

Student Name: Jonah Peeler 
Student Email: jzpeeler@syr.edu

### What it does 
My project is an interactive dashboard that displays the reasons behind NYC 311 Call Complaints. It uses data from the NYC Open Data API. You can explore the data through both borough as well as complaint type, making it easy to find data on a specific type of complaint. It also allows you to download the filtered data you want to look at, into a CSV file.

### How you run my project
1. Run "pip install -r requirements.txt"
2. Run these files in this order
    1. extract.py to get the data from NYC 311 API
    2. transform.py to clean and format the data
    3. dashboard.py using streamlit (Ctrl+Shift+D => F5) Make sure to select "Run With Streamlit"
3. Observe the data in your browser, and select which filters you want applied for the data shown.
4. If you want, scroll to the bottom and downlod the CSV file.

### Other things you need to know

I'm originally from New York, so I was naturally curious about the kinds of issues residents report across the city. It was especially interesting to see how this public 311 data translates into real patterns, like complaint hotspots or borough-level trends.
One surprising but relatable insight was that noise complaints dominate the dataset. Not just overall, but across multiple top complaint categories like "Noise - Street/Sidewalk" and "Loud Music/Party." This lines up with my own experience living in the city.
The dashboard is limited to the most recent 5,000 complaints for performance and simplicity, but it still gives a good view of what’s going on in NYC at a given time. All data is saved locally in a /cache folder to avoid repeated API calls. More complaints could be included to get more of a view over time, but it would require pagination in order to get all of them accurately and stop the API from timing out.
