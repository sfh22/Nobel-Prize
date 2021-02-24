import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

@st.cache(allow_output_mutation=True)
def read_file(file):
    df = pd.read_csv(file)
    return df

file = 'nobel.csv'
nobel = read_file(file)

nobel['birth_date'] = pd.to_datetime(nobel['birth_date'])
nobel['age'] = nobel['year'] - nobel['birth_date'].dt.year
nobel['decade'] = (np.floor(nobel['year']/10) * 10).astype(int)

st.set_option('deprecation.showPyplotGlobalUse', False)

purpose = st.sidebar.radio('Choose a Page', ['Nobel Prize: Overview', 'Nobel Prize: Quick Facts', 'Nobel Prize: All Prizes', 'Nobel Prize: Physics', 'Nobel Prize: Chemistry',\
                                                 'Nobel Prize: Literature', 'Nobel Prize: Medicine', 'Nobel Prize: Economics', 'Nobel Prize: Peace', 'Nobel Prize: USA', \
                                                 'Nobel Prize: Females', 'Nobel Prize: Age', 'Nobel Prize: More than Once'])

if purpose == 'Nobel Prize: Overview':
    st.title('A Visual History of Nobel Prize Winners')
    st.text('')

    image = Image.open(r"C:\Users\samer\Dropbox\fotos\Nobel_Prize.png")
    st.image(image)
    st.text('')

    st.header("**What is the Nobel Prize**")
    st.write('The Nobel prize is one of the most famous and prestigious intellectual awards.\
              It is awarded annually for 6 different categories. From Stockholm, the Royal Swedish \
              Academy of Sciences confers the prizes for physics, chemistry, and economics, the Karolinska \
              Institute confers the prize for physiology or medicine, and the Swedish Academy confers the \
              prize for literature. The Norwegian Nobel Committee based in Oslo confers the prize for peace.')

    st.write('A person or organization awarded the Nobel Prize is called a Nobel Laureate. The word "laureate" \
              refers to the laurel wreath (إكليل الغار) that was considered as "a trophy" in ancient greek, \
              given to victors of competitions (image below).')
    st.text('')

    image1 = Image.open(r"C:\Users\samer\Dropbox\fotos\wreath.PNG")
    st.image(image1, width=350)
    st.text('')

    st.header('**Alfred Nobel: The Founder of the Nobel Prize**')
    st.write("Alfred Nobel (1833-1896) was born in Stockholm, Sweden, on 21 October 1833. His family was descended \
              from Olof Rudbeck, the best-known technical genius in Sweden in the 17th century, an era in which \
              Sweden was a great power in northern Europe. Nobel was fluent in several languages, and wrote poetry \
              and drama. Nobel was also very interested in social and peace-related issues, and held views that were \
              considered radical during his time. Alfred Nobel’s interests are reflected in the prize he established.")
    st.text('')

    st.header('**Aphorisms by Alfred Nobel**')
    st.write('Literature occupied a central role in the life of Alfred Nobel. He regarded various literary forms of \
              expression as opportunities to achieve a greater understanding of our own thoughts, lives and relationships with \
              other people and our surroundings. Alfred Nobel had an extensive library, which included important European \
              literary works. Inspired by Shelley and Byron, he wrote poems in English as a young man. Toward the end of his \
              life, he wrote the tragedy Nemesis. His best literary form of expression was probably the aphorism, where he often \
              expressed himself drastically.')

    st.subheader('*"A heart can no more be forced to love than a stomach can be forced to digest food by persuasion."*')
    st.subheader('*"Second to agriculture, humbug is the biggest industry of our age."*')
    st.subheader('*"We build upon the sand, and the older we become, the more unstable this foundation becomes."*')
    st.subheader('*"It is not sufficient to be worthy of respect in order to be respected."*')
    st.subheader('*"The best excuse for the fallen ones is that Madame Justice herself is one of them."*')
    st.subheader('*"Self-respect without the respect of others is like a jewel which will not stand the daylight."*')

