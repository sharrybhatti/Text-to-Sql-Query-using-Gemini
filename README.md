Text-to-SQL Query Using Gemini

Description

Text-to-SQL Query Using Gemini is a project that leverages the Gemini model to convert natural language text into SQL queries. This tool aims to simplify the process of generating SQL queries from user input, making it easier for users to interact with databases without needing to write SQL code manually.
Features

    Converts natural language text to SQL queries using the Gemini model.
    Provides an easy-to-use interface for generating SQL queries.
    Allows for customization and extension of SQL queries based on user input.

Installation Instructions

    Clone the Repository

    bash

git clone https://github.com/sharrybhatti/Text-to-Sql-Query-using-Gemini.git
cd Text-to-Sql-Query-using-Gemini

Set Up a Virtual Environment

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

Install Dependencies

bash

    pip install -r requirements.txt

    Configure the Model

    Follow the instructions in the config.md file to set up and configure the Gemini model.

Usage Instructions

    Run the Application

    bash

    streamlit run app.py

    Interact with the Application
        Open your web browser and navigate to http://localhost:8501.
        Enter natural language text into the input field.
        The application will generate the corresponding SQL query and display the result.

Contributing

We welcome contributions to improve this project. If you have suggestions or would like to contribute, please follow these steps:

    Fork the repository.
    Create a new branch (git checkout -b feature-branch).
    Make your changes and commit them (git commit -am 'Add new feature').
    Push to the branch (git push origin feature-branch).
    Create a new Pull Request.

For any questions or support, please reach out to shaharyarshabbir348@gmail.com
