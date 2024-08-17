#!/usr/bin/Rscript

# Load necessary library
library(meta)

# Prepare the data
data <- read.csv("../Table_1_Characteristics_of_Study.csv", header = TRUE)

# Convert relevant columns to numeric if not already
data$Total_VRE_isolated_from_humans <- as.numeric(data$Total_VRE_isolated_from_humans)
data$Total_humans_sampled <- as.numeric(data$Total_humans_sampled)

# Run the meta-analysis using Freeman-Tukey double arcsine transformation
meta_analysis <- metaprop(event = data$Total_VRE_isolated_from_humans,
                          n = data$Total_humans_sampled,
                          studlab = data$Authors,
                          data = data,
                          sm = "PFT",
                          method = "Inverse",   # Inverse variance method (similar to GLMM but available in meta package)
                          comb.fixed = FALSE, 
                          comb.random = TRUE, 
                          pscale = 100
)


# Print the meta-analysis result
#print(meta_analysis)

# Save forest plot of the meta-analysis
output_image <- "Pooled_prevalence_univariate.png"
png(filename = output_image, width = 1200, height = 800, units = "px", pointsize = 16)
forest(meta_analysis,
       main = "Forest plot of pooled prevalence of VRE in hospitalized patients",
       xlab = "Proportion of VRE cases",
       leftcols = c("studlab", "n", "event"),
       leftlabs = c("Study", "Sample size", "Number of events"),
       colgap.forest.left = "1.0cm",
       colgap.forest.right = "1.0cm",
       col.square = "skyblue",
       col.diamond = "darkblue",
       col.diamond.lines = "black",
       col.diamond.polygon = "skyblue",
       col.study = "black",
       col.study.ci = "blue",
       col.inside = "grey30",
       col.labels = "darkred",
       col.polygon = "red",
       colgap.studlab = "1cm",
       fontsize = 16,
       text.random = "Random effects model",
       col.random = "red",
       cex = 2.0,
       spacing = 0.60
)
dev.off()



# Perform leave-one-out sensitivity analysis
leave_one_out_results <- metainf(meta_analysis)
#print(leave_one_out_results)

# Save forest plot for leave-one-out sensitivity analysis
leave_one_out_image <- "Forest_plot_sensitivity_analysis.png"
png(filename = leave_one_out_image, width = 1200, height = 800, units = "px", pointsize = 16)
forest(leave_one_out_results,
       main = "Leave-one-out sensitivity analysis",
       xlab = "Proportion of VRE cases",
       leftcols = c("studlab"),
       leftlabs = c("Study", "Sample size", "Number of events"),
       colgap.forest.left = "1.0cm",
       colgap.forest.right = "1.0cm",
       col.square = "skyblue",
       col.diamond = "darkblue",
       col.diamond.lines = "black",
       col.diamond.polygon = "skyblue",
       col.study = "black",
       col.study.ci = "blue",
       col.inside = "grey30",
       col.labels = "darkred",
       col.polygon = "red",
       colgap.studlab = "1cm",
       fontsize = 16,
       text.random = "Random effects model",
       col.random = "red",
       cex = 2.0,
       spacing = 0.60
)
dev.off()

# Perform subgroup analysis by region
subgroup_analysis <- update.meta(
    meta_analysis,
    byvar = data$Method_for_identification
)
# print(subgroup_analysis)

# Save subgroup analysis forest plot
subgroup_image <- "Forest_plot_subgroup_method_for_identificaton.png"
png(filename = subgroup_image, width = 1200, height = 800, units = "px", pointsize = 16)
forest(subgroup_analysis,
       main = "Subgroup analysis by method for VRE identification",
       xlab = "Prevalence of VRE cases",
       leftcols = c("studlab", "n", "event"),
       leftlabs = c("Study", "Sample size", "Number of events"),
       colgap.forest.left = "1.0cm",
       colgap.forest.right = "1.0cm",
       col.square = "skyblue",
       col.diamond = "darkblue",
       col.diamond.lines = "black",
       col.diamond.polygon = "skyblue",
       col.study = "black",
       col.study.ci = "blue",
       col.inside = "grey30",
       col.labels = "darkred",
       col.polygon = "red",
       colgap.studlab = "1cm",
       fontsize = 16,
       text.random = "Random effects model",
       col.random = "red",
       cex = 2.0,
       spacing = 0.60
)
dev.off()

