# CS-340-15660-M01-Client-Server-Development

How do you write programs that are maintainable, readable, and adaptable? 

I write programs that are maintainable, readable, and adaptable by keeping the code organized, using clear names, and separating different responsibilities into different parts of the program. In this course, the CRUD Python module from Project One helped me do this because it kept the MongoDB database operations separate from the dashboard code. Instead of writing database connection code directly inside the dashboard, I was able to import the AnimalShelter class and use its methods to retrieve data. 

The advantage of working this way was that the dashboard became easier to understand and update. The CRUD module handled the database logic, while the dashboard handled the table, filters, chart, and map. This made the project more adaptable because changes to the database connection or CRUD methods could be made in one file instead of being repeated throughout the dashboard. In the future, I could reuse this CRUD Python module for another dashboard, a web application, or a different animal shelter database project that needs to create, read, update, or delete animal records. 

How do you approach a problem as a computer scientist? 

I approach a problem as a computer scientist by first understanding what the client needs, then breaking the project into smaller steps. For this project, I looked at the requirements from Grazioso Salvare and identified what the dashboard needed to do. The client needed a way to filter animal shelter data and find dogs that may be good candidates for water rescue, mountain or wilderness rescue, disaster or individual tracking. After understanding those requirements, I worked on connecting the database, retrieving the correct records, creating the dashboard layout, and then adding the interactive table, filters, chart, and map. 

This project was different from previous assignments because it combined several parts into one larger application. I had to use MongoDB, Python, and Jupyter Notebook together instead of only writing a small program or script. I also had to think more about the client’s needs and how the user would interact with the final dashboard. In the future, I would use the same strategy by reviewing the client requirements, designing the database structure, testing queries, building reusable code, and checking that the final product solves the client’s problem. 

What do computer scientists do, and why does it matter? 

Computer scientists design and build software solutions that help people solve problems, organize information, and make better decisions. This matters because many organizations have large amounts of data, but they need tools that make the data useful. In this project, the dashboard helped turn animal shelter records into information that Grazioso Salvare could search, filter, and understand more easily. 

A project like this could help a company like Grazioso Salvare do its work better by saving time and improving decision-making. Instead of manually searching through many animal records, users can choose a rescue type and quickly see animals that match the needed traits. The chart helps show breed patterns in the filtered data, and the map helps show the selected animal’s location. This type of system makes the data easier to use and helps the organization focus on choosing strong rescue animal candidates. 
