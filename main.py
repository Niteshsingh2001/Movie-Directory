from flask import Flask, render_template , url_for,request,redirect,send_file
import jyserver.Flask as js
import requests as req
import json

app = Flask(__name__)



@js.use(app)
class App:
    def __init__(self) -> None:
        pass
    def search(self):
        self.movie_name = self.js.document.getElementById("name").value;
        url =f"http://www.omdbapi.com/?apikey=afb102e2&t={self.movie_name}"

        link = req.get(url)
        data = json.loads(link.content)
        
        i = f'''
        <div id="box">

            <div id="poster">
                <img id="image" src ="{data["Poster"]} alt="Image Not Found"">
            </div>

            <div id="text_data">
                
                <div id="title">
                    <b>{data["Title"]}</b><br>
                    {data["Released"]}
                </div>

                <div id="innertext_data">

                    <div id="txt">
                        <b>Genre:</b>
                        {data["Genre"]}
                    </div>
                    <div id="txt">
                        <b>BoxOffice:</b>
                        {data["BoxOffice"]}
                    </div>
                    <div id="txt">
                        <b>Language:</b>
                        {data["Language"]}
                    </div>
                    <div id="txt">
                        <b>Director:</b>
                       {data["Director"]}
                    </div>
                    <div id="txt">
                        <b>Actors:</b>
                        {data["Actors"]}
                    </div>
                    <div id="txt">
                        <b>Writer:</b>
                        {data["Writer"]}
                    </div>
                    <div id="txt">
                        <b>IMDB Rating:</b>
                        {data["imdbRating"]}/10
                    </div>
                    <div id="txt">
                        <b>Country:</b>
                        {data["Country"]}
                    </div>
                </div>

            </div>
        </div>
            
        '''

        
        self.js.document.getElementById("data").innerHTML = i;
        



        

@app.route("/")
def index():
    return App.render(render_template("index.html"))


if __name__ == "__main__":
    app.run(debug = True)
