import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("dataset/jobs_in_data.csv")

print("Dataset Shape:")
print(df.shape)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDataset Information:")
print(df.info())

print("\nStatistics:")
print(df.describe())
plt.figure(figsize=(12,6))

df['job_title'].value_counts().head(10).plot(kind='bar')

plt.title("Top 10 Job Roles")
plt.xlabel("Job Title")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("images/top_job_roles.png")

plt.show()
plt.figure(figsize=(10,6))

df['job_category'].value_counts().plot(kind='bar')

plt.title("Job Categories Distribution")
plt.xlabel("Category")
plt.ylabel("Count")

plt.tight_layout()

plt.savefig("images/job_categories.png")

plt.show()
plt.figure(figsize=(10,6))

sns.boxplot(
    x='experience_level',
    y='salary_in_usd',
    data=df
)

plt.title("Salary by Experience Level")

plt.tight_layout()

plt.savefig("images/experience_salary.png")

plt.show()
plt.figure(figsize=(8,8))

df['work_setting'].value_counts().plot(
    kind='pie',
    autopct='%1.1f%%'
)

plt.title("Work Setting Distribution")

plt.ylabel("")

plt.savefig("images/work_setting.png")

plt.show()
country_salary = df.groupby(
    'company_location'
)['salary_in_usd'].mean().sort_values(
    ascending=False
).head(10)

plt.figure(figsize=(12,6))

country_salary.plot(
    kind='bar',
    color='skyblue'
)

plt.title(
    'Top 10 Highest Paying Countries'
)

plt.xlabel('Country')
plt.ylabel('Average Salary (USD)')

plt.tight_layout()

plt.savefig(
    'images/highest_paying_countries.png'
)

plt.show()
salary_trend = df.groupby(
    'work_year'
)['salary_in_usd'].mean()

plt.figure(figsize=(10,6))

salary_trend.plot(
    marker='o',
    linewidth=3
)

plt.title(
    'Average Salary Trend Over Years'
)

plt.xlabel('Year')
plt.ylabel('Average Salary (USD)')

plt.grid(True)

plt.tight_layout()

plt.savefig(
    'images/salary_trend.png'
)

plt.show()
plt.figure(figsize=(10,6))

sns.boxplot(
    x='company_size',
    y='salary_in_usd',
    data=df
)

plt.title(
    'Company Size vs Salary'
)

plt.tight_layout()

plt.savefig(
    'images/company_size_salary.png'
)

plt.show()
plt.figure(figsize=(8,6))

df['employment_type'].value_counts().plot(
    kind='bar'
)

plt.title(
    'Employment Type Distribution'
)

plt.xlabel(
    'Employment Type'
)

plt.ylabel(
    'Count'
)

plt.tight_layout()

plt.savefig(
    'images/employment_type.png'
)

plt.show()
plt.figure(figsize=(12,6))

df['employee_residence'].value_counts().head(10).plot(
    kind='bar'
)

plt.title(
    'Top Employee Residence Countries'
)

plt.xlabel(
    'Country'
)

plt.ylabel(
    'Number of Employees'
)

plt.tight_layout()

plt.savefig(
    'images/employee_residence.png'
)

plt.show()
category_salary = df.groupby(
    'job_category'
)['salary_in_usd'].mean().sort_values(
    ascending=False
)

plt.figure(figsize=(12,6))

category_salary.plot(
    kind='bar'
)

plt.title(
    'Average Salary by Job Category'
)

plt.xlabel(
    'Job Category'
)

plt.ylabel(
    'Average Salary (USD)'
)

plt.tight_layout()

plt.savefig(
    'images/category_salary.png'
)

plt.show()