elif purpose == 'Nobel Prize: Quick Facts':
    st.title('Nobel Prize Quick Facts')
    st.text('')

    image2 = Image.open(r"C:\Users\samer\Dropbox\fotos\nob.PNG")
    st.image(image2)

    st.text('')

    st.write('On 27 November 1895, Alfred Nobel signed his last will and testament, giving the largest share of his fortune \
             to a series of prizes in Physics, Chemistry, Physiology or Medicine, Literature and Peace – the Nobel Prizes. \
             In 1968, Sveriges Riksbank (Sweden’s central bank) established The Sveriges Riksbank Prize in Economic Sciences \
             in Memory of Alfred Nobel. Learn more about the Nobel Laureates here.')

    st.header('603 Nobel Prizes')
    st.write('Between 1901 and 2020, the Nobel Prizes and the Prize in Economic Sciences were awarded 603 times.')

    image3 = Image.open(r"C:\Users\samer\Dropbox\fotos\num_prizes.PNG")
    st.image(image3)

    st.write('In the statutes of the Nobel Foundation it says: “A prize amount may be equally divided between two works, each \
            of which is considered to merit a prize. If a work that is being rewarded has been produced by two or three persons, \
            the prize shall be awarded to them jointly. In no case may a prize amount be divided between more than three persons.”')

    st.header('962 Nobel Laureates')
    st.write('A total of 934 Laureates and 28 organizations have been awarded the Nobel Prize between 1901 and 2020. Of them, 86 are  \
             Laureates in Economic Sciences. A small number of individuals and organizations have been honoured more than once, which  \
             means that 930 individuals and 25 unique organizations have received the Nobel Prize in total.')

    st.header('Years without Nobel Prizes')
    st.write('Since the start, in 1901, there are some years when the Nobel Prizes have not been awarded. The total number of times are 49. \
              Most of them during World War I (1914-1918) and II (1939-1945). In the statutes of the Nobel Foundation it says: “If none of \
              the works under consideration is found to be of the importance indicated in the first paragraph, the prize money shall be \
              reserved until the following year. If, even then, the prize cannot be awarded, the amount shall be added to the Foundation’s\
              restricted funds.”.')

    st.write('**Physics:** 1916, 1931, 1934, 1940, 1941, 1942')
    st.write('**Chemistry:** 1916, 1917, 1919, 1924, 1933, 1940, 1941, 1942')
    st.write('**Medicine:** 1915, 1916, 1917, 1918, 1921, 1925, 1940, 1941, 1942')
    st.write('**Literature:**  1914, 1918, 1935, 1940, 1941, 1942, 1943')
    st.write('**Peace:** 1914, 1915, 1916, 1918, 1923, 1924, 1928, 1932, 1939, 1940, 1941, 1942, 1943, 1948, 1955, 1956, 1966, 1967, 1972')
    st.write('**Economic Sciences:** –')

    st.header('The Nobel Prize Award Ceremonies')
    st.write('On December 10, 1901, the Nobel Prizes were awarded for the first time in Stockholm and in Christiania (now Oslo) respectively.')
    st.write('The Prize Award Ceremony in Stockholm took place at the Old Royal Academy of Music during the years 1901-1925. Since 1926, the ceremony has taken place at the Stockholm Concert Hall with few exceptions: 1971in the Philadelphia Church; 1972 in the St. Erik International Fair (known today as Stockholm International Fairs) in Älvsjö, 1975 in the St. Erik International Fair and in 1991 at the Stockholm Globe Arena. The King of Sweden hands over the Prize to the laureate/s.')
    st.write('In Norway, during the years 1901-1904 the decision on the Peace Prize was announced at a meeting of the Storting on 10 December, after which the recipients were informed in writing. During 1905-1946 the Prize Award Ceremonies were held at the Nobel Institute building, during 1947-1989 in the auditorium of the University of Oslo and since 1990 at the Oslo City Hall. The King of Norway is present, but it is the Chairman of the Nobel Committee who hands over the Prize to the laureate/s.')

