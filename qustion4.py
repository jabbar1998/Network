import requests


class Movies:
    def __init__(self):
        self.requst_url = 'https://my-json-server.typicode.com/horizon-code-academy/fake-movies-api/movies'
        self.requst = requests.get(self.requst_url)
        self.container = 0

    def show(self):
        if self.requst.status_code == 200:
            movie = self.requst.json()
            for i in movie:
                print(f"The name of the movie is {i['Title']} and the year of its production is {i['Year']}.")

    def addMovie(self, name: str, genre: str, story: str) -> str:
        """
        Add Movie to file json
        :param name: Name movie
        :param genre: The genre movie
        :param story: The movie story
        :return: String
        """
        self.container += 1
        new_movie = {'id': str(self.container), 'Title': name, 'Genre': genre, 'Story': story}
        post_requst = requests.post(self.requst_url, json=new_movie)
        if post_requst.status_code == 201:
            print("The movie add ")
        elif post_requst.status_code == 404:
            print("Not Found!")
        else:
            print("Error")


movie = Movies()
while True:
    print("""
    1.Show Movie
    2.Add Movie
    """)
    choice = input("Enter Your Choice: ")
    if choice == "1":
        movie.show()
    elif choice == "2":
        name, genre, story = input("Enter name,genre and story: ").split(" ")
        movie.addMovie(name, genre, story)
    else:
        print("Please Enter Correct Number!")
