This webpage contains Supplementary material for the manuscript: *Quantifying trade-offs in satellite hardware configurations via a super-resolution framework with realistic image degradation*.

# Satellite images

Satellite images in the different pages below show the variability of super-resolved image reconstructions, given different satellite hardware configurations.

For each terrain type, the following pages show zoomed images that highlight the variability of super-resolution image reconstruction quality under several different degradation values:

[Beach](beach.md)

[Forest](forest.md)

[Rural](rural.md)

[Rural with Urban](rural_w_urban.md)

[Urban](urban.md)

# Supplementary figures

These supplementary figures show SSIM values for different SNR50, GSD, and GRD values, averaged across all geographical types and crops, for the EDSR model trained on DIV2K data (Figure S1) and for the TransENet model trained on remote sensing data (Figure S2). Note that the scaling factors we implemented consistently across both models are x3 (GSD=1.8) and x4 (GSD=2.4), and associated SSIM values are almost identical for both models, suggesting little difference in the ability of each model to super-resolve satellite imagery used in the study.

![Figure S1](plots/meanSSIM_EDSR_by_GSD_GRD_SNR50.png)


![](plots/meanSSIM_TransENet-aid_by_GSD_GRD_SNR50.png)
