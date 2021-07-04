# # #import readFiles
# # import json
# # # t1=[['patient', 'was suffering from', 'breathing problem'], ['patient', 'was suffering from', 'problem'], ['She', 'consulted', 'doctor'], ['It she', 'told', 'covid-19'], ['She', 'was', 'quarantined'], ['She', 'was quarantined for', '14 days']]
# # # t2=[['patient', 'was suffering from', 'breathing problem'], ['patient', 'was suffering from', 'problem']]
# # # t1=[['It', 'was', 'summer'], ['It', 'was', 'hot summer'], ['Nobody', 'go', ''], ['patient', 'got', 'covid 19'], ['She', 'was', 'quarantined']]
# # # t2=[['patient', 'was suffering from', 'breathing problem'], ['patient', 'was suffering from', 'problem'], ['She', 'consulted', 'doctor'], ['she', 'was', 'quarantined'], ['she', 'was', 'then quarantined for 14 days'], ['she', 'was quarantined for', '14 days'], ['she', 'was', 'then quarantined']]
# # # # a=[]

# # # a=set([t[0]+" "+t[2] for t in t1])
# # # b=set([t[0]+" "+t[2] for t in t2])
# # # print("ans-->",a,b)
# # # print(a.intersection(b))
# # # files=["Doc.txt","s.txt"]
# # # tripletss=readFiles.process_files(files)

# # tripletss={'Doc.txt': [['It', 'was', 'summer'], ['It', 'was', 'hot summer'], ['Nobody', 'go', ''], ['patient', 'got', 'covid-19'], ['She', 'was', 'quarantined']], 's.txt': [['patient', 'was suffering from', 'breathing problem'], ['patient', 'was suffering from', 'problem'], ['She', 'consulted', 'doctor'], ['she', 'was', 'quarantined'], ['she', 'was', 'then quarantined for 14 days'], ['she', 'was quarantined for', '14 days'], ['she', 'was', 'quarantined']]}
# # # tripletss=[[['It', 'was', 'summer'], ['It', 'was', 'hot summer'], ['patient', 'got', 'covid 19']],[['It', 'was', 'summer'], ['It', 'was', 'hot summer'], ['Nobody', 'go', ''], ['patient', 'got', 'covid 19'], ['She', 'was', 'quarantined'],['patient', 'was suffering from', 'breathing problem']], [['patient', 'was suffering from', 'breathing problem'], ['patient', 'was suffering from', 'problem'], ['She', 'consulted', 'doctor'], ['she', 'was', 'quarantined'], ['she', 'was', 'then quarantined for 14 days'], ['she', 'was quarantined for', '14 days'], ['she', 'was', 'then quarantined']]]
# # #print(str(tripletss))
# # # try:
# # #     f = open('Triplets.txt', 'w')s
# # #     json.dump(tripletss, f)
# # #     #f=open("Triplets.txt",'w',encoding='utf-8')
# # #     #f.write(tripletss)
# # # finally:
# # #     f.close()
# # a=[]
# # for tp in tripletss.values():
# #     r=[]
# #     print("-->",tp)
# #     # x=[[t[i].lower() for i in range(len(t))] for t in tp]
# #     # a.append(x)
# #     for t in tp:
# #         for i in t:
# #             r.append(i)
# #     a.append(r)
# # print(a)

# #     # for t in tp:
# #         # s=((t[0]+" "+t[2]))
# #         # print("--",s)
# #         # a[i].append(s)
# #     #a[i]=set([t[0]+" "+t[2] for t in tp])
# # k="covid-19"
# # # print(list(tripletss.keys()))
# # for i in range(len(a)):
# #     #if(i!=j):
# #     #print(i,"-",a[i],"<->",j,'-',a[j])
# #     p=(a[i].count(k)/len(a[i]))*100
# #     print("occurance of ",k, "in ",list(tripletss.keys())[i],"==> ",round(p,2),"%") # (common strings/ all strings without repetition)*10
# #     # print("occurance of ",k, "in "0,list(tripletss.keys())[i],"==> ",len((a[i]) & (k)) / float(len((a[i]) | (k))) * 100) # (common strings/ all strings without repetition)*100
# #     # #print(a[i].intersection(a[j]))


