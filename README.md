# Hybrid-Movie-Recommender-System

![Python](https://img.shields.io/badge/Python-3.8-blueviolet)
![Framework](https://img.shields.io/badge/Framework-Flask-red)
![Frontend](https://img.shields.io/badge/Frontend-HTML/CSS/JS-green)
![API](https://img.shields.io/badge/API-TMDB-fcba03)

#### Content Based Filtering
Content Based engine computes similarity between movies based on certain metrics and suggests movies that are most similar to a particular movie that a user liked. Since we will be using movie metadata (or content) to build this engine, this also known as Content Based Filtering.
#### Collabrative Filtering
Collaborative Filtering is based on the idea that users similar to me can be used to predict how much I will like a particular product or service those users have used/experienced but I have not.
## Hybrid System
I tried to build a simple hybrid recommender that brings together techniques used in the content based and collaborative filter based engines.It first gets the top 25 movies based on the content similarity and ratings  and then gives the final recommendation of top 10 movies based on the collaborative filtering model. This is how it will work:
###### Input: User ID and the Title of a Movie
###### Output: Similar movies sorted on the basis of expected ratings by that particular user.

## Sample Testing

#### Enter Input Fields- Movie Title And UserId
<img width="1154" alt="1" src="https://user-images.githubusercontent.com/77124129/170842412-5b525f35-e1a1-4f7b-a463-536f56f63e20.png">

#### Let Movie-Iron Man with UserId-100 and Click Enter
<img width="969" alt="2" src="https://user-images.githubusercontent.com/77124129/170842425-a9fe14e5-8302-42bd-96a6-55f5d90aa8e7.png">

#### Movie Poster along with details are shown
<img width="1397" alt="3" src="https://user-images.githubusercontent.com/77124129/170842427-ac7d04b5-e2cc-4944-b7be-eba60e6ffe64.png">

#### Top 10 Movie recommendations are shown based on our hybrid Model in the decreasing order(L to R & T to B) based on UserId-100
<img width="1440" alt="4" src="https://user-images.githubusercontent.com/77124129/170842435-63d27725-16a5-4384-bbf8-ee18002cd768.png">

#### Let test for same Movie but with UserId-300
<img width="1440" alt="5" src="https://user-images.githubusercontent.com/77124129/170842445-86740589-7b7e-42c2-8e4b-f28c0770207f.png">

#### Additionally Our site Shows the top 5 cast of the movie
<img width="1440" alt="6" src="https://user-images.githubusercontent.com/77124129/170842448-3706b970-445d-44ac-9459-6ad86755eba0.png">

#### Get deails of Individual Cast by hovering(click know more) onto their poster 
<img width="1440" alt="7" src="https://user-images.githubusercontent.com/77124129/170842449-ecc42de2-dc43-4f35-9750-61c08b10f737.png">

## Built With

* Python
* JavaScript
* HTML,CSS
* Flask
* Numpy,Pandas,Scikit-learn
* Scikit-Surprise, NLTK
* Bootstrap
* JQuery
* TMDB API

## How to run the project?

1. Clone or download this repository to your local machine.
2. Install all the libraries mentioned in the [requirements.txt](https://github.com/yashgoel72/Hybrid-Recommender-System/blob/main/requirements.txt) file with the command `pip install -r requirements.txt`
3. Open your terminal/command prompt from your project directory and run the file `main.py` by executing the command `python main.py`.
4. Go to your browser and type `http://127.0.0.1:5000/` in the address bar.
5. Hurray! That's it.

<p align="right">(<a href="#top">back to top</a>)</p>
