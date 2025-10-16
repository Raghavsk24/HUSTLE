# Hustle - Full Stack Website Application
Hustle is an all-in-one web solution to finding the **perfect side hustle!** Simply upload your resume/CV, and our software will use ATS scanning to locate all the keywords within your the document and store them in a newly created database. That database is then compared to our comprehensive keyword database, with 200+ skills to recommend you your ideal side hustle, as well as the resources you need to succeed within that field. These resources include a market analysis, tips sourced from industry leaders, and job postings for entry-level freelancing roles within the industry.

Built by Raghav Senthil Kumar & Vignesh Nagarajan. Backed by [Jetson](https://www.jetson.app/).

**Product Demo**: https://youtu.be/JiFcL1ZbwDs?si=KUf0pZsQHnMRmk4t

**Software Features**
- Resume/CV Upload (PDF and DOCX Files)
- MySQL-based Relational Databases
- Automatically mapped to sites like Upwork & Fiverr
- Optimized Tech Stack
  - Frontend Design via Javascript & HTML/CSS
  - Backend Design via Python & Flask API
  - Text Processing via SpaCy NLP


**Startup Accomplishments**
- Built through Jetson's Entrepreneurs-in-Residence Program (June - July 2024)
  - Received direct mentorship from Jetson's CEO (Will Rush) & CTO (Natalie Young)
  - Pitched to a live audience of 32 angel investors/VCs and ultimately secured a $3,000 award
  - Grew to 53 users



## Website Features

- **Resume Upload:** Upload your resume in PDF, DOCX or txt format and recieve a personalized side hustle
- **Side Hustle Database:** Browse and filter through a vast databse of detailed side hustle
- **Job Matching:** Recieve a job that you can get started on immediately based on the skills and experiences mentioned in your resume

## How to Run the Project

### Prerequisites
- Python 3.x
- Virtual Environment (venv)
- VSCode

### Installation Steps
1. Clone the repository:
    ```bash
    git clone <repository-url>
    ```
2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    # For Mac or Linux OS
    source venv/bin/activate
    # For Windows
    venv\Scripts\activate
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the Flask application:
    ```bash
    flask run
    ```

5. Open the app in your browser at `http://127.0.0.1:5000/`.


## License

This project is licensed under the GNU General Public License v3.0. Please refer to [LICENSE](https://github.com/vignesh-nagarajan-vn/Hustle/blob/main/LICENSE) for more information.
