```python
import sqlite3
import re

conn = sqlite3.connect('scopus_references_youth.db')
cursor = conn.cursor()

```


```python
# Выполняем запрос для чтения строк из таблицы "ref"
cursor.execute("CREATE TABLE IF NOT EXISTS ref AS SELECT * FROM references_good_journal")
```




    <sqlite3.Cursor at 0x2725cf26d50>




```python
cursor.execute("SELECT ID, reference FROM ref")
rows = cursor.fetchall()
```


```python
cursor.execute('ALTER TABLE ref ADD COLUMN author TEXT')
cursor.execute('ALTER TABLE ref ADD COLUMN year YEAR')
cursor.execute('ALTER TABLE ref ADD COLUMN volume TEXT')
cursor.execute('ALTER TABLE ref ADD COLUMN page INTEGER')
```




    <sqlite3.Cursor at 0x2725cf26d50>




```python
a = ('c.', 'pp', 'P', 'p', 'С', 'стр', 'c', 'P.')
author_re = re.compile(r"([A-Z][a-z\-]+)[^,]*")
number_re = re.compile(r'(?:^|\D)([12]\d{3})(?!\d)')
page_re = rf"(?:{'|'.join(a)})[.,]?\s*[-–]?\s*(\d+)"
#volume_re = r"\d+(?=\s*,?\s*pp\.|$)"
volume_re2 = rf"(?:(?<=#|№)\s*)?(?P<number>\d+)\s*(?:(?:{'|'.join(a)})(?:[.,]|\s{{2,}})?\s*)?"
#volume_re3= r"\d+\s\(\d+\)"
```


```python
author = []
year = []
page = []
volume = []

numbers = []
vol = 0 
p = 0
```


```python
len(rows)
```




    144158




```python
st = str(rows[261][1])
```


```python
st
```




    'Samokhvalov, N.A., Formation and Development of the State Youth Policy in the Russian Federation (2018) Aktualnye problemy sovremennosti: nauka i obshchestvo = Actual Issues of Modern Science and Society, (3), pp. 20-25. , http://i-journal.net/jdoc/apc_20.pdf, (accessed 12.01.2021). (In Russ., abstract in Eng)'




```python
st = re.sub(r'http\S+', '', st)
st = re.sub(r'\b\d{1,2}\.\d{1,2}\.\d{4}\b', '', st)
```


```python
st
```




    'Samokhvalov, N.A., Formation and Development of the State Youth Policy in the Russian Federation (2018) Aktualnye problemy sovremennosti: nauka i obshchestvo = Actual Issues of Modern Science and Society, (3), pp. 20-25. ,  (accessed ). (In Russ., abstract in Eng)'




```python
ID = int(rows[30][0])
```


```python
ID
```




    31