elif purpose == 'Nobel Prize: All Prizes':
    st.title('Nobel Prize')

    st.subheader("Total Number of  Prizes Awarded")
    if st.checkbox('Total'):
        st.write('Total Number of Prizes: ', len(nobel))

    st.subheader('Number of Unique Countries that Won')
    if st.checkbox("Unique Countries"):
        st.write('Number of Unique Countries: ', len(nobel['birth_country'].unique()))

    st.subheader("Number of Prizes Awarded by Gender")
    if st.checkbox('By Gender'):
        st.write('Prizes awarded to Males: ', len(nobel[nobel['sex'] == 'Male']))
        st.write('Prizes awarded to Females: ', len(nobel[nobel['sex'] == 'Female']))

    st.subheader("Number of Prizes Awarded by Country")
    if st.checkbox('By Country'):
        x = st.sidebar.multiselect('Select Countries', nobel.birth_country.unique())
        for country in x:
            st.write('**Number of Prizes Awarded to **',country, '** Nationals: **', len(nobel[nobel['birth_country'] == country]))

    st.subheader('Countries whose Nationals won the most Prizes')
    if st.checkbox("Most Prizes"):
        number = st.sidebar.slider('Number of Countries to Display', 1, len(nobel['birth_country'].unique()))
        st.write(nobel['birth_country'].value_counts().head(number).rename_axis('Country').reset_index(name='Number of Winners'))

    st.subheader("The Age Distribution of Nobel Prize Winners")
    fig = plt.figure(figsize=(8, 5))
    sns.histplot(nobel, x='age')
    if st.checkbox("Age Distribution"):
        st.pyplot()

    st.subheader("The Oldest and Youngest to win the Nobel Prize")

    oldest = (nobel.nlargest(1, 'age'))
    youngest = (nobel.nsmallest(1, 'age'))

    if st.checkbox("Youngest and Oldest"):
        st.write('The youngest person to win the Nobel Prize is: ', youngest[['full_name', 'age', 'birth_country']])
        st.text('')
        st.write('The oldest person to win the Nobel Prize is: ', oldest[['full_name', 'age', 'birth_country']])

    st.subheader("Number of Prizes Awarded by Decade")
    z = nobel.groupby('decade')['laureate_id'].count()
    z = pd.DataFrame(z)

    fig = plt.figure(figsize=(8, 5))
    sns.lineplot(data = z, x = 'decade', y = 'laureate_id' )
    if st.checkbox('Awards by Decade'):
         st.pyplot()

elif purpose == 'Nobel Prize: Physics':
    st.title('Physics Prize')
    phys = nobel[nobel['category'] == "Physics"]
    phys.head()

    st.subheader("Total Number of Physics Prizes Awarded")
    if st.checkbox('Total'):
        st.write('Total Number of Prizes: ', len(phys))

    st.subheader('Number of Unique Countries that Won a Physics Prize')
    if st.checkbox("Unique Countries"):
        st.write('Number of Unique Countries: ', len(phys['birth_country'].unique()))

    st.subheader("Number of Physics Prizes Awarded by Gender")
    if st.checkbox('By Gender'):
        st.write('Prizes awarded to Males: ', len(phys[phys['sex'] == 'Male']))
        st.write('Prizes awarded to Females: ', len(phys[phys['sex'] == 'Female']))

    st.subheader("Number of Physics Prizes Awarded by Country")
    if st.checkbox('By Country'):
        x = st.sidebar.multiselect('Select Countries', phys.birth_country.unique())
        for country in x:
            st.write('**Number of Physics Prizes Awarded to **',country, '** Nationals: **', len(phys[phys['birth_country'] == country]))

    st.subheader('Countries whose Nationals won the most Physics Prizes')
    if st.checkbox("Most Prizes"):
        number = st.sidebar.slider('Number of Countries to Display', 1, len(phys['birth_country'].unique()))
        st.write(phys['birth_country'].value_counts().head(number).rename_axis('Country').reset_index(name='Number of Winners'))

    st.subheader("The Age Distribution of Physics Nobel Prize Winners")
    fig = plt.figure(figsize=(8, 5))
    sns.histplot(phys, x='age')
    if st.checkbox("Age Distribution"):
        st.pyplot()

    st.subheader("The Oldest and Youngest to win the Physics Nobel Prize")

    oldest = (phys.nlargest(1, 'age'))
    youngest = (phys.nsmallest(1, 'age'))

    if st.checkbox("Youngest and Oldest"):
        st.write('The youngest person to win the Physics Nobel Prize is: ', youngest[['full_name', 'age', 'birth_country']])
        st.text('')
        st.write('The oldest person to win the Physics Nobel Prize is: ', oldest[['full_name', 'age', 'birth_country']])


    st.subheader("Number of Physics Prizes Awarded by Decade")
    z = phys.groupby('decade')['laureate_id'].count()
    z = pd.DataFrame(z)

    fig = plt.figure(figsize=(8, 5))
    sns.lineplot(data = z, x = 'decade', y = 'laureate_id' )
    if st.checkbox('Awards by Decade'):
         st.pyplot()

