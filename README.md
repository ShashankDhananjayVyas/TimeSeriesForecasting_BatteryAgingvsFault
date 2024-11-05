# Battery Fault Distinction From Aging Using Transformers

We introduce a battery aging vs fault distinction algorithm using Transformer-based battery resistance prediction. The file "main.py" contains the code for fine tuning the pretrained Transformer model. The fine tuning is done based on the battery cycling data in the "data" folder. We used the "Chronos" package provided by Amazon Inc. for our pretrained model. See "https://github.com/amazon-science/chronos-forecasting" for more details.

## Citation

    @article{ansari2024chronos,
      author  = {Ansari, Abdul Fatir and Stella, Lorenzo and Turkmen, Caner and Zhang, Xiyuan and Mercado, Pedro and Shen, Huibin and Shchur, Oleksandr and Rangapuram, Syama Syndar and Pineda Arango, Sebastian and Kapoor, Shubham and Zschiegner, Jasper and Maddix, Danielle C. and Wang, Hao and Mahoney, Michael W. and Torkkola, Kari and Gordon Wilson, Andrew and Bohlke Schneider, Michael and Wang, Yuyang},
      title   = {Chronos: Learning the Language of Time Series},
      journal = {arXiv preprint arXiv:2403.07815},
      year    = {2024}
    }
