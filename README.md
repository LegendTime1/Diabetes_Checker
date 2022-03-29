<h1 align="center">
AnalyzeBloodwork '1.5'</h1>
<h2 align="center">
Biomarker discovery and predictive diagnostics with Machine Learning in R and Python</h2>

[![DOI](https://zenodo.org/badge/203414088.svg)](https://zenodo.org/badge/latestdoi/203414088)

## A. Intro
The repository contains workflows and example analysis for statistical and machine learning for biomarker discovery approaches.  The analyses investigate clinical and molecular data associated with obesity, chronic inflammation, and immune response pathways.

The repository has also provided a framework for undergraduate students learning R and Python programming, and biostatistics taught by Dr. Jeffrey Robinson at University of Maryland, Baltimore County (UMBC).  

Courses have included BTEC330 (Software Applications in Translational Science), BTEC395 (Bioinformatics), and BTEC423 (Machine Learning with Applications in Bioinformatics), and BTEC495 (Undergraduate Research Internship).  UMBC BTEC495 research interns have included Daniel Gidron (Summer 2021) and Brandon Lamotte (Spring 2022).

Computational resources have been provided by NSF Extreme Science and Engineering Discovery Environment (XSEDE) through an educational allocation awarded to Robinson: “Bioinformatics Training for Applications in Translational and Molecular Biosciences”, under NSF grant number ACI-1548562.  

[Analysis of Akimel O'otham (NIDDK Pima Diabetes dataset)](Content/Ookem_Diabetes.md), with *Python, Scikit-learn, and Jupyter Notebooks*.  Brandon Lamotte (Spring 2022)

[Linear Regression in R with Examples](Content/LinearRegressionR.md). R-script and examples for single and multiple linear regressions.

[Algorithm selection for predictive classification (ML)](Content/MLselection_CaretR.md). Compare performance of Machine Learning algorithms with R and Caret package.


## B. Use the code

The repository contains scripts with functional R and Python code, intended to use as example code and teaching templates.  Functionality currently includes:

#### Scripts: 
[AnalyzeBloodwork.R](scripts/AnalyzeBloodwork.R) 
1) Loads required packages and sample data,
2) Generates histograms for all variables, 
3) Generates linear regression models and diagnostic plots for single and multiple regressions for BMI, Complete Blood Count (CBC), and inflammation markers,  


[IBSclassification.R](scripts/IBSclassification.R)
1) Imputes data for columns with missing (NA) values, 
2) Balances unequally-sized sample groups, 
3) Generates box-and-whisker and scatterplot-matrix plots for WBC distributions,
4) Tests the performance of machine learning classification algorithms for IBS diagnosis using CBC-WBC count data.

## C. Description of the Sample Datasets:

### 1. Akimel O'otham (NIDDK Pima Indians Diabetes) data set:
Data from the Akimel O'otham dataset was collected from an NIH clinical study of the relationships between obesity, BMI, blood glucose, diastolic blood pressure, tricep fold thickness, serum insulin levels, family history of diabetes, number of times pregnant, age, and whether a person is diagnosed with type 2 diabetes or not. This data set is from a study of Akimel O'otham people on the Gila River Indian Reservation in Arizona. The study was conducted between the early 1960s and mid 1990s. These parameters can then be used to train a machine learning algorithm to diagnose a patient with diabetes using these data points.

### 2. NIH Complete Blood Count with RNA expression in IBS dataset

Data from the sample dataset was collected during an NIH natural history clinical study of the relationship between obesity, inflammation, stress, and gastrointestinal disorders and is fully open-sourced (citations and links below).  

The <em>standard CBC parameters</em> provide point-of-care physicians with powerful diagnostic capabilities using: 
1) White Blood Cell counts (absolute and relative counts for Monocytes, Lymphocytes, Neutrophils, Basophils, and Eosinophils), 
2) Red blood cell and hemoglobin parameters (RBC count, Hematocrit (HCT), Mean Corpuscular Hemoglobin (MCH), Erythrocyte Sedimentation Rate (ESR)), 
3) Platelet parameters (Platelet Counts, Mean Platelet Volume (MPV))

Additional parameters for obesity, inflammation, and GI-associated pain:
1) Body Mass Index (BMI), 
2) Stress hormones: Cortisol and ACTH,
3) Inflammation markers: C-Reactive Protein (CRP), sCD14, Lipopolysaccharide Binding Protein (LBP),
4) Clinical diagnoses of subtypes of Irritable Bowel Syndrome (IBS)
5) Nanostring White Blood Cell RNA expression data: an associated 250-gene panel of Nanostring RNA expression data (links in citations below).


### Literature Citations
Robinson, J. 2021. Predictive Classification of IBS-subtype: Performance of a 250-gene RNA expression panel vs. Complete Blood Count (CBC) profiles under a Random Forest model. medRxiv. doi: https://doi.org/10.1101/2021.08.31.21262766. 

Robinson, JM. et al. 2019. Complete blood count with differential: An effective diagnostic for IBS subtype in the context of BMI? BioRxiv. doi: https://doi.org/10.1101/608208.

Robinson, J. Differential Gene Expression Associated with BMI, Gender, and IBS-subtype in Human White Blood Cells: Results from a Custom 250-plex Nanostring Probe Panel. Preprints 2019, 2019120180 (doi: 10.20944/preprints201912.0180.v1).


### Sample Nanostring dataset: 
ImmunoGC custom Nanostring probe panel. 2019.  https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GPL25996. 

Human buffy coat gene expression, custom 250-plex Nanostring panel. GSE124549. 2019. https://www.ncbi.nlm.nih.gov/geo/query/acc.cgi?acc=GSE124549.  

### Funding:
This project was partially funded from NSF XSEDE Educational Allocation to Jeffrey Robinson:  “Bioinformatics Training for Applications in Translational and Molecular
Biosciences”. Extreme Science and Engineering Discovery Environment (XSEDE), supported by National Science
Foundation grant number ACI-1548562.

### Adapted R source code:
[STHDA: ggplot2 histogram: easy histogram with ggplot2 R package](http://www.sthda.com/english/articles/40-regression-analysis/167-simple-linear-regression-in-r/)

[STHDA: Scatterplot3d: 3D graphics - R software and data visualization](http://www.sthda.com/english/wiki/scatterplot3d-3d-graphics-r-software-and-data-visualization)

[Quick R by DataCamp (StatMethods.net): Scatterplots](https://www.statmethods.net/graphs/scatterplot.html)

[MachineLearningMastery.com: Machine Learning in R Step-by-Step](https://machinelearningmastery.com/machine-learning-in-r-step-by-step/)

[R-Bloggers.com: Regression analysis essentials for machine learning](https://www.r-bloggers.com/2018/03/regression-analysis-essentials-for-machine-learning/)

[R-Pubs: Residuals Analysis](https://rpubs.com/iabrady/residual-analysis)