elif purpose == 'Nobel Prize: Chemistry':
    st.title('Chemistry Prize')
    chem = nobel[nobel['category'] == "Chemistry"]
    chem.head()

    st.subheader("Total Number of Chemistry Prizes Awarded")
    if st.checkbox('Total'):
        st.write('Total Number of Prizes: ', len(chem))

    st.subheader('Number of Unique Countries that Won a Chemistry Prize')
    if st.checkbox("Unique Countries"):
        st.write('Number of Unique Countries: ', len(chem['birth_country'].unique()))

    st.subheader("Number of Chemistry Prizes Awarded by Gender")
    if st.checkbox('By Gender'):
        st.write('Prizes awarded to Males: ', len(chem[chem['sex'] == 'Male']))
        st.write('Prizes awarded to Females: ', len(chem[chem['sex'] == 'Female']))

    st.subheader("Number of Chemistry Prizes Awarded by Country")
    if st.checkbox('By Country'):
        x = st.sidebar.multiselect('Select Countries', chem.birth_country.unique())
        for country in x:
            st.write('**Number of Chemistry Prizes Awarded to **',country, '** Nationals: **', len(chem[chem['birth_country'] == country]))

    st.subheader('Countries whose Nationals won the most Chemistry Prizes')
    if st.checkbox("Most Prizes"):
        number = st.sidebar.slider('Number of Countries to Display', 1, len(chem['birth_country'].unique()))
        st.write(chem['birth_country'].value_counts().head(number).rename_axis('Country').reset_index(name='Number of Winners'))

    st.subheader("The Age Distribution of Chemistry Nobel Prize Winners")
    fig = plt.figure(figsize=(8, 5))
    sns.histplot(chem, x='age')
    if st.checkbox("Age Distribution"):
        st.pyplot()

    st.subheader("The Oldest and Youngest to win the Chemistry Nobel Prize")

    oldest = (chem.nlargest(1, 'age'))
    youngest = (chem.nsmallest(1, 'age'))

    if st.checkbox("Youngest and Oldest"):
        st.write('The youngest person to win the Chemistry Nobel Prize is: ', youngest[['full_name', 'age', 'birth_country']])
        st.text('')
        st.write('The oldest person to win the Chemistry Nobel Prize is: ', oldest[['full_name', 'age', 'birth_country']])

    st.subheader("Number of Chemistry Prizes Awarded by Decade")
    z = chem.groupby('decade')['laureate_id'].count()
    z = pd.DataFrame(z)

    fig = plt.figure(figsize=(8, 5))
    sns.lineplot(data = z, x = 'decade', y = 'laureate_id' )
    if st.checkbox('Awards by Decade'):
         st.pyplot()

elif purpose == 'Nobel Prize: Literature':
    st.title('Literature Prize')
    lit = nobel[nobel['category'] == "Literature"]
    lit.head()

    st.subheader("Total Number of Literature Prizes Awarded")
    if st.checkbox('Total'):
        st.write('Total Number of Prizes: ', len(lit))

    st.subheader('Number of Unique Countries that Won a Literature Prize')
    if st.checkbox("Unique Countries"):
        st.write('Number of Unique Countries: ', len(lit['birth_country'].unique()))

    st.subheader("Number of Literature Prizes Awarded by Gender")
    if st.checkbox('By Gender'):
        st.write('Prizes awarded to Males: ', len(lit[lit['sex'] == 'Male']))
        st.write('Prizes awarded to Females: ', len(lit[lit['sex'] == 'Female']))

    st.subheader("Number of Literature Prizes Awarded by Country")
    if st.checkbox('By Country'):
        x = st.sidebar.multiselect('Select Countries', lit.birth_country.unique())
        for country in x:
            st.write('**Number of Literature Prizes Awarded to **',country, '** Nationals: **', len(lit[lit['birth_country'] == country]))

    st.subheader('Countries whose Nationals won the most Literature Prizes')
    if st.checkbox("Most Prizes"):
        number = st.sidebar.slider('Number of Countries to Display', 1, len(lit['birth_country'].unique()))
        st.write(lit['birth_country'].value_counts().head(number).rename_axis('Country').reset_index(name='Number of Winners'))

    st.subheader("The Age Distribution of Literature Nobel Prize Winners")
    fig = plt.figure(figsize=(8, 5))
    sns.histplot(lit, x='age')
    if st.checkbox("Age Distribution"):
        st.pyplot()

    st.subheader("The Oldest and Youngest to win the Literature Nobel Prize")

    oldest = (lit.nlargest(1, 'age'))
    youngest = (lit.nsmallest(1, 'age'))

    if st.checkbox("Youngest and Oldest"):
        st.write('The youngest person to win the Literature Nobel Prize is: ', youngest[['full_name', 'age', 'birth_country']])
        st.text('')
        st.write('The oldest person to win the Literature Nobel Prize is: ', oldest[['full_name', 'age', 'birth_country']])

    st.subheader("Number of Literature Prizes Awarded by Decade")
    z = lit.groupby('decade')['laureate_id'].count()
    z = pd.DataFrame(z)

    fig = plt.figure(figsize=(8, 5))
    sns.lineplot(data = z, x = 'decade', y = 'laureate_id')
    if st.checkbox('Awards by Decade'):
         st.pyplot()

