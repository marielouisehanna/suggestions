from flask import Flask, render_template, redirect, url_for # type: ignore
import random

app = Flask(__name__)


movies = [
    {"title": "Pulp Fiction", "poster": "https://image.tmdb.org/t/p/original/vQWk5YBFWF4bZaofAbv0tShwBvQ.jpg"},
    {"title": "Forrest Gump", "poster": "https://www.petersbilliards.com/images/jcogs_img/cache/forrest-gump-movie-poster_-_28de80_-_05eceabacb1dc8673d4f4daff4ac77d09b282167.jpg"},
    {"title": "Goodfellas", "poster": "https://image.tmdb.org/t/p/original/A1dZNvdnOzkzwQJ7YPd6Bgo4fA2.jpg"},
    {"title": "Inception", "poster": "https://image.tmdb.org/t/p/original/edv5CZvWj09upOsy2Y6IwDhK8bt.jpg"},
    {"title": "Saving Private Ryan", "poster": "https://image.tmdb.org/t/p/original/b48swXW58rvrSM0ahsNW70TTZcJ.jpg"},
    {"title": "The Shawshank Redemption", "poster": "https://image.tmdb.org/t/p/w500/q6y0Go1tsGEsmtFryDOJo3dEmqu.jpg"},
    {"title": "The Godfather", "poster": "https://image.tmdb.org/t/p/w500/rPdtLWNsZmAtoZl9PK7S2wE3qiS.jpg"},
    {"title": "The Dark Knight", "poster": "https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911r6m7haRef0WH.jpg"},
    {"title": "The Lord of the Rings: The Return of the King", "poster": "https://image.tmdb.org/t/p/w500/rCzpDGLbOoPwLjy3OAm5NUPOTrC.jpg"},
    {"title": "Fight Club", "poster": "https://image.tmdb.org/t/p/w500/bptfVGEQuv6vDTIMVCHjJ9Dz8PX.jpg"},
    {"title": "The Matrix", "poster": "https://image.tmdb.org/t/p/w500/f89U3ADr1oiB1s9GkdPOEpXUk5H.jpg"},
    {"title": "Star Wars: Episode IV - A New Hope", "poster": "https://image.tmdb.org/t/p/w500/6FfCtAuVAW8XJjZ7eWeLibRLWTw.jpg"},
    {"title": "The Silence of the Lambs", "poster": "https://image.tmdb.org/t/p/w500/rplLJ2hPcOQmkFhTqUte0MkEaO2.jpg"},
    {"title": "Se7en", "poster": "https://image.tmdb.org/t/p/w500/6yoghtyTpznpBik8EngEmJskVUO.jpg"},
    {"title": "Interstellar", "poster": "https://image.tmdb.org/t/p/w500/gEU2QniE6E77NI6lCU6MxlNBvIx.jpg"},
    {"title": "Parasite", "poster": "https://image.tmdb.org/t/p/w500/7IiTTgloJzvGI1TAYymCfbfl3vT.jpg"},
    {"title": "The Green Mile", "poster": "https://image.tmdb.org/t/p/w500/velWPhVMQeQKcxggNEU8YmIo52R.jpg"},
    {"title": "Gladiator", "poster": "https://image.tmdb.org/t/p/w500/ty8TGRuvJLPUmAR1H1nRIsgwvim.jpg"},
    {"title": "Joker", "poster": "https://image.tmdb.org/t/p/w500/udDclJoHjfjb8Ekgsd4FDteOkCU.jpg"},
    {"title": "Schindler's List", "poster": "https://image.tmdb.org/t/p/w500/c8Ass7acuOe4za6DhSattE359gr.jpg"}

]
songs = [
    {"title": "Bohemian Rhapsody", "artist": "Queen",
     "description": "A rock opera that combines various musical styles into one song.",
     "reason": "It’s one of the most iconic and unique rock songs ever recorded.",
     "additional_info": "Known for its elaborate production and vocal harmonies."},

    {"title": "Stairway to Heaven", "artist": "Led Zeppelin",
     "description": "A classic rock ballad that gradually builds into a powerful guitar solo.",
     "reason": "It’s considered one of the greatest rock songs of all time.",
     "additional_info": "The song’s progressive structure and mystical lyrics have captivated listeners for decades."},

    {"title": "Hotel California", "artist": "Eagles",
     "description": "A song featuring a haunting melody and cryptic lyrics about a luxury hotel.",
     "reason": "It’s renowned for its memorable guitar solos and reflective lyrics.",
     "additional_info": "The song’s narrative explores themes of excess and disillusionment."},

    {"title": "Imagine", "artist": "John Lennon",
     "description": "A song with a simple, yet profound message about peace and unity.",
     "reason": "It’s a timeless anthem for peace and has universal appeal.",
     "additional_info": "John Lennon's vision for a world without borders or divisions is poignantly expressed in this song."},

    {"title": "Smells Like Teen Spirit", "artist": "Nirvana",
     "description": "A grunge anthem that helped define the 1990s music scene.",
     "reason": "It’s known for its raw energy and marked the rise of alternative rock.",
     "additional_info": "The song’s rebellious spirit and catchy riffs made it a cultural touchstone."},

    {"title": "Like a Rolling Stone", "artist": "Bob Dylan",
     "description": "A groundbreaking song that redefined the boundaries of popular music.",
     "reason": "It’s praised for its poetic lyrics and Dylan’s impactful delivery.",
     "additional_info": "The song’s long, narrative style was innovative for its time and remains influential."},

    {"title": "Purple Haze", "artist": "Jimi Hendrix",
     "description": "A psychedelic rock song featuring Hendrix’s signature guitar work.",
     "reason": "It’s celebrated for its experimental sound and Hendrix’s virtuosity.",
     "additional_info": "The song is a staple of Hendrix’s legacy and a highlight of his innovative approach to guitar."},

    {"title": "What's Going On", "artist": "Marvin Gaye",
     "description": "A soulful and socially conscious track addressing social issues of the time.",
     "reason": "It’s renowned for its smooth melody and powerful message about social justice.",
     "additional_info": "The song’s combination of soulful music and poignant lyrics made it a classic of the genre."},

    {"title": "Billie Jean", "artist": "Michael Jackson",
     "description": "A dance-pop song with a memorable beat and Jackson’s iconic vocal performance.",
     "reason": "It’s known for its innovative production and Jackson’s impressive dance moves.",
     "additional_info": "The song’s music video was groundbreaking and significantly influenced pop culture."},

    {"title": "Shape of You", "artist": "Ed Sheeran",
     "description": "A catchy pop song with a danceable beat and Sheeran’s signature style.",
     "reason": "It’s one of the most popular songs of the past decade and showcases Sheeran’s talent for crafting hooks.",
     "additional_info": "The song’s infectious rhythm and relatable lyrics contributed to its widespread success."}
]



