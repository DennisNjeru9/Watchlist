class Movie:
    '''
    Movie class to define Movie Objects.
    '''

    def __init__(self,id,title,overview,poster,vote_average,vote_count):
        '''
        Create an init method to allow the passing of parameters needed inside the movie objects.

        Args:
            id = The movie id.
            title = The movie's name
            overview = brief description of the movie
            poster = poster image of the movie
            vote_average = average rating of the movie
            vote_count = votes involved in rating the movie
        '''
        self.id = id
        self.title = title
        self.overview = overview
        self.poster = poster
        self.vote_average = vote_average
        self.vote_count = vote_count


        pass