elif purpose == 'Nobel Prize: Medicine':
    st.title('Medicine Prize')
    med = nobel[nobel['category'] == "Medicine"]
    med.head()

    st.subheader("Total Number of Medicine Prizes Awarded")
    if st.checkbox('Total'):
        st.write('Total Number of Prizes: ', len(med))

    st.subheader('Number of Unique Countries that Won a Medicine Prize')
    if st.checkbox("Unique Countries"):
        st.write('Number of Unique Countries: ', len(med['birth_country'].unique()))

    st.subheader("Number of Medicine Prizes Awarded by Gender")
    if st.checkbox('By Gender'):
        st.write('Prizes awarded to Males: ', len(med[med['sex'] == 'Male']))
        st.write('Prizes awarded to Females: ', len(med[med['sex'] == 'Female']))

    st.subheader("Number of Medicine Prizes Awarded by Country")
    if st.checkbox('By Country'):
        x = st.sidebar.multiselect('Select Countries', med.birth_country.unique())
        for country in x:
            st.write('**Number of Medicine Prizes Awarded to **',country, '** Nationals: **', len(med[med['birth_country'] == country]))

    st.subheader('Countries whose Nationals won the most Medicine Prizes')
    if st.checkbox("Most Prizes"):
        number = st.sidebar.slider('Number of Countries to Display', 1, len(med['birth_country'].unique()))
        st.write(med['birth_country'].value_counts().head(number).rename_axis('Country').reset_index(name='Number of Winners'))

    st.subheader("The Age Distribution of Medicine Nobel Prize Winners")
    fig = plt.figure(figsize=(8, 5))
    sns.histplot(med, x='age')
    if st.checkbox("Age Distribution"):
        st.pyplot()

    st.subheader("The Oldest and Youngest to win the Medicine Nobel Prize")

    oldest = (med.nlargest(1, 'age'))
    youngest = (med.nsmallest(1, 'age'))

    if st.checkbox("Youngest and Oldest"):
        st.write('The youngest person to win the Medicine Nobel Prize is: ', youngest[['full_name', 'age', 'birth_country']])
        st.text('')
        st.write('The oldest person to win the Medicine Nobel Prize is: ', oldest[['full_name', 'age', 'birth_country']])

    st.subheader("Number of Medicine Prizes Awarded by Decade")
    z = med.groupby('decade')['laureate_id'].count()
    z = pd.DataFrame(z)

    fig = plt.figure(figsize=(8, 5))
    sns.lineplot(data = z, x = 'decade', y = 'laureate_id')
    if st.checkbox('Awards by Decade'):
         st.pyplot()

