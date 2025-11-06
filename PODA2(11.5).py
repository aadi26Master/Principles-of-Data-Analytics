#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings

# --- 全局设置 ---

# 设置一个通用的字体，以避免图表中的方框或乱码问题
plt.rcParams['font.family'] = 'DejaVu Sans'

# 抑制未来的警告信息，使输出更整洁
warnings.filterwarnings('ignore')

# 设置Seaborn的默认绘图风格
sns.set(style="whitegrid")

print("Libraries imported and settings applied.")


# In[2]:


# --- 1. 加载和准备数据 ---
try:
    # 从CSV文件加载数据
    df = pd.read_csv("（PODA)cleaned_dataset.csv")

    # 定义类别变量的逻辑顺序 (这能确保图表的X轴按正确顺序排列)
    edu_order = ["Diploma", "Bachelor's", "Master's", "PhD"]
    lang_order = ["Basic", "Intermediate", "Advanced", "Fluent"]

    # --- 关键步骤 ---
    # 创建一个只包含“已就业”毕业生的新DataFrame
    # 我们只对已就业的人分析薪资，这在方法论上是正确的
    df_employed = df[df['Employment_Status'] == 'Employed'].copy()

    print("Data loaded and prepared successfully.")
    print(f"Total graduates: {len(df)}")
    print(f"Employed graduates for salary analysis: {len(df_employed)}")
    
except FileNotFoundError:
    print(f"错误：未找到文件 '（PODA)cleaned_dataset.csv'。")
    print("请确保该文件与你的Notebook在同一目录下。")
except Exception as e:
    print(f"加载数据时发生错误: {e}")


# In[3]:


# --- 2. 单变量可视化 (介绍变量) ---

