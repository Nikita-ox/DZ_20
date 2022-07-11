import pytest
from unittest.mock import MagicMock

from dao.genre import Genre
from service.genre import GenreService
from dao.genre import GenreDAO

@pytest.fixture
def genres_dao():
    dao = GenreDAO(None)

    dao.get_one = MagicMock()
    dao.get_all = MagicMock()
    dao.create = MagicMock()
    dao.update = MagicMock()
    dao.delete = MagicMock()

    return dao


class TestGenreService:
    @pytest.fixture(autouse=True)
    def genres_service(self, genres_dao):
        self.genres_service = GenreService(dao=genres_dao)

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
    @pytest.mark.parametrize('gid, genre', parametres)
    def test_get_one(self, gid, genre):
        self.genres_service.dao.get_one.return_value = genre
        assert self.genres_service.get_one(gid) == genre, 'BAD'

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

    @pytest.mark.parametrize('genres', parametres)
    def test_get_all(self, genres):
        self.genres_service.dao.get_all.return_value = genres
        assert self.genres_service.get_all() == genres, 'BAD'

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

    @pytest.mark.parametrize('genre', parametres)
    def test_create(self, genre):
        self.genres_service.dao.create.return_value = genre
        assert self.genres_service.create(genre) == genre, 'BAD'

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

    @pytest.mark.parametrize('genre_original, genre_new', parametres)
    def test_update(self, genre_original, genre_new):
        self.genres_service.dao.update.return_value = genre_new
        assert self.genres_service.update(genre_new) == genre_new
        self.genres_service.dao.update.assert_called_once_with(genre_new)

    def test_delete(self):
        self.genres_service.delete(1)
        self.genres_service.dao.delete.assert_called_once_with(1)