# Perform subgroup analysis by region
subgroup_analysis_1 <- update.meta(
    meta_analysis,
    byvar = data$Sample_taken
)
#print(subgroup_analysis_1)

# Save subgroup analysis forest plot
subgroup_image <- "Forest_plot_subgroup_sample_taken.png"
png(filename = subgroup_image, width = 1200, height = 800, units = "px", pointsize = 16)
forest(subgroup_analysis_1,
       main = "Subgroup analysis by types of samples collected for VRE identification",
       xlab = "Prevalence of VRE cases",
       leftcols = c("studlab", "n", "event"),
       leftlabs = c("Study", "Sample size", "Number of events"),
       colgap.forest.left = "1.0cm",
       colgap.forest.right = "1.0cm",
       col.square = "skyblue",
       col.diamond = "darkblue",
       col.diamond.lines = "black",
       col.diamond.polygon = "skyblue",
       col.study = "black",
       col.study.ci = "blue",
       col.inside = "grey30",
       col.labels = "darkred",
       col.polygon = "red",
       colgap.studlab = "1cm",
       fontsize = 16,
       text.random = "Random effects model",
       col.random = "red",
       cex = 2.0,
       spacing = 0.60
)
dev.off()


# Perform subgroup analysis by region
subgroup_analysis_2 <- update.meta(
    meta_analysis,
    byvar = data$Disease_Diagnosis
)
#print(subgroup_analysis_2)

# Save subgroup analysis forest plot
subgroup_image <- "Forest_plot_subgroup_disease_diagnosis.png"
png(filename = subgroup_image, width = 1200, height = 800, units = "px", pointsize = 16)
forest(subgroup_analysis_2,
       main = "Subgroup analysis by disease/diagnosis of the population sampled",
       xlab = "Prevalence of VRE cases",
       leftcols = c("studlab", "n", "event"),
       leftlabs = c("Study", "Sample size", "Number of events"),
       colgap.forest.left = "1.0cm",
       colgap.forest.right = "1.0cm",
       col.square = "skyblue",
       col.diamond = "darkblue",
       col.diamond.lines = "black",
       col.diamond.polygon = "skyblue",
       col.study = "black",
       col.study.ci = "blue",
       col.inside = "grey30",
       col.labels = "darkred",
       col.polygon = "red",
       colgap.studlab = "1cm",
       fontsize = 16,
       text.random = "Random effects model",
       col.random = "red",
       cex = 2.0,
       spacing = 0.60
)
dev.off()

# Grouping the years into five year groups 
# Convert the Publication_year column to a factor with the defined groups
data$Year_Group <- cut(data$Publication_year,
                       breaks = c(-Inf, 2010, 2015, 2020, 2024),
                       labels = c("before 2010", "2011-2015", "2016-2020", "2021-2024"),
                       right = TRUE
)

# Check the new column
table(data$Year_Group)

# Perform subgroup analysis based on the Year_Group
subgroup_analysis_year <- update.meta(
    meta_analysis,
    byvar = data$Year_Group
)
#print(subgroup_analysis_year)
# Save subgroup analysis forest plot for year groups
png(filename = "Forest_plot_subgroup_analysis_year_group.png", width = 1200, height = 800, units = "px", pointsize = 16)
forest(subgroup_analysis_year,
       main = "Subgroup analysis by year group",
       xlab = "Prevalence of VRE cases",
       leftcols = c("studlab", "n", "event"),
       leftlabs = c("Study", "Sample size", "Number of events"),
       colgap.forest.left = "1.0cm",
       colgap.forest.right = "1.0cm",
       col.square = "skyblue",
       col.diamond = "darkblue",
       col.diamond.lines = "black",
       col.diamond.polygon = "skyblue",
       col.study = "black",
       col.study.ci = "blue",
       col.inside = "grey30",
       col.labels = "darkred",
       col.polygon = "red",
       colgap.studlab = "1cm",
       fontsize = 16,
       text.random = "Random effects model",
       col.random = "red",
       cex = 2.0,
       spacing = 0.50
)
dev.off()