books = [
    {
        "title": "To Kill a Mockingbird",
        "description": "A novel exploring themes of racial injustice and moral growth through the eyes of a young girl.",
        "reason": "It’s a classic of modern American literature with a powerful social message.",
        "additional_info": "The book’s depiction of courage and empathy remains relevant and impactful.",
        "poster": "https://cdn.britannica.com/21/182021-050-666DB6B1/book-cover-To-Kill-a-Mockingbird-many-1961.jpg"
    },
    {
        "title": "Turtles All the Way Down",
        "description": "A story about a teenage girl dealing with mental illness while solving a mystery.",
        "reason": "It’s a deeply personal and empathetic portrayal of mental health issues.",
        "additional_info": "John Green’s writing is both poignant and relatable.",
        "poster": "https://images.penguinrandomhouse.com/cover/9780525555360"
    },
    {
        "title": "An Absolutely Remarkable Thing",
        "description": "A novel about the sudden fame of a young woman who discovers a mysterious statue.",
        "reason": "Explores themes of internet fame, identity, and human connection.",
        "additional_info": "Hank Green’s debut novel is thought-provoking and entertaining.",
        "poster": "https://images.penguinrandomhouse.com/cover/9781524743444"
    },
    {
        "title": "If We Were Villains",
        "description": "A suspenseful story about a group of Shakespearean actors involved in a murder mystery.",
        "reason": "Combines elements of classic literature with a thrilling plot.",
        "additional_info": "M.L. Rio’s debut novel is a compelling read for fans of dark academia.",
        "poster": "https://images.macmillan.com/folio-assets/macmillan_us_frontbookcovers_1000H/9781250095282.jpg"
    },
    {
        "title": "The Seven Husbands of Evelyn Hugo",
        "description": "A fictional biography of a reclusive Hollywood actress and her seven marriages.",
        "reason": "A captivating story of love, ambition, and the price of fame.",
        "additional_info": "Taylor Jenkins Reid creates a fascinating and complex character in Evelyn Hugo.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1664458703i/32620332.jpg"
    },
    {
        "title": "The Invisible Life of Addie LaRue",
        "description": "A woman makes a deal with the devil to live forever, only to be forgotten by everyone she meets.",
        "reason": "A beautifully written exploration of memory, identity, and the desire to leave a mark on the world.",
        "additional_info": "V.E. Schwab’s lyrical prose and imaginative storytelling shine in this novel.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1584633432i/50623864.jpg"
    },
    {
        "title": "Daisy Jones and the Six",
        "description": "A fictional oral history of a 1970s rock band’s rise and fall.",
        "reason": "The unique narrative style and realistic portrayal of the music industry make it a standout read.",
        "additional_info": "Taylor Jenkins Reid captures the era’s spirit and the complexities of relationships within a band.",
        "poster": "https://images.penguinrandomhouse.com/cover/9781524798628"
    },
    {
        "title": "The Inheritance Games",
        "description": "A teenage girl inherits a billionaire’s fortune but must solve a series of puzzles to claim it.",
        "reason": "A gripping and twisty mystery that keeps readers guessing.",
        "additional_info": "Jennifer Lynn Barnes crafts an engaging and suspenseful story with intriguing characters.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1587396413i/52439531.jpg"
    },
    {
        "title": "Daughter of No Worlds",
        "description": "A young woman with magical abilities embarks on a quest for freedom and justice.",
        "reason": "A richly detailed fantasy world with strong character development.",
        "additional_info": "Carissa Broadbent’s storytelling is immersive and captivating.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1577198904i/49826643.jpg"
    },


    {
        "title": "A Darker Shade of Magic",
        "description": "A fantasy novel about a magician who can travel between parallel Londons.",
        "reason": "An inventive and thrilling adventure with well-developed characters.",
        "additional_info": "V.E. Schwab’s world-building and storytelling are exceptional.",
        "poster": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1400322851l/22055262.jpg"
    },
    {
        "title": "What If? by Randall Munroe",
        "description": "A book that answers hypothetical scientific questions with humor and wit.",
        "reason": "Combines science and humor in an accessible and entertaining way.",
        "additional_info": "Randall Munroe’s background as a former NASA roboticist adds credibility to the fun scenarios.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1451351509i/21413662.jpg"
    },
    {
        "title": "The Kind Worth Killing",
        "description": "A psychological thriller about a man and a woman who plot to kill his unfaithful wife.",
        "reason": "A gripping and twisted story with unexpected plot twists.",
        "additional_info": "Peter Swanson delivers a dark and suspenseful narrative.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1417981750i/21936809.jpg"
    },
    {
        "title": "Six of Crows",
        "description": "A fantasy novel about a group of criminals attempting an impossible heist.",
        "reason": "A fast-paced and thrilling story with a diverse and intriguing cast of characters.",
        "additional_info": "Leigh Bardugo’s writing is engaging and the plot is full of surprises.",
        "poster": "https://i.gr-assets.com/images/S/compressed.photo.goodreads.com/books/1459349344l/23437156._SY475_.jpg"
    },
    {
        "title": "When Breath Becomes Air",
        "description": "A memoir by a neurosurgeon facing terminal cancer.",
        "reason": "A profound and moving exploration of life, death, and what makes life worth living.",
        "additional_info": "Paul Kalanithi’s reflections are both insightful and heartbreaking.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1492677644i/25899336.jpg"
    },
    {
        "title": "Circe",
        "description": "A reimagining of the story of Circe, the enchantress from Greek mythology.",
        "reason": "A beautifully written and empowering story with a strong female protagonist.",
        "additional_info": "Madeline Miller’s prose is lyrical and captivating.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1565909496i/35959740.jpg"
    },
    {
        "title": "A Good Girl’s Guide to Murder",
        "description": "A young girl investigates a local murder for her school project.",
        "reason": "A compelling and well-crafted mystery with a strong and resourceful protagonist.",
        "additional_info": "Holly Jackson creates an engaging and suspenseful story.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1545494980i/40916679.jpg"
    },
    {
        "title": "The Silent Patient",
        "description": "A psychological thriller about a woman who stops speaking after being accused of murdering her husband.",
        "reason": "A gripping and intense story with a shocking twist.",
        "additional_info": "Alex Michaelides crafts a suspenseful and thought-provoking narrative.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1668782119i/40097951.jpg"
    },
    {
        "title": "Malibu Rising",
        "description": "A family saga set in 1980s Malibu, centered around a famous annual party.",
        "reason": "A captivating story of family dynamics, secrets, and personal growth.",
        "additional_info": "Taylor Jenkins Reid’s characters are richly developed and the setting is vividly described.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1618293107i/55404546.jpg"
    },
    {
        "title": "A Flicker in the Dark",
        "description": "A suspenseful novel about a woman whose past comes back to haunt her when girls start disappearing.",
        "reason": "A chilling and gripping thriller with well-crafted suspense.",
        "additional_info": "Stacy Willingham creates a tense and atmospheric narrative.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1621347398i/57693172.jpg"},
    {
        "title": "Divine Rivals",
        "description": "A fantasy novel about rival gods and their influence on the mortal world.",
        "reason": "An epic and imaginative story with complex characters and a rich mythology.",
        "additional_info": "Rebecca Ross delivers a captivating and immersive fantasy tale.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1655928079i/60784546.jpg"},
    {
        "title": "Carrie Soto Is Back",
        "description": "A retired tennis champion makes a comeback to reclaim her record.",
        "reason": "An inspiring story of determination, resilience, and the pursuit of greatness.",
        "additional_info": "Taylor Jenkins Reid’s portrayal of the sports world is realistic and engaging.",
        "poster": "https://cdn.penguin.co.uk/dam-assets/books/9781804940877/9781804940877-jacket-large.jpg"},
    {
        "title": "Five Survive",
        "description": "A thrilling novel about six friends who survive a deadly encounter during a road trip.",
        "reason": "A fast-paced and suspenseful story with well-developed characters.",
        "additional_info": "Holly Jackson delivers a gripping and intense narrative.",
        "poster": "https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1664370443i/61313902.jpg"}
]


