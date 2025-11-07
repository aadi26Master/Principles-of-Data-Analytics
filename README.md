**What Drives Success? An Analysis of the Factors Determining Employment and Salary for International Graduates**
Table of Contents
1. Background, Significance, and Research Questions
2. Data Source and Presentation
2.1 Key Variables
2.2 Descriptive Analysis
3. Methodology, Concepts, and Approaches
3.1 Part 1: Employment Status (Categorical Analysis)
3.2 Part 2: Salary (Continuous Analysis)
4. Analysis, Findings, and Discussion
4.1 Part 1 Findings: Employment Status (Categorical Outcome)
4.2 Part 2 Findings: Salary (Continuous Outcome)
5. Limitations and Further Research
6. References
1. Background, Significance, and Research Questions
For international graduates, navigating the job market is a complex challenge, often compounded by cultural adjustments, visa constraints, and the need to validate foreign credentials in a local context [Crossman and Clarke, 2010]. This study moves beyond anecdotal evidence to quantitatively investigate the key drivers of career success. This topic is significant as it directly impacts university career services, employer hiring practices, and graduate expectations.

Building on Human Capital Theory, which posits that skills acquired through education and experience are investments that yield economic returns [Becker, 1964], this research examines three critical factors. Prior literature has established that practical experience via internships [Knouse and Fontenot, 2008], education level [Hout, 2012], and host-country language proficiency [Chiswick and Miller, 2007] are key determinants of labour market outcomes. Our case study will use the analytical techniques from the Principles of Data Analytics (PODA) course to investigate how these factors combine.

This leads to our specific, two-part research question:

”How do an international graduate’s Language Proficiency, Education Level, and Internship Experience combine to determine their Employment Status?”

**”How do these same factors combine to determine their annual Salary?”**

**2. Data Source and Presentation**
The data for this case study is a sample of 300,000 international graduates from the cleaned_dataset.csv file. This dataset contains variables on demographics, academic background, and employment outcomes.

**2.1 Key Variables**
Key Predictors (Categorical): Language Proficiency (Basic, Intermediate, Advanced, Fluent), Education Level (Diploma, Bachelor’s, Master’s, PhD), Internship Experience (Yes, No).

Outcome 1 (Categorical): Employment Status (Employed, Unemployed, Continuing Education).

Outcome 2 (Continuous): Salary (annual salary in USD, filtered for ’Employed’ graduates only).

**2.2 Descriptive Analysis**
The cohort profile shows an average age of 30.5. Approximately 52% of graduates are employed, while 48% are either unemployed or continuing education. 65% of graduates report having internship experience. For employed graduates, the mean annual salary was $58,094.

Figure A: Bar Chart for Employment Status

**3. Methodology, Concepts, and Approaches**
Since our research question has two distinct outcomes (one categorical, one continuous), the methodology is split into two parts, applying techniques from Weeks 3, 4, and 5 of the PODA course.

**3.1 Part 1: Employment Status (Categorical Analysis)**
This section examines the association between the three key predictors and the categorical outcome of Employment Status.

Methodology: Chi-square (χ2) tests of independence were applied to determine statistical significance, as discussed in Week 3 and 5 lectures and outlined by McHugh [2013] and Sharpe [2013].

Effect Size: Cramér’s V was computed to measure the strength of association, providing a standardized measure of effect size from 0 (no association) to 1 (perfect association), using Cohen [1988] benchmarks.

Interactions: Combined predictor analyses (e.g., Language × Education) were used to explore interaction effects, following the principles of multi-factor analysis [Agresti, 2018].

Figure B: Histogram for Salary (e.g., A histogram showing the salary distribution for employed graduates.)

**3.2 Part 2: Salary (Continuous Analysis)**
This section analysis the continuous outcome of Salary. The dataset was filtered for ’Employed’ graduates only (Salary > 0) to ensure the validity of the analysis.