elif purpose == 'Nobel Prize: Economics':
    st.title('Economics Prize')
    econ = nobel[nobel['category'] == "Economics"]
    econ.head()

    st.subheader("Total Number of Economics Prizes Awarded")
    if st.checkbox('Total'):
        st.write('Total Number of Prizes: ', len(econ))

    st.subheader('Number of Unique Countries that Won an Economics Prize')
    if st.checkbox("Unique Countries"):
        st.write('Number of Unique Countries: ', len(econ['birth_country'].unique()))

    st.subheader("Number of Economics Prizes Awarded by Gender")
    if st.checkbox('By Gender'):
        st.write('Prizes awarded to Males: ', len(econ[econ['sex'] == 'Male']))
        st.write('Prizes awarded to Females: ', len(econ[econ['sex'] == 'Female']))

    st.subheader("Number of Economics Prizes Awarded by Country")
    if st.checkbox('By Country'):
        x = st.sidebar.multiselect('Select Countries', econ.birth_country.unique())
        for country in x:
            st.write('**Number of Economics Prizes Awarded to **',country, '** Nationals: **', len(econ[econ['birth_country'] == country]))

    st.subheader('Countries whose Nationals won the most Economics Prizes')
    if st.checkbox("Most Prizes"):
        number = st.sidebar.slider('Number of Countries to Display', 1, len(econ['birth_country'].unique()))
        st.write(econ['birth_country'].value_counts().head(number).rename_axis('Country').reset_index(name='Number of Winners'))

    st.subheader("The Age Distribution of Economics Nobel Prize Winners")
    fig = plt.figure(figsize=(8, 5))
    sns.histplot(econ, x='age')
    if st.checkbox("Age Distribution"):
        st.pyplot()

    st.subheader("The Oldest and Youngest to win the Economics Nobel Prize")

    oldest = (econ.nlargest(1, 'age'))
    youngest = (econ.nsmallest(1, 'age'))

    if st.checkbox("Youngest and Oldest"):
        st.write('The youngest person to win the Economics Nobel Prize is: ', youngest[['full_name', 'age', 'birth_country']])
        st.text('')
        st.write('The oldest person to win the Economics Nobel Prize is: ', oldest[['full_name', 'age', 'birth_country']])

    st.subheader("Number of Economics Prizes Awarded by Decade")
    z = econ.groupby('decade')['laureate_id'].count()
    z = pd.DataFrame(z)

    fig = plt.figure(figsize=(8, 5))
    sns.lineplot(data = z, x = 'decade', y = 'laureate_id')
    if st.checkbox('Awards by Decade'):
         st.pyplot()

elif purpose == 'Nobel Prize: Peace':
    st.title('Peace Prize')
    peace = nobel[nobel['category'] == "Peace"]
    peace.head()

    st.subheader("Total Number of Peace Prizes Awarded")
    if st.checkbox('Total'):
        st.write('Total Number of Prizes: ', len(peace))

    st.subheader('Number of Unique Countries that Won a Peace Prize')
    if st.checkbox("Unique Countries"):
        st.write('Number of Unique Countries: ', len(peace['birth_country'].unique()))

    st.subheader("Number of Peace Prizes Awarded by Gender")
    if st.checkbox('By Gender'):
        st.write('Prizes awarded to Males: ', len(peace[peace['sex'] == 'Male']))
        st.write('Prizes awarded to Females: ', len(peace[peace['sex'] == 'Female']))

    st.subheader("Number of Peace Prizes Awarded by Country")
    if st.checkbox('By Country'):
        x = st.sidebar.multiselect('Select Countries', peace.birth_country.unique())
        for country in x:
            st.write('**Number of Peace Prizes Awarded to **',country, '** Nationals: **', len(peace[peace['birth_country'] == country]))

    st.subheader('Countries whose Nationals won the most Peace Prizes')
    if st.checkbox("Most Prizes"):
        number = st.sidebar.slider('Number of Countries to Display', 1, len(peace['birth_country'].unique()))
        st.write(peace['birth_country'].value_counts().head(number).rename_axis('Country').reset_index(name='Number of Winners'))

    st.subheader("The Age Distribution of Peace Nobel Prize Winners")
    fig = plt.figure(figsize=(8, 5))
    sns.histplot(peace, x='age')
    if st.checkbox("Age Distribution"):
        st.pyplot()

    st.subheader("The Oldest and Youngest to win the Peace Nobel Prize")

    oldest = (peace.nlargest(1, 'age'))
    youngest = (peace.nsmallest(1, 'age'))

    if st.checkbox("Youngest and Oldest"):
        st.write('The youngest person to win the Peace Nobel Prize is: ', youngest[['full_name', 'age', 'birth_country']])
        st.text('')
        st.write('The oldest person to win the Peace Nobel Prize is: ', oldest[['full_name', 'age', 'birth_country']])

    st.subheader("Number of Peace Prizes Awarded by Decade")
    z = peace.groupby('decade')['laureate_id'].count()
    z = pd.DataFrame(z)

    fig = plt.figure(figsize=(8, 5))
    sns.lineplot(data = z, x = 'decade', y = 'laureate_id')
    if st.checkbox('Awards by Decade'):
         st.pyplot()

