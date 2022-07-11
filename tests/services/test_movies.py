import pytest
from unittest.mock import MagicMock

from dao.model.movie import Movie
from service.movie import MovieService
from dao.movie import MovieDAO

@pytest.fixture
def movies_dao():
    dao = MovieDAO(None)

    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestMovieService:
    @pytest.fixture(autouse=True)
    def movies_service(self, movies_dao):
        self.movies_service = MovieService(dao=movies_dao)

    parametres = (
        (
            1,
            {
                'id': 1,
                'title': 'NoName',
            }
        ),
        (
            2,
            {
                'id': 2,
                'title': 'TestName',
            }
        ),
    )
    @pytest.mark.parametrize('mid, movie', parametres)
    def test_get_one(self, mid, movie):
        self.movies_service.dao.get_one.return_value = movie
        assert self.movies_service.get_one(mid) == movie, 'BAD'

    parametres = (
        (
            [
                {
                    'id': 1,
                    'title': 'NoName',
                },
                {
                    'id': 2,
                    'title': 'TestName',
                }
            ]
        ),
    )

    @pytest.mark.parametrize('movies', parametres)
    def test_get_all(self, movies):
        self.movies_service.dao.get_all.return_value = movies
        assert self.movies_service.get_all() == movies, 'BAD'

    parametres = (
        (
            {
                'id': 1,
                'title': 'NoName',
            }
        ),
        (
            {
                'id': 2,
                'title': 'TestName',
            }
        ),
    )

    @pytest.mark.parametrize('movie', parametres)
    def test_create(self, movie):
        self.movies_service.dao.create.return_value = movie
        assert self.movies_service.create(movie) == movie, 'BAD'

    parametres = (
        (
            {
                'id': 1,
                'title': 'NoName',
            },
            {
                'id': 1,
                'title': 'TestName',
            }
        ),
    )

    @pytest.mark.parametrize('movie_original, movie_new', parametres)
    def test_update(self, movie_original, movie_new):
        self.movies_service.dao.update.return_value = movie_new
        assert self.movies_service.update(movie_new) == movie_new
        self.movies_service.dao.update.assert_called_once_with(movie_new)

    def test_delete(self):
        self.movies_service.delete(1)
        self.movies_service.dao.delete.assert_called_once_with(1)




