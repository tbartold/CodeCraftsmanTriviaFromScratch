import trivia
import pytest

game = trivia.Game()


@pytest.fixture()
def get_gamefile_contents():
    game.readFile()

def test_initialize():
    assert game.has_categories()

def test_countCategory(get_gamefile_contents):
    # currently assumes the default size-4 array
    assert len(game.category) >= 1
    assert type(game.category) is dict
    for key in game.category.keys():
        assert type (game.category[key]) is list


def test_hasDefaultQuestionsFile():
    assert game.default_question_file != None

def test_openDefaultFile():
    assert game.readFile() == True


def fname(arg):
    pass