Method 1 - ANOVA (from Week 4): To explore Salary differences, One-Way and Two-Way Analysis of Variance (ANOVA) were used. Following the approach outlined by Field [2018], ANOVA is used to compare the mean Salary across multiple groups (e.g., Education Level) and to test for interaction effects (e.g., Education Level × Internship Experience). We used Tukey’s HSD post-hoc test to identify which specific groups were significantly different from one another.

Method 2 - MLR (from Week 5): To answer our research question about the combined effect of all three factors (Language, Education, Internship), a Multiple Linear Regression (MLR) model was conceptualised. This Week 5 method allows us to determine the individual contribution of each factor while controlling for the others, as described by Tabachnick and Fidell [2013].

Assumptions: For ANOVA/MLR, we checked for assumptions (e.g., Levene’s test for homogeneity of variance).

**4. Analysis, Findings, and Discussion**
**4.1 Part 1 Findings: Employment Status (Categorical Outcome)**
All individual and combined predictor tests were statistically significant (p < 0.001), indicating that all factors are associated with employment outcomes.

**4.1.1 Individual Predictors:**
Language Proficiency: (χ2 = 47, 438.76, p < 0.001, Cramér’s V = 0.281). Graduates with Advanced or Fluent language proficiency have the highest employment rates (approx. 71%).

Education Level: (χ2 = 46, 124.19, p < 0.001, Cramér’s V = 0.277). Graduates with a Master’s degree display the highest employment rates (71%).

Internship Experience: (χ2 = 6, 813.13, p < 0.001, Cramér’s V = 0.151). Graduates with internship experience are more likely to be employed (58%) than those without (42%).

University Ranking: (χ2 = 11, 249.76, p < 0.001, Cramér’s V = 0.137). Graduates from High-ranked universities have a notably higher employment rate (67%) compared to Medium (46%) and Low-ranked (46%) institutions.

**4.1.2 Combined Predictors (Interactions):**
Language × Education: (χ2 = 95, 948.64, p < 0.001, Cramér’s V = 0.400). This interaction shows the strongest relationship. Graduates with Advanced language skills and Master’s degrees have the highest employability.

Language × Internship: (χ2 = 54, 611.94, p < 0.001, Cramér’s V = 0.302).

Education × Internship: (χ2 = 53, 467.80, p < 0.001, Cramér’s V = 0.299).

Figure C: Ranked Cramér’s V Heatmap (Heatmap showing Cramér’s V values for all predictors, ranked from strongest (0.400) to weakest (0.137).)

**4.1.3 Discussion for Part 1**
The findings confirm that employability is multi-faceted. As per the Cramér’s V values (Figure 3), Language Proficiency (V=0.281) and Education Level (V=0.277) exhibit the strongest independent effects, while Internship (V=0.151) and University Rank (V=0.137) play a supportive, though less powerful, role.

The key finding is the strong interaction effect. The combination of Language × Education (V=0.400) is a far stronger predictor than any factor alone. This suggests that the value of a Master’s degree is highest when combined with strong communication skills. These results align with models of graduate capital [Tomlinson, 2012], suggesting that universities must emphasise both academic development (human capital) and communication skills (cultural capital) to maximise graduate outcomes.

**4.2 Part 2 Findings: Salary (Continuous Outcome)**
Analysis for salary was conducted using ANOVA and Tukey’s HSD tests on the subset of 156,644 employed graduates.

**4.2.1 ANOVA and Interaction Effects**
The One-Way ANOVA for Education Level was significant (F (3, 299996) = 48634.4, p < 0.001), showing that salary differs significantly across degrees. The Tukey test confirms a clear hierarchy: PhD (M = $50, 669) > Master’s (M = $30, 257) > Bachelor’s (M = $0) > Diploma (M = −$3, 159) (Note: M values are mean differences from a baseline, showing relative increase).

The One-Way ANOVA for Language Proficiency was also significant (F (3, 299996) = 11770.5, p < 0.001).

The Two-Way ANOVA for Education Level × Internship Experience revealed a significant interaction effect (F (3, 299992) = 433.46, p < 0.001).

The Two-Way ANOVA for Education Level × Language Proficiency also showed a significant interaction (F (9, 299984) = 690.79, p < 0.001).

