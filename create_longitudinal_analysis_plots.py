import sqlite3
import pandas as pd
import matplotlib.pyplot as plt


def plot_horizontal_bars(sql_quary: str, fig_name: str, shareyaxsis: bool=False):
    connection = sqlite3.connect("data/kaggle_survey.db")
    response_counts = pd.read_sql(sql_quary, con=connection)
    fig, axes = plt.subplots(ncols=3, figsize=(32, 8), sharey=shareyaxsis)
    survey_years = [2020, 2021, 2022]
    for i in range(len(survey_years)):
        survey_year = survey_years[i]
        response_counts_year = response_counts[response_counts["survey_in"] == survey_year]
        y = response_counts_year["response"].values
        width = response_counts_year["response_count"].values
        axes[i].barh(y, width)
        axes[i].set_title(f"{survey_year}")
    plt.tight_layout()
    fig.savefig(f"{fig_name}.png")

sql_query = """
SELECT 
    survey_in,
    question_type,
    response,
    response_count
FROM aggregated_responses
WHERE (question_index = 'Q5' AND survey_in IN (2020, 2021)) OR
      (question_index = 'Q23' AND survey_in = 2022)
ORDER BY survey_in, 
         response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_titles")

sql_query = """
SELECT 
    survey_in,
    question_type,
    response,
    response_count
FROM aggregated_responses
WHERE (question_index = 'Q23' AND survey_in = 2020) OR
      (question_index = 'Q24' AND survey_in = 2021) OR
      (question_index = 'Q28' AND survey_in = 2022)
ORDER BY survey_in, 
         response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_tasks", shareyaxsis=True)

sql_query = """
SELECT 
    survey_in,
    question_type,
    response,
    response_count
FROM aggregated_responses
WHERE (question_index = 'Q7' AND survey_in IN (2020, 2021)) OR
      (question_index = 'Q12' AND survey_in = 2022)
ORDER BY survey_in, 
         response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_programming_languages")

sql_query = """
SELECT 
    survey_in,
    question_type,
    response,
    response_count
FROM aggregated_responses
WHERE (question_index = 'Q29A' AND survey_in = 2020) OR
      (question_index = 'Q32A' AND survey_in = 2021) OR
      (question_index = 'Q35' AND survey_in = 2022)
ORDER BY survey_in, 
         response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_databases")

sql_query = """
SELECT 
    survey_in,
    question_type,
    response,
    response_count
FROM aggregated_responses
WHERE (question_index = 'Q14' AND survey_in IN (2020, 2021)) OR
      (question_index = 'Q15' AND survey_in = 2022)
ORDER BY survey_in, 
         response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_visualizations")

sql_query = """
SELECT 
    survey_in,
    question_type,
    response,
    response_count
FROM aggregated_responses
WHERE (question_index = 'Q17' AND survey_in IN (2020, 2021)) OR
      (question_index = 'Q18' AND survey_in = 2022)
ORDER BY survey_in, 
         response_count;
"""
plot_horizontal_bars(sql_query, "data_science_job_machine_learings")