games = [
    {"title": "The Legend of Zelda: Breath of the Wild",
     "description": "An open-world action-adventure game set in a vast, beautifully crafted fantasy world.",
     "reason": "It’s acclaimed for its expansive environment and innovative gameplay mechanics.",
     "additional_info": "The game allows for a high degree of exploration and freedom, making each player’s experience unique."},

    {"title": "Red Dead Redemption 2",
     "description": "A western-themed action-adventure game with a rich story and detailed open world.",
     "reason": "It’s praised for its immersive narrative and realistic depiction of the late 19th-century American frontier.",
     "additional_info": "The game’s attention to detail and character development create a deeply engaging experience."},

    {"title": "The Witcher 3: Wild Hunt",
     "description": "An open-world RPG featuring a rich story, complex characters, and a detailed fantasy world.",
     "reason": "It’s celebrated for its narrative depth and expansive world-building.",
     "additional_info": "The game’s dynamic quest system and moral choices offer a highly immersive experience."},

    {"title": "God of War",
     "description": "An action-adventure game following Kratos as he navigates the world of Norse mythology.",
     "reason": "It’s known for its engaging combat system and emotional storytelling.",
     "additional_info": "The game’s blend of mythological elements and personal story creates a compelling experience."},

    {"title": "Cyberpunk 2077",
     "description": "A futuristic RPG set in a sprawling metropolis with a focus on cybernetic enhancements and social issues.",
     "reason": "It’s notable for its expansive open world and detailed character customization.",
     "additional_info": "The game’s narrative and setting offer a unique look at a dystopian future shaped by technology."},

    {"title": "Horizon Zero Dawn",
     "description": "An action RPG set in a post-apocalyptic world overrun by robotic creatures.",
     "reason": "It’s praised for its innovative setting and engaging combat mechanics.",
     "additional_info": "The game’s mix of ancient and futuristic elements creates a distinctive"
    }
]

