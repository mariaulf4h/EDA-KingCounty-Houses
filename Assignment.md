## First Project - EDA     
 
This is your first project during the bootcamp. You'll be working with the King County House Sales dataset. Here, the focus is on EDA though you are required to demonstrate an entire Data Science Lifecycle using linear regression.
 
## The data
- The dataset can be found in the respective folders in this repository.
- The description of the column names can be found in the `column_names.md` files. 
- The column names may NOT be clear at times:

    *In the real world we will run into similar challenges. We would then go ask our business stakeholders for more information. In this case, let us assume our business stakeholder who would give us information, left the company. Meaning we would have to identify and look up what each column names might actually mean. (google is your friend ;) )*
 
## Tasks for you
1. Create a new repo using [the template](hhttps://github.com/neuefische/ds-eda-project-template).  

2. Through EDA/statistical analysis above please come up with **AT LEAST 3** insights/recommendations for your stakeholder. 
Note, you can take either the perspective of a buyer or a seller. Choose a stakeholder from the list at the end of this file.
If you use linear regression in the exploration phase remember that R2 close to 1 is good.

3. Then, model this dataset with a linear regression to explain the data but also to evaluate how well the model is fitting the data. We do expect **residuals** plotted for the model.

## Suggested workflow - POC
The work is timeboxed, and with that in mind, you need to change how you approach the task. You will want to employ an iterative approach. 

* write rough draft of plan with placeholders
* do simple plots
* main questions should already be answered -> POC (proof of concept) 
* iterate: go deeper, go prettier, go better
* clean up .. feel free to delete things that are not useful anymore
 
## The Deliverables
0. New repository from [template](https://github.com/neuefische/ds-eda-project-template)
1. A **well documented Jupyter Notebook** (see [here](https://www.kaggle.com/ekami66/detailed-exploratory-data-analysis-with-python) for an example) containing the code you've written for this project and comments explaining it. This work will need to be pushed to your GitHub repository in order to submit your project. Do not push all the analysis... just the analysis that is relevant!
2. A Python script for training the model, printing out the model statistics and saving the model. Look at this [stackoverflow discussion](https://stackoverflow.com/questions/16420407/python-statsmodels-ols-how-to-save-learned-model-to-file) on how to save a statsmodel.
3. An **organized README.md** file in the GitHub repository that describes the contents of the repository. This file should be the source of information for navigating through the repository.
4. A **short Keynote/PowerPoint/Google Slides/Jupyter slides presentation** giving a **high-level overview** of your methodology and recommendations for **non-technical stakeholders**. The duration of the presentation should be **10 minutes**, then the discussion will continue for 5 minutes. Also put your slides (delivered as a PDF export) on Github to get a well-rounded project.

## Stakeholders

  * We get to know our stakeholders:
  
Name | Stakeholder | Characteristics
-----|-------|------
Thomas Hansen | Buyer | 5 kids, no money, wants nice (social) neighbourhood, Timing?, Location?
Charles Christensen | Seller | Invest with big returns, wondering about renovation?, which Neighbourhood? Timing?
Bonnie Brown | Seller | Has house and wants to move soon (timing?), but wants high profit in middle class NH (neighborhood)
Larry Sanders | Buyer | Waterfront , limited budget, nice & isolated but central neighbourhood without kids (but got some of his own, just doesn't his kids to play with other kids .. because of germs)
Nicole Johnson | Buyer | Lively, central neighbourhood, middle price range, right timing (within a year)
Jennifer Montgomery | Buyer | High budget, wants to show off, timing within a month, waterfront, renovated, high grades, resell within 1 year
Bonnie Williams | Seller | Has several houses, some in bad neighbourhoods, willing to evict people, timing?, big returns, open for renovations
William Rodriguez | Buyer | 2 people, country (best timing & unrenovated) & city house (fast & central location), wants two houses
Erin Robinson | Buyer | Invest in poor neighbourhood, buying & selling, costs back + little profit, socially responsible
Jacob Phillips | Buyer | Unlimited Budget, 4+ bathrooms or smaller house nearby, big lot (tennis court & pool), golf, historic, no waterfront
Zachary Brooks | Seller | Invests in historical houses, best NHs, high profits, best timing within a year, should renovate?
Timothy Stevens | Seller | Owns expensive houses, needs to get rid, best timing within a year, open for renovation when profits rise
Amy Williams | Seller | Italian mafiosi, sells several central houses(top10%) over time, needs average outskirt houses over time to hide from the FBI

 
