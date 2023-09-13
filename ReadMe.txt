This work is to identify and test different attention models such as SASRec, TiSASRec, BERT4Rec, MEANTIME(Mixture of AtteNTIon mechanisms with Multi-temporal Embeddings), and CSE(Context-aware Self-attentive Encoder, My model) according to differnet hyper-parameters. I explain how to execute this experiment.

Step1) Download the input file from kaggle. 
       (https://www.kaggle.com/code/mfaaris/hybrid-and-tensorflow-recommender-system/input?
        select=ratings_small.csv)
       But, this file is already stored as 'ratings_small.csv' in a 'Preprocess' folder. 


Step2) Execute the preprocess files in order. #1 is for the basic preprocess. #2, #3, and #4 are for     
       the files having differnt dimensions.
       But, it's already stored in 'CSE' folder and 'Others' folder. So, you don't need to execute.

      (Eg.) tmp_rating.csv -> the output from preprocess#1
            prep_rating.csv4 -> the output from preprocess#3 (dimension 56 and for CSE)
            ratings4.csv -> the output from preprocess#3 (dimension 56 and for SASRec, TiSASRec, 
            BERT4Rec, MEANTIME)
      

Step3) Execute CSE or Others(SASRec, TiSASRec, BERT4Rec, MEANTIME) depending on a model you want to 
       test. Refer to the detail in readme.md of 'CSE' and 'Other' folder.