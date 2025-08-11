For your personal use of this mathjob script, you need to edit the parameters in the beginning:

Currently they are:

ACCEPTABLE_COUNTRIES = ["DE", "NL", "NO", "SE", "DK", "CH", "BE", "LU", "FR", "PL", "EE", "LV", "LT", "CZ", "HU", "GB", "FI"]
KEYWORDS_YES_NECESSARY = ["categor","Categor","homotop","Homotop","topolog","Topolog","mathematical physics","quantum","decarbonisation","decarbonization","greenhouse","climate","electricity","power"]
KEYWORDS_NO = ["PhD position","PhD Position","phd position"]
KEYWORDS_YES_OVERWRITE = ["postdoc","Postdoc"]
FILE_PATH = "/home/florian/Dokumente/python_projects/mathjob_check_files/job-search.csv"
KILL_MODE = False

For ACCEPTABLE_COUNTRIES type in a list of two-character strings describing a country (like "CA" for Canada)
For KEYWORDS_YES_NECESSARY type in a list keywords you would like tho search for
For KEYWORDS_NO type in keywords that you don't want to be in the description
For KEYWORDS_YES_OVERWRITE type in keywords upon which you want the listing to be included, even if a word from KEYWORDS_NO is included
For FILE_PATH type in the file path where the results should be saved
For KILL_MODE select "True" if you want to overwrite all previous results

EXAMPLES:
For the parameters above, the job described as
"A job about category theory" gets included,
"A PhD position in category theory" gets non included,
"A PhD position or postdoc position in category theory" gets included, and
"A Postdoc in algebra" gets not included.