# Perform bias analysis using a funnel plot and Egger's test
egger_test <- metabias(meta_analysis, method.bias = "linreg")
#print(egger_test)

# Save funnel plot of bias analysis
funnel_image <- "Funnel_plot_bias_analysis.png"
png(filename = funnel_image, width = 1200, height = 700, units = "px", pointsize = 16)
funnel(meta_analysis,
       main = "Funnel plot of bias analysis",
       xlab = "Effect size",
       col.random = "red",
       col.fixed = "blue",
       cex = 1.5
)
dev.off()

# Preparing data for meta-regression analysis
# Convert categorical variables to factors
data$Country <- factor(data$Country)
data$Publication_year <- factor(data$Publication_year)
data$Method_for_identification <- factor(data$Method_for_identification)
data$Sample_taken <- factor(data$Sample_taken)
data$Sampling_method <- factor(data$Sampling_method)
data$Adult_Child_Mixed <- factor(data$Adult_Child_Mixed)
data$Disease_Diagnosis <- factor(data$Disease_Diagnosis)
data$Confirmatory_test <- factor(data$Confirmatory_test)
data$Type_of_study <- factor(data$Type_of_study)
data$Region <- factor(data$Region)

# Check factor levels
levels(data$Country)
levels(data$Publication_year)
levels(data$Method_for_identification)
levels(data$Sample_taken)
levels(data$Sampling_method)
levels(data$Adult_Child_Mixed)
levels(data$Disease_Diagnosis)
levels(data$Confirmatory_test)
levels(data$Region)

# Set a reference level for each variable
data$Country <- relevel(data$Country, ref = "India")
data$Publication_year <- relevel(data$Publication_year, ref = "2011")
data$Method_for_identification <- relevel(data$Method_for_identification, ref = "Culture, Biochemical")
data$Sample_taken <- relevel(data$Sample_taken, ref = "Stool")
data$Sampling_method <- relevel(data$Sampling_method, ref = "Single")
data$Adult_Child_Mixed <- relevel(data$Adult_Child_Mixed, ref = "Adult")
data$Disease_Diagnosis <- relevel(data$Disease_Diagnosis, ref = "ND")
data$Confirmatory_test <- relevel(data$Confirmatory_test, ref = "Kirby_Bauer")
data$Region <- relevel(data$Region, ref = "Asia")

# Run the meta-regression
meta_regression <- metareg(meta_analysis, ~Country + Publication_year + Region + Method_for_identification 
                           + Sample_taken + Sampling_method + Adult_Child_Mixed + Disease_Diagnosis + 
                           Confirmatory_test, method.tau = "DL"
)
summary(meta_regression)

# Save meta-regression forest plot
output_image <- "Meta_regression_forest_plot.png"
png(filename = output_image, width = 1200, height = 800, units = "px", pointsize = 16)
forest(meta_regression,
       main = "Meta-Regression Forest Plot",
       xlab = "Effect Size",
       leftcols = c("studlab", "n", "event"),
       leftlabs = c("Study", "Sample size", "Number of events"),
       colgap.forest.left = "1.0cm",
       colgap.forest.right = "1.0cm",
       col.square = "skyblue",
       col.diamond = "darkblue",
       col.diamond.lines = "black",
       col.diamond.polygon = "skyblue",
       col.study = "black",
       col.study.ci = "blue",
       col.inside = "grey30",
       col.labels = "darkred",
       col.polygon = "red",
       colgap.studlab = "1cm",
       fontsize = 16,
       text.random = "Random Effects Model",
       col.random = "red",
       cex = 2.0,
       spacing = 0.60
)
dev.off()
