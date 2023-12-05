********************
# Mildew Detection in Cherry Leaves
********************


********************
## Table of Contents
1.  [Introduction](#Introduction)
2.  [Business Requirements](#Business-Requirements)
3.  [Hypothesis and Validation](#Hypothesis-and-Validation)
4.  [ML Task Rationale](#ML-Task-Rationale)
5.  [ML Business Case](#ML-Business-Case)
6.  [Project Setup](#Project-setup)
7.  [Jupyter Notebook Process](#jupyter-process)
8.  [Dashboard Design](#Dashboard-Design)
9.  [Unfixed Bugs](#Unfixed-Bugs)
10.  [Deployment](#Deployment)
11.  [Data Analysis and Machine Learning Libraries](#Data-Analysis-and-Machine-Learning-Libraries)
12.  [Credits](#Credits)
13.  [Acknowledgements](#Acknowledgements)
14.  [Personal Conclusions](#Personal-Conclusions)
********************



********************
## Introduction
********************

The customer is in search of a more efficient way of determining if their crop (Cherry Leaves) has been infected with a powdery mildew fungus or if it is healthy. Their current method of crop analysis is to manually inspect the leaves on every tree in their plantation, which is both time consuming and resource expensive.  
This project is to facilitate the means to create a Predictive Analysis Machine Learning Tool that can accurately and quickly determine if an uploaded image of a Cherry Leaf contains a healthy Cherry Leaf or one infected with a powdery Mildew. 
The outcome goal of this project is to positively impact the customers' profit margins by combining visual imagery with Machine Learning to save time, labour, resources and most of all, the health of the harvest. 


********************
## Business Requirements
********************
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is manual verification if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If there is powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees, located on multiple farms across the country. As a result, this manual process is not scalable due to the time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that detects instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project for all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


1 - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one with powdery mildew.

2 - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

3 - That the app is responsive to fit appropriately on all devices:



********************
## Hypothesis
********************

1 - Cherry Leaves infected with powdery mildew have white blotches, streaks and surface making them appear
differently than healthy Cherry leaves

2 - The ML image visualizer will be able to differentiate between a healthy cherry leaf and an infected cherry leaf with at least 97% accuracy.

3 - The ML image visualizer can help decrease the amount of time needed to differentiate between the images thereby saving the employee and company both time and money during the inspection process.

4 - Validation of the image visualizer will come from the ML pipeline performance of the validation and test set differentiating between an infected leaf and a healthy leaf with at least 97% accuracy.



********************
## ML Task Rational
********************

1 - The company requires a ML data visualization tool to efficiently and accurately determine a healthy cherry leaf from an infected cherry leaf. 

2 - The company requires a data visualization tool that can be used widespread through the company in order to save employee time, and company resources. 

3 - The company will benefit by saving time, money, resources and ultimately by increasing the amount of healthy produce to the market, thereby increasing the amount of revenue brought into the company.



********************
## ML Business Case
********************

1 - The business objective: Devising a method/tool to increase accuracy and efficiency evaluating a leaf infected with powdery mildew from a healthy leaf.

2 - The Customer requires a dashboard containing the ability to upload images of leaves for the machine to quickly determine if the image of the leaf is contains a healthy or a leaf infected with powdery mildew with 97% accuracy.

3 - The Customer requires for proprietary reasons that their internal data remains secret so as to not give the competition the ability to match the production of cherry leaves delivered to the market.

4 - The inputs are images of both healthy and infected cherry leaves that will be used to train the ML tool to learn the difference and the expected output is a ML tool that with an accuracy of 97% determines if the uploaded image shows a healthy or infected leaf.

5 - Conventional data analysis can be used to visually inspect and differentiate the images of the leaves to determine if the image contains a healthy leaf or one infected with powdery mildew.


*******************
## Project-setup
*******************

### Agile Project Construct:

* Github **Issues** and **Project** were used to develop a Kanban Agile setup as a method to keep the project headed in a successful direction. 


### CRISP-DM Project Method:

- The CRISP-DM method for data mining and AI development is a fantastic guide for maintaining perspective on connecting the business goals of the project with the steps of data collection, preparation, modelling and understanding. The model was repeatedly referenced throughout the duration of this project as a means to connect the hypothesis and model to the requirements of the stakeholders.

There are six main steps (that are both sequential and fluid) to the CRISP-DM methodology:

1. Business Understanding: Understanding the needs/problems of the stakeholders and the ouctcome goal of the project.

2. Data Understanding: What do we need and where can it be found? (usually provided by the stakeholders).

3. Data Preperation: Cleaning and organizing the data so that it can be used efficiently for modelling and to address the stakeholders outome goals. 

4. Modeling: Choosing the appropraite modeling process to match the data in order to produce complete the outcome goals of the stakeholder.

5. Evaluation: Selecting the correct model to meet the business requirements and outcome goals.

6. Deployment: Providing a means for the stakeholders to access and use the model and the results; meeting the business requirements. 


********************
## Jupyter Process
********************

1. The dataset content came from [Kaggle Cheery Leaves Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) which contains 4208 images of Cherry Leaves, equally divided between healthy and infected. The data was organized into **Healthy** and **Powdery Mildew** folders in the workspace

2. The data was then cleaned to remove any corrupt or non image files. Once cleaned it was split (using the standard train/test/validate method) into the three aforementioned grouping using the ratio of .7, .2, .1 respectively. As the groups were on the smaller size, the next step of the process was to augment all three groups to increase the amount of images to be used in the modelling process. The augmentation process uses the existing images and artificially randomly alters and saves them with small alterations such as image rotation, opacity, image placement, and rescaling to create a more robust data source.

3. The modelling process is set of steps to train a ML pipeline to be able to make a prediction on unseen data based from information (visual) used to train specific details of grouped images. 
A sequential modal was used to create all three groups of this pipeline so that it can accurately predict unseen images.

4. Evaluation and accuracy testing are the final steps in the pipeline development. This pipeline was tested and scored over 97% accurate which meets the needs of the customer.


********************
## Dashboard Design and Features
********************

1 - The **Project Summary page**, provides critical information concerning the backstory and source of the projects origins and subsequent information concerning the customer. Also on the summary page the business requirements chosen by the customer which extrapolate what a successful project will provide.

![Screenshot of the summary page](/assets/images/summary_1.jpg)


********************
2 - The **Hypothesis page** displays the 4 main objectives and outcome goals for the project, including measures of success.



********************
3 -The **Cherry Leaf Visualizer page** which visually differentiates image models between healthy cherry leaves from those that contains powdery mildew.


![Screenshot of the Cherry Leaf Visualizer page](/assets/images/Visual_1.jpg)
![Screenshot of the Cherry Leaf Visualizer page](/assets/images/Visual_2.jpg)
![Screenshot of the Cherry Leaf Visualizer page](/assets/images/Visual_3.jpg)
![Screenshot of the Cherry Leaf Visualizer page](/assets/images/Visual_4.jpg)
********************
4 - The **Detector page** is arguable the most important page in the dashboard, as it is the page that allows for the customer to interact with the ML app by uploading images and having the app predict if the leaf is infected or not. 


![Screenshot of the Detector page](/assets/images/detector_1.jpg)
![Screenshot of the Detector page](/assets/images/detector_2.jpg)
![Screenshot of the Detector page](/assets/images/detector_3.jpg)

********************
5 - The **Metrics** page displays the technical aspects of the model performance. The bar graph shows the breakdown of the amount of images, per label, contained in the train, validate and test groupings. The line graphs prove a normal learning curve through accuracy and loss plots and the last table shows the same information in a table graph. This ML model as normal and accurate to 99%.




********************
6 - The **Conclusions** page provides explanations and outcomes of the hypothesis and business requirements for the project.



![Screenshot of the Conclusions Page](/assets/images/conclusions_1.jpg)

********************
## Unfixed Bugs
********************

* As far as I am aware, there are no unfixed bugs. That is not to say that there is not any; its just that I am not aware of them.


* As the data content used for this project has a Non-Disclousre Agreement, the data collection files were not transferred to Heroku, therefor the Image Montage option DOES NOT work in the Heroku app, although it does still work in Github. This is not a bug, but rather an intentional and acceptable situation based on the requirements of the project.


********************
## Future Improvements
********************


* There is a limitation to this app that I am aware of, that given the opportunity to improve the overall product for the customer in the future. I would like to link the dashboard with a means for the operator to use the devices camera for image capture and upload, rather than file upload.


* A second large improvement for this app would be a GPS pinpoint for positive hits on infected trees. 
And combining the Geo-Locations with weather patterns to possibly create infectious spread patterns based on wind vectors to create predictive zones for anti-fungal compound dispersal in the different orchards to contain the spread of infection. 


********************
## Deployment
********************


### Heroku

The project was deployed to Heroku using the following steps.

1. Log in to Heroku and create an App
2. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
6. If the slug size is too large then add large files not required for the app to the .slugignore file. 


********************
## Data Analysis and Machine Learning Libraries
********************

* [Jupyter notebooks](https://jupyter.org/) was the main source used for running and executing the ML pipelines.

* [Streamlit](https://streamlit.io/) is used to host the interactive dashboard.

* [Pandas](https://pandas.pydata.org/) is used for data analysis, especially for structuring the data.

* [Numpy](https://numpy.org/) is used to handle and manipulate multi-dimensional arrays, including providing a wide set of mathematical functions to operate on those arrays.

* [Matplotlib](https://matplotlib.org/) is used for data visualization including embedding plots in Jupyter notebooks.

* [Plotly](https://plotly.com/) is used for plotting data, functions, and to add animation to data visualization.

* [Scikit-learn](https://scikit-learn.org/stable/) contains tools used for data processing, predictive analysis, specifically used in this case to train the machine learning models for classification.

* [Seaborn](https://seaborn.pydata.org/) is a high-level interface for statistical graphics and it offers numerous built-in themes for styling Matplot graphics.

* [Tensorflow](https://www.tensorflow.org/) is used to filter out corrupt images or missing data during image processing.

* [Keras](https://keras.io/) was used for the CNN model for the ML pipeline.

* [Joblib](https://joblib.readthedocs.io/en/latest/) was used for loading and saving the images shapes.

* [Github](https://github.com/) is used for hosting the project and accepting all of the pushed code.

* [Gitpod](https://github.com/) is the workspace that hosted all facets of the project.

* [Heroku](https://heroku.com) was used for deployment of the project.

********************
## Credits 
********************

- Assistance and support for this project came in two main groups: **content** and **data/images**. 

********************
### Content 

* [Code Institute Malaria Walk Through Project](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/07a3964f7a72407ea3e073542a2955bd/29ae4b4c67ed45a8a97bb9f4dcfa714b/) was heavily used for instructional purposes, and guidance through the development of this project. The code in the walk through project was used for guidance, reference and support in the jupyter notebooks, the app pages and the src folders (and accompanying pages).

* [Mildew Detection](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) was forked to provide the base foundation of this project.

* [Streamlit](https://docs.streamlit.io/library/api-reference/write-magic/st.write) documentation was used for assistance in the writting the app pages

* [Code Institute Streamlit lessons](https://learn.codeinstitute.net/courses/course-v1:code_institute+CI_DA_ML+2021_Q4/courseware/d186ae95191f48e9a2151559c7e6f85d/fc2f9892cfa44eee9cc8bf585c21df88/4?activate_block_id=block-v1%3Acode_institute%2BCI_DA_ML%2B2021_Q4%2Btype%40vertical%2Bblock%407636b337caeb4035bd7b5568404802f6) was used as guidance for the dashboard execution in this project.


* [Erik1007/mildew-detection-project](https://github.com/Erik1007/mildew-detection-project) github repository was used for readme guidance and some code reference in the jupyter notebooks and src files. 

* [Wikipedia](https://en.wikipedia.org/wiki/Powdery_mildew#:~:text=Powdery%20mildew%20is%20a%20fungal,its%20symptoms%20are%20quite%20distinctive.) was used as the resource pertaining to the powdery mildew fungal infection that is at the heart of this project.

* The icons in the footer were taken from [Font Awesome](https://fontawesome.com/).


********************
### Dataset / Media

* [Kaggle Cheery Leaves Dataset](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves) was used as the source for the data set and the images for this project

* The dataset contains +4 thousand images taken from the client's crop fields. The images show healthy cherry leaves and cherry leaves that have powdery mildew, a fungal disease that affects many plant species. 



********************
## Acknowledgements
* I would like to thank for codeinstitute student support for time, help, expertise and especially for motivation during the creation and execution of this project.
********************

********************
## Personal Conclusions
********************

### What have I learned from this project?

- I learned that jupyter notebooks and python are very user friendly even when dealing with complex situations such as developing and visual image ML pipeline model. 

- Streamlit is also very user friendly for displaying information and connecting the notebooks outputs and model information to the stakeholder in a convenient way. 

### What did I gain from this process?

- I personally gained alot of confidence in many areas involved in this path of development. I personally have more confidence in python coding as well as the ability to use python in more diverse ways. 

- I also have gained a significant understanding for predictive analysis, data analysis and machine learning processes. The two walk through projects appropriately framed the extensive lessons that make up the predictive analysis path; however, it was the execution of the project that truly connected the information with the process of understanding a problem, breaking it down in manageable steps and completing the outcome goals.

- Connecting previous lessons from the Fullstack Development path created a strong foundation and level of confidence that allowed for the predictive analysis path to be less daunting and more manageable. 

- The utilization of Agile combined with CRISP-DM created a straightforward step by step method to identify small hurdles and steps to accomplish to efficiently move through the whole project smoothly and successfully compelete the outcome goals.

- The largest realization came from being able to rely upon my previous educational background of Research Psychology and Statistics with the combined support of the CRISP-DM process to approach predictive analysis more confidently.   