elif purpose == 'Nobel Prize: USA':
    st.header('Nobel Prize: USA')

    nobel['usa_born_winner'] = nobel['birth_country'] == "United States of America"
    nobel['decade'] = (np.floor(nobel['year'] / 10) * 10).astype(int)
    prop_usa_winners = nobel.groupby('decade', as_index=False)['usa_born_winner'].mean()

    st.subheader("Percentage of Winners who are American over the Decades")

    sns.set()
    plt.rcParams['figure.figsize'] = [11, 7]
    ax = sns.lineplot(x='decade', y='usa_born_winner', data=prop_usa_winners)
    ax.set_xlabel("Decade")
    ax.set_ylabel("Percentage American")
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))

    if st.checkbox("Show the Proportion of American Winners Plot"):
        st.pyplot()
    st.subheader("Percentage of Winners who are American per Category over the Decades")

    categ_dec_usa = nobel.groupby(by=['decade', 'category'], as_index=False).usa_born_winner.mean()
    categ_dec_usa = categ_dec_usa.pivot(index='decade', columns='category', values='usa_born_winner')

    ax = categ_dec_usa.plot()
    vals = ax.get_yticks()
    ax.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
    ax.set_xlabel("Decade")
    ax.set_ylabel("Percentage American")

    if st.checkbox('Show Percentage of American Winners per Category'):
        st.pyplot()

    st.subheader("First and Last Amercian to Win the Nobel Prize")

    if st.checkbox("First and Last American to Win the Nobel Prize"):
        only_american = nobel[nobel.usa_born_winner == 1]
        st.write('The first American to win the Nobel Prize is: ', only_american.nsmallest(1, 'year'))
        st.text('')
        st.write('The last American to win the Nobel Prize is: ', only_american.nlargest(1, 'year'))

elif purpose == 'Nobel Prize: Females':
    st.header('Nobel Prize: Females')

    nobel['female_winner'] = nobel['sex'] == "Female"
    prop_female_winners = nobel.groupby('decade', as_index=False)['female_winner'].mean()

    st.subheader("Percentage of Winners who are Females over the Decades")

    sns.set()
    plt.rcParams['figure.figsize'] = [11, 7]
    ax = sns.lineplot(x='decade', y='female_winner', data=prop_female_winners)
    ax.set_xlabel("Decade")
    ax.set_ylabel("Percentage Females")
    ax.yaxis.set_major_formatter(PercentFormatter(1.0))

    if st.checkbox("Show the Proportion of Females Winners Plot"):
        st.pyplot()
    st.subheader("Percentage of Winners who are Females per Category over the Decades")

    categ_dec_females = nobel.groupby(by=['decade', 'category'], as_index=False).female_winner.mean()
    categ_dec_females = categ_dec_females.pivot(index='decade', columns='category', values='female_winner')

    ax = categ_dec_females.plot()
    vals = ax.get_yticks()
    ax.set_yticklabels(['{:,.2%}'.format(x) for x in vals])
    ax.set_xlabel("Decade")
    ax.set_ylabel("Percentage Females")

    if st.checkbox('Show Percentage of American Winners per Category'):
        st.pyplot()

    st.subheader("First and Last Female to Win the Nobel Prize")

    if st.checkbox("First and Last Female to Win the Nobel Prize"):
        only_females = nobel[nobel.female_winner == 1]
        st.write('The first female to win the Nobel Prize is: ', only_females.nsmallest(1, 'year'))
        st.text('')
        st.write('The last female to win the Nobel Prize is: ', only_females.nlargest(1, 'year'))

elif purpose == 'Nobel Prize: Age':
    st.header('Nobel Prize: Age')

    st.subheader('Age of Nobel Prize Winners')
    sns.lmplot(x="year", y="age", data=nobel, lowess=True, aspect=2, line_kws={'color': 'black'})
    if st.checkbox('Age of Nobel Prize Winners Plot'):
        st.pyplot()

    st.subheader('Age differences between prize categories')
    sns.lmplot(x="year", y="age", data=nobel, row='category', lowess=True, aspect=2, line_kws={'color': 'black'})
    if st.checkbox("Show Age Difference Plot"):
        st.pyplot()

elif purpose == 'Nobel Prize: More than Once':
    st.header('Nobel Prize: More than Once')

    st.subheader('Some Won more than One Nobel Prize')
    if st.checkbox('People who Won more than Once'):
        more_than_once = nobel.groupby(by="full_name", as_index=False).filter(lambda group: len(group) > 1)
        more_than_once = more_than_once[['full_name', 'category', 'prize', 'birth_country', 'year']]
        st.table(more_than_once)



