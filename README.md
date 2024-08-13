[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-2e0aaae1b6195c2367325f4f02e2d04e9abb55f0b24a779b69b11b9e10269abc.svg)](https://classroom.github.com/online_ide?assignment_repo_id=15481863&assignment_repo_type=AssignmentRepo)
# Ecorse - Recommender System Based on Customer Cluster
### FTDS-017-HCK-Team-2

## Team Members:
  1. Syihabuddin Ahmad Satisma (Data Analyst & Data Scientist)
  2. Ryan Trisnadi (Data Scientist)
  3. Gracia Valerine (Data Scientist)
  4. Vincent Kaunang (Data Engineering & Data Analyst)

## Problem Statement

This project is created to implement a recommender system on Ecorse's e-commerce website to recommend similarly purchased products for customers. The project's goal is to analyze various products using the K-means clustering method to differentiate the types of customers the recommender will target. The intended audience of the project would be the Software Engineering Division, PR/Marketing Division, and the Senior Management Team which will be analyzing the various metrics of each cluster to gain insights on increasing overall revenue, promotion, and reputation of Ecorse's website. 

## Objective:

  - Analyze the various factors that will allow the recommender system to identify similar products.
  - Identify which products will be classified within differentiating categories.
  - Observe the distribution of the sample size of each product and category, alongside the timestamp at which the products are bought in certain quantities.
  - Process and train the sampled dataset using Machine Learning techniques to distinguish variations within the clusters.  
  - Evaluate the model by analyzing the characteristics of each cluster for the metrics (such as price, address, and product category)
  - Test the model by initiating prompts by the intended User (Customers) to select products and expecting a recommendation as output. 

  Main Goal:
The goal of creating this recommendation model is to provide similar product recommendations to customers based on various metrics such as product category or order date.

  User/Target Audience:
Recommendation Model: Software Engineering Division, PR/Marketing Division
Exploratory Data Analysis: Senior Management Team
   
## Background: 

The Team was tasked to research sales figures at the electronics stores and found that the sales of electronic goods have been continuously increasing over time. The Team would like to improve the sales and profit metrics of the products at Ecorse, as such machine learning models have been created to provide recommendations for related or similar products based on customers' search history at the online store. The Team hopes to improve the overall shopping experience for its customers and drive further sales.

### Dataset:
The dataset is taken from Kaggle and can be found through this [link](https://www.kaggle.com/datasets/naofilahmad/sales-datset-product-sample).
## Workflow

**Data Engineering**

  - Implement DAG files through Apache Airflow to retrieve datasets.
  - Develop a Pipeline to process the raw files into clean, usable data.
  - Save and store the cleaned dataset.
  - Utilize Tableau to visualize the datasets based on Exploratory Data Analysis.

**Data Analysis**

  - Retrieve the cleaned dataset for Exploratory Data Analysis.
  - Modify the dataset to uncover insights such as distribution and other metrics
  - Use modes of visualization to illustrate the usability of each variable in the dataset.
  - Document insights on the variations of the raw and filtered datasets. 

**Data Science**  
  - Create the Pipeline model using K-means Clustering and train it on the current dataset.
  - Implement modifications such as dimensional reduction (PCA) to ensure compatibility.
  - Develop the Recommender System using Cosine Similarity to detect relevance among categorical data.
  - Deploy the Model in HuggingFace to demonstrate product recommendations to its Users. 

## Tools:

  - Python: Data Analysis, Processing, and Modeling.
  - Airflow (DAG): Data Pipeline.
  - PostgreSQL: Storing Datasets.
  - HuggingFace: Model Deployment.

## Conclusion & Business Recommendations:

Through the development of the model based on K-means clustering, the Team concludes the discovery of variations between the two clusters that are evident in the model-building stage. Aside from time (Hour) being the main difference, the cluster exhibits variations in sales by month, cities, product category, and quantity ordered. Cluster "1" shows higher frequencies in cities and product categories, whereas Cluster "0" shows slightly higher quantities for products ordered based on product type. This implies that Cluster "0" represents customers that have a lot of leisure time to purchase electronics, whereas Cluster "1" shows customers that purchase the electronics after-hours and are more urgent. Given the illustrations, Cluster "1" represents a greater share of purchases compared to Cluster "0" despite the slight differences in overall sales and quantity ordered.

  Business Recommendation:

#1: Recommend promotions to popular products for Cluster "1" customers: Because these customers shop later in the evening and are urgent spenders, it is advised to promote popular items such as USB chargers and batteries to increase sales because the majority of customers in this cluster are looking for low-cost items that can be bought and delivered easily.

#2: Recommend seasonal discounts for Cluster "0" customers: Because web traffic is slightly lower for morning and afternoon shoppers, it is advised to give timely discounts to ensure Users are willing to shop during the daytime. 

## Further Improvements:

#1: Using a larger dataset that includes more categorical columns (e.g.: description): This will ensure that keywords can be extracted using Python's Machine Learning to identify similarities among product offerings.

#2: Improving the Optimal Number of Clusters: Given the computational limitations, it will be advisable to use a more powerful backend tool to compute Python's clustering models to ensure more in-depth analysis. 

#3: Incorporating User Behavior: Although not in the dataset, by being able to track customer behavior through clicks and bookmarks of the products will enhance the recommender system by identifying more accurately of the products to recommend.
