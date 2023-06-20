from flask import Flask, redirect, url_for, render_template, request, session, flash
import requests
import os


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY')

def get_shows(genres: list, type_s: str, min_score: float):
    print('divider')
    print(min_score)
    print(type(min_score))
    print('divider')
    genres = ','.join(genres)
    url = (f'https://api.jikan.moe/v4/anime?type={type_s}&min_score={min_score}&genres={genres}')
    r = requests.get(url)
    animes = r.json()
    list_final = []
    i = 0
    k = 1
    for anime in animes['data']:
        dict_of_suggestions = {}
        list_final.append(dict_of_suggestions)
        list_final[i]['mal_id'] = anime['mal_id']
        list_final[i]['title'] = anime['title']
        list_final[i]['episodes'] = anime['episodes']
        list_genres = []
        for k in anime['genres']:
            list_genres.append(k['name'])
        list_genres = ', '.join(list_genres)
        list_final[i]['list_genres'] = list_genres
        list_final[i]['score'] = str(anime['score']) + '/10 from ' + str(anime['scored_by']) + ' users'
        list_final[i]['synopsis'] = anime['synopsis']
        list_final[i]['image_url'] = anime['images']['jpg']['image_url']
        list_final[i]['trailer'] = anime['trailer']['embed_url']
        list_final[i]['index'] = i+1
        i+=1
    return list_final
    #a list of dicts, each dict containing the keys 'mal_id', 'title', 'episodes', 'list_genres', 'score',
    #'synopsis', 'image_url', 'trailer'



def get_genre_names(genre_id_list):
    genre_id_list = [eval(i) for i in genre_id_list]
    response = requests.get('https://api.jikan.moe/v4/genres/anime')
    list_of_dict = response.json()['data']
    genre_names = []
    for id in genre_id_list:
        for dict in list_of_dict:
            if dict['mal_id'] == id:
                genre_names.append(dict['name'])
    genre_names = ', '.join(genre_names)
    return genre_names




@app.route('/')
def home():
    return redirect(url_for('generator')) #should be index.html

@app.route('/generator', methods=['POST', 'GET'])
def generator():
    if request.method == 'POST':
        type_anime = request.form['type']
        genres_a = request.form.getlist('list_of_genres')
        score_a = request.form['score']
        session['type_anime'] = type_anime
        session['genres'] = genres_a
        session['score'] = score_a
        return redirect(url_for('user'))
    else:
        return render_template('generator_page.html')


@app.route('/recommendation', methods=['GET', 'POST']) 
def user():
    if 'type_anime' in session:
        genres = session['genres']
        a_type = session['type_anime']
        score = session['score']
        if score:
            print(score)
        else:
            score=0
        shows_info = get_shows(genres, a_type, score)
        shows = []
        for i in shows_info:
            shows.append(i['title'])
        num_shows = len(shows)
        genre_names = get_genre_names(genres)
        empty_str = "*No recommendations found, please reduce the number of genres or lower the score rating."
        multiple_g = True
        if len(genres) == 1:
            multiple_g = False
        recommendations = len(shows)
        if recommendations == 0:
            flash('*No animes fit your criteria. Please try reducing the number of genres or lowering the score rating.', 'info')
        if recommendations > 0:
            return render_template('recommendation_page.html', genre=genre_names, type=a_type, min_score=score, t_or_f=multiple_g, num_shows=num_shows, shows_info=shows_info)
        else:
            return redirect(url_for('generator'))
    else:
        return redirect(url_for('generator'))

@app.route('/redo')
def redo():
    if 'type_anime' in session:
        a_type = session['type_anime']
    session.pop('type_anime', None)
    return redirect(url_for('generator'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)