# 图表 1: 学历分布
print("Generating: 1_education_level_distribution.png")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Education_Level', order=edu_order, palette='viridis')
plt.title('Distribution of Education Levels', fontsize=16)
plt.xlabel('Education Level', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.savefig('1_education_level_distribution.png', bbox_inches='tight')
plt.clf()  # 清除当前图表，为下一张做准备

# 图表 2: 语言能力分布
print("Generating: 2_language_proficiency_distribution.png")
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Language_Proficiency', order=lang_order, palette='plasma')
plt.title('Distribution of Language Proficiency', fontsize=16)
plt.xlabel('Language Proficiency', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.savefig('2_language_proficiency_distribution.png', bbox_inches='tight')
plt.clf()

print("...Done (Plots 1, 2)")


# In[4]:


# 图表 3: 实习经历分布 (饼图)→（条形图）

# ### --- MODIFICATION  (Chart 3) --- ###
# Original was a pie chart. Changed to a horizontal bar chart
# for better clarity and consistency with other plots.
print("Generating: 3_internship_distribution_MODIFIED.png")
plt.figure(figsize=(10, 6)) # 为条形图调整了figsize
sns.countplot(data=df, y='Internship_Experience', palette='Pastel1')
plt.title('Distribution of Internship Experience', fontsize=16)
plt.xlabel('Count', fontsize=12) # 为X轴添加了标签
plt.ylabel('Had Internship Experience', fontsize=12) # 为Y轴添加了标签
plt.savefig('3_internship_distribution_MODIFIED.png', bbox_inches='tight')
plt.clf()

# ### --- MODIFICATION (Chart 4) --- ###
# Original was a pie chart. This is a CRITICAL change.
# The pie chart could not visually distinguish 'Unemployed' (10.1%)
# from 'Studying' (10.0%). A bar chart is the correct choice here.
print("Generating: 4_employment_status_MODIFIED.png")
plt.figure(figsize=(10, 6)) # 为条形图调整了figsize
sns.countplot(data=df, x='Employment_Status', palette='Set2')
plt.title('Distribution of Employment Status', fontsize=16)
plt.xlabel('Employment Status', fontsize=12)
plt.ylabel('Count', fontsize=12)
plt.savefig('4_employment_status_MODIFIED.png', bbox_inches='tight')
plt.clf()


# 图表 5: 薪资分布 (直方图, 仅限已就业者)
print("Generating: 5_salary_distribution.png")
plt.figure(figsize=(12, 7))
sns.histplot(df_employed['Salary'], kde=True, bins=50, color='dodgerblue')
plt.title('Distribution of Annual Salary (Employed Graduates)', fontsize=16)
plt.xlabel('Annual Salary', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.axvline(df_employed['Salary'].mean(), color='red', linestyle='--', linewidth=2, label=f'Mean: ${df_employed["Salary"].mean():,.0f}')
plt.axvline(df_employed['Salary'].median(), color='green', linestyle='-', linewidth=2, label=f'Median: ${df_employed["Salary"].median():,.0f}')
plt.legend()
plt.savefig('5_salary_distribution.png', bbox_inches='tight')
plt.clf()

print("...Done (Plots 3, 4, 5)")


# In[5]:


# --- 3. 双变量可视化 (探索关系 - 薪资) ---

# 图表 6: 薪资 vs 学历 (箱线图)
print("Generating: 6_salary_by_education.png")
plt.figure(figsize=(12, 7))
sns.boxplot(data=df_employed, x='Education_Level', y='Salary', order=edu_order, palette='viridis')
plt.title('Annual Salary by Education Level', fontsize=16)
plt.xlabel('Education Level', fontsize=12)
plt.ylabel('Annual Salary', fontsize=12)
plt.savefig('6_salary_by_education.png', bbox_inches='tight')
plt.clf()

# 图表 7: 薪资 vs 语言能力 (箱线图)
print("Generating: 7_salary_by_language.png")
plt.figure(figsize=(12, 7))
sns.boxplot(data=df_employed, x='Language_Proficiency', y='Salary', order=lang_order, palette='plasma')
plt.title('Annual Salary by Language Proficiency', fontsize=16)
plt.xlabel('Language Proficiency', fontsize=12)
plt.ylabel('Annual Salary', fontsize=12)
plt.savefig('7_salary_by_language.png', bbox_inches='tight')
plt.clf()

# 图表 8: 薪资 vs 实习经历 (箱线图)
print("Generating: 8_salary_by_internship.png")
plt.figure(figsize=(10, 7))
sns.boxplot(data=df_employed, x='Internship_Experience', y='Salary', palette='Pastel1')
plt.title('Annual Salary by Internship Experience', fontsize=16)
plt.xlabel('Had Internship Experience', fontsize=12)
plt.ylabel('Annual Salary', fontsize=12)
plt.savefig('8_salary_by_internship.png', bbox_inches='tight')
plt.clf()

print("...Done (Plots 6, 7, 8)")


# In[6]:


# --- 3. 双变量可视化 (探索关系 - 就业状态) ---

# 图表 9: 就业状态 vs 实习经历 (堆叠百分比条形图)
print("Generating: 9_employment_by_internship.png")

# 这需要先计算交叉表并按行归一化 (normalize='index')
crosstab = pd.crosstab(df['Internship_Experience'], df['Employment_Status'], normalize='index')

# 使用pandas的内置plot功能来绘制堆叠图
crosstab.plot(kind='bar', stacked=True, figsize=(12, 7), colormap='Set2')
plt.title('Employment Status Breakdown by Internship Experience', fontsize=16)
plt.xlabel('Had Internship Experience', fontsize=12)
plt.ylabel('Proportion (of each group)', fontsize=12)
plt.xticks(rotation=0) # 保持X轴标签水平
plt.legend(title='Employment Status', bbox_to_anchor=(1.05, 1), loc='upper left') # 图例放到外面
plt.savefig('9_employment_by_internship.png', bbox_inches='tight')
plt.clf()

print("...Done (Plot 9)")


# In[7]:


# --- 4. 多变量可视化 (回答 "combine with") ---

# 图表 10: 薪资 vs 学历 & 实习经历 (分组箱线图)
print("Generating: 10_salary_by_education_and_internship_11.4.png")

# 将新的直观调色板定义为一个字典
intuitive_palette = {"No": "lightgrey", "Yes": "indianred"}

plt.figure(figsize=(14, 8))
sns.boxplot(data=df_employed,
            x='Education_Level',
            y='Salary',
            hue='Internship_Experience',
            order=edu_order,
            palette=intuitive_palette) # <-- 已修改的行
plt.title('Salary by Education Level and Internship Experience', fontsize=18)
plt.xlabel('Education Level', fontsize=14)
plt.ylabel('Annual Salary', fontsize=14)
plt.legend(title='Internship Experience', fontsize=12, title_fontsize=14)
plt.savefig('10_salary_by_education_and_internship_11.4.png', bbox_inches='tight')
plt.clf()

print("...Done (Plot 10)")
print("\n--- 所有图表已成功生成并保存！ ---")

# 最后，清除所有可能残留的图表内存
plt.close('all')


# In[ ]:




