# Pràctica Kaggle APC UAB 2021-22
### Nom: Àlex Correa Orri
### DATASET: Website classification using URL
### URL: [kaggle](https://www.kaggle.com/shaurov/website-classification-using-url)
## Dataset i motivació
Dataset que conté 1.6M d'enllaços, cadascún d'ells té assignada a una categoria ('class'). Tenim un total de 15 classes diferents, l'únic atribut (a part del propi enllaç) del dataset.
Tan l'URL com la categoria són dades en format string.
La classificació de url pot ser molt útil en els següents camps:
- Control parental
- Control d'accès desde un servidor
- Bloqueig de direccions desde un router
- Bloqueig d'amenaces / Antivirus
- Control i detecció d'anuncis o spam
- Classificació automàtica de notícies

### Objectius del dataset
L'objectiu del treball és predir a quina categoria pertany un enllaç o un conjunt d'enllaços donat amb la màxima precisió possible.
## Experiments
Durant el treball s'han realitzat diferents proves fins a trobar el model que millor funcionava. 
S'han realitzat concatenacions dels url, particions dels mateixos en ngrames o paraules, construit i definit pipelines amb models diversos, cercat els millors hiperparàmetres, etc.
### Preprocessat
S'han eliminat els possibles valor NAN del dataset.
Si volem reduir la mida del dataset per realitzar proves més ràpides i veure com funcionen alguns models, ho podem fer descomentant 2 comandes indicades.
Utilitzem la funció CountVectorizer per consultar quines són les paraules o ngrames més comuns als enllaços. He provat de fer servir els ngrames de l'estil http, com, org, uk, etc. (llista definida a mà) com a stop_words pel CountVectorizer, però veurem que obtenim pitjors resultats. e
Per a fer la separació del dataset ho fem desde l'inici de la classe fins a un valor definit segons el percentatge de train-test que volem (al dataset les dades van ordenades per classe). Això es fa per evitar problemes d'indexació al dataframe, i veurem que ens dona un millor resultat.
Això és degut a que tenim molta diferència en la mida de dades de cada categoria. Si agafem moltes dades del dataset per fer el test això provocarà que per algunes classes haurem entrenat molt poc o fins i tot gens si no controlem el factor aleatori.
Un cop feta la divisió, extreiem la X i la y de cada dataset (dataset de train i dataset de test).
### Model
Donada la quantitat de dades del dataset el que fa millorar molt la precisió és augmentar les dades d'entrenament. Això m'ha obligat a no poder utilitzar la majoria dels models per fer-ne les proves.
He testejat el Random Forest, el Decision Tree, el SVM, el SGDC, i d'altres que, com els mencionats, amb més del 10% del dataset per entrenament, eren gairebé impossibles d'executar.
És per això que m'he quedat amb un dels més ràpids i he dedicat més temps a trobar els millors hiperparàmetres donat que em donava millors resultats amb diferència.
He construit un Pipeline que consta de 3 components:
- CountVectorizer: crea una matriu (sparse matrix) on les columnes són les paraules (o ngrames) trobades per cada enllaç (cada fila).
- TfidfTransformer: Transforma una 'count matrix' a una representació normalitzada tf o tf-idf. Tf:'term-frequency'; Tf-idf: 'term-frequency times inverse document-frequency'
- MultinomialNB: 'Multinomial Naive Bayes'. Segons sklearn, 'The multinomial Naive Bayes classifier is suitable for classification with discrete features (e.g., word counts for text classification)' https://scikit-learn.org/stable/modules/naive_bayes.html#multinomial-naive-bayes
Les dades que consten a continuació estan realitzades amb un 95% del dataset a l'entrenament. Això ens dona 5210 url per classe destinat a l'entrenament. Si augmentem aquest 95% obtindrem millors resultats encara.

|     Model     |       Hiperparametres      | Precisió | Temps d'entrenament |
| MultinomialNB | fit_prior=False, alpha=0.0 |   95%    |         42s         |

## Demo
Per tal de fer una prova, es pot fer servir amb la següent comanda
``` python3 fast_test.py ``` 
Cal que el fitxer test_data es trobi a la mateixa carpeta que l'arxiu .py
Per canviar el fitxer de test es pot editar el nom del mateix al .py. 
L'arxiu test_data.csv es genera al executar el notebook classificacio_URL.ipynb, on també es genera el classificador definitiu, que es guarda a l'arxiu multinomialNB_trained.sav
Per executar-ho cal entrenar el model 1 vegada amb el notebook i generar l'arxiu multinomialNB_trained.sav. Aquest fitxer és massa pesat per pujar-lo al repositori de GitHub.
## Conclusions
El millor model que s'ha aconseguit ha estat el MultinomialNB utilitzant el Pipeline i hiperparàmetres mencionats.
Un dels majors problemes de treballar amb aquest dataset és la gran quantitat de dades que té i obliga a crear SparseMatrix per no excedir els límits de memòria.
Això també ens aporta molta informació i podem acabar obtenint una gran precisió.
## Idees per treballar en un futur
Podria ser interessant provar d'entrenar el model amb encara més dades reals. A nivell computacional hi ha marge per poder-ho fer amb un dataset inclús 10 vegades major. 
Amb això és possible que s'obtingui una precisió encara més alta i apropar-se bastant a la classificació perfecte, que no seria necessari supervisar. 

També seria interessant importar més diccionaris i fer les separacions per paraules existents a tots els diccionaris i no només per ngrames.