**4.2.2 Discussion for Part 2**
The significant interaction effect from the Education × Internship ANOVA (Figure 4) is a key finding. It demonstrates that the salary benefit of an internship is not uniform across all education levels. As the chart illustrates, an internship provides a substantial salary boost for Bachelor’s graduates but a much smaller relative boost for PhDs.

This supports Human Capital Theory [Becker, 1964]. For a Bachelor’s graduate, an internship signals practical readiness (human capital) that their degree alone may not, thus boosting their market value. A PhD graduate’s degree, however, already signals high-level specialised expertise; their salary is primarily determined by this specialisation, making the generalist signal of an internship less impactful on salary.

The second interaction (Figure 5) between Education and Language further reinforces this. The salary gap between ’Basic’ and ’Advanced/Fluent’ language skills widens significantly at the Master’s and PhD levels. This suggests that for high-level roles, advanced technical knowledge (the degree) must be paired with advanced communication skills (language) to unlock the highest salary potential.

**5. Limitations and Further Research**
A key limitation was the ’Unknown’ Job_Sector for 143,356 graduates, which prevented a crucial analysis of salary by industry. Future analysis should also test the MLR assumptions (e.g., homoscedasticity, multicollinearity) more robustly before interpreting its coefficients.

Further research could explore the significant gender pay gap that was visible in the descriptive data. Additionally, a (multinomial) logistic regression model, as introduced in Week 5 PODA content, could be built to model the probability of being in one of the three Employment Status categories, providing a more predictive model than the associative χ2 tests.

**6. References**
Agresti, A. (2018). Statistical Methods for the Social Sciences (5th ed.). London: Pearson Education.

Babbie, E. (2020). The Practice of Social Research (15th ed.). Boston: Cengage Learning.

Becker, G.S. (1964). Human Capital: A Theoretical and Empirical Analysis, with Special Reference to Education. New York: Columbia University Press.

Bewick, V., Cheek, L., & Ball, J. (2004). ‘Statistics review 8: Qualitative data – Tests of association’, Critical Care, 8(1), pp. 46–53.

Chiswick, B.R., & Miller, P.W. (2007). The Economics of Language: International Analyses. London: Routledge.

Cohen, J. (1988). Statistical Power Analysis for the Behavioral Sciences (2nd ed.). Hillsdale, NJ: Lawrence Erlbaum Associates.

Crossman, J.E., & Clarke, M. (2010). ’International experience and graduate employability: stakeholder perspectives on benefits, barriers and enabling factors’, Higher Education, 59(5), pp. 599-613.

Field, A. (2018). Discovering Statistics Using IBM SPSS Statistics (5th ed.). London: Sage Publications.

Hair, J.F., Black, W.C., Babin, B.J., & Anderson, R.E. (2019). Multivariate Data Analysis (8th ed.). Boston: Cengage Learning.

Hosmer, D.W., & Lemeshow, S. (2000). Applied Logistic Regression (2nd ed.). New York: John Wiley & Sons.

Hout, M. (2012). ’Social and Economic Returns to College Education’, Annual Review of Sociology, 38, pp. 379-400.

Knouse, S. B., & Fontenot, G. (2008). ’Benefits of the internship: a study of student and employer perspectives’, Education + Training, 50(2), pp. 151-161.

McHugh, M.L. (2013). ‘The Chi-square test of independence’, Biochemia Medica, 23(2), pp. 143–149.

Sharpe, D. (2013). ’Your Chi-Square Test is Statistically Significant: Now What?’, Practical Assessment, Research, and Evaluation, 18(1), 8.

Tabachnick, B.G., & Fidell, L.S. (2013). Using Multivariate Statistics (6th ed.). London: Pearson Education.

Tomlinson, M. (2012). ’Graduate Employability: A Review of Conceptual and Empirical Themes’, Higher Education Policy, 25(4), pp. 407-431.

Vaughan, T.S. (2017). ’One-Way, Two-Way, and Three-Way ANOVA’, in Encyclopedia of Statistics in Behavioral Science. New York: John Wiley & Sons.