shows = [
    {"title": "Breaking Bad", "poster": "https://image.tmdb.org/t/p/w500/ggFHVNu6YYI5L9pCfOacjizRGt.jpg"},
    {"title": "Game of Thrones", "poster": "https://image.tmdb.org/t/p/w500/u3bZgnGQ9T01sWNhyveQz0wH0Hl.jpg"},
    {"title": "Stranger Things", "poster": "https://image.tmdb.org/t/p/w500/x2LSRK2Cm7MZhjluni1msVJ3wDF.jpg"},
    {"title": "The Mandalorian", "poster": "https://image.tmdb.org/t/p/w500/sWgBv7LV2PRoQgkxwlibdGXKz1S.jpg"},
    {"title": "Friends", "poster": "https://image.tmdb.org/t/p/w500/f496cm9enuEsZkSPzCwnTESEK5s.jpg"},
    {"title": "The Witcher", "poster": "https://image.tmdb.org/t/p/w500/7vjaCdMw15FEbXyLQTVa04URsPm.jpg"},
    {"title": "The Simpsons", "poster": "https://image.tmdb.org/t/p/w500/zLudbPueg8CxGhMS2tyDh3p0TdK.jpg"},
    {"title": "The Boys", "poster": "https://image.tmdb.org/t/p/w500/mY7SeH4HFFxW1hiI6cWuwCRKptN.jpg"},
    {"title": "Black Mirror", "poster": "https://resizing.flixster.com/gDplIxm0Jqr6xzHAc462ro_JAQc=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p16944746_b_v13_ab.jpg"},
    {"title": "The Walking Dead", "poster": "https://image.tmdb.org/t/p/w500/reKs8y4mPwPkZG99ZpbKRhBPKsX.jpg"},
    {"title": "Lucifer", "poster": "https://image.tmdb.org/t/p/w500/4EYPN5mVIhKLfxGruy7Dy41dTVn.jpg"},
    {"title": "The Office", "poster": "https://resizing.flixster.com/vyosUj-kmnp_3X2OlsfHZ02d3wE=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p7893514_b_v13_ab.jpg"},
    {"title": "Sherlock", "poster": "https://resizing.flixster.com/q6FI2dCX4pcsGwHSJYl7WO_vwfM=/206x305/v2/https://resizing.flixster.com/-XZAfHZM39UwaGJIFWKAE8fS0ak=/v3/t/assets/p10406404_b_v13_ab.jpg"},
    {"title": "Narcos", "poster": "https://i.pinimg.com/736x/40/51/16/4051163666883f1183b3c223d8fbd121.jpg"},
    {"title": "The Crown", "poster": "https://entertainment-now.com/wp-content/uploads/2022/12/AAAAQZhA2K7UA9a52i3lR9dZCkIRI1OAX5b5zC8WmC2eSQzvjm6FeYzeVV7qGzxmu1tEzpfufGIWNPYnds6nFJumBNa9D9GdJuzJuelDvyTVrYAMAQkrWQ70OgsXdoEChyAg5ITCQ4txdq9hdGkEOP3m2zUO.jpg"},
    {"title": "The Expanse", "poster": "https://sfrareview.org/wp-content/uploads/2021/04/the-expanse.jpg"},
    {"title": "Better Call Saul", "poster": "https://miro.medium.com/v2/format:webp/1*WzvwHEKaiZBSL1awkwVONA.jpeg"},
    {"title": "Westworld", "poster": "https://resizing.flixster.com/3mS8V8KRVnX6onW6tJgoJHeYlCY=/206x305/v2/https://resizing.flixster.com/6dM9tDWswKxeyZ7FsTrckjSEYN4=/ems.cHJkLWVtcy1hc3NldHMvdHZzZWFzb24vUlRUVjI4MjU4MS53ZWJw"},
    {"title": "True Detective", "poster": "https://mir-s3-cdn-cf.behance.net/project_modules/disp/586c4169757841.5b8d01f728236.jpg"},
    {"title": "House of Cards", "poster": "https://img.fruugo.com/product/6/85/68548856_0340_0340.jpg"}

]



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/suggest_song')
def suggest_song():
    suggestion = random.choice(songs)
    return render_template('songs.html', suggestion=suggestion)

@app.route('/suggest_show')
def suggest_show():
    suggestion = random.choice(shows)
    return render_template('shows.html', suggestion=suggestion)

@app.route('/suggest_movie')
def suggest_movie():
    suggestion = random.choice(movies)
    return render_template('movies.html', suggestion=suggestion)

@app.route('/suggest_book')
def suggest_book():
    suggestion = random.choice(books)
    return render_template('books.html', suggestion=suggestion)

@app.route('/suggest_game')
def suggest_game():
    suggestion = random.choice(games)
    return render_template('games.html', suggestion=suggestion)

if __name__ == '__main__':
    app.run(debug=True)



"""
adding from the web new ones + who added it?
optimizing python lists?

"""