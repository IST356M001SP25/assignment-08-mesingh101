# Reflection

Student Name:  name
Sudent Email:  email

## Instructions

Reflection is a key activity of learning. It helps you build a strong metacognition, or "understanding of your own learning." A good learner not only "knows what they know", but they "know what they don't know", too. Learning to reflect takes practice, but if your goal is to become a self-directed learner where you can teach yourself things, reflection is imperative.

- Now that you've completed the assignment, share your throughts. What did you learn? What confuses you? Where did you struggle? Where might you need more practice?
- A good reflection is: **specific as possible**,  **uses the terminology of the problem domain** (what was learned in class / through readings), and **is actionable** (you can pursue next steps, or be aided in the pursuit). That last part is what will make you a self-directed learner.
- Flex your recall muscles. You might have to review class notes / assigned readings to write your reflection and get the terminology correct.
- Your reflection is for **you**. Yes I make you write them and I read them, but you are merely practicing to become a better self-directed learner. If you read your reflection 1 week later, does what you wrote advance your learning?

Examples:

**Poor Reflection:**  "I don't understand loops."   
**Better Reflection:** "I don't undersand how the while loop exits."   
**Best Reflection:** "I struggle writing the proper exit conditions on a while loop." It's actionable: You can practice this, google it, ask Chat GPT to explain it, etc. 

**Poor Reflection** "I learned loops."   
**Better Reflection** "I learned how to write while loops and their difference from for loops."   
**Best Reflection** "I learned when to use while vs for loops. While loops are for sentiel-controlled values (waiting for a condition to occur), vs for loops are for iterating over collections of fixed values."

`--- Reflection Below This Line ---`
This assignment helped me connect the dots between ETL and data visualization more than I expected. I’ve used Streamlit before, but this was the first time I had to transform data meaningfully before actually visualizing it — like filtering locations with over $1,000 in fines and prepping those new dataframes.

One of the most helpful things I learned was how to use groupby() in pandas to aggregate values, and then filter based on thresholds. I also got more comfortable chaining methods in pandas to keep things concise and readable. Something new for me was converting a DataFrame into a GeoDataFrame with shapely points and using folium to build an interactive map. Seeing the tickets plotted as color-coded circles really made the data feel more real.

What tripped me up was not knowing the correct column name at first — I kept using fine_amount until I realized it was just amount in the dataset. That taught me to always check column names before assuming. Also, I wasn’t 100% sure how to make the map color scale dynamic, but I figured out how to use LinearColormap to reflect fine amounts between $1,000 and $5,000.

If anything, I still want more practice with customizing Seaborn plots — especially adjusting label angles, adding counts on bars, or controlling layout when two charts are rendered in Streamlit. I also want to explore how to use side-by-side charts or tabs in Streamlit to make dashboards feel cleaner.

Overall, I feel more confident in building small data apps and transforming data for visualization — but I know there’s more to master when it comes to fine-tuning visuals and scaling interactivity.