# import streamlit as st 

# # EDA Pkgs
# import pandas as pd 
# import numpy as np 


# # Data Viz Pkg
# import matplotlib.pyplot as plt 
# import matplotlib
# matplotlib.use("Agg")
# import seaborn as sns 



# def main():
# 	"""Semi Automated ML App with Streamlit """

# 	activities = ["EDA","Plots"]	
# 	choice = st.sidebar.selectbox("Select Activities",activities)

# 	if choice == 'EDA':
# 		st.subheader("Exploratory Data Analysis")

# 		data = st.file_uploader("Upload a Dataset", type=["csv", "txt"])
# 		if data is not None:
# 			df = pd.read_csv(data)
# 			st.dataframe(df.head())
			

# 			if st.checkbox("Show Shape"):
# 				st.write(df.shape)

# 			if st.checkbox("Show Columns"):
# 				all_columns = df.columns.to_list()
# 				st.write(all_columns)

# 			if st.checkbox("Summary"):
# 				st.write(df.describe())

# 			if st.checkbox("Show Selected Columns"):
# 				selected_columns = st.multiselect("Select Columns",all_columns)
# 				new_df = df[selected_columns]
# 				st.dataframe(new_df)

# 			if st.checkbox("Show Value Counts"):
# 				st.write(df.iloc[:,-1].value_counts())

# 			if st.checkbox("Correlation Plot(Matplotlib)"):
# 				plt.matshow(df.corr())
# 				st.pyplot()

# 			if st.checkbox("Correlation Plot(Seaborn)"):
# 				st.write(sns.heatmap(df.corr(),annot=True))
# 				st.pyplot()


# 			if st.checkbox("Pie Plot"):
# 				all_columns = df.columns.to_list()
# 				column_to_plot = st.selectbox("Select 1 Column",all_columns)
# 				pie_plot = df[column_to_plot].value_counts().plot.pie(autopct="%1.1f%%")
# 				st.write(pie_plot)
# 				st.pyplot()



# 	elif choice == 'Plots':
# 		st.subheader("Data Visualization")
# 		data = st.file_uploader("Upload a Dataset", type=["csv", "txt", "xlsx"])
# 		if data is not None:
# 			df = pd.read_csv(data)
# 			st.dataframe(df.head())


# 			if st.checkbox("Show Value Counts"):
# 				st.write(df.iloc[:,-1].value_counts().plot(kind='bar'))
# 				st.pyplot()
		
# 			# Customizable Plot

# 			all_columns_names = df.columns.tolist()
# 			type_of_plot = st.selectbox("Select Type of Plot",["area","bar","line","hist","box","kde"])
# 			selected_columns_names = st.multiselect("Select Columns To Plot",all_columns_names)

# 			if st.button("Generate Plot"):
# 				st.success("Generating Customizable Plot of {} for {}".format(type_of_plot,selected_columns_names))

# 				# Plot By Streamlit
# 				if type_of_plot == 'area':
# 					cust_data = df[selected_columns_names]
# 					st.area_chart(cust_data)

# 				elif type_of_plot == 'bar':
# 					cust_data = df[selected_columns_names]
# 					st.bar_chart(cust_data)

# 				elif type_of_plot == 'line':
# 					cust_data = df[selected_columns_names]
# 					st.line_chart(cust_data)

# 				# Custom Plot 
# 				elif type_of_plot:
# 					cust_plot= df[selected_columns_names].plot(kind=type_of_plot)
# 					st.write(cust_plot)
# 					st.pyplot()
    


# if __name__ == '__main__':
# 	main()
print("Her")