```python
for i in range(len(rows)):
    
    st = str(rows[i][1])
    st = re.sub(r'http\S+', '', st)
    st = re.sub(r'\b\d{1,2}\.\d{1,2}\.\d{4}\b', '', st)
    ID = int(rows[i][0])
    
    extensionsToCheck = ['Studies', 'Ezhegodnik', 'Rossiiskii', 'Obrazovanie', 'Rossii', 'Population', 'data',
                    'Russian',  'Source', 'Catalogue', 'Journal', 'dictionary', ']', ':', '?']
    
    author_re = re.compile(r"([A-Z][a-z\-]+)[^,]*")


    match_author = re.search(author_re, st)
    if match_author:
        aut = match_author.group()
        aut = re.sub(r"\(\d{4}\)", "", aut)
        if len(aut) < 50 and aut.count(' ') < 2:
            if not(any(ext in aut for ext in extensionsToCheck)):
                author.append(aut)
                #print(aut)
            else:
                author.append('')
        else:
            author.append('')

    else:
        author.append('')

    for match in number_re.findall(st):
        numbers.append(int(match))

    if numbers:
        max_number = max(numbers)
        year.append(max_number)
    else:
        year.append("")
    
    match_page =  re.search(page_re, st)
    
    if match_page:
        p = int(match_page.group(1))
        page.append(p)
    else:
        page.append("")
        
    #match_volume = re.search(volume_re2, list1[i])
    matches = re.finditer(volume_re2, st)
    numbers = [int(match.group('number')) for match in matches if int(match.group('number')) < 1000]
    if len(numbers) >=1:
        vol = int(numbers[0])
    if vol!= p and vol!= 0:
        volume.append(vol)
    else:
        volume.append("")
    numbers = []
    vol = ''
    
    if i % 1000 == 0:
        print(st, (author[i], year[i], volume[i], page[i], int(rows[i][0])))
        
    cursor.execute("UPDATE ref SET author=?, year=?, volume=?, page=? WHERE ID=?",
                   (author[i], year[i], volume[i], page[i], ID))
    conn.commit()
conn.close()
```

    (2001) Elements of Course Design: A Practical Guide to Integrating ICT into Languages for Specific Purposes in Higher Education., , Farnham: Surrey Institute of Art and Design. At:  ('', 2001, '', '', 1)
    Fierman, W., Language education in post-Soviet Kazakhstan: Kazakh-medium instruction in urban schools (2006) The Russian Review, 65, pp. 98-116 ('Fierman', 2006, 65, 98, 1001)
    Discussion on veracity and scientificity., pp. 358-362. , 380 ('', '', '', 358, 2001)
    Emelin, V.A., Sh, T.A., Deformation of the chronotope in the so-cio-cultural conditions of accelerating (2015) Voprosy of Filosofii = Issius of Philosophy, 2, pp. 14-24. , Russ ('Emelin', 2015, 2, 14, 3001)
    Mkrtchyan, N., Vakulenko, E., Interregional Migration in Russia at Different Stages of the Life Cycle (2019) Geo Journal, 84 (6), pp. 1549-1565 ('Mkrtchyan', 2019, 84, 1549, 4001)
    Park, W., Wu, J. Y., Erduran, S., The nature of STEM disciplines in the science education standards documents from the USA, Korea and Taiwan (2020) Science & Education, 29 (4), pp. 899-927 ('Park', 2020, 29, 899, 5001)
    Isabelli-García, C.L., Study abroad social networks, motivation, and attitudes: Implications for SLA (2006) Language learners in study abroad contexts, pp. 231-258. , M. DuFon & E. Churchill (Eds.), Clevedon, UK: Multilingual Matters ('Isabelli-García', 2006, '', 231, 6001)
    Belz, J., Institutional and individual dimensions of transatlantic group work in network-based language teaching (2001) ReCALL, 13 (2), pp. 213-231 ('Belz', 2001, 13, 213, 7001)
    Ichikawa, S., (1991) Distinctive Features of Japanese Education, , Tokyo: National Institute for Educational Research ('Ichikawa', 1991, '', '', 8001)
    Tongren, H.N., Hecht, L., Kovach, K., Recognizing cultural differences: Key to successful U.S.Russian enterprises (1995) Public Personnel Management, 24, pp. 1-17 ('Tongren', 1995, 24, 1, 9001)
    Di Tella, R., MacCulloch, R., Oswald, A.J., The macroeconomics of happiness (1996) Amer. Econ. Rev. ('Di Tella', 1996, '', '', 10001)
    Dumais, S.A., Children’s Cultural Capital and Teachers’ Assessments of Effort and Ability: The Influence of School Sector (2005) Catholic Education: A Journal of Inquiry and Practice, 8 (4), pp. 418-439 ('Dumais', 2005, '', 8, 11001)
    Souza, S.C., Dourado, L., Problem-Based Learning (PBL): A learning methodology for innovative educational teaching (2015) HOLOS, 5, pp. 182-200. , In Brasil, abstract in Eng ('Souza', 2015, 5, 182, 12001)
    Dostoevsky, F., (1990) The Brothers Karamazov, , Translated by Richard Pevear and Larissa Volokhonsky. New York: Farrar, Straus and Girous ('Dostoevsky', 1990, '', '', 13001)
    Glenn, D., You will be tested on this (2007) The Chronicle of Higher Education, 53, pp. A14. , June 8 ('Glenn', 2007, 53, '', 14001)
    Bisyarina, V.P., Rapoport, Z.Z., Maltsyev, P.V., Minyaylo, E.K., (1978) Child health in the North, p. 152. , Moscow: Meditsina ('Bisyarina', 1978, '', 152, 15001)
    Cenoz, J., The influence of bilingualism on third language acquisition: Focus on multilingualism (2013) Language Teaching, 46 (1), pp. 71-86 ('Cenoz', 2013, 46, 71, 16001)
    (2012) Russian Second Division Regulation, ,  ('', 2012, '', '', 17001)
    Freiberg, H.J., (1999) School Climate: Measuring, Improving, and Sustaining Healthy Learning Environments, , London: Falmer ('Freiberg', 1999, '', '', 18001)
    Oldberg, I., The Emergence of a Regional Identity in the Kaliningrad Oblast (2000) Cooperation and Conflict, 35 (3), p. 273 ('Oldberg', 2000, '', 35, 19001)
    2-E ('', '', 2, '', 20001)
    Khayrullina, A.R., Acceptance information management decisions in small and medium entrepreneurship in digital economy (2019) Bull. USTU. Sci. Edu. Econ. Ser. Econ., 4 (30). , in Russian ('Khayrullina', 2019, 4, '', 21001)
    There is a further nuance in the Sino-Soviet aspect of the Nigerian conflict. The Chinese have granted substantial technical aid to Zambia and Tanzania on excellent fiscal terms and with no apparent reservations. Both countries had recognized Biafra. (Tanzania's statement of recognition is one of the most striking state documents of our time.) As Julius Nyerere, the President of Tanzania, has indicated, the so-called Chinese model can mean no more, realistically, than trade and technical relations between China and emergent African states ('', '', '', '', 22001)
    Koshelev, V.A., (1987) Konstantin Batyushkov. Stranstviya i strasti [Konstantin Batyushkov. Wanderings and passions], , Moscow: Sovremennik ('Koshelev', 1987, '', '', 23001)
    (2005), Russian Source ('', 2005, '', '', 24001)
    Heater, B., Bernie Sanders Intros “Stop Bad Employers by Zeroing Out Subsidies BEZOS” Bill (2018) Techcrunch, ,  ('Heater', 2018, '', '', 25001)
    Poletiek, F.H., Van Schijndel, T., Stimulus set size and statistical coverage of the grammar in artificial grammar learning (2009) Psychonomic Bulletin & Review, 16, pp. 1058-1064 ('Poletiek', 2009, 16, 1058, 26001)
    Heugh, K., Disabling and Enabling: implications of language policy in South Africa (1997) Cultural Democracy and Ethnic Pluralism - Multicultural and Multilingual Policies in Education, pp. 243-270. , Bern: Peter Lang ('Heugh', 1997, '', 243, 27001)
    Obler, Albert, Gordon, Asymmetrical cerebral dominance in bilinguals (1975) Paper presented at the Academy of Aphasia, , Victoria, BC, Canada ('Obler', 1975, '', '', 28001)
    (1999) Eurobarometer 51, ,  Brussels, Belgium: DC 10 ('Eurobarometer 51', 1999, 51, '', 29001)
    Resnick, D., (1995) Diagnosis of Bone and Joint Disorders, , Philadelphia: W.B. Saunders ('Resnick', 1995, '', '', 30001)
    Boldyrev-Kazarin, D.A., Narodnoe iskusstvo v Sibiri (Iz ocherkov po istorii russkogo iskusstva v Sibiri) (1924) Sibirskaya zhivaya starina: Etnografichesky sbornik, 2, pp. 5-20 ('Boldyrev-Kazarin', 1924, 2, 5, 31001)
    Barr, A., Serra, D., The effects of externalities and framing on bribery in a petty corruption experiment (2009) Experimental Economics, 12 (4), pp. 488-503 ('Barr', 2009, '', 12, 32001)
    Joy, L., Salaries of Recent Male and Female College Graduates: Educational and Labor Market Effects (2003) Industrial and Labor Relations Review, 56, pp. 600-621 ('Joy', 2003, 56, 600, 33001)
    Allen, K.R., Piercy, F.P., Feminist auto ethnography (2005) Research methods in family therapy (, pp. 155-169. , In:, In: Sprenkle D. H., editorsPiercy F. P., editors 2nd ed., New York, Guilford ('Allen', 2005, '', 155, 34001)
    Saveliev, A., Picko, P, (2015) Diagnoz - poiskovik [Diagnosed as Poiskovik], , Saint Petersburg: BIONT ('Saveliev', 2015, '', '', 35001)
    Vasil’ev, A., Naryady novykh bogov (1995) Novyi dzhentl’men, pp. 60-70. , Spring ('Vasil’ev', 1995, '', 60, 36001)
    Kuleshov, E.V., Knights of the gateway. Notes on street teenagers of the city of Tikhvin (2002) Na Putiakh K Novoi Shkole: Na Storone Podrostka 2, ,  ('Kuleshov', 2002, 2, '', 37001)
    Ponomarev, Vasilii & Habeck, Joachim Otto (eds.) Syktyvkar: Institut Biologii Komi Nauchnogo Tsentra Ural'skogo Otdeleniia RAN ('Ponomarev', '', '', '', 38001)
    Yavuzer, H., (1992) Resimleriyle cocuk [Child with pictures], , (5th ed). Remzi ('Yavuzer', 1992, 5, '', 39001)
    Curhan, J.R., Elfenbein, H.A., Xu, H., What do people value when they negotiate? Mapping the domain of subjective value in negotiation (2006) Journal of Personality and Social Psychology, 91, pp. 493-512. ,  ('Curhan', 2006, 91, 493, 40001)
    Barry, D., Berman, H., The soviet legal profession (1968) Harvard Law Review, 82 (1), pp. 1-41 ('Barry', 1968, 82, 1, 41001)
    Doble, J., (1988) U.S.‐Soviet relations in the year 2010: Americans look to the future, , New York and Providence:, Public Agenda Foundation and Center for Foreign Policy Development ('Doble', 2010, '', '', 42001)
    Bechara, A., Damasio, H., Damasio, A., Emotion, decision making and the orbitofrontal cortex (2000) Cereb. Cortex, 10, pp. 295-307 ('Bechara', 2000, 10, 295, 43001)
    Karamysheva, T.V., Learning Foreign Languages Based on a Format of Questions and Answers Using the Computer, , Saint-Petersburg: Soyuz. ISBN 5-94033-030-4 ('Karamysheva', '', 5, '', 44001)
    Guba, K.S., Quality of Higher Education: A Review of International Practice (2019) Universitetskoye upravleniye: praktika i analiz = University Management: Practice and Analysis, 23 (3), pp. 94-107. ,  (In Russ., abstract in Eng) ('Guba', 2019, 23, 94, 45001)
    Spencer-Brown, G., (2010) Laws of form: The new edition of this classic with the first-ever proof of rieman’s hypothesis, , 2, Bohmeier Verlag, Leipzig ('Spencer-Brown', 2010, 2, '', 46001)
    Frisbie, W., Neidert, P., Neidert, L. J., Inequality and the Relative Size of Minority Populations: A Comparative Analysis (1977) American Journal of Sociology, 82 (5), pp. 1007-1030 ('Frisbie', 1977, 82, 1007, 47001)
    Shcheglova, I., Koreshnikova, Y., Parshina, O., The Role of Engagement in the Development of Critical Thinking in Undergraduates (2019) Voprosy obrazovaniya / Educational Studies Moscow, 2019 (1), pp. 264-289 ('Shcheglova', 2019, 1, 264, 48001)
    Ferguson, Christopher, Coulson, Mark, Barnett, Jane, Psychological Profiles of School Shooters: Positive Directions and One Big Wrong Turn (2011) Journal of Police Crisis Negotiations, 11, pp. 141-158. , [CrossRef] ('Ferguson', 2011, 11, 141, 49001)
    Fahrutdinova, R.A., Yarmakeev, I.E., Fakhrutdinov, R.R., The Formation of Students' Foreign Learning Technologies (The Study on the Basis of Kazan Federal University) (2014) English Language Teaching, 7 (12), pp. 36-46 ('Fahrutdinova', 2014, 7, 36, 50001)
    Pajares, F., Miller, M.D., Role of Self-Efficacy and Self-Concept Beliefs in Mathematical Problem Solving: A path analysis (1994) J. Educ. Psychol, 86, pp. 193-203. , [CrossRef] ('Pajares', 1994, 86, 193, 51001)
    Marcia, J.E., Development and validation of ego-identity status (1966) Journal of Personality and Social Psychology, 3, pp. 551-558 ('Marcia', 1966, 3, 551, 52001)
    (2021) Oxford Learners Dictionary, ,  (accessed 19 July 2021) ('', 2021, 19, '', 53001)
    Zhurnaľnaia rugatnia (1864) Sσvremennik, (8 PT. 2), p. 297 ('', 1864, 8, 2, 54001)
    England, P., Hermsen, J.M., Cotter, D.A., The devaluation of women's work: A comment on tam (2000) American Journal of Sociology, 105 (6), pp. 1741-1751 ('England', 2000, 105, 1741, 55001)
    Ginevičius, R., Ginevičiené, V.B., The Compliance of Master's Degree Studies with the Economic Needs of the Country (2009) Technological and Economic Development of Economy, 15 (1), pp. 136-153 ('Ginevičius', 2009, 15, 136, 56001)
    Bruni, L., Sugden, R., The Road not Taken: How Psychology was Removed from Economics, and How it Might be Brought Back (2007) The Economic Journal, 117 (516), pp. 146-173. ,  ('Bruni', 2007, 117, 146, 57001)
    Coleman, J.S., Social capital in the creation of human capital (1988) American Journal of Sociology, 94, pp. S95-S120 ('Coleman', 1988, 94, '', 58001)
    Discoveries of the pre-eskimo sites in Alaska and the adjacent areas, according to excavations of 1945-1954 (1957) Sovetskaia Etnografiia, 2 ('', 1957, 2, '', 59001)
    Subbarao, K., Mehra, K., "Social Assistance and the Poor in Romania" (1995), ESP Discussion Paper 66, World Bank, Education and Social Policy Department ('Subbarao', 1995, 66, '', 60001)
    Yu, D., Estestvennyy yazyk kak lingvokul’turnyy semioticheskiy kontsept: na materiale russkogo i angliyskogo yazykov (2004) Cand. philol. sci. diss. Krasnodar, p. 179. , Polinichenko [Natural language as a linguocultural semiotic concept: Based on the material of the Russian and English languages] ('Yu', 2004, '', 179, 61001)
    Braun, V., Clarke, V., Using thematic analysis in psychology (2006) Qualitative Research in Psychology, 3 (2), pp. 77-101 ('Braun', 2006, 3, 77, 62001)
    Omel'chenko, E., Molodezh dlya politikov vs. molodezh dlya sebya? Razmyshleniya o cennostyakh n fobiakh rossiiskoy molodezhi (2006) Molodezh i politika, , Moskovskoe byuro fonda Fridrikha Naumanna. Moscow: Biblioteka liberalnogo chteniia 17 ("Omel'chenko", 2006, 17, '', 63001)
    Schreck, C., Boykewich, S., Masked men attack NBP activists The Moscow Times, 31 August 2005, Available at 〈 com ('Schreck', 2005, 31, '', 64001)
    Brunk, G.G., Secrest, D., Tamishiro, H., (1996) Understanding Attitudes about War: Modeling Moral Judgments, , Pittsburgh, PA: University of Pittsburgh ('Brunk', 1996, '', '', 65001)
    Sypiańska, J., (2013) Quantity and quality of language use and attrition of L1 Polish due to L2 Danish and L3 English, , Adam Mickiewicz University, [Unpublished doctoral dissertation] ('Sypiańska', 2013, 1, '', 66001)
    Goleman, D., (1998) Working with Emotional Intelligence, , London: Bloomsbury ('Goleman', 1998, '', '', 67001)
    Stoetzler, M., Yuval-Davis, N., Standpoint theory, situated knowledge and the situated imagination (2002) Feminist Theory, 3 (3), pp. 315-335 ('Stoetzler', 2002, 3, 315, 68001)
    Podlinova, A. D., Spetsifika vneredaktsionnoy raboty v ezhednevnoy gazete i informatsionnom agentstve [Extra-Editorial Work in a Daily Newspaper and News Agency] (2019) Vestn. Mosk. un-ta. Ser. 10. Zhurnalistika, 3, pp. 105-119. , (In Russian) ('Podlinova', 2019, 10, 105, 69001)
    Davydova, N.N., Dorozhkin, Е.М., Fedorov, V.A., Innovative process development in the framework of scientific educational network: Management model (2016) Naukovyi Visnyk Natsіonalnoho Hіrnychoho Unіversitetu, 5, pp. 157-163. ,  Internet. cited 2015 Oct 18 ('Davydova', 2016, 5, 157, 70001)
    Delanty, G., (2013) Formations of European Modernity: A Historical and Political Sociology of Europe, , Basingstoke: Palgrave Macmillan ('Delanty', 2013, '', '', 71001)
    Dewey, J., (1978) "theory and Practice". Contribution to A Cyclopedia of Education. Vol. 7 of John Dewey: The Middle Works, 1899-1924, pp. 354-355. , Carbondale, Southern Illinois University Press ('Dewey', 1978, 7, 354, 72001)
    Corijn, M., Klijzing, E., (2001) Transitions to Adulthood in Europe. European Studies of Population, 10. , Dordrecht: Kluwer ('Corijn', 2001, 10, '', 73001)
    Hauk, O., Pulvermüller, F., Effects of word length and frequency on the human event-related potential (2004) Clinical Neurophysiology, 115 (5), pp. 1090-1103 ('Hauk', 2004, 115, 1090, 74001)
    Halbwachs, M., Coser, L.A., (1992) On Collective Memory, , Chicago, University of Chicago Press ('Halbwachs', 1992, '', '', 75001)
    Belkova, T.M., Modeling of competence based teaching phrasal intonation to bilingual students (2014) Vestnik Chuvashskogo Gosudarstvennogo Pedagogicheskogo Universiteta Im. I. Ya. Yakovleva, 3 (83), pp. 103-109. ,  Yakovlev Chuvash State Pedagogical University Bulletin., Available at, (accessed ). (In R uss ('Belkova', 2014, 3, 103, 76001)
    Buhrich, N., Beaumont, T., Comparison of transvestism in Australia and America (1981) Arch. Sex Behav., 10 (3), pp. 269-279 ('Buhrich', 1981, 10, 269, 77001)
    Anli, G., Examining the predictive role of authenticity on internet addiction in Turkish high school students (2018) Universal Journal of Educational Research, 6 (7), pp. 1497-1503. ,  ('Anli', 2018, '', 6, 78001)
    Houston, D.J., Walking the walk” of public service motivation: Public employees and charitable gifts of time, blood, and money (2006) Journal of Public Administration Research and Theory, 16, pp. 67-86 ('Houston', 2006, 16, 67, 79001)
    Marjoribanks, K., Family background, individual and environmental influences on adolescents' aspirations (2002) Educational Studies, 28 (1), pp. 33-46 ('Marjoribanks', 2002, 28, 33, 80001)
    (2016) National core curriculum for basic education 2014, p. 5. , Publica-tions 2016 ('', 2016, '', 5, 81001)
    Greenwood, M.J., Migration: a review (1993) Regional Studies, 27, pp. 295-383 ('Greenwood', 1993, 27, 295, 82001)
    Kanios, A., Beliefs of secondary school youth and higher education students about elderly persons: A comparative survey (2021) Child and Adolescent Social Work Journal, 38 (2), pp. 131-137. ,  ('Kanios', 2021, 38, 131, 83001)
    Hornik, H.J., (1990) Michele Di Ridolfo Del Ghirlandaio (1503–1577) and the Reception of Mannerism in Florence, , Pennsylvania State University ('Hornik', 1990, '', '', 84001)
    Strategiya Gosudarstvennoy Natsional'Noy Politiki Rossiyskoy Federatsii Na Period Do 2025 Goda [The Strategy of the State National Policy of the Russian Federation for the Period up to 2025], ,  President of Russia online.: accessed ). In Russ ('', 2025, '', '', 85001)
    Goldstein, S., Naglieri, J., Princiotta, D., Otero, T., Introduction: a history of executive functioning as a theoretical and clinical construct (2014) Handbook of executive functioning, pp. 3-12. , S. Goldstein J. Naglieri Springer New York ('Goldstein', 2014, '', 3, 86001)
    Sussman, S., Dent, C.W., Galaif, E.R., The correlates of substance abuse and dependence among adolescents at high risk for drug abuse (1997) Journal of Substance Abuse, 9 (1), pp. 241-255. , DOI 10.1016/S0899-3289(97)90019-5 ('Sussman', 1997, 9, 241, 87001)
    Putnam, R.D., (2000) Bowling Alone: The Collapse and Revival of American Community, , Simon and Schuster Paperbacks, New York ('Putnam', 2000, '', '', 88001)
    Pasquarella, A., Gottardo, A., Grant, A., Comparing factors related to reading comprehension in adolescents who speak English as first (L1) or second (L2) language (2012) Scientific Studies of Reading, 16, pp. 475-503 ('Pasquarella', 2012, 1, 475, 89001)
    Cenoz, J., Gorter, D., Minority Languages and Sustainable Translanguaging: Threat or Opportunity? (2017) Journal of Multilingual and Multicultural Development, 38 (10), pp. 901-912 ('Cenoz', 2017, 38, 901, 90001)
    Brooks, S.K., Webster, R.K., Smith, L.E., Woodland, L., Wessely, S., Greenberg, N., Rubin, G.J., The psychological impact of quarantine and how to reduce it: rapid review of the evidence (2020) The Lancet, 395 (10227), pp. 912-920 ('Brooks', 2020, 395, 912, 91001)
    Lee, S.J., More than " model minorities" or " delinquents": a look at Hmong American high school students (2001) Harvard Educational Review, 71 (3), pp. 505-528 ('Lee', 2001, 71, 505, 92001)
    Interview with Alina, student of German-Russian philology, , 39. (translated from German) ('', '', 39, '', 93001)
    Kefeli, A., The tale of joseph and zulaykha on the volga frontier: The struggle for gender, religion, and national identity in imperial and post-revolutionary Russia (2012) Slavic Review, 70 (2), pp. 373-398 ('Kefeli', 2012, 70, 373, 94001)
    Gurova, O. Yu, Look Russian (2013) Russian migrants in Finland: social characteristics and clothing consumption, Ekonomicheskaya sotsiologiya [Economic sociology], 14 (2), pp. 17-41. , 23. (In Russ) ('Gurova', 2013, 14, 17, 95001)
    (1934) Pitkänen letter to Davis, , note ('', 1934, '', '', 96001)
    Zhabotinskii, Sochineniia, 1, pp. 322-323. , note ('Zhabotinskii', '', 1, 322, 97001)
    Guimarães Garcia, L., Strategic intelligence teaching to leverage professional success (2020) Foresight and STI Governance, 14 (3), pp. 101-112 ('Guimarães Garcia', 2020, '', 14, 98001)
    Alexandrov, V., Harry Potter on the world stage: Who invented football, or Harry Potter at school and at home (2001) New World, 7. ,  ('Alexandrov', 2001, 7, '', 99001)
    McDonough, S., Motivation in ELT (2007) Elt Journal, 61 (4), pp. 369-371 ('McDonough', 2007, 61, 369, 100001)
    Tamil-Russian Dictionary. Ed. Purnama Somamundarama. Moscow: Foreign and National Dictionaries State Publishing House, 1960 ('', 1960, '', '', 101001)
    Kholmogorova, A.B., (2006) Teoreticheskiye i empiricheskiye osnovaniya integrativnoy psikhoterapii rasstroystv affektivnogo spectra [Theoretical and empirical foundations of integrative psychotherapy disorders of affective spectrum] (Doctoral dissertation), , Moscow ('Kholmogorova', 2006, '', '', 102001)
    Shomova, S., (2018) Memy kak oni est' [Meme as they are], , Moscow: Aspekt Press ('Shomova', 2018, '', '', 103001)
    (1925) A Medical Review of Soviet Russia, , Pearce to Flexner, 16 December ('', 1925, 16, '', 104001)
    Kernberg, O.F., (2001) Tyazhelye lichnostnye rasstroistva. Strategii psikhoterapii [Severe personality disorders: Psychotherapeutic strategies], p. 464. , Moscow: Publ. Klass ('Kernberg', 2001, '', 464, 105001)
    Babiker, I., Cox, J., Miller, P., The measurement of cultural distance and its relationship to medical consultation, sypmtomatology, and examination performance of overseas students of Edinburgh University (1980) Journal of Social Psychiatry, 15, pp. 109-116 ('Babiker', 1980, 15, 109, 106001)
    Aleksandrov, V. A., Vlasova, I. V., Kalendarnye prazdniki i obryady (1999), pp. 616-647. , Тульцева Л. А. Календарные праздники и обряды. În: Русские. Отв. ред. Александров В. А., Власова И. В., Полищук Н. С. М.: Наука, 1999, с. 616-647. Tul’ceva L. A Russkie. Otv. red. Polishchuk N. S. M.: Nauka, s ('Aleksandrov', 1999, '', 616, 107001)
    Hitlin, S., Brown, J.S., Elder Jr, G.H., Racial self-categorization in adolescence: Multiracial development and social pathways (2006) Child Development, 77 (5), pp. 1298-1308 ('Hitlin', 2006, 77, 1298, 108001)
    Buller, P., Kohls, J., A model for addressing cross-cultural ethical conflicts (1997) Business and Society, 36 (2), pp. 169-194 ('Buller', 1997, 36, 169, 109001)
    Zagorski, K., Andorka, R., Tuma, N.B., Meyer, J.B., 'Comparisons of social mobility in different socio-economic systems' (1984) International Comparative Research, pp. 13-41. , In Oxford: Pergamon Press ('Zagorski', 1984, '', 13, 110001)
    Álvarez Veinguer, A., Davis, H.H., Building a Tatar Elite: Language and National Schooling in Kazan (2007) Ethnicities, 7 (2), pp. 186-207 ('Veinguer', 2007, 7, 186, 111001)
    Kendi, I., (2016) Stamped from the beginning: The definitive history of racist ideas in America, , Nation Books ('Kendi', 2016, '', '', 112001)
    Asser, H., Keelekeskkonna ja õppekava mõju vene kooli õpilaste eesti keele oskusele 1994-1999 (2001) Kasvatus Ja Aated, 11, pp. 7-16 ('Asser', 2001, 11, 7, 113001)
    Vasileva, G.M., Vinogradova, M.V., Miachina, V.W., The dynamics of cultural-geographic perceptions in the linguistic consciousness of Russian students (As exemplified by country images) (2019) Perspect. Sci. Educ., 5 (41), pp. 262-270 ('Vasileva', 2019, '', 5, 114001)
    Shirokshin, N.V., Geognostic survey of the shores of Kandalaksha Bay and the White Sea to the city of Kem in the Arkhangelsk Region (1835) Gornyi Journal, 1 (3). , [In Russian] ('Shirokshin', 1835, 1, '', 115001)
    Coyle, T.R., Pillow, D.R., SAT and ACT predict college GPA after removing g (2008) Intelligence, 36 (6), pp. 719-729. ,  ('Coyle', 2008, '', 36, 116001)
    Isralowitz, R.E., Reznik, A., Former Soviet Union immigrant and native-born adolescents in Israel: Substance use and related problem behavior (2007) Journal of Ethnicity in Substance Abuse, 6, pp. 131-138 ('Isralowitz', 2007, 6, 131, 117001)
    Vasil'chuk, Y., (2006) Povtorno-zhilnye l'dy: Geterotsiklichnost', geterokhronost', geterogennost' (Syngenetic Ice Wedges: Cyclical Formation, Radiocarbon Age and Stable Isotope Records), p. 404. , Moscow University Press, (in Russian) ("Vasil'chuk", 2006, '', 404, 118001)
    Bakaya, R.M., Pande, H.C., Unni, C.P.S., (1974) Slovar'-minimum Dlya Podgotovitel'nogo Kursa Tsentra Russkikh Issledovaniy [A Lexical Minimum Dictionary for the Preparatory Course of the Center for Russian Studies], , New Delhi: Jawaharlal Nehru University ('Bakaya', 1974, '', '', 119001)
    Smirnova, A.A., (2009) Vtoroe Otdelenie Sobstvennoy Ee.I.V. Kantselyarii [Second Division of Her Imperial Majesty's Chancellery], , History Cand. Diss. St. Petersburg: St. Petersburg State University ('Smirnova', 2009, '', '', 120001)
    Sandstrom, G., Global Sociology - Russian Style (2008) Canadian Journal of Sociology/ Cahiers canadiens de sociologie, 33 (3), p. 607 ('Sandstrom', 2008, 33, 607, 121001)
    Si, S., Zhang, S., Yu, Q., Zhang, J., The interaction of DRD2 and parenting style in predicting creativity (2018) Thinking Skills and Creativity, 27, pp. 64-77. ,  ('Si', 2018, 2, 64, 122001)
    Crompton, H., Burke, D., Gregory, K.H., The use of mobile learning in PK-12 education: A systematic review (2017) Computers & Education, 110, pp. 51-63 ('Crompton', 2017, '', 12, 123001)
    Rossii, N.O.U., (1997) Moskva: Sprav. Izd., , Les établissements non publics d'enseignement secondaire général de Russie vyp. 1 ('', 1997, '', 1, 124001)
    Dunstan, J., (1978) Paths to Excellence and the Soviet School, , Slough, NFER ('Dunstan', 1978, '', '', 125001)
    (2002) Identity and Foreign Policy in the Middle East, , Telhami S., and Barnett M. (Eds), Cornell University Press, Ithaca, NY ('', 2002, '', '', 126001)
    Krashen, S., Free voluntary reading: Linguistic and affective arguments and some new applications (1995) Second Language Acquisition Theory and Pedagogy, pp. 187-202. , In F. Eckman, D. Highland, P. Lee, J. Mileham, & R. Weber (Eds.), Mahwah, NJ: Lawrence Erlbaum ('Krashen', 1995, '', 187, 127001)
    Ruble, D.N., Boggiano, A.K., Feldman, N.S., Loebl, J.H., Developmental analysis of the role of social comparison in self-evaluation (1980) Developmental Psychology, 16, pp. 105-115 ('Ruble', 1980, 16, 105, 128001)
    Ellsberg, M., Jansen, H.A.F.M., Heise, L., Watts, C.H., Garcia-Moreno, C., Intimate partner violence and women's physical and mental health in the WHO multi-country study on women's health and domestic violence: an observational study (2008) Lancet, 371, pp. 1165-1172. , WHO Multi-country Study on Women's Health and Domestic Violence against Women Study Team ('Ellsberg', 2008, 371, 1165, 129001)
    Nikolaev, V., (1974) Putnik, Shagaiushchii Riadom: Ocherk Tvorchestva R. Fraermana, p. 97. , Moscow ('Nikolaev', 1974, '', 97, 130001)
    Triandis, H.C., (1995) Individualism & Collectivism, , Boulder, CO: Westview Press ('Triandis', 1995, '', '', 131001)
    Morozova, G.V., (2013) Political orientations and interests of student youth of the Republic of Tatarstan (by research results), 1, pp. 62-68. , Newsletter of Volgograd state university. Series 4: History. Regional studies ('Morozova', 2013, 1, 62, 132001)
    Pridemore, W.A., Kim, S.W., Democratization and political change as threats to collective sentiments: Testing Durkheim in Russia (2006) The Annals of the American Academy of Political and Social Science, 605 (1), pp. 82-103 ('Pridemore', 2006, '', 605, 133001)
    Costa, A., Hernández, M., Sebastián-Gallés, N., Bilingualism aids conflict resolution: Evidence from the ANT task (2008) Cognition, 106 (1), pp. 59-86 ('Costa', 2008, 106, 59, 134001)
    Inglehart, R., Welzel, C., (2011) Modernizacija kulturnye izmenenija i demokratija posledovatelnost chelovecheskogo razvitija [Modernization, Cultural Change and Democracy: The Human Development Sequence], , Moscow: Novoe izdatelstvo ('Inglehart', 2011, '', '', 135001)
    Kozyreva, L.D., Zverkova, S.A., Transformation of the social ties of youth in information society (2017) Sociodynamics, (4), pp. 94-104. ,  Козырева Л. Д., Зверькова С. А. Трансформация социальных связей молодежи в информационном обществе // Социодинамика. 2017. № 4. С. 94—104.  Russ ('Kozyreva', 2017, 4, 94, 136001)
    Dunaevskaya, T.N., Morfologicheskiye osobennosti i rostoviye protsessy u detey (1974) Razmernaya Tipologiya Naseleniya Stran-chlenov SEV., pp. 247-255. , Moscow: Legkaya industriya ('Dunaevskaya', 1974, '', 247, 137001)
    (1984) Narva Wie Es War, , Einhundert Ansichten. Lüneburg: Nordland-Druck ('', 1984, '', '', 138001)
    Tjaden, J., Auer, D., Laczko, F., Linking Migration Intentions with Flows: Evidence and Potential Use (2019) International Migration, 57 (1), pp. 36-57. ,  ('Tjaden', 2019, 57, 36, 139001)
    Semyonov, A. N., Kontsept kak kategoriya v obsko-ugorskoy i russkoy literature [Concept as a category in Ob-Ugric and Russian literature (2019) Vestnik ugrovedeniya [Bulletin of Ugric Studies], 9 (2), pp. 271-278. , (In Russian) ('Semyonov', 2019, 9, 271, 140001)
    Molchanova, E. H., (2005) Television in the culture of the modern information society (dis. of PhD in Philosophy), , Stavropol: Stavropol state university ('Molchanova', 2005, '', '', 141001)
    Attar-Schwartz, S., Maltreatment by staff in residential care facilities: the adolescents’ perspectives (2011) Social Service Review, 85 (4), pp. 635-664 ('Attar-Schwartz', 2011, 85, 635, 142001)
    Zhigaryova, O. G., Fizicheskaya kul'tura i fizicheskoe vospitanie v vuze. Mezhdunarodnyj opyt (2017) EhSGI, 4 (16), pp. 97-101. , S ('Zhigaryova', 2017, 4, 97, 143001)
    Lin, C-Y., Fear of COVID-19 Scale (FCV-19S) across countries: Measurement invariance issues (2021) Nursing Open, 8, pp. 1892-1908 ('Lin', 2021, 19, 1892, 144001)
    


```python
len(author) == len(year) == len(page) == len(volume)
```




    True




```python
exit()
```
```python
Пример ошибки 
Pin, S.C., Haron, F., Sarmady, S., Talib, A.Z., Khader, A.T., Applying TRIZ principles in crowd management (2011) Safety Science, 49 (2), pp. 286-291 ('Pin', 2011, '', 49, 16801)
Clarke, M., China’s Strategy in ‘Greater Central Asia’: Is Afghanistan the Missing Link? (2013) Asian Affairs: An American Review, 40 (1), pp. 1-19 ('Clarke', 2013, 40, 1, 17201)Общая структура алгоритма 
```
```python
Общая структура алгоритма
for row in rows:
    
    match_author = re.search(regex_author, str(row[1]))
    match_year = re.search(regex_year, str(row[1]))
    match_volume = re.match(regex_volume, str(row[1]))
    match_page = re.search(regex_page, str(row[1]))
    
    if match_author:
        author = match_author.group(1)
    else:
        author = ''
    
    if match_year:
        year = int(match_year.group(1))
    else:
        year = ''
    
    if match_volume:
        volume = match_tome.group(1)
    else:
        volume = ''
    
    if match_page:
        page = match_page.group(1)
    else:
        page = ''
    
    cursor.execute("UPDATE ref SET author=?, year=?, volume=?, page=? WHERE reference=?", 
                   (author, year, volume, page, row[1]))
    conn.commit()
    
    
```
```python
Блок для отладкки

#author_re = re.compile(r"^([\w-]+),")
#author_re = re.compile(r"(.*?),\s*(\b[A-Z]\.?[A-Z]?\.?)")
extensionsToCheck = ['Studies', 'Ezhegodnik', 'Rossiiskii', 'Obrazovanie', 'Rossii', 'Population', 'data',
                    'Russian',  'Source', 'Catalogue', 'Journal', 'dictionary', ']', ':', '?']
author_re = re.compile(r"([A-Z][a-z\-]+)[^,]*")
volume_re = re.compile(r"\d+\s\(\d+\)")

for i in range(len([0]*10000)):
    st = str(rows[i][1])
    st = re.sub(r'http\S+', '', st)
    st = re.sub(r'\b\d{1,2}\.\d{1,2}\.\d{4}\b', '', st)
    ID = int(rows[i][0])
    
    match_author = re.search(author_re, st)
    if match_author:
        aut = match_author.group()
        aut = re.sub(r"\(\d{4}\)", "", aut)
        if len(aut) < 50 and aut.count(' ') < 2:
            if not(any(ext in aut for ext in extensionsToCheck)):
                author.append(aut)
                print(aut)
            else:
                author.append('')
        else:
            author.append('')
        
    else:
        author.append('')
        
    match_volume = re.search(volume_re, st)
    if match_volume:
        vol= match_author.group()
        volume.append(vol)
    else:
        volume.append('')

    print(st, aut, vol)
 ```
 Точки для улучшения:
 - улучшить регулярные выражения
 - использовать инструенты для больших данных, например pyspark в случае переполнения памяти
 - сразу указывать типа данных при чтении(id: int)
 - использовать распарралеливание процесса обновления БД на два потока
