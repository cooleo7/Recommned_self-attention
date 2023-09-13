This is the guide for CSE model.

Step1) install requirements.txt in 'CSE' folder. (The version of python 3.9.13)
       If there are errors for the libraries, then you could refer Package in 'requirements.txt'


Step2) Execute the command below in your terminal according to a folder like CASE1, CASE2,...., CASE6
       (Eg.) this command for a CASE1, if you want to test CASE2, then change the file name like 
             transformer_model2.py and evaluation2.py

       1) python model/transformer_model1.py --save_data --no_load_data --no_train
       2) python model/transformer_model1.py --save_weights --epochs 100 --warmup_epochs 10
       3) python model/transformer_model1.py --load_weights --no_train
       4) python model/evaluation1.py

Step3) You can get the result from the command in step2-4.